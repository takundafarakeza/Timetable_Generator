from PySide6.QtCore import Signal, QObject
from . import Types, Formats
from .logger_config import logger
from .data import (Class, Venue, Subject, Teacher, Lecturer, Course,
                   TimeTableInitData, TimetableTempDataPrimary, Module,
                   TimetableTempDataSecondary, TimetableTempDataTertiary,
                   Block)
from .generators import PrimarySchool, SecondarySchool, TertiarySchool
import json


class PrimaryBuilder(QObject):
    generated = Signal(bool)
    saved = Signal(bool)

    def __init__(self, file_path: str,
                 init_data: TimeTableInitData = None):
        super().__init__()

        file = open(file_path)
        try:
            time_table_data = json.loads(file.read())
        except Exception as e:
            logger.warning(str(e))
            time_table_data = None
        file.close()

        self._time_table_data: dict = ({} if time_table_data is None else time_table_data)
        if not self._time_table_data:
            self.timetable_init_headers(init_data)

        self._init_data = init_data
        self.save_path: str = file_path
        self.unsaved_changes: bool = False
        self.non_generated_changes: bool = False
        self._patches: dict = {}

    def set_saved(self):
        self.unsaved_changes: bool = False
        self.saved.emit(True)

    def set_generated(self):
        self.non_generated_changes: bool = False
        self.generated.emit(True)

    def set_unsaved(self):
        self.unsaved_changes: bool = True
        self.saved.emit(False)

    def set_not_generated(self):
        self.non_generated_changes: bool = True
        self.generated.emit(False)

    def is_saved(self) -> bool:
        return self.unsaved_changes

    def is_generated(self) -> bool:
        return self.non_generated_changes

    def get_file(self):
        return self.save_path

    def reload(self):
        file = open(self.save_path)
        time_table_data = json.loads(file.read())
        file.close()

        self._time_table_data: dict = ({} if time_table_data is None else time_table_data)
        if not self._time_table_data:
            self.timetable_init_headers(self._init_data)
        self.set_saved()

    def timetable_init_headers(self, data: TimeTableInitData):
        self._time_table_data[Types.TIMETABLE_NAME] = data.timetable_name
        self._time_table_data[Types.INSTITUTION_TYPE] = data.institution_type
        self._time_table_data[Types.INSTITUTION_NAME] = data.school_name
        self._time_table_data[Types.TIME_SLOT_LENGTH] = data.time_slot_length
        self._time_table_data[Types.DAYS_PER_CYCLE] = data.days_per_cycle
        self._time_table_data[Types.SLOTS_PER_DAY] = data.slots_per_day
        self._time_table_data[Types.BREAKING_SLOTS] = data.break_slots

        self._time_table_data[Types.CLASSES] = {}
        self._time_table_data[Types.SUBJECTS] = {}
        self._time_table_data[Types.VENUES] = {"unavailable": {"name": "Unavailable", "location": [0, 0],
                                                               "location_description": "Unavailable"}}
        self._time_table_data[Types.SEQUENCE] = {
            Types.CLASSES: 0,
            Types.SUBJECTS: 0,
            Types.VENUES: 0
        }
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()

    def timetable_init_timetable(self):
        try:
            time_table = {day: {slot: {} for slot in range(1, self._time_table_data[Types.SLOTS_PER_DAY] + 1)}
                          for day in range(1, self._time_table_data[Types.DAYS_PER_CYCLE] + 1)}

            breaks = self._time_table_data[Types.BREAKING_SLOTS]
            for day in time_table:
                for break_ in breaks:
                    time_slots = breaks[break_]
                    for time_slot in time_slots:
                        time_table[day][time_slot] = break_
            return json.loads(json.dumps(time_table))
        except Exception as e:
            logger.critical(f"Error: {str(e)}")
            return {}

    def timetable_change_header(self, header: str, value):
        self._time_table_data[header] = value
        self.set_unsaved()

    def timetable_save(self):
        data = json.dumps(self._time_table_data)
        with open(self.save_path, "w") as tbl:
            tbl.write(data)
        self.set_saved()

    def timetable_add_patch(self, class_id: str,
                            subject_id: str, sub_time_slots: int,
                            sub_daily_slots: int):
        venue_id = self._time_table_data[Types.CLASSES][class_id][Types.VENUE]
        patch = Formats.format_patch_primary(self._time_table_data[Types.CLASSES][class_id][Types.NAME],
                                             venue_id, subject_id, sub_time_slots, sub_daily_slots)
        self._patches[class_id] = patch

    def timetable_remove_patch(self, class_id, subject_id):
        if class_id in self._patches:
            if subject_id in self._patches[class_id][Types.SUBJECTS]:
                del self._patches[class_id][Types.SUBJECTS][subject_id]
                if len(self._patches[class_id][Types.SUBJECTS]) == 0:
                    del self._patches[class_id]

    def timetable_remove_subject(self, subject_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot]
                      if not isinstance(time_table[day][slot], str)
                      if time_table[day][slot][class_id][Types.SUBJECT] == subject_id]
        for r in removables:
            day, slot, class_id = r
            del time_table[day][slot][class_id]
        self.set_unsaved()

    def timetable_remove_class_subject(self, class_, subject_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot]
                      if class_id == class_ if time_table[day][slot][class_id][Types.SUBJECT] == subject_id]
        for r in removables:
            day, slot, class_id = r
            del time_table[day][slot][class_id]
        self.set_unsaved()

    def timetable_remove_class(self, class_):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot]
                      if class_id == class_]
        for r in removables:
            day, slot, class_id = r
            del time_table[day][slot][class_id]
        self.set_unsaved()

    """ ========== TIMETABLE READ =========="""

    def timetable_get(self):
        return self._time_table_data[Types.TIMETABLE]

    def timetable_get_days_per_cycle(self):
        return self._time_table_data[Types.DAYS_PER_CYCLE]

    def timetable_get_slots_per_day(self):
        return self._time_table_data[Types.SLOTS_PER_DAY]

    def timetable_get_name(self):
        return self._time_table_data[Types.TIMETABLE_NAME]

    def timetable_get_institution_type(self):
        return self._time_table_data[Types.INSTITUTION_TYPE]

    def timetable_get_institution_name(self):
        return self._time_table_data[Types.INSTITUTION_NAME]

    def timetable_get_time_slot_length(self):
        return self._time_table_data[Types.TIME_SLOT_LENGTH]

    # =============================== GENERATOR FUNCTIONS ============================= #

    def generate(self):
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()
        data = TimetableTempDataPrimary(self._time_table_data[Types.CLASSES],
                                        self._time_table_data[Types.SUBJECTS],
                                        self._time_table_data[Types.DAYS_PER_CYCLE],
                                        self._time_table_data[Types.BREAKING_SLOTS],
                                        self._time_table_data[Types.TIMETABLE])
        generator = PrimarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}
        self.set_generated()

    def generate_patches(self):
        data = TimetableTempDataPrimary(self._patches,
                                        self._time_table_data[Types.SUBJECTS],
                                        self._time_table_data[Types.DAYS_PER_CYCLE],
                                        self._time_table_data[Types.BREAKING_SLOTS],
                                        self._time_table_data[Types.TIMETABLE])
        generator = PrimarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}
        self.set_generated()

    def get_possible_slots(self, class_id: str, subject_venue: str,
                           time_slots: int, time_slots_daily: int):
        data = TimetableTempDataPrimary(self._time_table_data[Types.CLASSES],
                                        self._time_table_data[Types.SUBJECTS],
                                        self._time_table_data[Types.DAYS_PER_CYCLE],
                                        self._time_table_data[Types.BREAKING_SLOTS],
                                        self.timetable_init_timetable())
        generator = PrimarySchool(data)
        time_table = generator.generate()
        return generator.possible_slots(class_id, subject_venue, time_slots,
                                        time_slots_daily, time_table)

    # ======================================= CLASSES ================================== #

    def add_class(self, name: str, venue: str,
                  subjects: dict):
        class_id = str(self._time_table_data[Types.SEQUENCE][Types.CLASSES] + 1)
        self._time_table_data[Types.CLASSES][class_id] = (
            Formats.format_class_primary(name, venue, subjects)
        )
        self._time_table_data[Types.SEQUENCE][Types.CLASSES] = int(class_id)
        self.set_unsaved()

    def class_exists(self, name: str):
        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if classes[class_][Types.NAME] == name:
                return True
        return False

    def class_change_data(self, class_id: str, dtype: str, value):
        self._time_table_data[Types.CLASSES][class_id][dtype] = value
        self.set_unsaved()

    def class_remove(self, class_id: str):
        del self._time_table_data[Types.CLASSES][class_id]
        self.set_unsaved()
        self.set_not_generated()
        self.timetable_remove_class(class_id)

    def class_remove_data(self, class_id: str, dtype: str):
        if dtype == Types.VENUE:
            self._time_table_data[Types.CLASSES][class_id][dtype] = "unavailable"
        else:
            self._time_table_data[Types.CLASSES][class_id][dtype] = {}
        self.set_unsaved()
        self.set_not_generated()

    def class_add_subject(self, class_id: str, subject_id: str,
                          time_slots: int, slots_per_day):
        self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id] = (
            Formats.format_class_subject_primary(time_slots, slots_per_day)
        )
        self.timetable_add_patch(class_id, subject_id, time_slots, slots_per_day)
        self.set_unsaved()
        self.set_not_generated()

    def class_remove_subject(self, class_id: str, subject_id: str):
        try:
            del self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id]
        except Exception as e:
            logger.warning(str(e))

        self.set_unsaved()
        self.set_not_generated()
        self.timetable_remove_patch(class_id, subject_id)
        self.timetable_remove_class_subject(class_id, subject_id)

    def class_get_all(self):
        classes_data = self._time_table_data[Types.CLASSES]

        classes = [Class(class_, classes_data[class_][Types.NAME], classes_data[class_][Types.VENUE],
                         classes_data[class_][Types.SUBJECTS]) for class_ in classes_data]
        return classes

    def class_get(self, class_id):
        class_data = self._time_table_data[Types.CLASSES][class_id]
        return Class(class_id, class_data[Types.NAME], class_data[Types.VENUE], class_data[Types.SUBJECTS])

    # =================================== VENUES  ================================ #

    def add_venue(self, name: str, location: list,
                  location_description: str):
        venue_id = str(self._time_table_data[Types.SEQUENCE][Types.VENUES] + 1)
        self._time_table_data[Types.VENUES][venue_id] = (
            Formats.format_venue(name, location, location_description)
        )
        self._time_table_data[Types.SEQUENCE][Types.VENUES] = int(venue_id)
        self.set_unsaved()

    def venue_exists(self, name: str):
        venues = self._time_table_data[Types.VENUES]
        for venue in venues:
            if venues[venue][Types.NAME] == name:
                return True
        return False

    def venue_remove(self, venue_id):

        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if venue_id == classes[class_][Types.VENUE]:
                self.class_remove_data(class_, Types.VENUE)

        subjects = self._time_table_data[Types.SUBJECTS]

        for subject in subjects:
            if venue_id == subjects[subject][Types.SUBJECT_PRIMARY_VENUE]:
                self.subject_remove_data(subject, Types.SUBJECT_PRIMARY_VENUE)

        del self._time_table_data[Types.VENUES][venue_id]
        self.set_unsaved()
        self.set_not_generated()

    def venue_change_data(self, venue_id: str, dtype: str, value):
        self._time_table_data[Types.VENUES][venue_id][dtype] = value
        self.set_unsaved()

    def venue_get_all(self):
        venues_data = self._time_table_data[Types.VENUES]
        venues = [Venue(venue, venues_data[venue]["name"],
                        venues_data[venue]["location"],
                        venues_data[venue]["location_description"]) for venue in venues_data]
        return venues

    def venue_get(self, venue_id: str):
        venue_data = self._time_table_data[Types.VENUES][venue_id]
        return Venue(venue_id, venue_data["name"], venue_data["location"],
                     venue_data["location_description"])

    # ======================================== SUBJECTS =================================== #

    def add_subject(self, name: str,
                    primary_venue: str):
        subject_id = str(self._time_table_data[Types.SEQUENCE][Types.SUBJECTS] + 1)
        self._time_table_data[Types.SUBJECTS][subject_id] = (
            Formats.format_subject_primary(name, primary_venue)
        )
        self._time_table_data[Types.SEQUENCE][Types.SUBJECTS] = int(subject_id)
        self.set_unsaved()

    def subject_exits(self, name: str):
        subjects = self._time_table_data[Types.SUBJECTS]

        for subject in subjects:
            if subjects[subject][Types.NAME] == name:
                return True
        return False

    def subject_remove(self, subject_id):
        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if subject_id in classes[class_][Types.SUBJECTS]:
                self.class_remove_subject(class_, subject_id)

        self.timetable_remove_subject(subject_id)
        del self._time_table_data[Types.SUBJECTS][subject_id]
        self.set_unsaved()
        self.set_not_generated()

    def subject_change_data(self, subject_id: str, dtype: str, value):
        self._time_table_data[Types.SUBJECTS][subject_id][dtype] = value
        self.set_unsaved()

    def subject_remove_data(self, subject_id: str, dtype: str):
        if dtype == Types.SUBJECT_PRIMARY_VENUE:
            self._time_table_data[Types.SUBJECTS][subject_id][dtype] = "unavailable"
        self.set_unsaved()
        self.set_not_generated()

    def subject_get_all(self):
        subjects_data = self._time_table_data[Types.SUBJECTS]
        subjects = [Subject(subject, subjects_data[subject][Types.NAME],
                            subjects_data[subject]["primary_venue"])
                    for subject in subjects_data]
        return subjects

    def subject_get(self, subject_id: str):
        subject_data = self._time_table_data[Types.SUBJECTS][subject_id]
        return Subject(subject_id, subject_data[Types.NAME],
                       subject_data["primary_venue"])

    def subject_get_classes(self, subject_id: str):
        classes_data = self._time_table_data[Types.CLASSES]

        classes = [Class(class_, classes_data[class_][Types.NAME], classes_data[class_][Types.VENUE],
                         classes_data[class_][Types.SUBJECTS]) for class_ in classes_data
                   if subject_id in classes_data[class_][Types.SUBJECTS]]
        return classes


