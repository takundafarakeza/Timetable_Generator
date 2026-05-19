from ortools.sat.python import cp_model


model = cp_model.CpModel()


days = range(2)
slots = range(3)

modules = {"Math": {"lecturer": "Mr A", "venue": ["Lab 1", "Lab 3"]},
           "Physics": {"lecturer": "Mr A", "venue": ["Lab 1"]},
           "Biology": {"lecturer": "Mrs B", "venue": ["Lab 2", "Lab 3"]}}
all_lecturers = {modules[m]["lecturer"] for m in modules}
all_venues = {v for m in modules for v in modules[m]["venue"]}
x = {}

for m_id in modules:
    for d in days:
        for s in slots:
            for v in modules[m_id]["venue"]:
                x[m_id, d, s, v] = model.NewBoolVar(f"x_{m_id}_{d}_{s}_{v}")


for m_id in modules:
    model.Add(sum(
        x[m_id, d, s, v]
        for d in days
        for s in slots
        for v in modules[m_id]["venue"]
    ) == 2)


for lecturer in all_lecturers:
    for d in days:
        for s in slots:
            model.Add(
                sum(
                    x[m_id, d, s, v]
                    for m_id in modules
                    for v in modules[m_id]["venue"]
                    if lecturer == modules[m_id]["lecturer"]
                ) <= 1
            )

for v in all_venues:
    for d in days:
        for s in slots:
            model.Add(
                sum(
                    x[m_id, d, s, v]
                    for m_id in modules
                    if v in modules[m_id]["venue"]
                ) <= 1
            )


solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
    for day in days:
        for slot in slots:
            for m_id in modules:
                for venue in modules[m_id]["venue"]:
                    if solver.Value(x[m_id, day, slot, venue]):
                        print(f"{m_id} Day: {day} Slot: {slot} Venue: {venue}")
