from dataclasses import dataclass


@dataclass
class Class:
    id: str
    name: str
    venue: str
    subjects: list


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
class TimeTableInitData:
    school_name: str
    time_slot_length: int
    days_per_cycle: int
    slots_per_day: int
    break_slots: list


@dataclass
class TimetableTemplateData:
    classes: dict
    subjects: dict
    days_per_cycle: int
    breaks: dict
    time_table: dict
