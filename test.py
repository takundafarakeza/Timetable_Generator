from ortools.sat.python import cp_model


# =========================================================
# SAMPLE DATA
# =========================================================

DAYS = 5
SLOTS = 6

days = range(DAYS)
slots = range(SLOTS)

modules = {
    "1": {
        "name": "Math101",

        # shared by multiple courses
        "courses": {
            "CS": {"level": "1"},
            "EE": {"level": "1"},
        },

        "venues": ["RoomA", "RoomB"],

        # sessions per cycle/week
        "sessions_per_cycle": 3,

        # preferred maximum sessions/day
        "max_sessions_per_day": 1,

        # double period
        "session_length": 2,

        "lecturer": "L1",
    },

    "2": {
        "name": "Physics101",

        "courses": {
            "CS": {"level": "1"},
            "ME": {"level": "1"},
        },

        "venues": ["RoomA"],

        "sessions_per_cycle": 2,
        "max_sessions_per_day": 1,

        # single period
        "session_length": 1,

        "lecturer": "L2",
    },

    "3": {
        "name": "Programming",

        "courses": {
            "CS": {"level": "1"},
        },

        "venues": ["Lab1"],

        "sessions_per_cycle": 2,
        "max_sessions_per_day": 1,

        # triple period
        "session_length": 3,

        "lecturer": "L1",
    }
}


courses = {
    "CS-1": {"size": 60},
    "EE-1": {"size": 40},
    "ME-1": {"size": 35},
}


venues = {
    "RoomA": {"capacity": 120},
    "RoomB": {"capacity": 80},
    "Lab1": {"capacity": 40},
}


# =========================================================
# MODEL
# =========================================================

model = cp_model.CpModel()


# =========================================================
# DERIVED SETS
# =========================================================

all_venues = set(venues.keys())

all_courses = set()

for m in modules.values():
    for c_name, c_data in m["courses"].items():
        all_courses.add(f"{c_name}-{c_data['level']}")

all_lecturers = {
    m["lecturer"]
    for m in modules.values()
}


# =========================================================
# MODULE DEMANDS
# =========================================================

module_demand = {}

for m_id, m in modules.items():

    total = 0

    for c_name, c_data in m["courses"].items():

        course_key = f"{c_name}-{c_data['level']}"

        total += courses[course_key]["size"]

    module_demand[m_id] = total


# =========================================================
# VARIABLES
# =========================================================

# start variables:
# start[module, day, slot, venue]
#
# means:
# session STARTS here

start = {}

# occupied variables:
# x[module, day, slot, venue]
#
# means:
# module occupies this slot

x = {}

# soft overflow variables
overflow = {}


# =========================================================
# CREATE START VARIABLES
# =========================================================

for m_id, m in modules.items():

    duration = m["session_length"]

    demand = module_demand[m_id]

    for d in days:

        # valid starting positions only
        for s in range(SLOTS - duration + 1):

            for v in m["venues"]:

                # capacity filtering
                if venues[v]["capacity"] >= demand:

                    start[m_id, d, s, v] = model.NewBoolVar(
                        f"start_{m_id}_{d}_{s}_{v}"
                    )


# =========================================================
# CREATE OCCUPIED VARIABLES
# =========================================================

for m_id, m in modules.items():

    demand = module_demand[m_id]

    for d in days:
        for s in slots:
            for v in m["venues"]:

                if venues[v]["capacity"] >= demand:

                    x[m_id, d, s, v] = model.NewBoolVar(
                        f"x_{m_id}_{d}_{s}_{v}"
                    )


# =========================================================
# LINK START -> OCCUPIED SLOTS
# =========================================================

