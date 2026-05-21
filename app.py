from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QLineEdit
from PySide6.QtGui import QIcon
from utils.builders import PrimaryBuilder, SecondaryBuilder, TertiaryBuilder
from utils.data import TimeTableInitData
from utils import Types
from utils import Utils, Settings, FileLoader
from utils.logger_config import logger
from windows import Main, StartUp, Viewer, Export, TertiaryExport
from widgets import (ModulesTable, SubjectsTable, BlocksTable,
                     TeachersTable, LecturersTable, ClassesTable,
                     CoursesTable, VenuesTable, LoadingDialog, ExitConfirm,
                     TertiaryVenuesTable, CoursesEnrollmentTable, MessageBox,
                     Confirmation)
from windows.dialog_windows import (AddModuleWindow, AddModuleDataWindow, AddSubjectWindow,
                                    AddLecturerWindow, AddTeacherWindow, AddCourseWindow,
                                    AddClassWindow, AddClassDataWindow, AddClassDataPrimaryWindow,
                                    AddVenueWindow, AddBlockWindow, AddBlockDataWindow, AddBreakWindow,
                                    ProjectsWindow, AddTertiaryVenueWindow)
from developers import Developers
from typing import Union, Optional
import sys
import functools


class StartUpWindow(StartUp):

    def __init__(self):
        super().__init__()
        self.open_project_btn.clicked.connect(self.open_project)
        self.import_project_btn.clicked.connect(self.import_project)

    def open_project(self):
        loading_dialog = LoadingDialog(self)
        loading_dialog.show()
        app.processEvents()
        file_path = ProjectsWindow.get_project(self)
        loading_dialog.close()

        if file_path:
            try:
                file_loader = FileLoader(file_path)
                time_table_data = file_loader.load_tbl()
            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            if time_table_data and file_loader:
                institution = time_table_data[Types.INSTITUTION_TYPE]
                builder = (
                    PrimaryBuilder if institution == Types.INSTITUTION_PRIMARY else
                    SecondaryBuilder if institution == Types.INSTITUTION_SECONDARY else
                    TertiaryBuilder
                )
                builder = builder(file_path, file_loader=file_loader)
                project_name = Utils.project_path_to_name(file_path)
                settings.add_recent_file(project_name, file_path)
                app_window.set_builder(builder)
                self.populate_recent()
                self.close()
                self.project_open.emit(institution, project_name)

    def import_project(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        if file_path:
            try:
                import_path = Utils.get_timetables_path()
                file_loader = FileLoader(file_path)
                time_table_data = file_loader.load_tbl()
                file_path = Utils.save_file(file_path, None, import_path)

            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            if time_table_data:
                institution = time_table_data[Types.INSTITUTION_TYPE]
                builder = (
                    PrimaryBuilder if institution == Types.INSTITUTION_PRIMARY else
                    SecondaryBuilder if institution == Types.INSTITUTION_SECONDARY else
                    TertiaryBuilder
                )
                builder = builder(file_path, file_loader=file_loader)
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
                                          days_per_cycle, slots_per_day)
            file = Utils().create_project_file(time_table_name, name)
            file_loader = FileLoader(file)
            builder = builder(file, init_data, file_loader)
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
                file_loader = FileLoader(file_path)
                try:
                    time_table_data = file_loader.load_tbl()
                except Exception as e:
                    MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                    logger.warning(str(e))
                    return

                if time_table_data:
                    institution = time_table_data[Types.INSTITUTION_TYPE]
                    builder = (
                        PrimaryBuilder if institution == Types.INSTITUTION_PRIMARY else
                        SecondaryBuilder if institution == Types.INSTITUTION_SECONDARY else
                        TertiaryBuilder
                    )
                    builder = builder(file_path, file_loader=file_loader)
                    project_name = Utils.project_path_to_name(file_path)
                    settings.add_recent_file(project_name, file_path)
                    app_window.set_builder(builder)
                    self.populate_recent()
                    self.close()
                    self.project_open.emit(institution, project_name)

    def populate_recent(self):
        loading_dialog = LoadingDialog(self)
        loading_dialog.show()
        app.processEvents()
        super().populate_recent()
        loading_dialog.close()


