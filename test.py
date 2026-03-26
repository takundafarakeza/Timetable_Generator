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