from PySide6.QtCore import QObject, Signal
from .utils import Utils
from .logger_config import logger
from .dtypes import Types
from .data import (TimetableTempDataPrimary,
                   TimetableTempDataSecondary,
                   TimetableTempDataTertiary, Timetable)
from ortools.sat.python import cp_model
import random


class PrimarySchool(QObject):
    status = Signal(int, str)
    complete = Signal(Timetable)
    finished = Signal()

    def __init__(self, time_table_temp: TimetableTempDataPrimary, parent=None):
        super().__init__(parent)
        self.time_table_template = time_table_temp
        self.status_code = 0

        self.status_messages = {
            0: "Timetable generation was successful with an optimal timetable. You can view it now.",
            1: "Generation is complete with a feasible timetable but with some subjects not added. "
               "You can view it now.",
            2: "Generation was unsuccessful due to an unexpected error.",
            3: "Generating timetable, please wait..."
        }

    def generate(self):

        try:
            self.status_code = 0
            self.status.emit(3, self.status_messages[3])
            for class_ in self.time_table_template.classes:

                subjects = self.time_table_template.classes[class_]["subjects"]
                for subject_id in subjects:

                    subject = self.time_table_template.classes[class_]["subjects"][subject_id]
                    remaining_slots = subject["time_slots"]

                    if (self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE] ==
                            Types.VENUE_PRIMARY):
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
                    if remaining_slots > 0:
                        self.status_code = 1

            self.status.emit(self.status_code, self.status_messages[self.status_code])
            self.complete.emit(Timetable(self.time_table_template.time_table))
        except Exception as e:
            logger.critical(str(e))
            self.status.emit(2, self.status_messages[2])
        self.finished.emit()
        return self.time_table_template.time_table

    def possible_slots(self, class_: str, subject_venue: str,
                       sub_time_slots: int, sub_daily_time_slots: int,
                       cur_table: dict):

        possible_slots = 0

        try:
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
        except Exception as e:
            logger.critical(str(e))
        return possible_slots, possible_slots - sub_time_slots

    @staticmethod
    def is_empty(slot, class_, venue: str = Types.VENUE_PRIMARY):
        for event in slot:
            if class_ == event:
                return False
            elif slot[event][Types.VENUE] != Types.VENUE_PRIMARY and slot[event][Types.VENUE] == venue:
                return False
        return True


