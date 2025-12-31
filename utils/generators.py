from .utils import Utils
from .dtypes import Types
from .data import (TimetableTempDataPrimary,
                   TimetableTempDataSecondary,
                   TimetableTempDataTertiary)
from ortools.sat.python import cp_model
import random


class PrimarySchool:
    def __init__(self, time_table_temp: TimetableTempDataPrimary):
        self.time_table_template = time_table_temp

    def generate(self):
        for class_ in self.time_table_template.classes:

            subjects = self.time_table_template.classes[class_]["subjects"]
            for subject_id in subjects:

                subject = self.time_table_template.classes[class_]["subjects"][subject_id]
                remaining_slots = subject["time_slots"]

                if self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE] == Types.VENUE_PRIMARY:
                    venue = self.time_table_template.classes[class_][Types.VENUE]
                else:
                    venue = self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE]

                days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
                random.shuffle(days)
                day_count = self.time_table_template.days_per_cycle

                while remaining_slots > 0 and day_count > 0:

                    for day in days:

                        slots = self.time_table_template.time_table[day]
                        empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
                                                             not in self.time_table_template.breaks and
                                                             self.is_empty(slots[slot], class_, venue)],
                                                            subject["slots_per_day"])
                        assign_count = min(remaining_slots, len(empty_slots), subject["slots_per_day"])

                        while assign_count > 0:
                            slots[empty_slots[0]][class_] = \
                                {Types.SUBJECT: subject_id,
                                 Types.VENUE: venue}

                            empty_slots.remove(empty_slots[0])
                            assign_count -= 1
                            remaining_slots -= 1
                        day_count -= 1
        return self.time_table_template.time_table

    def possible_slots(self, class_: str, subject_venue: str,
                       sub_time_slots: int, sub_daily_time_slots: int,
                       cur_table: dict):

        possible_slots = 0

        if subject_venue == Types.VENUE_PRIMARY:
            venue = self.time_table_template.classes[class_][Types.VENUE]
        else:
            venue = subject_venue

        days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
        random.shuffle(days)

        for day in days:
            slots = cur_table[day]
            empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
                                                 not in self.time_table_template.breaks and
                                                 self.is_empty(slots[slot], class_, venue)],
                                                sub_daily_time_slots)
            possible_slots += len(empty_slots)
        return possible_slots, possible_slots - sub_time_slots

    @staticmethod
    def is_empty(slot, class_, venue: str = Types.VENUE_PRIMARY):
        for event in slot:
            if class_ == event:
                return False
            elif slot[event][Types.VENUE] != Types.VENUE_PRIMARY and slot[event][Types.VENUE] == venue:
                return False
        return True


class SecondarySchool:
    def __init__(self, time_table_temp: TimetableTempDataSecondary):
        self.time_table_template = time_table_temp

    def generate(self):

        for block in self.time_table_template.blocks:
            subject = self.time_table_template.blocks[block][Types.SUBJECT]
            teachers = self.time_table_template.blocks[block][Types.TEACHERS]
            venues = self.time_table_template.blocks[block][Types.VENUES]
            classes = self.time_table_template.blocks[block][Types.CLASSES]
            block_length = block["time_slots"]

            days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
            random.shuffle(days)
            for day in days:
                slots = self.time_table_template.time_table[day]

                empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
                                                     not in self.time_table_template.breaks and
                                                     self.is_empty(slots[slot], classes, venues,
                                                                   teachers)],
                                                    block_length, strict=True)
                if len(empty_slots) >= block_length:
                    for class_ in classes:

                        if (self.time_table_template.subjects[subject][Types.SUBJECT_PRIMARY_VENUE]
                                == Types.VENUE_PRIMARY):
                            venue = self.time_table_template.classes[class_][Types.VENUE]
                        else:
                            venue = self.time_table_template.subjects[subject][Types.SUBJECT_PRIMARY_VENUE]
                        teacher = self.time_table_template.classes[Types.SUBJECTS][subject][Types.TEACHER]

                        slots[empty_slots[0]][Types.EVENTS][class_] = \
                            {Types.SUBJECT: self.time_table_template.subjects[subject][Types.NAME],
                             Types.VENUE: venue,
                             Types.TEACHER: teacher}

                        slots[empty_slots[0]][Types.DATA][Types.CLASSES].append(class_)
                        slot_teachers = slots[empty_slots[0]][Types.DATA][Types.TEACHERS]
                        if teacher not in slot_teachers:
                            slot_teachers.append(teacher)
                        slot_venues = slots[empty_slots[0]][Types.DATA][Types.VENUES]
                        if venue not in slot_venues:
                            slots[empty_slots[0]][Types.DATA][Types.VENUES].append(venue)
                    break

        for class_ in self.time_table_template.classes:
            subjects = self.time_table_template.classes[class_]["subjects"]
            for subject_id in subjects:

                subject = self.time_table_template.classes[class_]["subjects"][subject_id]
                remaining_slots = subject["time_slots"]

                if self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE] == Types.VENUE_PRIMARY:
                    venue = self.time_table_template.classes[class_][Types.VENUE]
                else:
                    venue = self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE]

                teacher = self.time_table_template.classes[class_][Types.SUBJECTS][subject_id][Types.TEACHER]
                days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
                random.shuffle(days)
                day_count = self.time_table_template.days_per_cycle

                while remaining_slots > 0 and day_count > 0:

                    for day in days:
                        slots = self.time_table_template.time_table[day]

                        empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
                                                             not in self.time_table_template.breaks and
                                                             self.is_empty(slots[slot], [class_], [venue],
                                                                           [teacher])],
                                                            subject["slots_per_day"])
                        assign_count = min(remaining_slots, len(empty_slots), subject["slots_per_day"])

                        while assign_count > 0:
                            slots[empty_slots[0]][Types.EVENTS][class_] = \
                                {Types.SUBJECT: subject_id,
                                 Types.VENUE: venue,
                                 Types.TEACHER: teacher}
                            slots[empty_slots[0]][Types.DATA][Types.TEACHERS].append(teacher)
                            slots[empty_slots[0]][Types.DATA][Types.VENUES].append(venue)
                            slots[empty_slots[0]][Types.DATA][Types.CLASSES].append(class_)

                            empty_slots.remove(empty_slots[0])
                            assign_count -= 1
                            remaining_slots -= 1
                        day_count -= 1
        return self.time_table_template.time_table

    def possible_slots(self, class_: str, subject_venue: str,
                       sub_time_slots: int, sub_daily_time_slots: int,
                       teacher: str, cur_table: dict):

        possible_slots = 0

        if subject_venue == Types.VENUE_PRIMARY:
            venue = self.time_table_template.classes[class_][Types.VENUE]
        else:
            venue = subject_venue

        days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
        random.shuffle(days)

        for day in days:
            slots = cur_table[day]
            empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
                                                 not in self.time_table_template.breaks and
                                                 self.is_empty(slots[slot], [class_], [venue],
                                                               [teacher])],
                                                sub_daily_time_slots)
            possible_slots += len(empty_slots)
        return possible_slots, possible_slots - sub_time_slots

    @staticmethod
    def is_empty(slot, classes: list, venues: list = Types.VENUE_PRIMARY,
                 teachers: list = Types.UNAVAILABLE):
        for event in slot[Types.EVENTS]:
            for class_ in classes:
                if class_ in slot[Types.DATA][Types.CLASSES]:
                    return False
            if slot[Types.EVENTS][event][Types.VENUE] != Types.VENUE_PRIMARY:
                for venue in venues:
                    if venue in slot[Types.DATA][Types.VENUES]:
                        return False
            if slot[Types.EVENTS][event][Types.TEACHER] != Types.UNAVAILABLE:
                for teacher in teachers:
                    if teacher in slot[Types.DATA][Types.TEACHERS]:
                        return False
        return True