for m_id, m in modules.items():

    duration = m["session_length"]

    for d in days:
        for s in slots:
            for v in m["venues"]:

                if (m_id, d, s, v) not in x:
                    continue

                covering_starts = []

                # all possible starts that cover slot s
                for k in range(
                        max(0, s - duration + 1),
                        s + 1
                ):

                    if (m_id, d, k, v) in start:

                        covering_starts.append(
                            start[m_id, d, k, v]
                        )

                model.Add(
                    x[m_id, d, s, v] == sum(covering_starts)
                )


# =========================================================
# ONE VENUE PER MODULE SLOT
# =========================================================

for m_id, m in modules.items():

    for d in days:
        for s in slots:

            model.Add(
                sum(
                    x[m_id, d, s, v]
                    for v in m["venues"]
                    if (m_id, d, s, v) in x
                ) <= 1
            )


# =========================================================
# VENUE CLASHES
# =========================================================

for d in days:
    for s in slots:
        for v in all_venues:

            model.Add(
                sum(
                    x[m_id, d, s, v]

                    for m_id, m in modules.items()

                    if (m_id, d, s, v) in x
                ) <= 1
            )


# =========================================================
# SESSIONS PER CYCLE
# =========================================================

for m_id, m in modules.items():

    total_sessions = m["sessions_per_cycle"]

    model.Add(

        sum(

            start[m_id, d, s, v]

            for d in days
            for s in range(SLOTS - m["session_length"] + 1)
            for v in m["venues"]

            if (m_id, d, s, v) in start

        ) == total_sessions
    )


# =========================================================
# SOFT MAX SESSIONS PER DAY
# =========================================================

for m_id, m in modules.items():

    max_daily = m["max_sessions_per_day"]

    for d in days:

        overflow[m_id, d] = model.NewIntVar(
            0,
            SLOTS,
            f"overflow_{m_id}_{d}"
        )

        daily_sessions = sum(

            start[m_id, d, s, v]

            for s in range(SLOTS - m["session_length"] + 1)
            for v in m["venues"]

            if (m_id, d, s, v) in start
        )

        model.Add(
            daily_sessions <= max_daily + overflow[m_id, d]
        )


# =========================================================
# COURSE CLASHES
# =========================================================

for course in all_courses:

    c_name, c_level = course.split("-")

    for d in days:
        for s in slots:

            model.Add(

                sum(

                    x[m_id, d, s, v]

                    for m_id, m in modules.items()

                    if (
                            c_name in m["courses"]
                            and
                            m["courses"][c_name]["level"] == c_level
                    )

                    for v in m["venues"]

                    if (m_id, d, s, v) in x

                ) <= 1
            )


# =========================================================
# LECTURER CLASHES
# =========================================================

for lecturer in all_lecturers:

    for d in days:
        for s in slots:

            model.Add(

                sum(

                    x[m_id, d, s, v]

                    for m_id, m in modules.items()

                    if m["lecturer"] == lecturer

                    for v in m["venues"]

                    if (m_id, d, s, v) in x

                ) <= 1
            )


# =========================================================
# OBJECTIVE
# =========================================================

# minimize daily overflow violations

model.Minimize(

    sum(
        overflow[m_id, d]

        for m_id in modules
        for d in days
    )
)


# =========================================================
# SOLVE
# =========================================================

solver = cp_model.CpSolver()

solver.parameters.max_time_in_seconds = 30

status = solver.Solve(model)


# =========================================================
# OUTPUT
# =========================================================

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):

    print("\nTIMETABLE\n")

    for m_id, m in modules.items():

        print(f"\n{m['name']}")

        for d in days:

            for s in range(SLOTS - m["session_length"] + 1):

                for v in m["venues"]:

                    if (
                            (m_id, d, s, v) in start
                            and
                            solver.Value(start[m_id, d, s, v])
                    ):

                        end_slot = s + m["session_length"] - 1

                        print(
                            f"  Day {d} | "
                            f"Slots {s}-{end_slot} | "
                            f"Venue {v} | "
                            f"Lecturer {m['lecturer']}"
                        )

else:
    print("No feasible solution found.")

