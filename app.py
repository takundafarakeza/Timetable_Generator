from PySide6.QtWidgets import QApplication, QFileDialog
from utils.builders import PrimaryBuilder, SecondaryBuilder, TertiaryBuilder
from utils.data import TimeTableInitData
from utils import Types
from utils import Utils, Settings
from utils.logger_config import logger
from windows import (Main, StartUp)
from widgets import (ModulesTable, SubjectsTable,
                     TeachersTable, LecturersTable, ClassesTable,
                     CoursesTable, VenuesTable)
from windows.dialog_windows import (AddModuleWindow, AddModuleDataWindow, AddSubjectWindow,
                                    AddLecturerWindow, AddTeacherWindow, AddCourseWindow,
                                    AddClassWindow, AddClassDataWindow, AddClassDataPrimaryWindow,
                                    AddVenueWindow)
from typing import Union, Optional
import sys
import json
import functools


class StartUpWindow(StartUp):

    def __init__(self):
        super().__init__()
        self.open_project_btn.clicked.connect(self.open_project)
        self.boarding.create.connect(self.create_project)

    def open_project(self):

        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file", Utils.get_timetables_path(),
                                                   "Timetable (*tbl)")

        if file_path:
            with open(file_path) as file:
                try:
                    time_table_data = json.loads(file.read())
                except Exception as e:
                    logger.warning(str(e))
                    time_table_data = None

            if time_table_data:
                institution = time_table_data[Types.INSTITUTION_TYPE]
                builder = (
                    PrimaryBuilder if institution == Types.INSTITUTION_PRIMARY else
                    SecondaryBuilder if institution == Types.INSTITUTION_SECONDARY else
                    TertiaryBuilder
                )
                builder = builder(file_path)
                project_name = Utils.project_path_to_name(file_path)
                settings.add_recent_file(project_name, file_path)
                app_window.set_builder(builder)
                self.populate_recent()
                self.close()
                self.project_open.emit(institution, project_name)

    def create_project(self, data: tuple):
        try:
            institution, name, time_table_name, slots_per_day, days_per_cycle, slot_length = data
            builder = (
                PrimaryBuilder if institution == Types.INSTITUTION_PRIMARY else
                SecondaryBuilder if institution == Types.INSTITUTION_SECONDARY else
                TertiaryBuilder
            )
            init_data = TimeTableInitData(time_table_name, institution, name, slot_length,
                                          days_per_cycle, slots_per_day, [])
            file = Utils().create_project_file(time_table_name, name)
            builder = builder(file, init_data)
            builder.timetable_save()
            app_window.set_builder(builder)
            project_name = f"{time_table_name}_{name}".replace(" ", "_")
            settings.add_recent_file(project_name, file)

            self.boarding.close()
            self.close()
            self.project_create.emit(institution, project_name)
        except Exception as e:
            logger.critical(f"Error: {str(e)}")

    def manage_recent(self, name: str, action: str):
        if action == "del":
            Settings().remove_recent_file(name)
            self.populate_recent()
        else:
            file_path = Settings().get_recent_file(name)
            if file_path:
                file = open(file_path)
                try:
                    time_table_data = json.loads(file.read())
                except Exception as e:
                    logger.warning(str(e))
                    time_table_data = None
                file.close()
                if time_table_data:
                    institution = time_table_data[Types.INSTITUTION_TYPE]
                    builder = (
                        PrimaryBuilder if institution == Types.INSTITUTION_PRIMARY else
                        SecondaryBuilder if institution == Types.INSTITUTION_SECONDARY else
                        TertiaryBuilder
                    )
                    builder = builder(file_path)
                    project_name = Utils.project_path_to_name(file_path)
                    settings.add_recent_file(project_name, file_path)
                    app_window.set_builder(builder)
                    self.populate_recent()
                    self.close()
                    self.project_open.emit(institution, project_name)


