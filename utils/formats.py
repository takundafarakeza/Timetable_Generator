class Formats:

    @staticmethod
    def format_venue(name: str, location: list,
                     location_description: str):
        return {"name": name, "location": location,
                "location_description": location_description}

    @staticmethod
    def format_class_primary(name: str, venue: str,
                             subjects: list):
        return {"name": name, "venue": venue,
                "subjects": subjects}

    @staticmethod
    def format_class_subject_primary(time_slots: int,
                                     slots_per_day: int):
        return {"time_slots": time_slots, "slots_per_day": slots_per_day}

    @staticmethod
    def format_subject_primary(name: str, primary_venue: str):
        return {"name": name,
                "primary_venue": primary_venue}

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