class TertiarySchool:
    def __init__(self, data: TimetableTempDataTertiary):
        self.time_table_data = data

    def generate(self):
        model = cp_model.CpModel()

        days = range(self.time_table_data.days_per_cycle)
        slots = range(self.time_table_data.slots_per_day)

        modules = self.time_table_data.modules

        all_venues = {v for m in modules.values() for v in m[Types.VENUES] if len(m[Types.COURSES]) > 0}
        all_courses = {f"{c}-{m[Types.COURSES][c][Types.LEVEL]}" for m in modules.values() for c in m[Types.COURSES]
                       if len(m[Types.COURSES]) > 0}
        all_lecturers = {m[Types.LECTURER] for m in modules.values() if len(m[Types.COURSES]) > 0}

        x = {}

        for m_id, m in modules.items():
            if len(m[Types.COURSES]) > 0:
                for d in days:
                    for s in slots:
                        for v in m[Types.VENUES]:
                            x[m_id, d, s, v] = model.NewBoolVar(f"x_{m_id}_{d}_{s}_{v}")

        for m_id, m in modules.items():
            if len(m[Types.COURSES]) > 0:
                for d in days:
                    for s in slots:
                        model.Add(sum(x[m_id, d, s, v] for v in m[Types.VENUES]) <= 1)

        for d in days:
            for s in slots:
                for v in all_venues:
                    model.Add(sum(
                        x[m_id, d, s, v]
                        for m_id, m in modules.items()
                        if v in m[Types.VENUES] and len(m[Types.COURSES]) > 0
                    ) <= 1)

        for m_id, m in modules.items():
            if len(m[Types.COURSES]) > 0:
                max_per_day = m["slots_per_day"]
                for d in days:
                    model.Add(sum(
                        x[m_id, d, s, v] for s in slots
                        for v in m[Types.VENUES]
                    ) <= max_per_day)

        for m_id, m in modules.items():
            if len(m[Types.COURSES]) > 0:
                total = m["time_slots"]
                model.Add(sum(
                    x[m_id, d, s, v]
                    for d in days
                    for s in slots
                    for v in m[Types.VENUES]
                ) == total)

        for course in all_courses:
            for d in days:
                for s in slots:
                    model.Add(sum(
                        x[m_id, d, s, v]
                        for m_id, m in modules.items()
                        if course.split("-")[0] in m[Types.COURSES]
                        if course.split("-")[1] == m[Types.COURSES][course.split("-")[0]][Types.LEVEL]
                        for v in m[Types.VENUES]
                    ) <= 1)

        for lecturer in all_lecturers:
            for d in days:
                for s in slots:
                    model.Add(sum(
                        x[m_id, d, s, v]
                        for m_id, m in modules.items()
                        if len(m[Types.COURSES]) > 0
                        if lecturer == m[Types.LECTURER]
                        for v in m[Types.VENUES]
                    ) <= 1)

        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        time_table = self.time_table_data.time_table

        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            for m_id, m in modules.items():
                if len(m[Types.COURSES]) > 0:
                    for d in days:
                        for s in slots:
                            for v in m[Types.VENUES]:
                                if solver.Value(x[m_id, d, s, v]):
                                    courses = []
                                    for c_ in m[Types.COURSES]:
                                        courses.append(f"{self.time_table_data.courses[c_][Types.SHORT_NAME]}-"
                                                       f"{m[Types.COURSES][c_][Types.LEVEL]}")
                                    time_table[f"{d + 1}"][f"{s + 1}"][m_id] = {Types.VENUE: v, Types.COURSES: courses}

        return time_table

    def possible_slots(self, *args):
        pass