class SecondaryBuilder(QObject):
    generated = Signal(bool)
    saved = Signal(bool)

    def __init__(self, file_path: str,
                 init_data: TimeTableInitData = None):
        super().__init__()

        file = open(file_path)
        try:
            time_table_data = json.loads(file.read())
        except Exception as e:
            logger.warning(str(e))
            time_table_data = None
        file.close()

        self._time_table_data = ({} if time_table_data is None else time_table_data)
        if not self._time_table_data:
            self.timetable_init_headers(init_data)

        self._init_data = init_data
        self.save_path = file_path
        self.unsaved_changes = False
        self.non_generated_changes = False
        self._patches = {}

    def set_saved(self):
        self.unsaved_changes: bool = False
        self.saved.emit(True)

    def set_generated(self):
        self.non_generated_changes: bool = False
        self.generated.emit(True)

    def set_unsaved(self):
        self.unsaved_changes: bool = True
        self.saved.emit(False)

    def set_not_generated(self):
        self.non_generated_changes: bool = True
        self.generated.emit(False)

    def is_saved(self) -> bool:
        return self.unsaved_changes

    def is_generated(self) -> bool:
        return self.non_generated_changes

    def get_file(self):
        return self.save_path

    def reload(self):
        file = open(self.save_path)
        time_table_data = json.loads(file.read())
        file.close()

        self._time_table_data: dict = ({} if time_table_data is None else time_table_data)
        if not self._time_table_data:
            self.timetable_init_headers(self._init_data)
        self.set_saved()

    def timetable_init_headers(self, data: TimeTableInitData):
        self._time_table_data[Types.TIMETABLE_NAME] = data.timetable_name
        self._time_table_data[Types.INSTITUTION_TYPE] = data.institution_type
        self._time_table_data[Types.INSTITUTION_NAME] = data.school_name
        self._time_table_data[Types.TIME_SLOT_LENGTH] = data.time_slot_length
        self._time_table_data[Types.DAYS_PER_CYCLE] = data.days_per_cycle
        self._time_table_data[Types.SLOTS_PER_DAY] = data.slots_per_day
        self._time_table_data[Types.SEQUENCE] = {
            Types.CLASSES: 0,
            Types.SUBJECTS: 0,
            Types.VENUES: 0,
            Types.TEACHERS: 0,
            Types.BLOCKS: "b0"
        }
        self._time_table_data[Types.BREAKING_SLOTS] = data.break_slots

        self._time_table_data[Types.BLOCK_SLOTS] = {}
        self._time_table_data[Types.CLASSES] = {}
        self._time_table_data[Types.SUBJECTS] = {}
        self._time_table_data[Types.VENUES] = {"unavailable": {"name": "Unavailable", "location": [0, 0],
                                                               "location_description": "Unavailable"}}
        self._time_table_data[Types.TEACHERS] = {"unavailable": {"name": "Unavailable"}}
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()

    def timetable_init_timetable(self):
        try:
            time_table = {day: {slot: {Types.DATA: {
                Types.TEACHERS: [],
                Types.VENUES: [],
                Types.CLASSES: []
            }, Types.EVENTS: {}} for slot in range(1, self._time_table_data[Types.SLOTS_PER_DAY] + 1)}
                for day in range(1, self._time_table_data[Types.DAYS_PER_CYCLE] + 1)}

            breaks = self._time_table_data[Types.BREAKING_SLOTS]
            for day in time_table:
                for break_ in breaks:
                    time_slots = breaks[break_]
                    for time_slot in time_slots:
                        time_table[day][time_slot] = break_
            return json.loads(json.dumps(time_table))
        except Exception as e:
            logger.critical(f"Error: {str(e)}")
            return {}

    def timetable_change_header(self, header: str, value):
        self._time_table_data[header] = value
        self.set_unsaved()

    def timetable_save(self):
        data = json.dumps(self._time_table_data)
        with open(self.save_path, "w") as tbl:
            tbl.write(data)
        self.set_saved()

    def timetable_add_patch(self, class_id: str, teacher: str,
                            subject_id: str, sub_time_slots: int,
                            sub_daily_slots: int):
        venue_id = self._time_table_data[Types.CLASSES][class_id][Types.VENUE]
        patch = Formats.format_patch_secondary(self._time_table_data[Types.CLASSES][class_id][Types.NAME],
                                               venue_id, subject_id, sub_time_slots, sub_daily_slots,
                                               teacher)
        self._patches[class_id] = patch

    def timetable_remove_patch(self, class_id, subject_id):
        if class_id in self._patches:
            if subject_id in self._patches[class_id][Types.SUBJECTS]:
                del self._patches[class_id][Types.SUBJECTS][subject_id]
                if len(self._patches[class_id][Types.SUBJECTS]) == 0:
                    del self._patches[class_id]

    def timetable_remove_subject(self, subject_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if not isinstance(time_table[day][slot], str)
                      if time_table[day][slot][Types.EVENTS][class_id][Types.SUBJECT] == subject_id]
        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.DATA][Types.TEACHERS].remove(
                time_table[day][slot][Types.EVENTS][class_id][Types.TEACHER])
            time_table[day][slot][Types.DATA][Types.CLASSES].remove(class_id)
            time_table[day][slot][Types.DATA][Types.VENUES].remove(
                time_table[day][slot][Types.EVENTS][class_id][Types.VENUE])
            del time_table[day][slot][Types.EVENTS][class_id]

    def timetable_remove_venue(self, venue_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if not isinstance(time_table[day][slot][Types.EVENTS], str)
                      if time_table[day][slot][Types.EVENTS][class_id][Types.VENUE] == venue_id]
        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.EVENTS][class_id][Types.VENUE] = Types.UNAVAILABLE
            time_table[day][slot][Types.DATA][Types.VENUES].remove(venue_id)
        self.set_unsaved()

    def timetable_remove_teacher(self, teacher_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if not isinstance(time_table[day][slot][Types.EVENTS], str)
                      if time_table[day][slot][Types.EVENTS][class_id][Types.TEACHER] == teacher_id]
        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.EVENTS][class_id][Types.TEACHER] = Types.UNAVAILABLE
            time_table[day][slot][Types.DATA][Types.TEACHERS].remove(teacher_id)
        self.set_unsaved()

    def timetable_remove_class_subject(self, class_, subject_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if class_id == class_ if time_table[day][slot][Types.EVENTS][class_id][Types.SUBJECT]
                      == subject_id]
        for r in removables:
            day, slot, class_id = r
            del time_table[day][slot][Types.EVENTS][class_id]
        self.set_unsaved()

    def timetable_remove_class_subject_teacher(self, class_, teacher_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if class_id == class_ if time_table[day][slot][Types.EVENTS][class_id][Types.TEACHER]
                      == teacher_id]
        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.EVENTS][class_id][Types.TEACHER] = Types.UNAVAILABLE
        self.set_unsaved()

    def timetable_remove_class_subject_venue(self, class_, venue_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if class_id == class_ if time_table[day][slot][Types.EVENTS][class_id][Types.VENUE]
                      == venue_id]
        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.EVENTS][class_id][Types.VENUE] = Types.UNAVAILABLE
        self.set_unsaved()

    def timetable_change_class_subject_teacher(self, class_, subject_id, teacher_id):
        time_table = self._time_table_data[Types.TIMETABLE]

        for day in time_table:
            for slot in time_table[day]:
                if teacher_id in time_table[day][slot][Types.TEACHERS]:
                    return False

        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if class_id == class_ if time_table[day][slot][Types.EVENTS][class_id][Types.SUBJECT]
                      == subject_id]

        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.EVENTS][class_id][Types.TEACHER] = teacher_id
            time_table[day][slot][Types.DATA][Types.TEACHERS].append(teacher_id)
        self.set_unsaved()
        return True

    def timetable_change_class_subject_venue(self, class_, subject_id, venue_id):
        time_table = self._time_table_data[Types.TIMETABLE]

        for day in time_table:
            for slot in time_table[day]:
                if venue_id in time_table[day][slot][Types.VENUES]:
                    return False

        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot][Types.EVENTS]
                      if class_id == class_ if time_table[day][slot][Types.EVENTS][class_id][Types.SUBJECT]
                      == subject_id]

        for r in removables:
            day, slot, class_id = r
            time_table[day][slot][Types.EVENTS][class_id][Types.VENUE] = venue_id
            time_table[day][slot][Types.DATA][Types.VENUES].append(venue_id)
        self.set_unsaved()
        return True

    def timetable_remove_class(self, class_):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot]
                      if class_id == class_]
        for r in removables:
            day, slot, class_id = r
            del time_table[day][slot][class_id]
        self.set_unsaved()

    """ ========== TIMETABLE READ =========="""

    def timetable_get(self):
        return self._time_table_data[Types.TIMETABLE]

    def timetable_get_days_per_cycle(self):
        return self._time_table_data[Types.DAYS_PER_CYCLE]

    def timetable_get_slots_per_day(self):
        return self._time_table_data[Types.SLOTS_PER_DAY]

    def timetable_get_name(self):
        return self._time_table_data[Types.TIMETABLE_NAME]

    def timetable_get_institution_type(self):
        return self._time_table_data[Types.INSTITUTION_TYPE]

    def timetable_get_institution_name(self):
        return self._time_table_data[Types.INSTITUTION_NAME]

    def timetable_get_time_slot_length(self):
        return self._time_table_data[Types.TIME_SLOT_LENGTH]

    # =============================== GENERATOR FUNCTIONS ============================= #

    def generate(self):
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()
        data = TimetableTempDataSecondary(self._time_table_data[Types.CLASSES],
                                          self._time_table_data[Types.SUBJECTS],
                                          self._time_table_data[Types.TEACHERS],
                                          self._time_table_data[Types.DAYS_PER_CYCLE],
                                          self._time_table_data[Types.BREAKING_SLOTS],
                                          self._time_table_data[Types.BLOCK_SLOTS],
                                          self._time_table_data[Types.TIMETABLE])
        generator = SecondarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}
        self.set_generated()

    def generate_patches(self):
        data = TimetableTempDataSecondary(self._patches,
                                          self._time_table_data[Types.SUBJECTS],
                                          self._time_table_data[Types.TEACHERS],
                                          self._time_table_data[Types.DAYS_PER_CYCLE],
                                          self._time_table_data[Types.BREAKING_SLOTS], {},
                                          self._time_table_data[Types.TIMETABLE])
        generator = SecondarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}
        self.set_generated()

    def get_possible_slots(self, class_id: str, subject_venue: str,
                           time_slots: int, time_slots_daily: int,
                           teacher: str):
        data = TimetableTempDataSecondary(self._time_table_data[Types.CLASSES],
                                          self._time_table_data[Types.SUBJECTS],
                                          self._time_table_data[Types.TEACHERS],
                                          self._time_table_data[Types.DAYS_PER_CYCLE],
                                          self._time_table_data[Types.BREAKING_SLOTS],
                                          self._time_table_data[Types.BLOCK_SLOTS],
                                          self.timetable_init_timetable())
        generator = SecondarySchool(data)
        time_table = generator.generate()
        return generator.possible_slots(class_id, subject_venue, time_slots,
                                        time_slots_daily, teacher, time_table)

    # ======================================= CLASSES ================================== #

    def add_class(self, name: str, venue: str,
                  subjects: dict):
        class_id = str(self._time_table_data[Types.SEQUENCE][Types.CLASSES] + 1)
        self._time_table_data[Types.CLASSES][class_id] = (
            Formats.format_class_primary(name, venue, subjects)
        )
        self._time_table_data[Types.SEQUENCE][Types.CLASSES] = int(class_id)
        self.set_unsaved()

    def class_exists(self, name: str):
        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if classes[class_][Types.NAME] == name:
                return True
        return False

    def class_change_data(self, class_id: str, dtype: str, value):
        self._time_table_data[Types.CLASSES][class_id][dtype] = value
        self.set_unsaved()

    def class_remove(self, class_id: str):
        del self._time_table_data[Types.CLASSES][class_id]
        self.set_unsaved()
        self.set_not_generated()
        self.timetable_remove_class(class_id)

    def class_remove_data(self, class_id: str, dtype: str):
        if dtype == Types.VENUE:
            self._time_table_data[Types.CLASSES][class_id][dtype] = "unavailable"
        else:
            self._time_table_data[Types.CLASSES][class_id][dtype] = {}
        self.unsaved_changes = True
        self.non_generated_changes = True

    def class_add_subject(self, class_id: str, subject_id: str,
                          time_slots: int, slots_per_day,
                          teacher_id: str):
        self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id] = (
            Formats.format_class_subject_secondary(teacher_id, time_slots, slots_per_day)
        )
        self.timetable_add_patch(class_id, teacher_id, subject_id, time_slots, slots_per_day)
        self.set_unsaved()
        self.set_not_generated()

    def class_add_subject_teacher(self, class_id: str, teacher_id: str,
                                  subject_id: str):
        if self.timetable_change_class_subject_teacher(class_id, subject_id, teacher_id):
            try:
                subject = self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id]
                subject[Types.TEACHER] = teacher_id
            except Exception as e:
                logger.warning(str(e))

            self.set_unsaved()
            self.set_not_generated()
            return True
        else:
            return False

    def class_add_subject_venue(self, class_id: str, venue_id: str,
                                subject_id: str):
        if self.timetable_change_class_subject_venue(class_id, subject_id, venue_id):
            try:
                subject = self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id]
                subject[Types.VENUE] = venue_id
            except Exception as e:
                logger.warning(str(e))

            self.set_unsaved()
            self.set_not_generated()
            return True
        else:
            return False

    def class_remove_subject(self, class_id: str, subject_id: str):
        try:
            del self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id]
        except Exception as e:
            logger.warning(str(e))

        self.set_unsaved()
        self.set_not_generated()
        self.timetable_remove_patch(class_id, subject_id)
        self.timetable_remove_class_subject(class_id, subject_id)

    def class_remove_subject_teacher(self, class_id: str, teacher_id: str):
        try:
            subjects = self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS]
            for subject in subjects:
                subject_data = subjects[subject]
                if subject_data[Types.TEACHER] == teacher_id:
                    subject_data[Types.TEACHER] = Types.UNAVAILABLE
        except Exception as e:
            logger.warning(str(e))

        self.set_unsaved()
        self.set_not_generated()
        self.timetable_remove_class_subject_teacher(class_id, teacher_id)

    def class_get_all(self):
        classes_data = self._time_table_data[Types.CLASSES]

        classes = [Class(class_, classes_data[class_][Types.NAME], classes_data[class_][Types.VENUE],
                         classes_data[class_][Types.SUBJECTS]) for class_ in classes_data]
        return classes

    def class_get(self, class_id):
        class_data = self._time_table_data[Types.CLASSES][class_id]
        return Class(class_id, class_data[Types.NAME], class_data[Types.VENUE], class_data[Types.SUBJECTS])

    # =================================== VENUES  ================================ #

    def add_venue(self, name: str, location: list,
                  location_description: str):
        venue_id = str(self._time_table_data[Types.SEQUENCE][Types.VENUES] + 1)
        self._time_table_data[Types.VENUES][venue_id] = (
            Formats.format_venue(name, location, location_description)
        )
        self._time_table_data[Types.SEQUENCE][Types.VENUES] = int(venue_id)
        self.set_unsaved()

    def venue_exists(self, name: str):
        venues = self._time_table_data[Types.VENUES]
        for venue in venues:
            if venues[venue][Types.NAME] == name:
                return True
        return False

    def venue_remove(self, venue_id):

        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if venue_id == classes[class_][Types.VENUE]:
                self.class_remove_data(class_, Types.VENUE)

        subjects = self._time_table_data[Types.SUBJECTS]

        for subject in subjects:
            if venue_id == subjects[subject][Types.SUBJECT_PRIMARY_VENUE]:
                self.subject_remove_data(subject, Types.SUBJECT_PRIMARY_VENUE)

        del self._time_table_data[Types.VENUES][venue_id]
        self.set_unsaved()
        self.set_not_generated()

    def venue_change_data(self, venue_id: str, dtype: str, value):
        self._time_table_data[Types.VENUES][venue_id][dtype] = value
        self.set_unsaved()

    def venue_get_all(self):
        venues_data = self._time_table_data[Types.VENUES]
        venues = [Venue(venue, venues_data[venue]["name"],
                        venues_data[venue]["location"],
                        venues_data[venue]["location_description"]) for venue in venues_data]
        return venues

    def venue_get(self, venue_id: str):
        venue_data = self._time_table_data[Types.VENUES][venue_id]
        return Venue(venue_id, venue_data["name"], venue_data["location"],
                     venue_data["location_description"])

    # ======================================== SUBJECTS =================================== #

    def add_subject(self, name: str,
                    primary_venue: str):
        subject_id = str(self._time_table_data[Types.SEQUENCE][Types.SUBJECTS] + 1)
        self._time_table_data[Types.SUBJECTS][subject_id] = (
            Formats.format_subject_primary(name, primary_venue)
        )
        self._time_table_data[Types.SEQUENCE][Types.SUBJECTS] = int(subject_id)
        self.set_unsaved()

    def subject_exits(self, name: str):
        subjects = self._time_table_data[Types.SUBJECTS]

        for subject in subjects:
            if subjects[subject][Types.NAME] == name:
                return True
        return False

    def subject_remove(self, subject_id):
        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if subject_id in classes[class_][Types.SUBJECTS]:
                self.class_remove_subject(class_, subject_id)
        self.timetable_remove_subject(subject_id)
        del self._time_table_data[Types.SUBJECTS][subject_id]
        self.set_unsaved()
        self.set_not_generated()

    def subject_change_data(self, subject_id: str, dtype: str, value):
        self._time_table_data[Types.SUBJECTS][subject_id][dtype] = value
        self.set_unsaved()

    def subject_remove_data(self, subject_id: str, dtype: str):
        if dtype == Types.SUBJECT_PRIMARY_VENUE:
            self._time_table_data[Types.SUBJECTS][subject_id][dtype] = "unavailable"
        self.set_unsaved()

    def subject_get_all(self):
        subjects_data = self._time_table_data[Types.SUBJECTS]
        subjects = [Subject(subject, subjects_data[subject][Types.NAME],
                            subjects_data[subject]["primary_venue"])
                    for subject in subjects_data]
        return subjects

    def subject_get(self, subject_id: str):
        subject_data = self._time_table_data[Types.SUBJECTS][subject_id]
        return Subject(subject_id, subject_data[Types.NAME],
                       subject_data["primary_venue"])

    def subject_get_classes(self, subject_id: str):
        classes_data = self._time_table_data[Types.CLASSES]

        classes = [Class(class_, classes_data[class_][Types.NAME], classes_data[class_][Types.VENUE],
                         classes_data[class_][Types.SUBJECTS]) for class_ in classes_data
                   if subject_id in classes_data[class_][Types.SUBJECTS]]
        return classes

    # ======================================== SUBJECTS =================================== #

    def add_teacher(self, name: str):
        teacher_id = str(self._time_table_data[Types.SEQUENCE][Types.TEACHERS] + 1)
        self._time_table_data[Types.TEACHERS][teacher_id] = (
            Formats.format_teacher_secondary(name)
        )
        self._time_table_data[Types.SEQUENCE][Types.TEACHERS] = int(teacher_id)
        self.set_unsaved()

    def teacher_exits(self, name: str):
        teachers = self._time_table_data[Types.TEACHERS]

        for teacher in teachers:
            if teachers[teacher][Types.NAME] == name:
                return True
        return False

    def teacher_remove(self, teacher_id):
        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            for subject_id in classes[class_][Types.SUBJECTS]:
                if teacher_id == classes[class_][Types.SUBJECTS][subject_id][Types.TEACHER]:
                    self.class_remove_subject_teacher(class_, teacher_id)

        self.timetable_remove_teacher(teacher_id)
        del self._time_table_data[Types.TEACHERS][teacher_id]
        self.set_unsaved()
        self.set_not_generated()

    def teacher_change_name(self, teacher_id: str, new_name: str):
        self._time_table_data[Types.TEACHERS][teacher_id][Types.NAME] = new_name
        self.set_unsaved()

    def teacher_get_all(self):
        teachers_data = self._time_table_data[Types.TEACHERS]
        teachers = [Teacher(teacher, teachers_data[teacher][Types.NAME])
                    for teacher in teachers_data]
        return teachers

    def teacher_get(self, teacher_id: str):
        teacher_data = self._time_table_data[Types.TEACHERS][teacher_id]
        return Teacher(teacher_id, teacher_data[Types.NAME])

    # ============================ BLOCKS =================================

    def add_block(self, block_name: str, subjects: dict, classes: list, length: int):
        block_id = "b" + str(int(self._time_table_data[Types.SEQUENCE][Types.BLOCKS][1:]) + 1)
        self._time_table_data[Types.BLOCKS][block_id] = (
            Formats.format_block_secondary(block_name, subjects, classes, length)
        )
        self._time_table_data[Types.SEQUENCE][Types.BLOCKS] = int(block_id[1:])
        self.set_unsaved()
        self.set_not_generated()

    def block_remove(self, block_id):
        del self._time_table_data[Types.BLOCKS][block_id]
        self.set_unsaved()
        self.set_not_generated()

    def block_change_name(self, block_id: str, new_name: str):
        self._time_table_data[Types.BLOCKS][block_id][Types.NAME] = new_name
        self.set_unsaved()

    def block_change_size(self, block_id: str, new_size: int):
        self._time_table_data[Types.BLOCKS][block_id]["time_slots"] = new_size
        self.set_unsaved()
        self.set_not_generated()

    def block_get_all(self):
        blocks_data = self._time_table_data[Types.BLOCKS]
        blocks = [Block(block, blocks_data[block][Types.NAME], blocks_data[block][Types.SUBJECTS],
                        blocks_data[block][Types.CLASSES], blocks_data[block]["time_slots"])
                  for block in blocks_data]
        return blocks

    def block_get(self, block_id: str):
        block_data = self._time_table_data[Types.BLOCKS][block_id]
        return Block(block_id, block_data[Types.NAME], block_data[Types.SUBJECTS],
                     block_data[Types.CLASSES], block_data["time_slots"])


