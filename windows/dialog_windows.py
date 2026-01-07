from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDoubleValidator
from typing import Union
from widgets import RemovableTableItem, MessageBox, ProjectItem
from functools import partial
from utils.builders import PrimaryBuilder, SecondaryBuilder, TertiaryBuilder
from utils import Types, Utils
from utils.logger_config import logger
from ui import (ui_add_module_dialog, ui_add_class_dialog,
                ui_add_venue_dialog, ui_add_course_dialog, ui_add_subject_dialog,
                ui_add_teacher_dialog, ui_add_lecturer_dialog,
                ui_add_module_data_dialog, ui_add_class_data_dialog,
                ui_add_class_primary_data_dialog, ui_add_block_dialog,
                ui_add_block_data_dialog, ui_add_break_dialog,
                ui_open_project)
import os


class ProjectsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.project = None
        self.ui = ui_open_project.Ui_Projects()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.table = self.ui.projects_table
        self.ui.close_btn.clicked.connect(self.close)
        self.populate()

    def populate(self):
        path = Utils.get_timetables_path()
        files = os.listdir(path)
        files = [(file.replace(".tbl", ""), os.path.join(path, file)) for file in files
                 if os.path.isfile(os.path.join(path, file)) and
                 file.endswith(".tbl")]
        self.table.clearContents()
        self.table.setRowCount(0)

        for project in files:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setRowHeight(row, 35)
            project_item = ProjectItem(self, project[0], project[1], self.callback)
            self.table.setCellWidget(row, 0, project_item)

    def callback(self, path, action):
        if action == "del":
            os.remove(path)
            self.populate()
        elif action == "open":
            self.project = path
            self.accept()

    @staticmethod
    def get_project(parent=None):
        dialog = ProjectsWindow(parent)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            return dialog.project
        return None


class AddModuleWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, edit: bool = False,
                 module_id: str = None, parent=None):
        super().__init__(parent=parent)
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
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")
            return

        self.saved.emit(Types.MODULES)
        self.clear()
        self.close()


class AddModuleDataWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, module_id: str, parent=None):
        super().__init__(parent=parent)
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
        self.module_venue_select = self.ui.module_venue_select
        self.module_venue_add_btn = self.ui.module_add_venue_btn

        self.module_course_level.lineEdit().setPlaceholderText("Level")
        self.module_course_select.lineEdit().setPlaceholderText("Course")
        self.module_venue_select.lineEdit().setPlaceholderText("Venue")
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

        if not venue:
            MessageBox(self).warning("Not Found", "This venue is not found! You can add it"
                                                  " in the venue section.")
            return

        module_venues = self.builder.module_get(self.module_id).venues

        if venue in module_venues:
            MessageBox(self).warning("Already Exits", "This venue is already used!")
            return
        else:
            if self.builder.module_add_venue(venue, self.module_id):
                self.venues_populate()
                self.venues_select_populate()
            else:
                MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

    def add_course(self):
        course = self.module_course_select.currentData()

        if not course:
            MessageBox(self).warning("Not Found", "This course is not found! You can add it"
                                                  " in the courses section.")
            return

        module_courses = self.builder.module_get(self.module_id).courses

        if course in module_courses:
            MessageBox(self).warning("Already Exits", "This course is already added!")
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
                self.courses_select_populate()
            else:
                MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

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
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

    def delete_course(self, module_id, course_id):
        try:
            self.builder.module_remove_course(course_id, module_id)
            self.courses_populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")


class AddSubjectWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder], edit: bool = False,
                 subject_id: str = None, parent=None):
        super().__init__(parent=parent)
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
            self.subject_venue.setCurrentText(self.builder.venue_get(subject.primary_venue).name
                                              if subject.primary_venue != Types.VENUE_PRIMARY else "Primary")

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
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.subject_change_data(self.subject_id, Types.NAME, subject_name)
                    self.builder.subject_change_data(self.subject_id, Types.VENUE, subject_venue)
                    self.saved.emit(Types.SUBJECTS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")

    def venue_select_populate(self):
        venues = self.builder.venue_get_all()
        self.subject_venue.clear()
        self.subject_venue.addItem("Primary", userData="primary")

        for venue in venues:
            self.subject_venue.addItem(venue.name, userData=venue.id)


class AddLecturerWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, edit: bool = False,
                 lecturer_id: str = None, parent=None):
        super().__init__(parent=parent)
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
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.lecturer_change_name(self.lecturer_id, lecturer_name)
                    self.saved.emit(Types.LECTURERS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")


class AddTeacherWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder], edit: bool = False,
                 teacher_id: str = None, parent=None):
        super().__init__(parent=parent)
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
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.teacher_change_name(self.teacher_id, teacher_name)
                    self.saved.emit(Types.TEACHERS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")


class AddCourseWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: TertiaryBuilder, edit: bool = False,
                 course_id: str = None, parent=None):
        super().__init__(parent=parent)
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
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.course_change_data(self.course_id, Types.NAME, course_name)
                    self.builder.course_change_data(self.course_id, Types.SHORT_NAME, course_short_name)
                    self.saved.emit(Types.COURSES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")


class AddClassWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: SecondaryBuilder, edit: bool = False,
                 class_id: str = None, parent=None):
        super().__init__(parent=parent)
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
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.class_change_data(self.class_id, Types.NAME, class_name)
                    self.builder.class_change_data(self.class_id, Types.VENUE, class_venue)
                    self.saved.emit(Types.CLASSES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")

    def venue_select_populate(self):
        venues = self.builder.venue_get_all()
        self.class_venue.clear()

        for venue in venues:
            self.class_venue.addItem(venue.name, userData=venue.id)


class AddClassDataWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: SecondaryBuilder, class_id: str, parent=None):
        super().__init__(parent=parent)
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
        self.ui.class_add_subject_btn.clicked.connect(self.add_subject)
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
            MessageBox(self).warning("Already Exits", "This subject is already added!")
            return
        else:
            try:
                if self.builder.get_possible_slots(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value(), teacher)[1] >= 0:
                    self.builder.class_add_subject(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value(), teacher)
                    self.saved.emit(Types.CLASSES)
                    self.populate()
                    self.clear()
                    self.teachers_select_populate()
                    self.subjects_select_populate()
                else:
                    MessageBox(self).warning("Out of slots",
                                             "There are not enough slots for this subject. Try adjusting the time"
                                             " slots and changing the teacher.")
            except Exception as e:
                logger.critical(str(e))
                MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

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
        subjects = [(subject, self.builder.subject_get(subject).name,
                     self.builder.teacher_get(subjects[subject][Types.TEACHER]).name,
                     f" Slots: [{subjects[subject]['time_slots']}, {subjects[subject]['slots_per_day']}]")
                    for subject in subjects]

        for subject in subjects:
            row = self.class_data_table.rowCount()
            self.class_data_table.insertRow(row)
            self.class_data_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(subject[1])
            text = f"Teacher: {subject[2]} ~" + str(subject[3])
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
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")


class AddClassDataPrimaryWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: PrimaryBuilder, class_id: str, parent=None):
        super().__init__(parent=parent)
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
        self.ui.class_add_subject_btn.clicked.connect(self.add_subject)
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
            MessageBox(self).warning("Already Exits", "This subject is already added!")
            return
        else:
            try:
                if self.builder.get_possible_slots(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value())[1] >= 0:
                    self.builder.class_add_subject(self.class_id, subject, self.slots_per_cycle.value(),
                                                   self.slots_per_day.value())
                    self.saved.emit(Types.CLASSES)
                    self.populate()
                    self.clear()
                    self.subjects_select_populate()
                else:
                    MessageBox(self).warning("Out of slots",
                                             "There are not enough slots for this subject. Try adjusting the time"
                                             " slots and changing the teacher.")
            except Exception as e:
                logger.critical(str(e))
                MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

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
                     f" Slots: [{subjects[subject]['time_slots']}, {subjects[subject]['slots_per_day']}]")
                    for subject in subjects]

        for subject in subjects:
            row = self.class_data_table.rowCount()
            self.class_data_table.insertRow(row)
            self.class_data_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(subject[1])
            text = str(subject[2])
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
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")