class SecondarySchool(QObject):
    status = Signal(int, str)
    complete = Signal(Timetable)
    finished = Signal()

    def __init__(self, time_table_temp: TimetableTempDataSecondary, parent=None):
        super().__init__(parent)
        self.time_table_template = time_table_temp
        self.status_code = 0

        self.status_messages = {
            0: "Timetable generation was successful with an optimal timetable. You can view it now.",
            1: "Generation is complete with a feasible timetable but with some subjects not added. "
               "You can view it now.",
            2: "Generation was unsuccessful due to an unexpected error.",
            3: "Generating timetable, please wait..."
        }

    def generate(self):

        self.status_code = 0

        try:
            self.status.emit(3, self.status_messages[3])
            unassigned_blocks = len(self.time_table_template.blocks)

            for block in self.time_table_template.blocks:
                block_data = self.time_table_template.blocks[block]
                subjects = block_data[Types.SUBJECTS]
                classes = block_data[Types.CLASSES]
                venues = [subjects[subject][Types.VENUE] for subject in subjects]
                teachers = [subjects[subject][Types.TEACHER] for subject in subjects]
                block_length = block_data["time_slots"]

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
                            for subject in subjects:

                                block_slots = empty_slots[0:block_length]
                                teacher = subjects[subject][Types.TEACHER]
                                venue = subjects[subject][Types.VENUE]

                                while len(block_slots) > 0:
                                    slots[block_slots[0]][Types.EVENTS][class_] = \
                                        {Types.SUBJECT: block,
                                         Types.TEACHER: "block_teachers",
                                         Types.VENUE: "block_venues"}

                                    if class_ not in slots[block_slots[0]][Types.DATA][Types.CLASSES]:
                                        slots[block_slots[0]][Types.DATA][Types.CLASSES].append(class_)

                                    if teacher not in slots[block_slots[0]][Types.DATA][Types.TEACHERS]:
                                        slots[block_slots[0]][Types.DATA][Types.TEACHERS].append(teacher)

                                    if venue not in slots[block_slots[0]][Types.DATA][Types.VENUES]:
                                        slots[block_slots[0]][Types.DATA][Types.VENUES].append(venue)

                                    block_slots.remove(block_slots[0])
                        unassigned_blocks -= 1
                        break

            if unassigned_blocks > 0:
                self.status_code = 1

            for class_ in self.time_table_template.classes:
                subjects = self.time_table_template.classes[class_]["subjects"]
                for subject_id in subjects:

                    subject = self.time_table_template.classes[class_]["subjects"][subject_id]
                    remaining_slots = subject["time_slots"]

                    if (self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE] ==
                            Types.VENUE_PRIMARY):
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

                    if remaining_slots > 0:
                        self.status_code = 1

            self.status.emit(self.status_code, self.status_messages[self.status_code])
            self.complete.emit(Timetable(self.time_table_template.time_table))
        except Exception as e:
            logger.critical(str(e))
            self.status.emit(2, self.status_messages[2])
        self.finished.emit()
        return self.time_table_template.time_table

    def possible_block_slots(self, new_block: dict):
        self.time_table_template.blocks["new_block"] = new_block

        try:
            for block in self.time_table_template.blocks:
                block_data = self.time_table_template.blocks[block]
                subjects = block_data[Types.SUBJECTS]
                classes = block_data[Types.CLASSES]
                venues = [subjects[subject][Types.VENUE] for subject in subjects]
                teachers = [subjects[subject][Types.TEACHER] for subject in subjects]
                block_length = block_data["time_slots"]

                days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
                random.shuffle(days)

                for day in days:
                    slots = self.time_table_template.time_table[day]
                    empty_slots = [slot for slot in slots if str(slots[slot])
                                   not in self.time_table_template.breaks and
                                   self.is_empty(slots[slot], classes, venues,
                                                 teachers)]
                    empty_slots = Utils.randomize_slots(empty_slots, block_length, strict=True)
                    if len(empty_slots) >= block_length:
                        if block == "new_block":
                            del self.time_table_template.blocks["new_block"]
                            return True
                        for class_ in classes:
                            for subject in subjects:

                                block_slots = empty_slots[0:block_length]
                                teacher = subjects[subject][Types.TEACHER]
                                venue = subjects[subject][Types.VENUE]

                                while len(block_slots) > 0:
                                    slots[block_slots[0]][Types.EVENTS][class_] = \
                                        {Types.SUBJECT: block,
                                         Types.TEACHER: "block_teachers",
                                         Types.VENUE: "block_venues"}

                                    if class_ not in slots[block_slots[0]][Types.DATA][Types.CLASSES]:
                                        slots[block_slots[0]][Types.DATA][Types.CLASSES].append(class_)

                                    if teacher not in slots[block_slots[0]][Types.DATA][Types.TEACHERS]:
                                        slots[block_slots[0]][Types.DATA][Types.TEACHERS].append(teacher)

                                    if venue not in slots[block_slots[0]][Types.DATA][Types.VENUES]:
                                        slots[block_slots[0]][Types.DATA][Types.VENUES].append(venue)

                                    block_slots.remove(block_slots[0])
                        break
        except Exception as e:
            logger.critical(str(e))
        del self.time_table_template.blocks["new_block"]
        return False

    def possible_slots(self, class_: str, subject_venue: str,
                       sub_time_slots: int, sub_daily_time_slots: int,
                       teacher: str, cur_table: dict):

        possible_slots = 0
        try:
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
        except Exception as e:
            logger.critical(str(e))
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


class TertiarySchool(QObject):
    status = Signal(int, str)
    complete = Signal(Timetable)
    finished = Signal()

    def __init__(self, data: TimetableTempDataTertiary, parent=None):
        super().__init__(parent)
        self.time_table_data = data
        self.generation_messages = {
            cp_model.INFEASIBLE: "Generation is complete with an infeasible timetable "
                                 "try adjusting module lecturers or module venues and courses.",
            cp_model.MODEL_INVALID: "Generation was unsuccessful due to an invalid data model.",
            cp_model.FEASIBLE: "Generation is complete with a feasible but not optimal timetable."
                               " You can view it now.",
            cp_model.OPTIMAL: "Timetable generation was successful with an optimal timetable. You "
                              "can view it now."
        }

    def generate(self):
        model = cp_model.CpModel()
        self.status.emit(1, "Preparing constraints...")
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

        self.status.emit(1, "Starting generation...")
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        time_table = self.time_table_data.time_table

        if status == cp_model.INFEASIBLE:
            self.status.emit(2, self.generation_messages[status])
        elif status == cp_model.MODEL_INVALID:
            self.status.emit(2, self.generation_messages[status])
        elif status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
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
            self.status.emit(0, self.generation_messages[status])
        self.complete.emit(Timetable(time_table))
        self.finished.emit()

    def possible_slots(self, *args):
        pass