class AppWindow(Main):
    def __init__(self):
        super().__init__()
        self.builder: Optional[PrimaryBuilder, SecondaryBuilder, TertiaryBuilder] = None
        self.file: Optional[str] = None
        self.institution_type: Optional[str] = None
        self.dialog_window = None

        self.modules_table = ModulesTable()
        self.subjects_table = SubjectsTable()
        self.teachers_table = TeachersTable()
        self.lecturers_table = LecturersTable()
        self.classes_table = ClassesTable()
        self.courses_table = CoursesTable()
        self.venues_table = VenuesTable()

        self.ui.modules_table_layout.addWidget(self.modules_table)
        self.ui.subjects_table_layout.addWidget(self.subjects_table)
        self.ui.lecturers_table_layout.addWidget(self.lecturers_table)
        self.ui.teachers_table_layout.addWidget(self.teachers_table)
        self.ui.courses_table_layout.addWidget(self.courses_table)
        self.ui.classes_table_layout.addWidget(self.classes_table)
        self.ui.venues_table_layout.addWidget(self.venues_table)

        self.ui.modules_course_filter.lineEdit().setPlaceholderText("Filter by course")
        self.ui.subjects_class_filter.lineEdit().setPlaceholderText("Filter by class")
        self.set_generated(True)
        self.set_saved(True)

        self._init_signals()

    def _init_signals(self):
        startup.project_open.connect(self.open_project)
        startup.project_create.connect(self.create_project)
        self.close_project_btn.clicked.connect(close_project)

        self.ui.modules_course_filter.currentTextChanged.connect(self.modules_filter)
        self.ui.modules_search.textChanged.connect(self.modules_module_search)
        self.ui.subjects_class_filter.currentTextChanged.connect(self.subjects_filter)
        self.ui.subjects_search.textChanged.connect(self.subjects_subject_search)
        self.ui.lecturers_search.textChanged.connect(self.lecturers_lecturer_search)
        self.ui.teachers_search.textChanged.connect(self.teachers_teacher_search)
        self.ui.courses_search.textChanged.connect(self.courses_course_search)
        self.ui.classes_search.textChanged.connect(self.classes_class_search)
        self.ui.venues_search.textChanged.connect(self.venues_venue_search)

        self.modules_table.set_action_handler(self.modules_callback)
        self.subjects_table.set_action_handler(self.subjects_callback)
        self.teachers_table.set_action_handler(self.teachers_callback)
        self.lecturers_table.set_action_handler(self.lecturers_callback)
        self.classes_table.set_action_handler(self.classes_callback)
        self.courses_table.set_action_handler(self.courses_callback)
        self.venues_table.set_action_handler(self.venues_callback)

        self.ui.modules_add_btn.clicked.connect(self.modules_add)
        self.ui.subjects_add_btn.clicked.connect(self.subjects_add)
        self.ui.lecturers_add_btn.clicked.connect(self.lecturers_add)
        self.ui.teachers_add_btn.clicked.connect(self.teachers_add)
        self.ui.courses_add_btn.clicked.connect(self.courses_add)
        self.ui.classes_add_btn.clicked.connect(self.classes_add)
        self.ui.venues_add_btn.clicked.connect(self.venues_add)

    """
    =============================================================
        UI MANIPULATION
    =============================================================
    """

    def build_menu(self, institution_type):
        super().build_menu(institution_type)

        self.file_menu.addAction("Open", startup.open_project)
        self.file_menu.addAction("New Project", startup.boarding.show)
        self.file_menu.addAction("Save", self.builder.timetable_save)
        self.file_menu.addAction("Save As", self.save_as)
        self.file_menu.addAction("Exit", self.close)

        self.timetable_menu.addAction("Clear", self.builder.timetable_init_timetable)
        self.timetable_menu.addAction("Generate", self.builder.generate)

        if institution_type == Types.INSTITUTION_PRIMARY or institution_type == Types.INSTITUTION_SECONDARY:
            self.timetable_menu.addAction("Generate Update", self.builder.generate_patches)

        if institution_type == Types.INSTITUTION_PRIMARY:
            self.edit_menu.addAction("Add Subject", self.subjects_add)
            self.edit_menu.addAction("Add Class", self.classes_add)

        elif institution_type == Types.INSTITUTION_SECONDARY:
            self.edit_menu.addAction("Add Teacher", self.teachers_add)
            self.edit_menu.addAction("Add Subject", self.subjects_add)
            self.edit_menu.addAction("Add Class", self.classes_add)

        elif institution_type == Types.INSTITUTION_COLLEGE:
            self.edit_menu.addAction("Add Lecturer", self.lecturers_add)
            self.edit_menu.addAction("Add Module", self.modules_add)
            self.edit_menu.addAction("Add Course", self.courses_add)

        self.edit_menu.addAction("Revert changes", self.builder.reload)

        func = functools.partial(self.viewer.view, self.builder.timetable_get)
        self.tools_menu.addAction("Viewer", func)
        self.tools_menu.addAction("Online Portal", Utils.view_portal)
        self.tools_btn.setMenu(self.tools_menu)

        self.edit_btn.setMenu(self.edit_menu)
        self.timetable_btn.setMenu(self.timetable_menu)
        self.file_btn.setMenu(self.file_menu)
        self.save_btn.clicked.connect(self.builder.timetable_save)
        self.builder.saved.connect(self.set_saved)
        self.builder.generated.connect(self.set_generated)

    def modules_callback(self, module_id, action):
        if action == "edit":
            self.dialog_window = AddModuleWindow(self.builder, True, module_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "add_data":
            self.dialog_window = AddModuleDataWindow(self.builder, module_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.module_remove(module_id)
            self.modules_populate()

    def subjects_callback(self, subject_id, action):
        if action == "edit":
            self.dialog_window = AddSubjectWindow(self.builder, True, subject_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.subject_remove(subject_id)

    def lecturers_callback(self, lecturer_id, action):
        if action == "edit":
            self.dialog_window = AddLecturerWindow(self.builder, True, lecturer_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.lecturer_remove(lecturer_id)

    def teachers_callback(self, teacher_id, action):
        if action == "edit":
            self.dialog_window = AddTeacherWindow(self.builder, True, teacher_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.teacher_remove(teacher_id)

    def courses_callback(self, course_id, action):
        if action == "edit":
            self.dialog_window = AddCourseWindow(self.builder, True, course_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.course_remove(course_id)

    def classes_callback(self, class_id, action):
        if action == "edit":
            self.dialog_window = AddClassWindow(self.builder, True, class_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "add_subjects":
            if self.builder.timetable_get_institution_type() == Types.INSTITUTION_SECONDARY:
                self.dialog_window = AddClassDataWindow(self.builder, class_id, self)
            else:
                self.dialog_window = AddClassDataPrimaryWindow(self.builder, class_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.class_remove(class_id)

    def venues_callback(self, venue_id, action):
        if action == "edit":
            self.dialog_window = AddVenueWindow(self.builder, True, venue_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.venue_remove(venue_id)

    """
    =============================================
        PROJECT MANAGEMENT
    =============================================
    """

    def close(self, /):
        self.builder = None
        super().close()

    def save_as(self):
        saved = Utils.save_file(self.file, self)
        self.set_saved(saved)

    def save(self):
        self.builder.timetable_save()
        self.set_saved(True)

    def set_builder(self, builder: Union[PrimaryBuilder, SecondaryBuilder, TertiaryBuilder]):
        self.builder = builder

    def create_project(self, institution, project_name):
        self.current_project.setText(project_name.replace("_", " "))
        self.file = self.builder.get_file()
        self.build_menu(institution)
        self.setup_window()
        self.show()

    def open_project(self, institution: str, project_name: str):
        self.current_project.setText(project_name.replace("_", " "))
        self.file = self.builder.get_file()
        self.build_menu(institution)
        self.setup_window()
        self.show()

    """
    =============================================
        PROJECT DATA MANAGEMENT
    =============================================
    """

    def setup_primary(self):
        self.subjects_populate()
        self.classes_populate_primary()
        self.venues_populate()
        self.institution_type = Types.INSTITUTION_PRIMARY

    def setup_secondary(self):
        self.subjects_populate()
        self.teachers_populate()
        self.classes_populate_secondary()
        self.venues_populate()
        self.institution_type = Types.INSTITUTION_SECONDARY

    def setup_tertiary(self):
        self.modules_populate()
        self.lecturers_populate()
        self.courses_populate()
        self.venues_populate()
        self.institution_type = Types.INSTITUTION_COLLEGE

    def setup_window(self):
        institution = self.builder.timetable_get_institution_type()
        if institution == Types.INSTITUTION_PRIMARY:
            self.setup_primary()
        elif institution == Types.INSTITUTION_SECONDARY:
            self.setup_secondary()
        else:
            self.setup_tertiary()
            
    def refresh_data(self, data_type: str):
        if data_type == Types.MODULES:
            self.modules_populate()
        elif data_type == Types.SUBJECTS:
            self.subjects_populate()
        elif data_type == Types.LECTURERS:
            self.lecturers_populate()
        elif data_type == Types.TEACHERS:
            self.teachers_populate()
        elif data_type == Types.CLASSES:
            institution = self.builder.timetable_get_institution_type()
            if institution == Types.INSTITUTION_PRIMARY:
                self.classes_populate_primary()
            elif institution == Types.INSTITUTION_SECONDARY:
                self.classes_populate_secondary()
        elif data_type == Types.COURSES:
            self.courses_populate()
        elif data_type == Types.VENUES:
            self.venues_populate()

    # ============================= MODULES ==========================
    # ================================================================

    def modules_add(self):
        self.dialog_window = AddModuleWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def modules_populate(self):
        modules = self.builder.module_get_all()
        self.modules_table.clearContents()
        self.modules_table.setRowCount(0)
        courses_set = []

        for module in modules:
            courses = [(f"{self.builder.course_get(course).short_name} - "
                        f"{module.courses[course][Types.LEVEL]} - "
                        f"[{module.courses[course][Types.COURSE_MODULE_CODE]}]")
                       for course in module.courses]

            for course in module.courses:
                courses_set.append((f"{self.builder.course_get(course).short_name} - "
                                    f"{module.courses[course][Types.LEVEL]} - "
                                    f"{self.builder.course_get(course).name}"
                                    ))

            venues = [self.builder.venue_get(venue).name for venue in module.venues]
            lecturer = self.builder.lecturer_get(module.lecturer).name
            self.modules_table.add_item(module.id, module.name, module.code,
                                        lecturer, courses,
                                        venues, module.time_slots,
                                        module.slots_per_day)

        courses_set = {course_ for course_ in courses_set}
        for course_ in courses_set:
            self.ui.modules_course_filter.addItem(course_)

    def modules_module_search(self):
        modules = self.builder.module_get_all()
        self.modules_table.clearContents()
        self.modules_table.setRowCount(0)
        search_text = self.ui.modules_search.text()

        if len(modules) > 0 and search_text:

            search_index = [module.name for module in modules]
            results = Utils().list_search(search_text, search_index)
            matches = [modules[i] for i in results]

            if len(matches) > 0:
                for module in matches:
                    courses = [(f"{self.builder.course_get(course).short_name} - "
                                f"{module.courses[course][Types.LEVEL]} - "
                                f"[{module.courses[course][Types.COURSE_MODULE_CODE]}]")
                               for course in module.courses]
                    venues = [self.builder.venue_get(venue).name for venue in module.venues]
                    lecturer = self.builder.lecturer_get(module.lecturer).name
                    self.modules_table.add_item(module.id, module.name, module.code,
                                                lecturer, courses,
                                                venues, module.time_slots,
                                                module.slots_per_day)
        else:
            self.modules_populate()

    def modules_filter(self):
        modules = self.builder.module_get_all()
        self.modules_table.clearContents()
        self.modules_table.setRowCount(0)

        if (len(modules) > 0 and self.ui.modules_course_filter.currentText()
                and self.ui.modules_course_filter.currentText() != "Filter By Course"):
            for module in modules:

                for course in module.courses:
                    course_filter_prefix = (f"{self.builder.course_get(course).short_name} - "
                                            f"{module.courses[course][Types.LEVEL]} - "
                                            f"{self.builder.course_get(course).name}"
                                            )
                    if course_filter_prefix == self.ui.modules_course_filter.currentText():
                        courses = [(f"{self.builder.course_get(course).short_name} - "
                                    f"{module.courses[course][Types.LEVEL]} - "
                                    f"[{module.courses[course][Types.COURSE_MODULE_CODE]}]")
                                   for course in module.courses]
                        venues = [self.builder.venue_get(venue).name for venue in module.venues]
                        lecturer = self.builder.lecturer_get(module.lecturer).name
                        self.modules_table.add_item(module.id, module.name, module.code,
                                                    lecturer, courses,
                                                    venues, module.time_slots,
                                                    module.slots_per_day)
                        break
        else:
            self.modules_populate()

    # ============================= SUBJECTS =========================
    # ================================================================

    def subjects_add(self):
        self.dialog_window = AddSubjectWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def subjects_populate(self):
        subjects = self.builder.subject_get_all()

        self.subjects_table.clearContents()
        self.subjects_table.setRowCount(0)
        classes_set = []

        for subject in subjects:

            for class_ in self.builder.subject_get_classes(subject.id):
                classes_set.append(class_.name)

            venue = (self.builder.venue_get(subject.primary_venue).name
                     if subject.primary_venue != Types.VENUE_PRIMARY else "Classroom")
            self.subjects_table.add_item(subject.id, subject.name, venue)

        classes_set = {class_ for class_ in classes_set}
        for class_ in classes_set:
            self.ui.subjects_class_filter.addItem(class_)

    def subjects_subject_search(self):
        subjects = self.builder.subject_get_all()
        self.subjects_table.clearContents()
        self.subjects_table.setRowCount(0)
        search_text = self.ui.subjects_search.text()

        if len(subjects) > 0 and search_text:

            search_index = [subject.name for subject in subjects]
            results = Utils().list_search(search_text, search_index)
            matches = [subjects[i] for i in results]

            if len(matches) > 0:
                for subject in matches:
                    venue = (self.builder.venue_get(subject.primary_venue).name
                             if subject.primary_venue != Types.VENUE_PRIMARY else "Classroom")
                    self.subjects_table.add_item(subject.id, subject.name, venue)
        else:
            self.subjects_populate()

    def subjects_filter(self):
        subjects = self.builder.subject_get_all()
        self.subjects_table.clearContents()
        self.subjects_table.setRowCount(0)

        if (len(subjects) > 0 and self.ui.subjects_class_filter.currentText()
                and self.ui.subjects_class_filter.currentText() != "Filter By Class"):
            subjects = [subject.id for subject in subjects]
            for class_ in self.builder.class_get_all():
                if class_.name == self.ui.subjects_class_filter.currentText():
                    class_subjects = class_.subjects
                    for subject in class_subjects:
                        if subject in subjects:
                            subject = self.builder.subject_get(subject)
                            venue = (self.builder.venue_get(subject.primary_venue).name
                                     if subject.primary_venue != Types.VENUE_PRIMARY else "Classroom")
                            self.subjects_table.add_item(subject.id, subject.name, venue)
                    break
        else:
            self.subjects_populate()

    # ============================= LECTURERS ========================
    # ================================================================

    def lecturers_add(self):
        self.dialog_window = AddLecturerWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def lecturers_populate(self):
        lecturers = self.builder.lecturer_get_all()
        self.lecturers_table.clearContents()
        self.lecturers_table.setRowCount(0)

        for lecturer in lecturers:
            if lecturer.id != Types.UNAVAILABLE:
                self.lecturers_table.add_item(lecturer.id, lecturer.name)

    def lecturers_lecturer_search(self):

        lecturers = self.builder.lecturer_get_all()
        self.lecturers_table.clearContents()
        self.lecturers_table.setRowCount(0)
        search_text = self.ui.lecturers_search.text()

        if len(lecturers) > 0 and search_text:

            search_index = [lecturer.name for lecturer in lecturers]
            results = Utils().list_search(search_text, search_index)
            matches = [lecturers[i] for i in results]

            if len(matches) > 0:
                for lecturer in matches:
                    if lecturer.id != Types.UNAVAILABLE:
                        self.lecturers_table.add_item(lecturer.id, lecturer.name)
        else:
            self.lecturers_populate()

    # ============================= TEACHERS =========================
    # ================================================================

    def teachers_add(self):
        self.dialog_window = AddTeacherWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def teachers_populate(self):
        teachers = self.builder.teacher_get_all()
        self.teachers_table.clearContents()
        self.teachers_table.setRowCount(0)

        for teacher in teachers:
            if teacher.id != Types.UNAVAILABLE:
                self.teachers_table.add_item(teacher.id, teacher.name)

    def teachers_teacher_search(self):
        teachers = self.builder.teacher_get_all()
        self.teachers_table.clearContents()
        self.teachers_table.setRowCount(0)
        search_text = self.ui.teachers_search.text()

        if len(teachers) > 0 and search_text:

            search_index = [teacher.name for teacher in teachers]
            results = Utils().list_search(search_text, search_index)
            matches = [teachers[i] for i in results]

            if len(matches) > 0:
                for teacher in matches:
                    if teacher.id != Types.UNAVAILABLE:
                        self.teachers_table.add_item(teacher.id, teacher.name)
        else:
            self.teachers_populate()

    # ============================= CLASSES ==========================
    # ================================================================

    def classes_add(self):
        self.dialog_window = AddClassWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def classes_populate_primary(self):
        classes = self.builder.class_get_all()
        self.classes_table.clearContents()
        self.classes_table.setRowCount(0)

        for class_ in classes:
            subjects = [(f"<font color='#414141'><b>{i + 1}. "
                         f"{self.builder.subject_get(subject).name}</b></font> - Slots: "
                         f"{class_.subjects[subject]['time_slots']} - Daily: "
                         f"{class_.subjects[subject]['slots_per_day']}<br><br>\n")
                        for i, subject in enumerate(class_.subjects)]
            self.classes_table.add_item(class_.id, class_.name, self.builder.venue_get(class_.venue).name, subjects)

    def classes_class_search(self):
        classes = self.builder.class_get_all()
        self.classes_table.clearContents()
        self.classes_table.setRowCount(0)
        search_text = self.ui.classes_search.text()

        if len(classes) > 0 and search_text:

            search_index = [class_.name for class_ in classes]
            results = Utils().list_search(search_text, search_index)
            matches = [classes[i] for i in results]

            if len(matches) > 0:

                if self.institution_type == Types.INSTITUTION_PRIMARY:
                    for class_ in matches:
                        subjects = [(f"<font color='#414141'><b>{i + 1}. "
                                     f"{self.builder.subject_get(subject).name}</b></font> - Slots: "
                                     f"{class_.subjects[subject]['time_slots']} - Daily: "
                                     f"{class_.subjects[subject]['slots_per_day']}<br><br>\n")
                                    for i, subject in enumerate(class_.subjects)]
                        self.classes_table.add_item(class_.id, class_.name, self.builder.venue_get(class_.venue).name,
                                                    subjects)
                else:
                    for class_ in matches:
                        subjects = [(f"<font color='#414141'><b>{i + 1}. "
                                     f"{self.builder.subject_get(subject).name}</b>"
                                     f"<br>{self.builder.teacher_get(class_.subjects[subject]['teacher']).name}"
                                     f" - Slots: "
                                     f"{class_.subjects[subject]['time_slots']} - Daily: "
                                     f"{class_.subjects[subject]['slots_per_day']}</font><br><br>")
                                    for i, subject in enumerate(class_.subjects)]
                        self.classes_table.add_item(class_.id, class_.name, self.builder.venue_get(class_.venue).name,
                                                    subjects)
        else:
            if self.institution_type == Types.INSTITUTION_PRIMARY:
                self.classes_populate_primary()
            else:
                self.classes_populate_secondary()

    def classes_populate_secondary(self):
        classes = self.builder.class_get_all()
        self.classes_table.clearContents()
        self.classes_table.setRowCount(0)

        for class_ in classes:
            subjects = [(f"<font color='#414141'><b>{i + 1}. "
                         f"{self.builder.subject_get(subject).name}</b>"
                         f"<br>{self.builder.teacher_get(class_.subjects[subject]['teacher']).name} - Slots: "
                         f"{class_.subjects[subject]['time_slots']} - Daily: "
                         f"{class_.subjects[subject]['slots_per_day']}</font><br><br>")
                        for i, subject in enumerate(class_.subjects)]
            self.classes_table.add_item(class_.id, class_.name, self.builder.venue_get(class_.venue).name, subjects)

    # ============================= COURSES ==========================
    # ================================================================

    def courses_add(self):
        self.dialog_window = AddCourseWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def courses_populate(self):
        courses = self.builder.course_get_all()
        self.courses_table.clearContents()
        self.courses_table.setRowCount(0)

        for course in courses:
            self.courses_table.add_item(course.id, course.name, course.short_name)

    def courses_course_search(self):
        courses = self.builder.course_get_all()
        self.courses_table.clearContents()
        self.courses_table.setRowCount(0)
        search_text = self.ui.courses_search.text()

        if len(courses) > 0 and search_text:

            search_index = [course.name for course in courses]
            results = Utils().list_search(search_text, search_index)
            matches = [courses[i] for i in results]

            if len(matches) > 0:
                for course in matches:
                    self.courses_table.add_item(course.id, course.name, course.short_name)
        else:
            self.courses_populate()

    # ============================= VENUES ===========================
    # ================================================================

    def venues_add(self):
        self.dialog_window = AddVenueWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def venues_populate(self):
        venues = self.builder.venue_get_all()
        self.venues_table.clearContents()
        self.venues_table.setRowCount(0)

        for venue in venues:
            if venue.id != Types.UNAVAILABLE:
                self.venues_table.add_item(venue.id, venue.name, venue.location, venue.location_description)

    def venues_venue_search(self):
        venues = self.builder.venue_get_all()
        self.venues_table.clearContents()
        self.venues_table.setRowCount(0)
        search_text = self.ui.venues_search.text()

        if len(venues) > 0 and search_text:

            search_index = [venue.name for venue in venues]
            results = Utils().list_search(search_text, search_index)
            matches = [venues[i] for i in results]

            if len(matches) > 0:
                for venue in matches:
                    if venue.id != Types.UNAVAILABLE:
                        self.venues_table.add_item(venue.id, venue.name, venue.location, venue.location_description)
        else:
            self.venues_populate()


def close_project():
    app_window.close()
    app_window.ui.stacked_container.setCurrentIndex(0)
    startup.populate_recent()
    startup.show()


if __name__ == "__main__":
    app = QApplication()

    settings = Settings()
    startup = StartUpWindow()
    app_window = AppWindow()

    startup.show()

    sys.exit(app.exec())
