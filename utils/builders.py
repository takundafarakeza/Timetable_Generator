from . import Types, Formats
from .logger_config import logger
from .data import (Class, Venue, Subject,
                   TimeTableInitData, TimetableTemplateData)
from .generators import PrimarySchool
import json


class PrimarySchoolBuilder:
    def __init__(self, file_path: str,
                 init_data: TimeTableInitData = None):

        file = open(file_path)
        time_table_data = json.loads(file.read())
        file.close()

        self._time_table_data = ({} if time_table_data is None else time_table_data)
        if len(self._time_table_data) == 0:
            self.timetable_init_headers(init_data)

        self.save_path = file_path
        self.unsaved_changes = False
        self.non_generated_changes = False
        self._patches = {}

    def timetable_init_headers(self, data: TimeTableInitData):
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
        self.unsaved_changes = True

    def timetable_save(self):
        data = json.dumps(self._time_table_data)
        with open(self.save_path, "w") as tbl:
            tbl.write(data)
        self.unsaved_changes = False

    def timetable_get(self):
        return self._time_table_data[Types.TIMETABLE]

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

    def timetable_remove_class_subject(self, class_, subject_id):
        time_table = self._time_table_data[Types.TIMETABLE]
        removables = [[day, slot, class_id] for day in time_table
                      for slot in time_table[day] for class_id in time_table[day][slot]
                      if class_id == class_ if time_table[day][slot][class_id][Types.SUBJECT] == subject_id]
        for r in removables:
            day, slot, class_id = r
            del time_table[day][slot][class_id]

    # =============================== GENERATOR FUNCTIONS ============================= #

    def generate(self):
        self._time_table_data[Types.TIMETABLE] = self.timetable_init_timetable()
        data = TimetableTemplateData(self._time_table_data[Types.CLASSES],
                                     self._time_table_data[Types.SUBJECTS],
                                     self._time_table_data[Types.DAYS_PER_CYCLE],
                                     self._time_table_data[Types.BREAKING_SLOTS],
                                     self._time_table_data[Types.TIMETABLE])
        generator = PrimarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}
        self.non_generated_changes = False

    def generate_patches(self):
        data = TimetableTemplateData(self._patches,
                                     self._time_table_data[Types.SUBJECTS],
                                     self._time_table_data[Types.DAYS_PER_CYCLE],
                                     self._time_table_data[Types.BREAKING_SLOTS],
                                     self._time_table_data[Types.TIMETABLE])
        generator = PrimarySchool(data)
        self._time_table_data[Types.TIMETABLE] = generator.generate()
        self.timetable_save()
        self._patches = {}

    def get_possible_slots(self, class_id: str, subject_venue: str,
                           time_slots: int, time_slots_daily: int):
        data = TimetableTemplateData(self._time_table_data[Types.CLASSES],
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
                  subjects: list):
        class_id = str(self._time_table_data[Types.SEQUENCE][Types.CLASSES] + 1)
        self._time_table_data[Types.CLASSES][class_id] = (
            Formats.format_class_primary(name, venue, subjects)
        )
        self._time_table_data[Types.SEQUENCE][Types.CLASSES] = int(class_id)
        self.unsaved_changes = True
        self.non_generated_changes = True

    def class_exists(self, name: str):
        classes = self._time_table_data[Types.CLASSES]
        for class_ in classes:
            if classes[class_][Types.NAME] == name:
                return True
        return False

    def class_change_data(self, class_id: str, dtype: str, value):
        self._time_table_data[Types.CLASSES][class_id][dtype] = value
        self.unsaved_changes = True
        self.non_generated_changes = True

    def class_remove_data(self, class_id: str, dtype: str):
        if dtype == Types.VENUE:
            self._time_table_data[Types.CLASSES][class_id][dtype] = "unavailable"
        else:
            self._time_table_data[Types.CLASSES][class_id][dtype] = {}
        self.unsaved_changes = True
        self.non_generated_changes = True

    def class_add_subject(self, class_id: str, subject_id: str,
                          time_slots: int, slots_per_day):
        self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id] = (
            Formats.format_class_subject_primary(time_slots, slots_per_day)
        )
        self.timetable_add_patch(class_id, subject_id, time_slots, slots_per_day)
        self.unsaved_changes = True
        self.non_generated_changes = True

    def class_remove_subject(self, class_id: str, subject_id: str):
        try:
            del self._time_table_data[Types.CLASSES][class_id][Types.SUBJECTS][subject_id]
        except Exception as e:
            logger.warning(str(e))

        self.unsaved_changes = True
        self.non_generated_changes = True
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
        self.unsaved_changes = True
        self.non_generated_changes = True

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
        self.unsaved_changes = True
        self.non_generated_changes = True

    def venue_change_data(self, venue_id: str, dtype: str, value):
        self._time_table_data[Types.VENUES][venue_id][dtype] = value
        self.unsaved_changes = True
        self.non_generated_changes = True

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
        self.unsaved_changes = True
        self.non_generated_changes = True

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
        self.unsaved_changes = True
        self.non_generated_changes = True

    def subject_change_data(self, subject_id: str, dtype: str, value):
        self._time_table_data[Types.SUBJECTS][subject_id][dtype] = value
        self.unsaved_changes = True
        self.non_generated_changes = True

    def subject_remove_data(self, subject_id: str, dtype: str):
        if dtype == Types.SUBJECT_PRIMARY_VENUE:
            self._time_table_data[Types.SUBJECTS][subject_id][dtype] = "unavailable"
        self.unsaved_changes = True
        self.non_generated_changes = True

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
