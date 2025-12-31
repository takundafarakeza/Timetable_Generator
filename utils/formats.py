class Formats:

    @staticmethod
    def format_venue(name: str, location: list,
                     location_description: str):
        return {"name": name, "location": location,
                "location_description": location_description}

    @staticmethod
    def format_class_primary(name: str, venue: str,
                             subjects: dict):
        return {"name": name, "venue": venue,
                "subjects": subjects}

    @staticmethod
    def format_course(name: str, short_name: str):
        return {"name": name, "short_name": short_name}

    @staticmethod
    def format_class_subject_primary(time_slots: int,
                                     slots_per_day: int):
        return {"time_slots": time_slots, "slots_per_day": slots_per_day}

    @staticmethod
    def format_module_course(level: str, course_module_code: str):
        return {"level": level, "course_module_code": course_module_code}

    @staticmethod
    def format_subject_primary(name: str, primary_venue: str):
        return {"name": name,
                "primary_venue": primary_venue}

    @staticmethod
    def format_module(name: str, code: str, lecturer: str,
                      courses: dict, venues: list,
                      time_slots: int, slots_per_day: int):
        return {"name": name, "code": code, "lecturer": lecturer,
                "courses": courses, "venues": venues,
                "time_slots": time_slots, "slots_per_day": slots_per_day}

    @staticmethod
    def format_patch_primary(class_name: str, venue: str,
                             subject: str, time_slots: int,
                             slots_per_day: int):
        return {
            'name': class_name, 'venue': venue,
            'subjects': {
                subject: {
                    'time_slots': time_slots,
                    'slots_per_day': slots_per_day
                }
            }
        }

    @staticmethod
    def format_class_subject_secondary(teacher_id: str, time_slots: int,
                                       slots_per_day: int):
        return {"teacher": teacher_id, "time_slots": time_slots, "slots_per_day": slots_per_day}

    @staticmethod
    def format_patch_secondary(class_name: str, venue: str,
                               subject: str, time_slots: int,
                               slots_per_day: int, teacher: str):
        return {
            'name': class_name, 'venue': venue,
            'subjects': {
                subject: {
                    'teacher': teacher,
                    'time_slots': time_slots,
                    'slots_per_day': slots_per_day
                }
            }
        }

    @staticmethod
    def format_patch_tertiary(module_name: str, venue: str,
                              courses: dict, lecturer: str, time_slots: int,
                              slots_per_day: int):
        return {
            'name': module_name,
            'venue': venue,
            'lecturer': lecturer,
            'courses': courses,
            'time_slots': time_slots,
            'slots_per_day': slots_per_day
        }

    @staticmethod
    def format_teacher_secondary(name: str):
        return {"name": name}

    @staticmethod
    def format_lecturer(name: str):
        return {"name": name}

    @staticmethod
    def format_block_secondary(subject: str, length: int, classes: str,
                               teachers: str, venues: str):
        return {
            "subject": subject,
            "time_slots": length,
            "classes": classes,
            "teachers": teachers,
            "venues": venues
        }
