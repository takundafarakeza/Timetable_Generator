from dataclasses import dataclass


@dataclass
class Class:
    id: str
    name: str
    venue: str
    subjects: dict


@dataclass
class Course:
    id: str
    name: str
    short_name: str


@dataclass
class Venue:
    id: str
    name: str
    location: list
    location_description: str


@dataclass
class Subject:
    id: str
    name: str
    primary_venue: str


@dataclass
class Module:
    id: str
    name: str
    code: str
    lecturer: str
    courses: dict
    venues: list
    time_slots: int
    slots_per_day: int


@dataclass
class Teacher:
    id: str
    name: str


@dataclass
class Lecturer:
    id: str
    name: str


@dataclass
class TimeTableInitData:
    timetable_name: str
    institution_type: str
    school_name: str
    time_slot_length: int
    days_per_cycle: int
    slots_per_day: int
    break_slots: list


@dataclass
class TimetableTempDataPrimary:
    classes: dict
    subjects: dict
    days_per_cycle: int
    breaks: dict
    time_table: dict


@dataclass
class TimetableTempDataSecondary:
    classes: dict
    subjects: dict
    teachers: dict
    days_per_cycle: int
    breaks: dict
    blocks: dict
    time_table: dict


@dataclass
class TimetableTempDataTertiary:
    modules: dict
    courses: dict
    days_per_cycle: int
    slots_per_day: int
    breaks: dict
    time_table: dict
