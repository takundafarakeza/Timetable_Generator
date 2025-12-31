from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDoubleValidator
from typing import Union
from widgets import RemovableTableItem, MessageBox
from functools import partial
from utils.builders import PrimaryBuilder, SecondaryBuilder, TertiaryBuilder
from utils import Types
from utils.logger_config import logger
from ui import (ui_add_module_dialog, ui_add_class_dialog,
                ui_add_venue_dialog, ui_add_course_dialog, ui_add_subject_dialog,
                ui_add_teacher_dialog, ui_add_lecturer_dialog,
                ui_add_module_data_dialog, ui_add_class_data_dialog,
                ui_add_class_primary_data_dialog)


class AddModuleWindow(QDialog):

    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, edit: bool = False,
                 module_id: str = None):
        super().__init__()
        self.ui = ui_add_module_dialog.Ui_AddModule()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.edit = edit
        self.module_id = module_id
        self.builder = builder
        self.timetable_days_per_cycle = self.builder.timetable_get_days_per_cycle()
        self.timetable_slots_per_day = self.builder.timetable_get_slots_per_day()

        self.module_name = self.ui.module_name
        self.module_code = self.ui.module_code
        self.module_lecturer = self.ui.module_lecturer
        self.module_slots_per_cycle = self.ui.slots_per_cycle
        self.module_slots_per_day = self.ui.slots_per_day
        self.save_btn = self.ui.module_save

        self.set_slot_max()
        self.save_btn.clicked.connect(self.save)
        self.ui.close_btn.clicked.connect(self.close)
        self.populate_lecturers()

        if self.edit:
            module_data = self.builder.module_get(self.module_id)
            self.module_name.setText(module_data.name)
            self.module_code.setText(module_data.code)
            self.module_lecturer.setCurrentText(self.builder.lecturer_get(module_data.lecturer).name)
            self.module_slots_per_cycle.setValue(module_data.time_slots)
            self.module_slots_per_day.setValue(module_data.slots_per_day)

    def clear(self):
        self.module_name.clear()
        self.module_code.clear()
        self.module_slots_per_day.setValue(0)
        self.module_slots_per_cycle.setValue(0)

    def set_slot_max(self):
        self.module_slots_per_cycle.setMaximum(self.timetable_days_per_cycle *
                                               self.timetable_slots_per_day)
        self.module_slots_per_day.setMaximum(self.timetable_slots_per_day)

    def populate_lecturers(self):
        lecturers = self.builder.lecturer_get_all()
        self.module_lecturer.clear()

        for lecturer in lecturers:
            self.module_lecturer.addItem(lecturer.name, userData=lecturer.id)

    def validate(self):
        return (self.module_name.text() and self.module_code.text()
                and self.module_lecturer.currentText() != "Lecturer")

    def save(self):
        if self.validate():
            if not self.edit:
                self.builder.add_module(self.module_name.text(), self.module_code.text(),
                                        self.module_lecturer.currentData(), {}, [],
                                        self.module_slots_per_cycle.value(), self.module_slots_per_day.value())
            else:
                self.builder.module_update(self.module_id, self.module_name.text(), self.module_code.text(),
                                           self.module_lecturer.currentData(), self.module_slots_per_cycle.value(),
                                           self.module_slots_per_day.value())
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")
            return

        self.saved.emit(Types.MODULES)
        self.clear()
        self.close()


class AddModuleDataWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, module_id: str):
        super().__init__()
        self.ui = ui_add_module_data_dialog.Ui_AddModule()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.module_id = module_id
        self.ui.module_name.setText(self.builder.module_get(self.module_id).name)

        self.module_courses_table = self.ui.module_courses_table
        self.module_course_select = self.ui.module_course_select
        self.module_course_module_code = self.ui.module_course_module_code
        self.module_course_level = self.ui.module_course_level_select
        self.module_course_add_btn = self.ui.module_add_course_btn
        self.module_venues_table = self.ui.module_venues_table
        self.module_venue_select = self.ui.module_course_select
        self.module_venue_add_btn = self.ui.module_add_venue_btn

        self.module_course_level.lineEdit().setPlaceholderText("Level")
        self.module_course_select.lineEdit().setPlaceholderText("Course")
        self.ui.module_save.clicked.connect(self.save)
        self.ui.close_btn.clicked.connect(self.save)
        self.ui.module_add_course_btn.clicked.connect(self.add_course)
        self.ui.module_add_venue_btn.clicked.connect(self.add_venue)
        self.module_courses_table.setShowGrid(False)
        self.module_venues_table.setShowGrid(False)

        self.venues_populate()
        self.venues_select_populate()
        self.courses_populate()
        self.courses_select_populate()

    def clear(self):
        self.module_course_level.clear()
        self.module_course_module_code.clear()
        self.module_course_select.clear()
        self.module_venue_select.clear()
        self.module_courses_table.clearContents()
        self.module_venues_table.clearContents()

    def close(self, /):
        self.clear()
        super().close()

    def save(self):
        self.saved.emit(Types.MODULES)
        self.close()

    def add_venue(self):
        venue = self.module_venue_select.currentData()
        module_venues = self.builder.module_get(self.module_id).venues

        if venue in module_venues:
            MessageBox().warning(self, "Already Exits", "This venue is already used!")
            return
        else:
            if self.builder.module_add_venue(venue, self.module_id):
                self.venues_populate()
            else:
                MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")

    def add_course(self):
        course = self.module_course_select.currentData()
        module_courses = self.builder.module_get(self.module_id).courses

        if course in module_courses:
            MessageBox().warning(self, "Already Exits", "This course is already added!")
            return
        else:
            course_module_code = (self.ui.module_course_module_code.text() if
                                  self.ui.module_course_module_code.text() else
                                  self.builder.module_get(self.module_id).code)

            if self.builder.module_add_course(course, self.module_id, self.module_course_level.currentText(),
                                              course_module_code):
                self.courses_populate()
                self.module_course_module_code.clear()
                self.module_course_level.setCurrentText("")
                self.venues_select_populate()
                self.courses_select_populate()
            else:
                MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")

    def venues_select_populate(self):
        venues = self.builder.venue_get_all()
        self.module_venue_select.clear()

        for venue in venues:
            self.module_venue_select.addItem(venue.name, userData=venue.id)

    def courses_select_populate(self):
        courses = self.builder.course_get_all()
        self.module_course_select.clear()

        for course in courses:
            self.module_course_select.addItem(course.name, userData=course.id)

    def venues_populate(self):
        venues = self.builder.module_get(self.module_id).venues
        venues = [self.builder.venue_get(venue) for venue in venues]
        self.module_venues_table.clearContents()
        self.module_venues_table.setRowCount(0)

        for venue in venues:
            row = self.module_venues_table.rowCount()
            self.module_venues_table.insertRow(row)
            self.module_venues_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(venue.name)
            item.set_text(venue.location_description)
            remove_func = partial(self.delete_venue, self.module_id, venue.id)
            item.remove_btn.clicked.connect(remove_func)
            self.module_venues_table.setCellWidget(row, 0, item)

    def courses_populate(self):
        courses = self.builder.module_get(self.module_id).courses
        courses = [self.builder.course_get(course) for course in courses]
        self.module_courses_table.clearContents()
        self.module_courses_table.setRowCount(0)

        for course in courses:
            row = self.module_courses_table.rowCount()
            self.module_courses_table.insertRow(row)
            self.module_courses_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(course.name)
            item.set_text(course.short_name)
            remove_func = partial(self.delete_course, self.module_id, course.id)
            item.remove_btn.clicked.connect(remove_func)
            self.module_courses_table.setCellWidget(row, 0, item)

    def delete_venue(self, module_id, venue_id):
        try:
            self.builder.module_remove_venue(module_id, venue_id)
            self.venues_populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")

    def delete_course(self, module_id, course_id):
        try:
            self.builder.module_remove_course(course_id, module_id)
            self.courses_populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")


class AddSubjectWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder], edit: bool = False,
                 subject_id: str = None):
        super().__init__()
        self.ui = ui_add_subject_dialog.Ui_AddSubject()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.subject_id = subject_id

        self.subject_name = self.ui.subject_name
        self.subject_venue = self.ui.subject_venue
        self.subject_save = self.ui.subject_save

        self.subject_save.clicked.connect(self.save)
        self.ui.close_btn.clicked.connect(self.close)
        self.venue_select_populate()

        if self.edit:
            subject = self.builder.subject_get(self.subject_id)
            self.subject_name.setText(subject.name)
            self.subject_venue.setCurrentText(self.builder.venue_get(subject.primary_venue).name)

    def close(self):
        self.subject_name.clear()
        self.subject_venue.clear()
        super().close()

    def validate(self):
        return self.subject_name.text() and self.subject_venue.currentText()

    def save(self):
        if self.validate():

            subject_name = self.subject_name.text()
            subject_venue = self.subject_venue.currentData()

            if not self.edit:
                try:
                    self.builder.add_subject(subject_name, subject_venue)
                    self.saved.emit(Types.SUBJECTS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.subject_change_data(self.subject_id, Types.NAME, subject_name)
                    self.builder.subject_change_data(self.subject_id, Types.VENUE, subject_venue)
                    self.saved.emit(Types.SUBJECTS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")

    def venue_select_populate(self):
        venues = self.builder.venue_get_all()
        self.subject_venue.clear()
        self.subject_venue.addItem("Primary", userData="primary")

        for venue in venues:
            self.subject_venue.addItem(venue.name, userData=venue.id)


class AddLecturerWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, edit: bool = False,
                 lecturer_id: str = None):
        super().__init__()
        self.ui = ui_add_lecturer_dialog.Ui_AddLecturer()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.lecturer_id = lecturer_id

        self.lecturer_name = self.ui.lecturer_name
        self.save_btn = self.ui.lecturer_save

        if self.edit:
            self.lecturer_name.setText(self.builder.lecturer_get(lecturer_id).name)

        self.ui.close_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.save)

    def close(self):
        self.lecturer_name.clear()
        super().close()

    def validate(self):
        return self.lecturer_name.text()

    def save(self):
        if self.validate():

            lecturer_name = self.lecturer_name.text()

            if not self.edit:
                try:
                    self.builder.add_lecturer(lecturer_name)
                    self.saved.emit(Types.LECTURERS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.lecturer_change_name(self.lecturer_id, lecturer_name)
                    self.saved.emit(Types.LECTURERS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")


class AddTeacherWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder], edit: bool = False,
                 teacher_id: str = None):
        super().__init__()
        self.ui = ui_add_teacher_dialog.Ui_AddTeacher()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.teacher_id = teacher_id

        self.teacher_name = self.ui.teacher_name
        self.save_btn = self.ui.teacher_save

        if self.edit:
            self.teacher_name.setText(self.builder.teacher_get(teacher_id).name)

        self.ui.close_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.save)

    def close(self):
        self.teacher_name.clear()
        super().close()

    def validate(self):
        return self.teacher_name.text()

    def save(self):
        if self.validate():

            teacher_name = self.teacher_name.text()

            if not self.edit:
                try:
                    self.builder.add_teacher(teacher_name)
                    self.saved.emit(Types.TEACHERS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.teacher_change_name(self.teacher_id, teacher_name)
                    self.saved.emit(Types.TEACHERS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")


class AddCourseWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, edit: bool = False,
                 course_id: str = None):
        super().__init__()
        self.ui = ui_add_course_dialog.Ui_AddCourse()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.course_id = course_id

        self.course_name = self.ui.course_name
        self.course_short_name = self.ui.course_short_name

        if self.edit:
            course = self.builder.course_get(self.course_id)
            self.course_name.setText(course.name)
            self.course_short_name.setText(course.short_name)

        self.ui.course_save.clicked.connect(self.save)
        self.ui.close_btn.clicked.connect(self.close)

    def close(self):
        self.course_name.clear()
        self.course_short_name.clear()
        super().close()

    def validate(self):
        return self.course_name.text() and self.course_short_name.text()

    def save(self):
        if self.validate():

            course_name = self.course_name.text()
            course_short_name = self.course_short_name.text()

            if not self.edit:
                try:
                    self.builder.add_course(course_name, course_short_name)
                    self.saved.emit(Types.COURSES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.course_change_data(self.course_id, Types.NAME, course_name)
                    self.builder.course_change_data(self.course_id, Types.SHORT_NAME, course_short_name)
                    self.saved.emit(Types.COURSES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")


class AddClassWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: SecondaryBuilder, edit: bool = False,
                 class_id: str = None):
        super().__init__()
        self.ui = ui_add_class_dialog.Ui_AddClass()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.class_id = class_id

        self.class_name = self.ui.class_name
        self.class_venue = self.ui.class_venue
        self.venue_select_populate()

        if self.edit:
            class_ = self.builder.class_get(self.class_id)
            self.class_name.setText(class_.name)
            self.class_venue.setCurrentText(self.builder.venue_get(class_.venue).name)

        self.ui.class_save.clicked.connect(self.save)
        self.ui.close_btn.clicked.connect(self.close)

    def close(self):
        self.class_name.clear()
        self.class_venue.clear()
        super().close()

    def validate(self):
        return self.class_name.text() and self.class_venue.currentText()

    def save(self):
        if self.validate():

            class_name = self.class_name.text()
            class_venue = self.class_venue.currentData()

            if not self.edit:
                try:
                    self.builder.add_class(class_name, class_venue, {})
                    self.saved.emit(Types.CLASSES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.class_change_data(self.class_id, Types.NAME, class_name)
                    self.builder.class_change_data(self.class_id, Types.VENUE, class_venue)
                    self.saved.emit(Types.CLASSES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")

    def venue_select_populate(self):
        venues = self.builder.venue_get_all()
        self.class_venue.clear()

        for venue in venues:
            self.class_venue.addItem(venue.name, userData=venue.id)


class AddClassDataWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: SecondaryBuilder, class_id: str):
        super().__init__()
        self.ui = ui_add_class_data_dialog.Ui_AddClass()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.class_id = class_id
        self.ui.class_name.setText(self.builder.class_get(self.class_id).name)

        self.class_data_table = self.ui.class_subjects_table
        self.subject_select = self.ui.class_subject_select
        self.teacher_select = self.ui.class_teacher_select
        self.slots_per_day = self.ui.slots_per_day
        self.slots_per_cycle = self.ui.slots_per_cycle

        self.ui.class_save.clicked.connect(self.close)
        self.ui.close_btn.clicked.connect(self.close)
        self.class_data_table.setShowGrid(False)

        self.populate()
        self.teachers_select_populate()
        self.subjects_select_populate()

    def clear(self):
        self.subject_select.clear()
        self.teacher_select.clear()
        self.slots_per_day.setValue(0)
        self.slots_per_cycle.setValue(0)

    def close(self, /):
        self.clear()
        super().close()

    def add_subject(self):
        subject = self.subject_select.currentData()
        teacher = self.teacher_select.currentData()
        class_subjects = self.builder.class_get(self.class_id).subjects

        if subject in class_subjects:
            MessageBox().warning(self, "Already Exits", "This subject is already added!")
            return
        else:
            try:
                if self.builder.get_possible_slots(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value(), teacher)[1] >= 0:
                    self.builder.class_add_subject(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value(), teacher)
                    self.saved.emit(Types.CLASSES)
                    self.populate()
                else:
                    MessageBox().warning(self, "Out of slots",
                                         "There are not enough slots for this subject. Try adjusting the time"
                                         " slots and changing the teacher.")
            except Exception as e:
                logger.critical(str(e))
                MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")

    def teachers_select_populate(self):
        teachers = self.builder.teacher_get_all()
        self.teacher_select.clear()

        for teacher in teachers:
            self.teacher_select.addItem(teacher.name, userData=teacher.id)

    def subjects_select_populate(self):
        subjects = self.builder.subject_get_all()
        self.subject_select.clear()

        for subject in subjects:
            self.subject_select.addItem(subject.name, userData=subject.id)

    def populate(self):
        subjects = self.builder.class_get(self.class_id).subjects
        self.class_data_table.clearContents()
        self.class_data_table.setRowCount(0)
        subjects = [(subject, self.builder.subject_get(subject).name, subject[Types.TEACHER],
                     f" slots: [{subjects[subject]['time_slots']}, {subjects[subject]['slots_per_day']}]")
                    for subject in subjects]

        for subject in subjects:
            row = self.class_data_table.rowCount()
            self.class_data_table.insertRow(row)
            self.class_data_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(subject[1])
            text = f"Teacher: {subject[2]}" + str(subjects[3])
            item.set_text(text)
            remove_func = partial(self.delete_subject, self.class_id, subject[0])
            item.remove_btn.clicked.connect(remove_func)
            self.class_data_table.setCellWidget(row, 0, item)

    def delete_subject(self, class_id, subject_id):
        try:
            self.builder.class_remove_subject(class_id, subject_id)
            self.populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")


class AddClassDataPrimaryWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: PrimaryBuilder, class_id: str):
        super().__init__()
        self.ui = ui_add_class_primary_data_dialog.Ui_AddClass()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.class_id = class_id
        self.ui.class_name.setText(self.builder.class_get(self.class_id).name)

        self.class_data_table = self.ui.class_subjects_table
        self.subject_select = self.ui.class_subject_select
        self.slots_per_day = self.ui.slots_per_day
        self.slots_per_cycle = self.ui.slots_per_cycle

        self.ui.class_save.clicked.connect(self.close)
        self.ui.close_btn.clicked.connect(self.close)
        self.class_data_table.setShowGrid(False)

        self.populate()
        self.subjects_select_populate()

    def clear(self):
        self.subject_select.clear()
        self.slots_per_day.setValue(0)
        self.slots_per_cycle.setValue(0)

    def close(self, /):
        self.clear()
        super().close()

    def add_subject(self):
        subject = self.subject_select.currentData()
        class_subjects = self.builder.class_get(self.class_id).subjects

        if subject in class_subjects:
            MessageBox().warning(self, "Already Exits", "This subject is already added!")
            return
        else:
            try:
                if self.builder.get_possible_slots(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value())[1] >= 0:
                    self.builder.class_add_subject(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value())
                    self.saved.emit(Types.CLASSES)
                    self.populate()
                else:
                    MessageBox().warning(self, "Out of slots",
                                         "There are not enough slots for this subject. Try adjusting the time"
                                         " slots and changing the teacher.")
            except Exception as e:
                logger.critical(str(e))
                MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")

    def subjects_select_populate(self):
        subjects = self.builder.subject_get_all()
        self.subject_select.clear()

        for subject in subjects:
            self.subject_select.addItem(subject.name, userData=subject.id)

    def populate(self):

        subjects = self.builder.class_get(self.class_id).subjects
        self.class_data_table.clearContents()
        self.class_data_table.setRowCount(0)
        subjects = [(subject, self.builder.subject_get(subject).name,
                     f" slots: [{subjects[subject]['time_slots']}, {subjects[subject]['slots_per_day']}]")
                    for subject in subjects]

        for subject in subjects:
            row = self.class_data_table.rowCount()
            self.class_data_table.insertRow(row)
            self.class_data_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(subject[1])
            text = str(subjects[2])
            item.set_text(text)
            remove_func = partial(self.delete_subject, self.class_id, subject[0])
            item.remove_btn.clicked.connect(remove_func)
            self.class_data_table.setCellWidget(row, 0, item)

    def delete_subject(self, class_id, subject_id):
        try:
            self.builder.class_remove_subject(class_id, subject_id)
            self.populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")


class AddVenueWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder, TertiaryBuilder],
                 edit: bool = False, venue_id: str = None):
        super().__init__()
        self.ui = ui_add_venue_dialog.Ui_AddVenue()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.venue_id = venue_id

        self.venue_name = self.ui.venue_name
        self.venue_latitude = self.ui.venue_latitude
        self.venue_latitude.setValidator(QDoubleValidator())
        self.venue_longitude = self.ui.venue_longitude
        self.venue_longitude.setValidator(QDoubleValidator())
        self.venue_description = self.ui.venue_location_description
        self.save_btn = self.ui.venue_save

        if self.edit:
            venue = self.builder.venue_get(venue_id)
            self.venue_name.setText(venue.name)
            self.venue_latitude.setText(str(venue.location[0]))
            self.venue_longitude.setText(str(venue.location[1]))
            self.venue_description.setText(venue.location_description)

        self.ui.close_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.save)

    def close(self):
        self.venue_name.clear()
        self.venue_latitude.clear()
        self.venue_longitude.clear()
        self.venue_description.clear()
        super().close()

    def validate(self):
        return (self.venue_name.text() and self.venue_latitude.text() and
                self.venue_longitude.text() and self.venue_description.toPlainText())

    def save(self):
        if self.validate():

            venue_name = self.venue_name.text()
            venue_location = [float(self.venue_latitude.text()),
                              float(self.venue_longitude.text())]
            venue_description = self.venue_description.toPlainText()

            if not self.edit:
                try:
                    self.builder.add_venue(venue_name, venue_location, venue_description)
                    self.saved.emit(Types.VENUES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.venue_change_data(self.venue_id, Types.NAME, venue_name)
                    self.builder.venue_change_data(self.venue_id, "location", venue_location)
                    self.builder.venue_change_data(self.venue_id, "location_description", venue_description)
                    self.saved.emit(Types.VENUES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox().critical(None, "Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox().warning(self, "Incomplete Input", "Please fill in all the required fields!")