class TertiaryBuilder(QObject):
    generated = Signal(bool)
    saved = Signal(bool)

    def __init__(self, file_path: str,
                 init_data: TimeTableInitData = None):
        super().__init__()

        try:
            file = open(file_path)
            time_table_data = json.loads(file.read())
            file.close()
        except Exception as e:
            logger.warning(str(e))
            time_table_data = None

        self._time_table_data = ({} if time_table_data is None else time_table_data)
        if not self._time_table_data:
            self.timetable_init_headers(init_data)

        self._init_data = init_data
        self.save_path = file_path
        self.unsaved_changes = False
        self.non_generated_changes = False
        self._patches = {}

    def set_saved(self):
        self.unsaved_changes: bool = False
        self.saved.emit(True)

    def set_generated(self):
        self.non_generated_changes: bool = False
        self.generated.emit(True)

    def set_unsaved(self):
        self.unsaved_changes: bool = True
        self.saved.emit(False)

    def set_not_generated(self):
        self.non_generated_changes: bool = True
        self.generated.emit(False)

    def is_saved(self) -> bool:
        return self.unsaved_changes

    def is_generated(self) -> bool:
        return self.non_generated_changes

    def get_file(self):
        return self.save_path

    def reload(self):
        file = open(self.save_path)
        time_table_data = json.loads(file.read())
        file.close()

        self._time_table_data: dict = ({} if time_table_data is None else time_table_data)
        if not self._time_table_data:
            self.timetable_init_headers(self._init_data)
        self.set_saved()

    def timetable_init_headers(self, data: TimeTableInitData):
        self._time_table_data[Types.TIMETABLE_NAME] = data.timetable_name
        self._time_table_data[Types.INSTITUTION_TYPE] = data.institution_type
        self._time_table_data[Types.INSTITUTION_NAME] = data.school_name
        self._time_table_data[Types.TIME_SLOT_LENGTH] = data.time_slot_length
        self._time_table_data[Types.DAYS_PER_CYCLE] = data.days_per_cycle
        self._time_table_data[Types.SLOTS_PER_DAY] = data.slots_per_day
        self._time_table_data[Types.SEQUENCE] = {
            Types.COURSES: 0,
            Types.MODULES: 0,
            Types.VENUES: 0,
            Types.LECTURERS: 0,
            Types.BLOCKS: 0
        }
        self._time_table_data[Types.BREAKING_SLOTS] = data.break_slots

        self._time_table_data[Types.COURSES] = {}
        self._time_table_data[Types.MODULES] = {}
        self._time_table_data[Types.VENUES] = {"unavailable": {"name": "Unavailable", "location": [0, 0],
                                                               "location_description": "Unavailable"}}
        self._time_table_data[Types.LECTURERS] = {"unavailable": {"name": "Unavailable"}}
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()

    def timetable_init_timetable(self):
        try:
            time_table = {day: {slot: {} for slot in range(1, self._time_table_data[Types.SLOTS_PER_DAY] + 1)}
                          for day in range(1, self._time_table_data[Types.DAYS_PER_CYCLE] + 1)}

            breaks = self._time_table_data[Types.BREAKING_SLOTS]
            for day in time_table:
                for break_ in breaks:
                    time_slots = breaks[break_]
                    for time_slot in time_slots:
                        time_table[day][time_slot] = break_
            return json.loads(json.dumps(time_table))
        except Exception as e:
            logger.critical(f"Error: {str(e)}")
            return {}

    def timetable_change_header(self, header: str, value):
        self._time_table_data[header] = value
        self.set_unsaved()

    def timetable_reset(self):
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()
        self.set_unsaved()

    def timetable_save(self):
        data = json.dumps(self._time_table_data)
        with open(self.save_path, "w") as tbl:
            tbl.write(data)
        self.set_saved()

    def timetable_add_patch(self, module_id: str):
        patch = Formats.format_module(self._time_table_data[Types.MODULES][module_id][Types.NAME],
                                      self._time_table_data[Types.MODULES][module_id][Types.CODE],
                                      self._time_table_data[Types.MODULES][module_id][Types.LECTURER],
                                      self._time_table_data[Types.MODULES][module_id][Types.COURSES],
                                      self._time_table_data[Types.MODULES][module_id][Types.VENUES],
                                      self._time_table_data[Types.MODULES][module_id]["time_slots"],
                                      self._time_table_data[Types.MODULES][module_id]["slots_per_day"])
        self._patches[module_id] = patch

    def timetable_remove_patch(self, module_id):
        if module_id in self._patches:
            del self._patches[module_id]

    def timetable_remove_module(self, module):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, module_id] for day in time_table
                      for slot in time_table[day] for module_id in time_table[day][slot]
                      if not isinstance(time_table[day][slot], str)
                      if module_id == module]
        for r in removables:
            day, slot, course_id = r
            del time_table[day][slot][module]
        self.set_unsaved()

    def timetable_remove_venue(self, venue_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, module_id] for day in time_table
                      for slot in time_table[day] for module_id in time_table[day][slot]
                      if not isinstance(time_table[day][slot], str)
                      if time_table[day][slot][module_id][Types.VENUE] == venue_id]
        for r in removables:
            day, slot, module_id = r
            time_table[day][slot][module_id][Types.VENUE] = Types.UNAVAILABLE
        self.set_unsaved()

    def timetable_remove_module_venue(self, module, venue_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, module_id] for day in time_table
                      for slot in time_table[day] for module_id in time_table[day][slot]
                      if module_id == module if time_table[day][slot][module_id][Types.VENUE]
                      == venue_id]
        for r in removables:
            day, slot, module_id = r
            time_table[day][slot][module_id][Types.VENUE] = Types.UNAVAILABLE
        self.set_unsaved()

    def timetable_change_module_venue(self, module, old_venue_id, venue_id):
        time_table = self._time_table_data[Types.TIMETABLE]

        for day in time_table:
            for slot in time_table[day]:
                if module in time_table[day][slot]:
                    for module_ in time_table[day][slot]:
                        if venue_id == time_table[day][slot][module_][Types.VENUE] and module_ != module:
                            return False

        if old_venue_id is not None:
            changes = [[day, slot, module_id] for day in time_table
                       for slot in time_table[day] for module_id in time_table[day][slot]
                       if module_id == module if time_table[day][slot][Types.VENUE] == old_venue_id]

            for r in changes:
                day, slot, module_id = r
                time_table[day][slot][module_id][Types.VENUE] = venue_id
        self.set_unsaved()
        return True

    def timetable_change_module_lecturer(self, module, lecturer_id):

        time_table = self._time_table_data[Types.TIMETABLE]

        for day in time_table:
            for slot in time_table[day]:
                if module in time_table[day][slot]:
                    for module_ in time_table[day][slot]:
                        if (self._time_table_data[Types.MODULES][module_][Types.LECTURER] == lecturer_id
                                and module_ != module):
                            return False
        self.set_unsaved()
        return True

    def timetable_remove_course(self, course_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, module_id] for day in time_table
                      for slot in time_table[day] for module_id in time_table[day][slot]
                      for course in time_table[day][slot][module_id][Types.COURSES]
                      if self.course_get(course_id).short_name == course.split("-")[0]]
        for r in removables:
            day, slot, module_id = r
            time_table[day][slot][module_id][Types.COURSES].remove(course_id)
        self.set_unsaved()

    """ ========== TIMETABLE READ =========="""

    def timetable_get(self):
        return self._time_table_data[Types.TIMETABLE]

    def timetable_get_days_per_cycle(self):
        return self._time_table_data[Types.DAYS_PER_CYCLE]

    def timetable_get_slots_per_day(self):
        return self._time_table_data[Types.SLOTS_PER_DAY]

    def timetable_get_name(self):
        return self._time_table_data[Types.TIMETABLE_NAME]

    def timetable_get_institution_type(self):
        return self._time_table_data[Types.INSTITUTION_TYPE]

    def timetable_get_institution_name(self):
        return self._time_table_data[Types.INSTITUTION_NAME]

    def timetable_get_time_slot_length(self):
        return self._time_table_data[Types.TIME_SLOT_LENGTH]

    # =============================== GENERATOR FUNCTIONS ============================= #

    def generate(self):
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()
        data = TimetableTempDataTertiary(self._time_table_data[Types.MODULES],
                                         self._time_table_data[Types.COURSES],
                                         self._time_table_data[Types.DAYS_PER_CYCLE],
                                         self._time_table_data[Types.SLOTS_PER_DAY],
                                         self._time_table_data[Types.BREAKING_SLOTS],
                                         self._time_table_data[Types.TIMETABLE])
        generator = TertiarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}
        self.set_generated()

    def generate_patches(self):
        pass

    def get_possible_slots(self, module_id: str, venues: list,
                           time_slots: int, time_slots_daily: int,
                           lecturer: str):
        data = TimetableTempDataTertiary(self._time_table_data[Types.MODULES],
                                         self._time_table_data[Types.COURSES],
                                         self._time_table_data[Types.DAYS_PER_CYCLE],
                                         self._time_table_data[Types.SLOTS_PER_DAY],
                                         self._time_table_data[Types.BREAKING_SLOTS],
                                         self.timetable_init_timetable())
        generator = TertiarySchool(data)
        time_table = generator.generate()
        return generator.possible_slots(module_id, venues, time_slots,
                                        time_slots_daily, lecturer, time_table)

    # ======================================= COURSES ================================== #

    def add_course(self, name: str, short_name: str):
        course_id = str(self._time_table_data[Types.SEQUENCE][Types.COURSES] + 1)
        self._time_table_data[Types.COURSES][course_id] = (
            Formats.format_course(name, short_name)
        )
        self._time_table_data[Types.SEQUENCE][Types.COURSES] = int(course_id)
        self.set_unsaved()

    def course_exists(self, name: str):
        courses = self._time_table_data[Types.COURSES]
        for course_id in courses:
            if courses[course_id][Types.NAME] == name:
                return True
        return False

    def course_change_data(self, course_id: str, dtype: str, value):
        self._time_table_data[Types.COURSES][course_id][dtype] = value
        self.set_unsaved()

    def course_remove(self, course_id: str):
        del self._time_table_data[Types.COURSES][course_id]
        self.modules_remove_course(course_id)
        self.timetable_remove_course(course_id)
        self.set_unsaved()
        self.set_not_generated()

    def course_remove_data(self, course_id: str, dtype: str):
        if dtype == Types.VENUE:
            self._time_table_data[Types.COURSES][course_id][dtype] = "unavailable"
        else:
            self._time_table_data[Types.COURSES][course_id][dtype] = ""
        self.set_unsaved()

    def course_get_all(self):
        courses_data = self._time_table_data[Types.COURSES]

        courses = [Course(course_id, courses_data[course_id][Types.NAME],
                          courses_data[course_id][Types.SHORT_NAME]) for course_id in courses_data]
        return courses

    def course_get(self, course_id):
        course_data = self._time_table_data[Types.COURSES][course_id]
        return Course(course_id, course_data[Types.NAME], course_data[Types.SHORT_NAME])

    # =================================== VENUES  ================================ #

    def add_venue(self, name: str, location: list,
                  location_description: str):
        venue_id = str(self._time_table_data[Types.SEQUENCE][Types.VENUES] + 1)
        self._time_table_data[Types.VENUES][venue_id] = (
            Formats.format_venue(name, location, location_description)
        )
        self._time_table_data[Types.SEQUENCE][Types.VENUES] = int(venue_id)
        self.set_unsaved()

    def venue_exists(self, name: str):
        venues = self._time_table_data[Types.VENUES]
        for venue in venues:
            if venues[venue][Types.NAME] == name:
                return True
        return False

    def venue_remove(self, venue_id):
        modules = self._time_table_data[Types.MODULES]

        for module in modules:
            if venue_id in modules[module][Types.VENUES]:
                modules[module][Types.VENUES].remove(venue_id)

        del self._time_table_data[Types.VENUES][venue_id]
        self.set_unsaved()
        self.set_not_generated()

    def venue_change_data(self, venue_id: str, dtype: str, value):
        self._time_table_data[Types.VENUES][venue_id][dtype] = value
        self.set_unsaved()

    def venue_get_all(self):
        venues_data = self._time_table_data[Types.VENUES]
        venues = [Venue(venue, venues_data[venue]["name"],
                        venues_data[venue]["location"],
                        venues_data[venue]["location_description"]) for venue in venues_data]
        return venues

    def venue_get(self, venue_id: str):
        venue_data = self._time_table_data[Types.VENUES][venue_id]
        return Venue(venue_id, venue_data["name"], venue_data["location"],
                     venue_data["location_description"])

    # ======================================== MODULES =================================== #

    def add_module(self, name: str, code: str, lecturer: str, courses: dict, venues: list,
                   time_slots: int, slots_per_day: int):
        module_id = str(self._time_table_data[Types.SEQUENCE][Types.MODULES] + 1)
        self._time_table_data[Types.MODULES][module_id] = (
            Formats.format_module(name, code, lecturer, courses, venues, time_slots, slots_per_day)
        )
        self._time_table_data[Types.SEQUENCE][Types.MODULES] = int(module_id)
        self.set_unsaved()

    def module_exits(self, name: str):
        modules = self._time_table_data[Types.MODULES]

        for module in modules:
            if modules[module][Types.NAME] == name:
                return True
        return False

    def module_remove(self, module_id):
        self.timetable_remove_module(module_id)
        del self._time_table_data[Types.MODULES][module_id]
        self.set_unsaved()
        self.set_not_generated()

    def module_change_data(self, module_id: str, dtype: str, value):
        self._time_table_data[Types.MODULES][module_id][dtype] = value
        self.set_unsaved()

    def module_add_lecturer(self, lecturer_id: str, module_id: str):

        if self.timetable_change_module_lecturer(module_id, lecturer_id):
            try:
                module = self._time_table_data[Types.MODULES][module_id]
                module[Types.LECTURER] = lecturer_id
            except Exception as e:
                logger.warning(str(e))

            self.set_unsaved()
            self.set_not_generated()
            return True
        else:
            return False

    def module_add_venue(self, venue_id: str, module_id: str):
        try:
            module = self._time_table_data[Types.MODULES][module_id]
            module[Types.VENUES].append(venue_id)
        except Exception as e:
            logger.warning(str(e))
            return False
        self.set_unsaved()
        self.set_not_generated()
        return True

    def module_update(self, module_id: str, name: str, code: str, lecturer: str,
                      time_slots: int, slots_per_day: int):
        module = self._time_table_data[Types.MODULES][module_id]
        module["name"] = name
        module["code"] = code
        module["lecturer"] = lecturer
        module["time_slots"] = time_slots
        module["slots_per_day"] = slots_per_day
        self.set_unsaved()

    def module_add_course(self, course_id: str, module_id: str, level: str, course_module_code: str):
        try:
            if course_id not in self._time_table_data[Types.MODULES][module_id][Types.COURSES]:
                self._time_table_data[Types.MODULES][module_id][Types.COURSES][course_id] \
                    = Formats.format_module_course(level, course_module_code)
            self.set_unsaved()
            self.set_not_generated()
            return True
        except Exception as e:
            logger.warning(str(e))

    def module_remove_course(self, course_id: str, module_id: str):
        try:
            del self._time_table_data[Types.MODULES][module_id][Types.COURSES][course_id]
        except Exception as e:
            logger.warning(str(e))

        self.set_unsaved()
        self.set_not_generated()
        self.timetable_remove_patch(module_id)

    def modules_remove_course(self, course_id: str):
        try:
            modules = self._time_table_data[Types.MODULES]
            for module in modules:
                if course_id in module[Types.COURSES]:
                    del self._time_table_data[Types.MODULES][module][Types.COURSES][course_id]
        except Exception as e:
            logger.warning(str(e))

        self.set_unsaved()
        self.set_not_generated()

    def module_remove_lecturer(self, module_id: str):
        try:
            self._time_table_data[Types.MODULES][module_id][Types.LECTURER] = Types.UNAVAILABLE
        except Exception as e:
            logger.warning(str(e))

        self.set_unsaved()
        self.set_not_generated()

    def module_remove_venue(self, module_id, venue_id):
        self._time_table_data[Types.MODULES][module_id][Types.VENUES].remove(venue_id)
        self.set_unsaved()
        self.set_not_generated()

    def module_get_all(self):
        modules_data = self._time_table_data[Types.MODULES]
        modules = [Module(module, modules_data[module][Types.NAME],
                          modules_data[module][Types.CODE],
                          modules_data[module][Types.LECTURER],
                          modules_data[module][Types.COURSES],
                          modules_data[module][Types.VENUES],
                          modules_data[module]["time_slots"],
                          modules_data[module]["slots_per_day"])
                   for module in modules_data]
        return modules

    def module_get(self, module_id: str):
        module_data = self._time_table_data[Types.MODULES][module_id]
        return Module(module_id, module_data[Types.NAME],
                      module_data[Types.CODE],
                      module_data[Types.LECTURER],
                      module_data[Types.COURSES],
                      module_data[Types.VENUES],
                      module_data["time_slots"],
                      module_data["slots_per_day"])

    # ======================================== MODULES =================================== #

    def add_lecturer(self, name: str):
        lecturer_id = str(self._time_table_data[Types.SEQUENCE][Types.LECTURERS] + 1)
        self._time_table_data[Types.LECTURERS][lecturer_id] = (
            Formats.format_lecturer(name)
        )
        self._time_table_data[Types.SEQUENCE][Types.LECTURERS] = int(lecturer_id)
        self.set_unsaved()

    def lecturer_exits(self, name: str):
        lecturers = self._time_table_data[Types.LECTURERS]

        for lecturer in lecturers:
            if lecturers[lecturer][Types.NAME] == name:
                return True
        return False

    def lecturer_remove(self, lecturer_id):
        modules = self._time_table_data[Types.MODULES]
        for module_id in modules:
            if lecturer_id == modules[module_id][Types.LECTURER]:
                self.module_remove_lecturer(module_id)
        del self._time_table_data[Types.LECTURERS][lecturer_id]
        self.set_unsaved()
        self.set_not_generated()

    def lecturer_change_name(self, lecturer_id: str, new_name: str):
        self._time_table_data[Types.LECTURERS][lecturer_id][Types.NAME] = new_name
        self.set_unsaved()

    def lecturer_get_all(self):
        lecturers_data = self._time_table_data[Types.LECTURERS]
        lecturers = [Lecturer(lecturer, lecturers_data[lecturer][Types.NAME])
                     for lecturer in lecturers_data]
        return lecturers

    def lecturer_get(self, lecturer_id: str):
        lecturer_data = self._time_table_data[Types.LECTURERS][lecturer_id]
        return Lecturer(lecturer_id, lecturer_data[Types.NAME])