class AppWindow(Main):
    def __init__(self):
        super().__init__()
        self.builder: Optional[PrimaryBuilder, SecondaryBuilder, TertiaryBuilder] = None
        self.file: Optional[str] = None
        self.institution_type: Optional[str] = None
        self.dialog_window = None
        self.viewer = Viewer()

        self.modules_table = ModulesTable()
        self.subjects_table = SubjectsTable()
        self.blocks_table = BlocksTable()
        self.teachers_table = TeachersTable()
        self.lecturers_table = LecturersTable()
        self.classes_table = ClassesTable()
        self.courses_table = CoursesTable()
        self.venues_table = VenuesTable()
        self.tertiary_venues_table = TertiaryVenuesTable()
        self.courses_enrollment_table = CoursesEnrollmentTable()

        self.ui.modules_table_layout.addWidget(self.modules_table)
        self.ui.subjects_table_layout.addWidget(self.subjects_table)
        self.ui.lecturers_table_layout.addWidget(self.lecturers_table)
        self.ui.teachers_table_layout.addWidget(self.teachers_table)
        self.ui.courses_table_layout.addWidget(self.courses_table)
        self.ui.enrollment_courses_table_layout.addWidget(self.courses_enrollment_table)
        self.ui.classes_table_layout.addWidget(self.classes_table)
        self.ui.blocks_table_layout.addWidget(self.blocks_table)

        self.ui.modules_course_filter.lineEdit().setPlaceholderText("Filter by course")
        self.ui.subjects_class_filter.lineEdit().setPlaceholderText("Filter by class")
        self.set_generated(True)
        self.set_saved(True)
        self.settings_btn.hide()
        self.ui.name_start_time_txt.setDisplayFormat("HH:mm")

        self._init_signals()

    def _init_signals(self):
        self.close_btn.clicked.connect(self.close_app)
        startup.project_open.connect(self.open_project)
        startup.project_create.connect(self.create_project)
        self.close_project_btn.clicked.connect(close_project)

        self.ui.modules_course_filter.currentTextChanged.connect(self.modules_filter)
        self.ui.modules_search.textChanged.connect(self.modules_module_search)
        self.ui.subjects_class_filter.currentTextChanged.connect(self.subjects_filter)
        self.ui.subjects_search.textChanged.connect(self.subjects_subject_search)
        self.ui.blocks_search.textChanged.connect(self.blocks_block_search)
        self.ui.lecturers_search.textChanged.connect(self.lecturers_lecturer_search)
        self.ui.teachers_search.textChanged.connect(self.teachers_teacher_search)
        self.ui.courses_search.textChanged.connect(self.courses_course_search)
        self.ui.classes_search.textChanged.connect(self.classes_class_search)
        self.ui.venues_search.textChanged.connect(self.venues_venue_search)

        self.modules_table.set_action_handler(self.modules_callback)
        self.subjects_table.set_action_handler(self.subjects_callback)
        self.blocks_table.set_action_handler(self.blocks_callback)
        self.teachers_table.set_action_handler(self.teachers_callback)
        self.lecturers_table.set_action_handler(self.lecturers_callback)
        self.classes_table.set_action_handler(self.classes_callback)
        self.courses_table.set_action_handler(self.courses_callback)
        self.venues_table.set_action_handler(self.venues_callback)
        self.tertiary_venues_table.set_action_handler(self.venues_callback)
        self.courses_enrollment_table.set_action_handler(self.enrollment_callback)

        self.ui.modules_add_btn.clicked.connect(self.modules_add)
        self.ui.modules_auto_assign_btn.clicked.connect(self.modules_assign_venues)
        self.ui.subjects_add_btn.clicked.connect(self.subjects_add)
        self.ui.add_break_btn.clicked.connect(self.break_add)
        self.ui.blocks_add_btn.clicked.connect(self.blocks_add)
        self.ui.lecturers_add_btn.clicked.connect(self.lecturers_add)
        self.ui.teachers_add_btn.clicked.connect(self.teachers_add)
        self.ui.courses_add_btn.clicked.connect(self.courses_add)
        self.ui.classes_add_btn.clicked.connect(self.classes_add)
        self.ui.venues_add_btn.clicked.connect(self.venues_add)
        self.ui.name_times_btn.clicked.connect(self.name_slots_and_days)

    """
    =============================================================
        UI MANIPULATION
    =============================================================
    """

    def signal_clear(self):
        self.ui.cfg_daily_slots.valueChanged.disconnect()
        self.ui.cfg_days_per_cycle.valueChanged.disconnect()

    def clear(self):
        self.ui.current_project.setText("")
        self.signal_clear()
        self.dialog_window = None
        self.modules_table.clearContents()
        self.subjects_table.clearContents()
        self.blocks_table.clearContents()
        self.teachers_table.clearContents()
        self.lecturers_table.clearContents()
        self.classes_table.clearContents()
        self.courses_table.clearContents()
        self.venues_table.clearContents()

    def close_app(self):
        proceed = True
        if not self.builder.is_saved():
            proceed = ExitConfirm.confirm(self)
        if proceed:
            self.close()
            app.quit()

    def build_menu(self, institution_type):
        super().build_menu(institution_type)

        if self.ui.venues_table_layout.count() > 0:
            w = self.ui.venues_table_layout.takeAt(0).widget()
            w.setParent(None)
        if institution_type == Types.INSTITUTION_TERTIARY:
            self.ui.venues_table_layout.addWidget(self.tertiary_venues_table)
        else:
            self.ui.venues_table_layout.addWidget(self.venues_table)
        self.edit_menu.addAction("Undo", self.undo)
        self.edit_menu.addAction("Add Venue")

        self.file_menu.addAction("Open", self.change_project)
        self.file_menu.addAction("New Project", self.new_project)
        self.file_menu.addAction("Save", self.builder.timetable_save)
        self.file_menu.addAction("Save As", self.save_as)
        self.file_menu.addAction("Export", self.export)

        if institution_type == Types.INSTITUTION_TERTIARY:
            self.file_menu.addAction("Export html", self.export_html)
            self.file_menu.addAction("Export Js API", self.export_js)

        self.file_menu.addAction("Exit", self.close)

        self.timetable_menu.addAction("Clear timetable", self.timetable_clear)
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
            self.edit_menu.addAction("Add Block", self.blocks_add)

        elif institution_type == Types.INSTITUTION_TERTIARY:
            self.edit_menu.addAction("Add Lecturer", self.lecturers_add)
            self.edit_menu.addAction("Add Module", self.modules_add)
            self.edit_menu.addAction("Add Program", self.courses_add)
            self.edit_menu.addAction("Import Modules", self.modules_import)
            self.edit_menu.addAction("Import Lecturers", self.lecturers_import)
            self.edit_menu.addAction("Import Programs", self.courses_import)
            self.edit_menu.addAction("Import Venues", self.venues_import)
            self.edit_menu.addAction("Import Enrollments", self.enrollments_import)
            self.edit_menu.addAction("Merge Timetable data", self.datas_merge)

        self.tools_menu.addAction("Viewer", self.show_viewer)
        self.tools_menu.addAction("Online Portal", Utils.view_portal)
        self.tools_btn.setMenu(self.tools_menu)

        self.edit_btn.setMenu(self.edit_menu)
        self.timetable_btn.setMenu(self.timetable_menu)
        self.file_btn.setMenu(self.file_menu)
        self.save_btn.clicked.connect(self.builder.timetable_save)
        self.builder.saved.connect(self.set_saved)
        self.builder.generated.connect(self.set_generated)

    def change_project(self):
        self.signal_clear()
        startup.open_project()

    def new_project(self):
        self.signal_clear()
        startup.boarding.show()

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
            self.subjects_populate()
            institution = self.builder.timetable_get_institution_type()
            if institution == Types.INSTITUTION_SECONDARY:
                self.classes_populate_secondary()

    def blocks_callback(self, block_id, action):
        if action == "edit":
            self.dialog_window = AddBlockWindow(self.builder, True, block_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "add_data":
            self.dialog_window = AddBlockDataWindow(self.builder, block_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.block_remove(block_id)
            self.blocks_populate()

    def lecturers_callback(self, lecturer_id, action):
        if action == "edit":
            self.dialog_window = AddLecturerWindow(self.builder, True, lecturer_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.lecturer_remove(lecturer_id)
            self.lecturers_populate()
            self.modules_populate()

    def teachers_callback(self, teacher_id, action):
        if action == "edit":
            self.dialog_window = AddTeacherWindow(self.builder, True, teacher_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.teacher_remove(teacher_id)
            self.teachers_populate()
            institution = self.builder.timetable_get_institution_type()
            if institution == Types.INSTITUTION_SECONDARY:
                self.classes_populate_secondary()
                self.blocks_populate()

    def courses_callback(self, course_id, action):
        if action == "edit":
            self.dialog_window = AddCourseWindow(self.builder, True, course_id, self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        elif action == "delete":
            self.builder.course_remove(course_id)
            self.courses_populate()
            self.modules_populate()

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
            self.refresh_data(Types.CLASSES)

    def venues_callback(self, venue_id, action):
        if action == "edit":
            if self.builder.timetable_get_institution_type() == Types.INSTITUTION_TERTIARY:
                self.dialog_window = AddTertiaryVenueWindow(self.builder, True, venue_id, self)
                self.dialog_window.saved.connect(self.refresh_data)
                self.dialog_window.show()
            else:
                self.dialog_window = AddVenueWindow(self.builder, True, venue_id, self)
                self.dialog_window.saved.connect(self.refresh_data)
                self.dialog_window.show()
        elif action == "delete":
            self.builder.venue_remove(venue_id)
            self.venues_populate()
            institution = self.builder.timetable_get_institution_type()
            if institution == Types.INSTITUTION_SECONDARY:
                self.classes_populate_secondary()
                self.subjects_populate()
            elif institution == Types.INSTITUTION_TERTIARY:
                self.modules_populate()

    def enrollment_callback(self, course_id, action):
        if action == "edit_enrollment":
            self.populate_course_enrollment(course_id)

    """
    ======================================================
        PROJECT MANAGEMENT
    ======================================================
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

    def export(self):
        if self.institution_type == Types.INSTITUTION_TERTIARY:
            self.dialog_window = TertiaryExport(self.builder, self)
            self.dialog_window.show()
        else:
            self.dialog_window = Export(self.builder, self)
            self.dialog_window.show()

    def export_html(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export HTML Timetable",
            f"{self.builder.timetable_get_name().replace(" ", "_").lower()}.html",
            "Html Files (*.html)")

        if file_path:
            with open(str(file_path), "w") as f:
                f.write(Developers.get_timetable_html(self.builder.timetable_data_get()))
            MessageBox(self).information("Export success", f"Html Timetable exported successfully! "
                                                           f"\n{file_path}")

    def export_js(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Js API",
            f"{self.builder.timetable_get_name().replace(" ", "_").lower()}_api.js",
            "JavaScript Files (*.js)")

        if file_path:
            with open(str(file_path), "w") as f:
                f.write(Developers.get_js_api(self.builder.timetable_data_get()))
            MessageBox(self).information("Export success", f"JavaScript Timetable API exported successfully! "
                                                           f"\n{file_path}")

    def undo(self):
        loading_dialog = LoadingDialog(app_window)
        loading_dialog.show()
        app.processEvents()
        self.builder.reload()
        self.set_generated(True)
        self.setup_window()
        loading_dialog.close()

    def set_builder(self, builder: Union[PrimaryBuilder, SecondaryBuilder, TertiaryBuilder]):
        self.builder = builder
        self.builder.builder_parent = self

    def create_project(self, institution, project_name):
        loading_dialog = LoadingDialog()
        loading_dialog.show()
        app.processEvents()
        try:
            self.current_project.setText(project_name.replace("_", " "))
            self.file = self.builder.get_file()
            self.build_menu(institution)
            self.setup_window()
            self.show()
        except Exception as e:
            MessageBox(self).critical("Invalid file", f"Could not use this file: {str(e)}")
            logger.critical(str(e))
        loading_dialog.close()

    def open_project(self, institution: str, project_name: str):
        loading_dialog = LoadingDialog()
        loading_dialog.show()
        app.processEvents()
        try:
            self.current_project.setText(project_name.replace("_", " "))
            self.file = self.builder.get_file()
            self.build_menu(institution)
            self.setup_window()
            self.show()
        except Exception as e:
            MessageBox(self).critical("Invalid file", f"Could not use this file: {str(e)}")
            logger.critical(str(e))
        loading_dialog.close()

    def populate_slots_days(self):
        self.days_table.clearContents()
        self.days_table.setRowCount(0)
        self.slots_table.clearContents()
        self.slots_table.setRowCount(0)

        slots = self.builder.timetable_slots()
        days = self.builder.timetable_days()

        for slot in range(self.builder.timetable_get_slots_per_day()):
            slot = str(slot + 1)
            if slot in slots:
                self.add_slot_table_item(slot, slots[slot])
            else:
                self.add_slot_table_item(slot, "")

        for day in range(self.builder.timetable_get_days_per_cycle()):
            day = str(day + 1)
            if day in days:
                self.add_day_table_item(day, days[day])
            else:
                self.add_day_table_item(day, "")

    def populate_slots(self):
        self.slots_table.clearContents()
        self.slots_table.setRowCount(0)

        slots = self.builder.timetable_slots()
        for slot in range(self.builder.timetable_get_slots_per_day()):
            slot = str(slot + 1)
            if slot in slots:
                self.add_slot_table_item(slot, slots[slot])
            else:
                self.add_slot_table_item(slot, "")

    def populate_days(self):
        self.days_table.clearContents()
        self.days_table.setRowCount(0)
        days = self.builder.timetable_days()

        for day in range(self.builder.timetable_get_days_per_cycle()):
            day = str(day + 1)
            if day in days:
                self.add_day_table_item(day, days[day])
            else:
                self.add_day_table_item(day, "")

    def show_viewer(self):
        loading_dialog = LoadingDialog()
        loading_dialog.show()
        app.processEvents()
        self.viewer.view(self.builder)
        loading_dialog.close()

    """
    =========================================================
        PROJECT DATA MANAGEMENT
    =========================================================
    """

    def setup_primary(self):
        self.subjects_populate()
        self.classes_populate_primary()
        self.venues_populate()
        self.institution_type = Types.INSTITUTION_PRIMARY

        self.ui.cfg_daily_slots.setValue(self.builder.timetable_get_slots_per_day())
        self.ui.cfg_days_per_cycle.setValue(self.builder.timetable_get_days_per_cycle())

    def setup_secondary(self):
        self.subjects_populate()
        self.teachers_populate()
        self.classes_populate_secondary()
        self.venues_populate()
        self.blocks_populate()
        self.institution_type = Types.INSTITUTION_SECONDARY

        self.ui.cfg_daily_slots.setValue(self.builder.timetable_get_slots_per_day())
        self.ui.cfg_days_per_cycle.setValue(self.builder.timetable_get_days_per_cycle())

    def setup_tertiary(self):
        self.modules_populate()
        self.lecturers_populate()
        self.courses_populate()
        self.venues_populate()
        self.institution_type = Types.INSTITUTION_TERTIARY

        self.ui.cfg_daily_slots.setValue(self.builder.timetable_get_slots_per_day())
        self.ui.cfg_days_per_cycle.setValue(self.builder.timetable_get_days_per_cycle())

    def setup_window(self):
        institution = self.builder.timetable_get_institution_type()
        self.ui.timetable_generate_btn.clicked.connect(self.builder.generate)
        self.ui.timetable_view_btn.clicked.connect(self.show_viewer)
        self.set_saved(True)
        self.set_generated(True)

        if institution == Types.INSTITUTION_PRIMARY:
            self.setup_primary()
            self.ui.timetable_generate_updates_btn.show()
            self.ui.timetable_generate_updates_btn.clicked.connect(self.builder.generate_patches)
        elif institution == Types.INSTITUTION_SECONDARY:
            self.setup_secondary()
            self.ui.timetable_generate_updates_btn.show()
            self.ui.timetable_generate_updates_btn.clicked.connect(self.builder.generate_patches)
        else:
            self.ui.timetable_generate_updates_btn.hide()
            self.setup_tertiary()

        self.ui.cfg_daily_slots.valueChanged.connect(self.timetable_change_slots_per_day)
        self.ui.cfg_days_per_cycle.valueChanged.connect(self.timetable_change_days_per_cycle)
        self.populate_slots_days()

    def refresh_data(self, data_type: str):
        if data_type == Types.MODULES:
            self.modules_populate()
        elif data_type == Types.SUBJECTS:
            self.subjects_populate()
        elif data_type == Types.BLOCKS:
            self.blocks_populate()
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
            institution = self.builder.timetable_get_institution_type()
            if institution == Types.INSTITUTION_SECONDARY:
                self.classes_populate_secondary()
                self.subjects_populate()

    # ============================= TIMETABLE ========================
    # ================================================================

    def timetable_clear(self):
        self.builder.reset_timetable()

    def timetable_change_slots_per_day(self):
        self.builder.timetable_change_header(Types.SLOTS_PER_DAY, self.ui.cfg_daily_slots.value())
        self.name_slots_and_days()
        self.populate_slots()

    def timetable_change_days_per_cycle(self):
        self.builder.timetable_change_header(Types.DAYS_PER_CYCLE, self.ui.cfg_days_per_cycle.value())
        self.name_slots_and_days()
        self.populate_days()

    def add_slot_table_item(self, slot_id, slot_name):
        row = self.slots_table.rowCount()
        self.slots_table.insertRow(row)
        slot = QLabel(slot_id)
        name = QLineEdit()
        name.setPlaceholderText("Period Name")
        name.setText(slot_name)
        func = functools.partial(self.change_slot_name, slot_id)
        name.textChanged.connect(func)
        name.returnPressed.connect(name.clearFocus)
        self.slots_table.setCellWidget(row, 0, slot)
        self.slots_table.setCellWidget(row, 1, name)

    def add_day_table_item(self, day_id, day_name):
        row = self.days_table.rowCount()
        self.days_table.insertRow(row)
        day = QLabel(day_id)
        name = QLineEdit()
        name.setPlaceholderText("Day Name")
        name.setText(day_name)
        func = functools.partial(self.change_day_name, day_id)
        name.textChanged.connect(func)
        name.returnPressed.connect(name.clearFocus)
        self.days_table.setCellWidget(row, 0, day)
        self.days_table.setCellWidget(row, 1, name)

    def change_slot_name(self, slot_id, slot_name: str):
        self.builder.timetable_name_slot(slot_id, slot_name)

    def change_day_name(self, day_id, day_name: str):
        self.builder.timetable_name_day(day_id, day_name)

    def name_slots_and_days(self):
        start_time = self.ui.name_start_time_txt.time().toString("HH:mm")
        slot_names = Utils.generate_slot_names(start_time, self.builder.timetable_get_time_slot_length(),
                                               self.builder.timetable_get_slots_per_day())
        day_names = Utils.generate_day_names(self.builder.timetable_get_days_per_cycle())
        slots = {}
        days = {}

        for slot_id, slot_name in enumerate(slot_names):
            slots[str(slot_id + 1)] = slot_name
        self.builder.timetable_set_slots(slots)

        for day_id, day_name in enumerate(day_names):
            days[str(day_id + 1)] = day_name
        self.builder.timetable_set_days(days)

        self.populate_slots_days()

    def add_enrollment_table_item(self, c_name, level, course_id, enrollment):
        row = self.ui.enrollment_table.rowCount()
        self.ui.enrollment_table.insertRow(row)
        slot = QLabel(c_name + " - " + level)
        name = QLineEdit()
        name.setPlaceholderText("Enrollment")
        name.setText(str(enrollment))
        func = functools.partial(self.change_enrollment, course_id, level)
        name.textChanged.connect(func)
        name.returnPressed.connect(name.clearFocus)
        self.ui.enrollment_table.setCellWidget(row, 0, slot)
        self.ui.enrollment_table.setCellWidget(row, 1, name)

    def change_enrollment(self, course_id, level, enrollment):
        self.builder.add_course_enrollment(course_id, level, enrollment)

    def populate_course_enrollment(self, course_id):
        self.ui.enrollment_table.clearContents()
        self.ui.enrollment_table.setRowCount(0)

        course = self.builder.course_get(course_id)
        short_name = course.short_name
        enrollments = self.builder.get_course_enrollment(course_id)

        for level in enrollments:
            self.add_enrollment_table_item(short_name, level, course_id, enrollments[level][Types.CAPACITY])

    # ============================= MODULES ==========================
    # ================================================================

    def modules_add(self):
        self.dialog_window = AddModuleWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def modules_populate(self):
        self.ui.modules_count.setText(str(self.builder.module_count()))
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
                                        module.slots_per_day, module.duration)

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
                                                module.slots_per_day, module.duration)
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
                                                    module.slots_per_day, module.duration)
                        break
        else:
            self.modules_populate()

    def modules_assign_venues(self):
        loading_dialog = LoadingDialog(self)
        loading_dialog.show()

        try:
            report = self.builder.assign_venues()
            self.modules_populate()
            MessageBox(self).information("Success", f"Automatic venue assignment completed successfully! {report}")
        except Exception as e:
            logger.critical(str(e))
            MessageBox(self).critical("Error", "An error occurred while trying to assign venues.")

        loading_dialog.close()

    # ============================= SUBJECTS =========================
    # ================================================================

    def subjects_add(self):
        self.dialog_window = AddSubjectWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def subjects_populate(self):
        self.ui.subjects_count.setText(str(self.builder.subject_count()))
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

    # ============================= BLOCKS ===========================
    # ================================================================

    def break_add(self):
        self.dialog_window = AddBreakWindow(self.builder, parent=self)
        self.dialog_window.show()

    def blocks_add(self):
        self.dialog_window = AddBlockWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def blocks_populate(self):
        self.ui.blocks_count.setText(str(self.builder.block_count()))
        blocks = self.builder.block_get_all()

        self.blocks_table.clearContents()
        self.blocks_table.setRowCount(0)

        for block in blocks:
            subjects = block.subjects
            block_subjects = [(f"<font color='#414141'><b>{self.builder.subject_get(subject).name}</b><br>"
                               f"Teacher: {self.builder.teacher_get(subjects[subject][Types.TEACHER]).name}<br>"
                               f"Venue: {self.builder.venue_get(subjects[subject][Types.VENUE]).name}"
                               f"<br><br></font>")
                              for subject in subjects]
            classes = [self.builder.class_get(class_).name
                       for class_ in block.classes]
            classes = ", ".join(classes)
            block_subjects = "\n".join(block_subjects)
            self.blocks_table.add_item(block.id, block.name, block_subjects, classes, block.length)

    def blocks_block_search(self):
        blocks = self.builder.block_get_all()
        self.blocks_table.clearContents()
        self.blocks_table.setRowCount(0)
        search_text = self.ui.blocks_search.text()

        if len(blocks) > 0 and search_text:

            search_index = [block.name for block in blocks]
            results = Utils().list_search(search_text, search_index)
            matches = [blocks[i] for i in results]

            if len(matches) > 0:
                for block in matches:
                    subjects = block.subjects
                    block_subjects = [(f"<font color='#414141'><b>{self.builder.subject_get(subject).name}<b><br>"
                                       f"Teacher: {self.builder.teacher_get(subjects[subject][Types.TEACHER]).name} ~ "
                                       f"Venue: {self.builder.venue_get(subjects[subject][Types.VENUE]).name}"
                                       f"<br><br></font>")
                                      for subject in subjects]
                    classes = [self.builder.class_get(class_).name
                               for class_ in block.classes]
                    classes = ", ".join(classes)
                    block_subjects = "".join(block_subjects)
                    self.blocks_table.add_item(block.id, block.name, block_subjects, classes, block.length)
        else:
            self.blocks_populate()

    # ============================= LECTURERS ========================
    # ================================================================

    def lecturers_add(self):
        self.dialog_window = AddLecturerWindow(self.builder, parent=self)
        self.dialog_window.saved.connect(self.refresh_data)
        self.dialog_window.show()

    def lecturers_populate(self):
        self.ui.lecturers_count.setText(str(self.builder.lecturer_count()))
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
        self.ui.teachers_count.setText(str(self.builder.teacher_count()))
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
        self.ui.classes_count.setText(str(self.builder.class_count()))
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
        self.ui.classes_count.setText(str(self.builder.class_count()))
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
        self.ui.courses_count.setText(str(self.builder.course_count()))
        courses = self.builder.course_get_all()
        self.courses_table.clearContents()
        self.courses_table.setRowCount(0)
        self.courses_enrollment_table.clearContents()
        self.courses_enrollment_table.setRowCount(0)

        for course in courses:
            self.courses_table.add_item(course.id, course.name, course.short_name)
            self.courses_enrollment_table.add_item(course.id, course.name, course.short_name)

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
        if self.institution_type == Types.INSTITUTION_TERTIARY:
            self.dialog_window = AddTertiaryVenueWindow(self.builder, parent=self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()
        else:
            self.dialog_window = AddVenueWindow(self.builder, parent=self)
            self.dialog_window.saved.connect(self.refresh_data)
            self.dialog_window.show()

    def venues_populate(self):
        if self.builder.timetable_get_institution_type() == Types.INSTITUTION_TERTIARY:
            self.venues_populate_tertiary()
        else:
            self.ui.venues_count.setText(str(self.builder.venue_count()))
            venues = self.builder.venue_get_all()
            self.venues_table.clearContents()
            self.venues_table.setRowCount(0)

            for venue in venues:
                if venue.id != Types.UNAVAILABLE:
                    self.venues_table.add_item(venue.id, venue.name, venue.location, venue.location_description)

    def venues_populate_tertiary(self):
        self.ui.venues_count.setText(str(self.builder.venue_count()))
        venues = self.builder.venue_get_all()
        self.tertiary_venues_table.clearContents()
        self.tertiary_venues_table.setRowCount(0)

        for venue in venues:
            if venue.id != Types.UNAVAILABLE:
                self.tertiary_venues_table.add_item(venue.id, venue.name, venue.capacity, venue.special)

    def venues_venue_search(self):
        if self.builder.timetable_get_institution_type() == Types.INSTITUTION_TERTIARY:
            self.venues_venue_search_tertiary()
        else:
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

    def venues_venue_search_tertiary(self):
        venues = self.builder.venue_get_all()
        self.tertiary_venues_table.clearContents()
        self.tertiary_venues_table.setRowCount(0)
        search_text = self.ui.venues_search.text()

        if len(venues) > 0 and search_text:

            search_index = [venue.name for venue in venues]
            results = Utils().list_search(search_text, search_index)
            matches = [venues[i] for i in results]

            if len(matches) > 0:
                for venue in matches:
                    if venue.id != Types.UNAVAILABLE:
                        self.tertiary_venues_table.add_item(venue.id, venue.name, venue.capacity, venue.special)
        else:
            self.venues_populate()

    # ============================ IMPORTS ===========================
    # ================================================================

    def courses_import(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        if file_path:
            try:
                file_loader = FileLoader(file_path)
                timetable_data = file_loader.load_tbl()
            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            courses = timetable_data[Types.COURSES]
            do_for_all = False, False

            if len(courses) > 0:
                existing_courses = [course.name.lower().strip() for course in self.builder.course_get_all()]

                for c in courses:
                    name = courses[c][Types.NAME]
                    if name.lower() in existing_courses:
                        if not do_for_all[1]:
                            confirmation = Confirmation.confirm(self, "Already exists",
                                                                f"A program with this name ({name}) already exists. "
                                                                "Do you want to import it anyway?")
                            if confirmation[1]:
                                do_for_all = confirmation
                        else:
                            confirmation = do_for_all

                        if confirmation[0]:
                            self.builder.add_course(name, courses[c][Types.SHORT_NAME])
                    else:
                        self.builder.add_course(name, courses[c][Types.SHORT_NAME])

                self.courses_populate()
                MessageBox(self).information("Success", "Programs imported successfully.")
            else:
                MessageBox(self).warning("Nothing found", "No programs were found in this file.")

    def modules_import(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        if file_path:
            try:
                file_loader = FileLoader(file_path)
                timetable_data = file_loader.load_tbl()
            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            modules = timetable_data[Types.MODULES]
            do_for_all = False, False

            if len(modules) > 0:
                existing_modules = [module.name.lower().strip() for module in self.builder.module_get_all()]

                for m in modules:
                    name = modules[m][Types.NAME]
                    if name.lower().strip() in existing_modules:

                        if not do_for_all[1]:
                            confirmation = Confirmation.confirm(self, "Already exists",
                                                                f"A module with this name ({name}) already "
                                                                f"exists. Do you want to import it anyway?")
                            if confirmation[1]:
                                do_for_all = confirmation
                        else:
                            confirmation = do_for_all

                        if confirmation[0]:
                            courses = modules[m][Types.COURSES]

                            lecturer_name = timetable_data[Types.LECTURERS][modules[m][Types.LECTURER]][Types.NAME]
                            lecturer_exists = self.builder.lecturer_get_by_name(lecturer_name)
                            lecturer = lecturer_exists if lecturer_exists else "unavailable"

                            venues_list = []
                            venues = modules[m][Types.VENUES]

                            for v in venues:
                                v_name = timetable_data[Types.VENUES][v][Types.NAME]
                                if self.builder.venue_exists(v_name):
                                    venues_list.append(self.builder.venue_get_by_name(v_name))

                            courses_list = {}
                            for c in courses:
                                c_name = timetable_data[Types.COURSES][c][Types.NAME]
                                if self.builder.course_exists(c_name):
                                    courses_list[self.builder.course_get_by_name(c_name)] = courses[c]

                            self.builder.add_module(name, modules[m][Types.CODE], lecturer, courses_list,
                                                    venues_list, modules[m][Types.TIME_SLOTS],
                                                    modules[m][Types.SLOTS_PER_DAY], modules[m][Types.DURATION],
                                                    modules[m][Types.FIXED_SESSIONS])

                    else:
                        lecturer_name = timetable_data[Types.LECTURERS][modules[m][Types.LECTURER]][Types.NAME]
                        lecturer_exists = self.builder.lecturer_get_by_name(lecturer_name)
                        lecturer = lecturer_exists if lecturer_exists else "unavailable"

                        venues_list = []
                        venues = modules[m][Types.VENUES]

                        for v in venues:
                            v_name = timetable_data[Types.VENUES][v][Types.NAME]
                            if self.builder.venue_exists(v_name):
                                venues_list.append(self.builder.venue_get_by_name(v_name))

                        courses = modules[m][Types.COURSES]
                        courses_list = {}
                        for c in courses:
                            c_name = timetable_data[Types.COURSES][c][Types.NAME]
                            if self.builder.course_exists(c_name):
                                courses_list[self.builder.course_get_by_name(c_name)] = courses[c]

                        self.builder.add_module(name, modules[m][Types.CODE], lecturer, courses_list,
                                                venues_list, modules[m][Types.TIME_SLOTS],
                                                modules[m][Types.SLOTS_PER_DAY], modules[m][Types.DURATION],
                                                modules[m][Types.FIXED_SESSIONS])
                self.modules_populate()
                MessageBox(self).information("Success", "Modules imported successfully.")
            else:
                MessageBox(self).warning("Nothing found", "No modules were found in this file.")

    def lecturers_import(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        if file_path:
            try:
                file_loader = FileLoader(file_path)
                timetable_data = file_loader.load_tbl()
            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            lecturers = timetable_data[Types.LECTURERS]
            do_for_all = False, False

            if len(lecturers) > 0:
                existing_lecturers = [lecturer.name.lower().strip() for lecturer in self.builder.lecturer_get_all()]

                for lecturer in lecturers:

                    if lecturer == "unavailable":
                        continue

                    name = lecturers[lecturer][Types.NAME]

                    if name.lower() in existing_lecturers:

                        if not do_for_all[1]:
                            confirmation = Confirmation.confirm(self, "Already exists",
                                                                f"A lecturer with this name ({name}) "
                                                                f"already exists. Do you want to import it anyway?")
                            if confirmation[1]:
                                do_for_all = confirmation
                        else:
                            confirmation = do_for_all

                        if confirmation[0]:
                            self.builder.add_lecturer(name)
                    else:
                        self.builder.add_lecturer(name)

                self.lecturers_populate()
                MessageBox(self).information("Success", "Lecturers imported successfully.")
            else:
                MessageBox(self).warning("Nothing found", "No lecturers were found in this file.")

    def venues_import(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        if file_path:
            try:
                file_loader = FileLoader(file_path)
                timetable_data = file_loader.load_tbl()
            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            venues = timetable_data[Types.VENUES]
            do_for_all = False, False

            if len(venues) > 0:
                existing_venues = [venue.name.lower().strip() for venue in self.builder.venue_get_all()]

                for v in venues:

                    if v == "unavailable":
                        continue

                    name = venues[v][Types.NAME]
                    if name.lower() in existing_venues:

                        if not do_for_all[1]:
                            confirmation = Confirmation.confirm(self, "Already exists",
                                                                f"A venue with this name ({name}) already exists. "
                                                                "Do you want to import it anyway?")
                            if confirmation[1]:
                                do_for_all = confirmation
                        else:
                            confirmation = do_for_all

                        if confirmation[0]:
                            self.builder.add_venue(name, venues[v][Types.CAPACITY], venues[v][Types.SPECIAL] == "Yes",
                                                   venues[v][Types.LOCATION], venues[v][Types.LOCATION_DESCRIPTION],
                                                   venues[v][Types.AVAILABLE_DAYS])
                    else:
                        self.builder.add_venue(name, venues[v][Types.CAPACITY], venues[v][Types.SPECIAL] == "Yes",
                                               venues[v][Types.LOCATION], venues[v][Types.LOCATION_DESCRIPTION],
                                               venues[v][Types.AVAILABLE_DAYS])

                self.venues_populate()
                MessageBox(self).information("Success", "Venues imported successfully.")
            else:
                MessageBox(self).warning("Nothing found", "No venues were found in this file.")

    def enrollments_import(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        if file_path:
            try:
                file_loader = FileLoader(file_path)
                timetable_data = file_loader.load_tbl()
            except Exception as e:
                MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                logger.warning(str(e))
                return

            if not isinstance(self.builder, TertiaryBuilder):
                return

            enrollments = timetable_data[Types.CAPACITIES]

            if len(enrollments) > 0:

                existing_courses = [course.id for course in self.builder.course_get_all()]

                for course in enrollments:
                    if course in existing_courses:
                        course_levels = enrollments[course]
                        for level in course_levels:
                            self.builder.add_course_enrollment(course, level, course_levels[level][Types.CAPACITY])

                MessageBox(self).information("Success", "Enrollments imported successfully.")
            else:
                MessageBox(self).warning("Nothing found", "No enrollments were found in this file.")

    def datas_merge(self):

        file_path, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file",
                                                   "", "Timetable (*tbl)")

        confirmation = Confirmation.confirm(self, "Warning",
                                            f"This is a very dangerous process which may result in data damage. "
                                            f"We advise keeping the original file backed up before merging. Continue?")
        if not confirmation[1]:
            return

        loading_dialog = LoadingDialog(self)
        loading_dialog.show()
        app.processEvents()
        try:
            if file_path:
                try:
                    file_loader = FileLoader(file_path)
                    timetable_data = file_loader.load_tbl()
                except Exception as e:
                    MessageBox(self).critical("Invalid file", f"Could not open this file: {str(e)}")
                    logger.warning(str(e))
                    return

                courses = timetable_data[Types.COURSES]
                do_for_all = False, False

                if len(courses) > 0:
                    existing_courses = [course.name.lower().strip() for course in self.builder.course_get_all()]

                    for c in courses:
                        name = courses[c][Types.NAME]
                        if name.lower() in existing_courses:
                            if not do_for_all[1]:
                                confirmation = Confirmation.confirm(self, "Already exists",
                                                                    f"A program with this name ({name}) "
                                                                    f"already exists. Do you want to import it anyway?")
                                if confirmation[1]:
                                    do_for_all = confirmation
                            else:
                                confirmation = do_for_all

                            if confirmation[0]:
                                self.builder.add_course(name, courses[c][Types.SHORT_NAME])
                        else:
                            self.builder.add_course(name, courses[c][Types.SHORT_NAME])

                lecturers = timetable_data[Types.LECTURERS]
                do_for_all = False, False

                if len(lecturers) > 0:
                    existing_lecturers = [lecturer.name.lower().strip() for lecturer in
                                          self.builder.lecturer_get_all()]

                    for lecturer in lecturers:

                        if lecturer == "unavailable":
                            continue

                        name = lecturers[lecturer][Types.NAME]
                        if name.lower() in existing_lecturers:

                            if not do_for_all[1]:
                                confirmation = Confirmation.confirm(self, "Already exists",
                                                                    f"A lecturer with this name ({name}) "
                                                                    f"already exists. Do you want to import it anyway?")
                                if confirmation[1]:
                                    do_for_all = confirmation
                            else:
                                confirmation = do_for_all

                            if confirmation[0]:
                                self.builder.add_lecturer(name)
                        else:
                            self.builder.add_lecturer(name)

                venues = timetable_data[Types.VENUES]
                do_for_all = False, False

                if len(venues) > 0:
                    existing_venues = [venue.name.lower().strip() for venue in self.builder.venue_get_all()]

                    for v in venues:

                        if v == "unavailable":
                            continue

                        name = venues[v][Types.NAME]
                        if name.lower() in existing_venues:

                            if not do_for_all[1]:
                                confirmation = Confirmation.confirm(self, "Already exists",
                                                                    f"A venue with this name ({name}) "
                                                                    f"already exists. Do you want to import it anyway?")
                                if confirmation[1]:
                                    do_for_all = confirmation
                            else:
                                confirmation = do_for_all

                            if confirmation[0]:
                                self.builder.add_venue(name, venues[v][Types.CAPACITY],
                                                       venues[v][Types.SPECIAL] == "Yes",
                                                       venues[v][Types.LOCATION],
                                                       venues[v][Types.LOCATION_DESCRIPTION],
                                                       venues[v][Types.AVAILABLE_DAYS])
                            else:
                                self.builder.add_venue(name, venues[v][Types.CAPACITY],
                                                       venues[v][Types.SPECIAL] == "Yes",
                                                       venues[v][Types.LOCATION], venues[v][Types.LOCATION_DESCRIPTION],
                                                       venues[v][Types.AVAILABLE_DAYS])

                enrollments = timetable_data[Types.CAPACITIES]

                if len(enrollments) > 0:

                    existing_courses = [course.id for course in self.builder.course_get_all()]

                    for course in enrollments:
                        if course in existing_courses:
                            course_levels = enrollments[course]
                            for level in course_levels:
                                self.builder.add_course_enrollment(course, level,
                                                                   course_levels[level][Types.CAPACITY])

                modules = timetable_data[Types.MODULES]
                do_for_all = False, False

                if len(modules) > 0:
                    existing_modules = [module.name.lower().strip() for module in self.builder.module_get_all()]

                    for m in modules:
                        name = modules[m][Types.NAME]
                        if name.lower().strip() in existing_modules:

                            if not do_for_all[1]:
                                confirmation = Confirmation.confirm(self, "Already exists",
                                                                    f"A module with this name ({name}) already "
                                                                    f"exists. Do you want to import it anyway?")
                                if confirmation[1]:
                                    do_for_all = confirmation
                            else:
                                confirmation = do_for_all

                            if confirmation[0]:
                                courses = modules[m][Types.COURSES]

                                lecturer_name = timetable_data[Types.LECTURERS][modules[m][Types.LECTURER]][Types.NAME]
                                lecturer_exists = self.builder.lecturer_get_by_name(lecturer_name)
                                lecturer = lecturer_exists if lecturer_exists else "unavailable"

                                venues_list = []
                                venues = modules[m][Types.VENUES]

                                for v in venues:
                                    v_name = timetable_data[Types.VENUES][v][Types.NAME]
                                    if self.builder.venue_exists(v_name):
                                        venues_list.append(self.builder.venue_get_by_name(v_name))

                                courses_list = {}
                                for c in courses:
                                    c_name = timetable_data[Types.COURSES][c][Types.NAME]
                                    if self.builder.course_exists(c_name):
                                        courses_list[self.builder.course_get_by_name(c_name)] = courses[c]

                                self.builder.add_module(name, modules[m][Types.CODE], lecturer, courses_list,
                                                        venues_list, modules[m][Types.TIME_SLOTS],
                                                        modules[m][Types.SLOTS_PER_DAY], modules[m][Types.DURATION],
                                                        modules[m][Types.FIXED_SESSIONS])

                        else:
                            lecturer_name = timetable_data[Types.LECTURERS][modules[m][Types.LECTURER]][Types.NAME]
                            lecturer_exists = self.builder.lecturer_get_by_name(lecturer_name)
                            lecturer = lecturer_exists if lecturer_exists else "unavailable"

                            venues_list = []
                            venues = modules[m][Types.VENUES]

                            for v in venues:
                                v_name = timetable_data[Types.VENUES][v][Types.NAME]
                                if self.builder.venue_exists(v_name):
                                    venues_list.append(self.builder.venue_get_by_name(v_name))

                            courses = modules[m][Types.COURSES]
                            courses_list = {}
                            for c in courses:
                                c_name = timetable_data[Types.COURSES][c][Types.NAME]
                                if self.builder.course_exists(c_name):
                                    courses_list[self.builder.course_get_by_name(c_name)] = courses[c]

                            self.builder.add_module(name, modules[m][Types.CODE], lecturer, courses_list,
                                                    venues_list, modules[m][Types.TIME_SLOTS],
                                                    modules[m][Types.SLOTS_PER_DAY], modules[m][Types.DURATION],
                                                    modules[m][Types.FIXED_SESSIONS])

                self.modules_populate()
                self.lecturers_populate()
                self.modules_populate()
                self.courses_populate()
                self.venues_populate()
                MessageBox(self).information("Success", "Timetable projects merged successfully.")
        except Exception as e:
            logger.critical(str(e))
            MessageBox(self).information("Error", f"An error occurred while trying to merge")
        loading_dialog.close()


def close_project():
    proceed = True
    if not app_window.builder.is_saved():
        proceed = ExitConfirm.confirm(app_window)

    if proceed:
        loading_dialog = LoadingDialog(app_window)
        loading_dialog.show()
        app.processEvents()
        try:
            app_window.close()
            app_window.clear()
            loading_dialog.close()
            startup.populate_recent()
            startup.show()
        except Exception as e:
            logger.critical(str(e))


if __name__ == "__main__":
    app = QApplication()

    settings = Settings()
    startup = StartUpWindow()
    app_window = AppWindow()
    startup.show()

    app.setWindowIcon(QIcon("icon.ico"))
    sys.exit(app.exec())
