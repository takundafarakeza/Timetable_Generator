from .utils import Utils
from .dtypes import Types
from .data import TimetableTemplateData
import random


class PrimarySchool:
    def __init__(self, time_table_temp: TimetableTemplateData):
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

                while remaining_slots > 0:

                    for day in days:

                        slots = self.time_table_template.time_table[day]
                        empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
                                                             not in self.time_table_template.breaks and
                                                             self.is_empty(slots[slot], class_, venue)],
                                                            subject["slots_per_day"])
                        assignment_count = min(remaining_slots, len(empty_slots), subject["slots_per_day"])

                        while assignment_count > 0:
                            slots[empty_slots[(assignment_count - assignment_count) ** 2]][class_] = \
                                {Types.SUBJECT: self.time_table_template.subjects[subject_id][Types.NAME],
                                 Types.VENUE: venue}

                            empty_slots.remove(empty_slots[(assignment_count - assignment_count) ** 2])
                            assignment_count -= 1
                        remaining_slots -= subject["slots_per_day"]
        return self.time_table_template.time_table

    # def patch(self, class_: str, subject_id: str,
    #           sub_time_slots: int, sub_daily_time_slots: int):
    #
    #     remaining_slots = sub_time_slots
    #
    #     if self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE] == Types.VENUE_PRIMARY:
    #         venue = self.time_table_template.classes[class_][Types.VENUE]
    #     else:
    #         venue = self.time_table_template.subjects[subject_id][Types.SUBJECT_PRIMARY_VENUE]
    #
    #     days = [str(day) for day in range(1, self.time_table_template.days_per_cycle + 1)]
    #     random.shuffle(days)
    #
    #     while remaining_slots > 0:
    #
    #         for day in days:
    #             slots = self.time_table_template.time_table[day]
    #             empty_slots = Utils.randomize_slots([slot for slot in slots if str(slots[slot])
    #                                                  not in self.time_table_template.breaks and
    #                                                  self.is_empty(slots[slot], class_, venue)],
    #                                                 sub_daily_time_slots)
    #
    #             assignment_count = min(remaining_slots, len(empty_slots), sub_time_slots)
    #
    #             while assignment_count > 0:
    #                 slots[empty_slots[(assignment_count - assignment_count) ** 2]][class_] = \
    #                     {Types.SUBJECT: self.time_table_template.subjects[subject_id][Types.NAME],
    #                      Types.VENUE: venue}
    #
    #                 empty_slots.remove(empty_slots[(assignment_count - assignment_count) ** 2])
    #                 assignment_count -= 1
    #             remaining_slots -= sub_daily_time_slots

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