class AddBreakWindow(QDialog):

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder], parent=None):
        super().__init__(parent=parent)
        self.ui = ui_add_break_dialog.Ui_AddBreak()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder

        self.breaks_data_table = self.ui.breaks_table
        self.break_slot_select = self.ui.break_slot_select
        self.break_name = self.ui.break_name

        self.ui.break_save.clicked.connect(self.close)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.break_add_btn.clicked.connect(self.add_break)
        self.breaks_data_table.setShowGrid(False)

        self.populate()
        self.slot_select_populate()

    def clear(self):
        self.break_slot_select.clear()
        self.breaks_data_table.clearContents()
        self.break_name.clear()

    def close(self, /):
        self.clear()
        super().close()

    def add_break(self):
        break_name = self.break_name.text()
        break_slot = self.break_slot_select.currentText()

        if not break_slot:
            MessageBox(self).warning("Period Error", "Please select a  valid time period!")
            return
        elif self.builder.timetable_break_slot_taken(break_slot):
            MessageBox(self).warning("Period Taken", "This period selected is already used!")
            return
        elif not break_name:
            MessageBox(self).warning("Incomplete input", "Please enter the break name!")
            return

        try:
            self.builder.timetable_add_break(break_name, break_slot)
            self.populate()
            self.break_name.clear()
            self.slot_select_populate()
        except Exception as e:
            print(str(e))
            logger.critical(str(e))
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

    def slot_select_populate(self):
        slots = self.builder.timetable_get_slots_per_day()
        self.break_slot_select.clear()

        for slot in range(1, slots + 1):
            self.break_slot_select.addItem(str(slot))

    def populate(self):

        breaks = self.builder.timetable_get_breaks()
        self.breaks_data_table.clearContents()
        self.breaks_data_table.setRowCount(0)

        for break_ in breaks:
            row = self.breaks_data_table.rowCount()
            self.breaks_data_table.insertRow(row)
            self.breaks_data_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(break_)
            break_slots = [str(slot) for slot in breaks[break_]]
            text = ", ".join(break_slots)
            item.set_text("Periods: " + text)
            remove_func = partial(self.delete_break, break_)
            item.remove_btn.clicked.connect(remove_func)
            self.breaks_data_table.setCellWidget(row, 0, item)

    def delete_break(self, break_name: str):
        try:
            self.builder.timetable_remove_break(break_name)
            self.populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")


class AddBlockWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: SecondaryBuilder, edit: bool = False,
                 block_id: str = None, parent=None):
        super().__init__(parent=parent)
        self.ui = ui_add_block_dialog.Ui_AddBlock()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.edit = edit
        self.block_id = block_id

        self.block_name = self.ui.block_name
        self.block_size = self.ui.block_size

        if self.edit:
            block_ = self.builder.block_get(self.block_id)
            self.block_name.setText(block_.name)
            self.block_size.setValue(block_.length)

        self.ui.block_save.clicked.connect(self.save)
        self.ui.close_btn.clicked.connect(self.close)

    def close(self):
        self.block_name.clear()
        self.block_size.setValue(0)
        super().close()

    def validate(self):
        return self.block_name.text()

    def save(self):
        if self.validate():

            block_name = self.block_name.text()
            block_size = self.block_size.value()

            if not self.edit:
                try:
                    if self.builder.get_possible_blocks(block_name, {}, [], block_size):
                        self.builder.add_block(block_name, {}, [], block_size)
                        self.saved.emit(Types.BLOCKS)
                        self.close()
                    else:
                        MessageBox(self).warning("Error", "A block of that size has no remaining slots to be"
                                                          " added!")
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.block_change_name(self.block_id, block_name)
                    self.builder.block_change_size(self.block_id, block_size)
                    self.saved.emit(Types.BLOCKS)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")


class AddBlockDataWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: SecondaryBuilder, block_id: str, parent=None):
        super().__init__(parent=parent)
        self.ui = ui_add_block_data_dialog.Ui_AddBlock()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.builder = builder
        self.block_id = block_id
        self.ui.block_name.setText(self.builder.block_get(self.block_id).name)

        self.subjects_table = self.ui.subjects_table
        self.classes_table = self.ui.classes_table
        self.subject_select = self.ui.subject_select
        self.teacher_select = self.ui.teacher_select
        self.venue_select = self.ui.venue_select
        self.class_select = self.ui.class_select

        self.subject_select.lineEdit().setPlaceholderText("Subject name")
        self.teacher_select.lineEdit().setPlaceholderText("Teacher name")
        self.venue_select.lineEdit().setPlaceholderText("Subject venue")
        self.class_select.lineEdit().setPlaceholderText("Class name")

        self.ui.block_save.clicked.connect(self.close)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.subject_add_btn.clicked.connect(self.add_subject)
        self.ui.class_add_btn.clicked.connect(self.add_class)
        self.subjects_table.setShowGrid(False)
        self.classes_table.setShowGrid(False)

        self.populate()
        self.teachers_select_populate()
        self.subjects_select_populate()
        self.class_select_populate()
        self.venue_select_populate()

    def clear(self):
        self.subject_select.clear()
        self.teacher_select.clear()
        self.class_select.clear()
        self.venue_select.clear()

    def close(self, /):
        self.clear()
        super().close()

    def add_subject(self):

        if not (self.subject_select.currentText() and
                self.teacher_select.currentText() and
                self.venue_select.currentText()):
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")
            return

        subject = self.subject_select.currentData()
        teacher = self.teacher_select.currentData()
        venue = self.venue_select.currentData()

        if not subject:
            MessageBox(self).warning("Not Found", "The selected subject is not found!")
            return

        if not teacher:
            MessageBox(self).warning("Not Found", "The selected teacher is not found!")
            return

        if not venue:
            MessageBox(self).warning("Not Found", "The selected venue is not found!")
            return

        block_subjects = self.builder.block_get(self.block_id).subjects
        block_teachers = [block_subjects[subject][Types.TEACHER] for subject in block_subjects]
        block_venues = [block_subjects[subject][Types.VENUE] for subject in block_subjects]

        if subject in block_subjects:
            MessageBox(self).warning("Already Exits", "This subject is already added!")
            return
        elif teacher in block_teachers:
            MessageBox(self).warning("Already Exits", "This teacher is already added!")
            return
        if venue in block_venues:
            MessageBox(self).warning("Already Exits", "This venue is already added!")
            return
        else:
            try:
                self.builder.block_add_subject(self.block_id, subject, teacher, venue)
                self.saved.emit(Types.BLOCKS)
                self.populate()
                self.clear()
                self.teachers_select_populate()
                self.subjects_select_populate()
                self.venue_select_populate()
                self.class_select_populate()
            except Exception as e:
                logger.critical(str(e))
                MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

    def add_class(self):

        if not self.class_select.currentText():
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")
            return

        class_ = self.class_select.currentData()

        if not class_:
            MessageBox(self).warning("Not Found", "The selected class is not found!")
            return

        block_classes = self.builder.block_get(self.block_id).classes

        if class_ in block_classes:
            MessageBox(self).warning("Already Exits", "This class is already added!")
            return
        else:
            try:
                self.builder.block_add_class(self.block_id, class_)
                self.saved.emit(Types.BLOCKS)
                self.populate()
                self.class_select_populate()
            except Exception as e:
                logger.critical(str(e))
                MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

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

    def class_select_populate(self):
        classes = self.builder.class_get_all()
        self.class_select.clear()

        for class_ in classes:
            self.class_select.addItem(class_.name, userData=class_.id)

    def venue_select_populate(self):
        venues = self.builder.venue_get_all()
        self.venue_select.clear()

        for venue in venues:
            self.venue_select.addItem(venue.name, userData=venue.id)

    def populate(self):
        subjects = self.builder.block_get(self.block_id).subjects
        classes = self.builder.block_get(self.block_id).classes

        self.subjects_table.clearContents()
        self.subjects_table.setRowCount(0)
        self.classes_table.clearContents()
        self.classes_table.setRowCount(0)

        subjects = [(subject, self.builder.subject_get(subject).name,
                     self.builder.teacher_get(subjects[subject][Types.TEACHER]).name,
                     self.builder.venue_get(subjects[subject][Types.VENUE]).name)
                    for subject in subjects]

        for subject in subjects:
            row = self.subjects_table.rowCount()
            self.subjects_table.insertRow(row)
            self.subjects_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(subject[1])
            text = f"Teacher: {subject[2]} ~ " + f"Venue: {subject[3]}"
            item.set_text(text)
            remove_func = partial(self.delete_subject, self.block_id, subject[0])
            item.remove_btn.clicked.connect(remove_func)
            self.subjects_table.setCellWidget(row, 0, item)

        for class_ in classes:
            row = self.classes_table.rowCount()
            self.classes_table.insertRow(row)
            self.classes_table.setRowHeight(row, 50)
            item = RemovableTableItem()
            item.set_header(self.builder.class_get(class_).name)
            remove_func = partial(self.delete_class, self.block_id, class_)
            item.remove_btn.clicked.connect(remove_func)
            self.classes_table.setCellWidget(row, 0, item)

    def delete_subject(self, block_id, subject_id):
        try:
            self.builder.block_remove_subject(block_id, subject_id)
            self.populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")

    def delete_class(self, block_id, class_id):
        try:
            self.builder.block_remove_class(block_id, class_id)
            self.populate()
        except Exception as e:
            logger.critical(str(e))
            MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")


class AddVenueWindow(QDialog):
    saved = Signal(str)

    def __init__(self, builder: Union[PrimaryBuilder, SecondaryBuilder, TertiaryBuilder],
                 edit: bool = False, venue_id: str = None, parent=None):
        super().__init__(parent=parent)
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
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
            else:
                try:
                    self.builder.venue_change_data(self.venue_id, Types.NAME, venue_name)
                    self.builder.venue_change_data(self.venue_id, "location", venue_location)
                    self.builder.venue_change_data(self.venue_id, "location_description", venue_description)
                    self.saved.emit(Types.VENUES)
                    self.close()
                except Exception as e:
                    logger.critical(str(e))
                    MessageBox(self).critical("Error", "This is embarrassing! An unexpected error occurred.")
        else:
            MessageBox(self).warning("Incomplete Input", "Please fill in all the required fields!")
