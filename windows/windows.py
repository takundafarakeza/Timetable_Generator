from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox,
                               QGraphicsDropShadowEffect, QPushButton,
                               QMenu, QWidget)
from PySide6.QtGui import QGuiApplication, QColor, QIcon
from PySide6.QtCore import Qt, Signal, QSize
from ui import ui_startup, ui_boarding, ui_main_window
from utils import Types, Settings
from widgets import RecentItem
import functools


class Viewer(QWidget):
    def __init__(self, data: str = None):
        super().__init__()
        if data:
            self.view(data)

    def view(self, data: str):
        self.show()


class Main(QMainWindow):
    file_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = ui_main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        self.viewer = Viewer()

        window_width = int(screen_width * 0.85)
        window_height = int(screen_height * 0.85)
        self.ui.setupUi(self)
        self.resize(window_width, window_height)
        self.move((screen_width - window_width) // 2,
                  (screen_height - window_height) // 2)

        self.home_btn = self.ui.home_btn
        self.subjects_btn = self.ui.subjects_btn
        self.modules_btn = self.ui.modules_btn
        self.teachers_btn = self.ui.teachers_btn
        self.lecturers_btn = self.ui.lecturers_btn
        self.classes_btn = self.ui.classes_btn
        self.courses_btn = self.ui.courses_btn
        self.venues_btn = self.ui.venues_btn
        self.blocks_btn = self.ui.blocks_btn
        self.menu_btns = {
            self.home_btn: {"icons": [u":/icons/icons/home.svg", u":/icons/icons/home-white.svg"],
                            "page": 1},
            self.subjects_btn: {"icons": [u":/icons/icons/subject.svg", u":/icons/icons/subject-white.svg"],
                                "page": 3},
            self.modules_btn: {"icons": [u":/icons/icons/subject.svg", u":/icons/icons/subject-white.svg"],
                               "page": 2},
            self.blocks_btn: {"icons": [u":/icons/icons/blocks.svg", u":/icons/icons/blocks-white.svg"],
                              "page": 4},
            self.teachers_btn: {"icons": [u":/icons/icons/teacher.svg", u":/icons/icons/teacher-white.svg"],
                                "page": 6},
            self.lecturers_btn: {"icons": [u":/icons/icons/teacher.svg", u":/icons/icons/teacher-white.svg"],
                                 "page": 5},
            self.classes_btn: {"icons": [u":/icons/icons/classes.svg", u":/icons/icons/classes-white.svg"],
                               "page": 8},
            self.courses_btn: {"icons": [u":/icons/icons/classes.svg", u":/icons/icons/classes-white.svg"],
                               "page": 7},
            self.venues_btn: {"icons": [u":/icons/icons/venues.svg", u":/icons/icons/venues-white.svg"],
                              "page": 9}
        }

        self.settings_btn = self.ui.settings_btn
        self.close_project_btn = self.ui.close_project_btn

        self.close_btn = self.ui.close_btn
        self.minimize_btn = self.ui.minimize_btn
        self.maximize_btn = self.ui.maximize_btn

        self.menu_btn = self.ui.menu_btn
        self.file_btn = self.ui.file_btn
        self.tools_btn = self.ui.tools_btn
        self.view_btn = self.ui.view_btn
        self.edit_btn = self.ui.edit_btn
        self.timetable_btn = self.ui.timetable_btn
        self.save_btn = self.ui.save_btn
        self.save_indicator = self.ui.save_indicator
        self.generate_indicator = self.ui.generate_indicator
        self.current_project = self.ui.current_project

        self.close_btn.clicked.connect(self.close)
        self.minimize_btn.clicked.connect(self.showMinimized)
        self.maximize_btn.clicked.connect(self.showMaximized)

        self.edit_menu = QMenu()
        self.file_menu = QMenu()
        self.tools_menu = QMenu()

        self.view_menu = QMenu()
        self.view_menu.addAction("Fullscreen", self.showFullScreen)
        self.view_menu.addAction("Maximize", self.showMaximized)
        self.view_menu.addAction("Minimize", self.showMinimized)
        self.view_btn.setMenu(self.view_menu)

        self.timetable_menu = QMenu()

        self.setup_menu()

    """
    ======================================================
            UI Manipulation
            20/12/2025
    ======================================================
    """

    def showMaximized(self, /):
        if self.isMaximized():
            self.showNormal()
        else:
            super().showMaximized()

    def showFullScreen(self, /):
        if self.isFullScreen():
            self.showNormal()
        else:
            super().showFullScreen()

    def activate_btn(self, button_: QPushButton):
        icon = QIcon()
        icon.addFile(self.menu_btns[button_]["icons"][1],
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        button_.setIcon(icon)
        button_.setStyleSheet(
            u"background: #2F69B2;"
            "color: #F3F4F6;"
        )
        self.ui.stacked_container.setCurrentIndex(self.menu_btns[button_]["page"] - 1)
        for button__ in self.menu_btns:
            if button__ != button_:
                self.deactivate_btn(button__)

    def deactivate_btn(self, button_: QPushButton):
        icon = QIcon()
        icon.addFile(self.menu_btns[button_]["icons"][0],
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        button_.setIcon(icon)
        button_.setStyleSheet(
            u"background: #transparent;"
            "color: #414141;"
        )

    def toggle_menu(self):
        menu = self.ui.menu_container
        menu.setMinimumWidth(170 if menu.minimumWidth() == 42 else 42)

    def show_hide_menu_buttons(self, buttons: list):
        for button in self.menu_btns:
            if button not in buttons:
                button.show()
            else:
                button.hide()

    def setup_menu(self):
        for button in self.menu_btns:
            activate_func = functools.partial(self.activate_btn, button)
            button.clicked.connect(activate_func)
        self.menu_btn.clicked.connect(self.toggle_menu)

    def build_menu(self, institution_type: str):
        self.edit_menu.clear()
        self.timetable_menu.clear()
        self.file_menu.clear()
        self.tools_menu.clear()

        self.edit_menu.addAction("Add Venue")

        if institution_type == Types.INSTITUTION_PRIMARY:
            buttons = [self.teachers_btn, self.lecturers_btn,
                       self.modules_btn, self.courses_btn,
                       self.blocks_btn]
            self.show_hide_menu_buttons(buttons)

        elif institution_type == Types.INSTITUTION_SECONDARY:
            buttons = [self.lecturers_btn, self.modules_btn,
                       self.courses_btn]
            self.show_hide_menu_buttons(buttons)

        elif institution_type == Types.INSTITUTION_COLLEGE:
            buttons = [self.teachers_btn, self.subjects_btn,
                       self.classes_btn, self.blocks_btn]
            self.show_hide_menu_buttons(buttons)

    def set_saved(self, status: bool):
        self.save_indicator.setVisible(not status)

    def set_generated(self, status: bool):
        self.generate_indicator.setVisible(not status)

    """
    ======================================================
            Operations
            20/12/2025
    ======================================================
    """

    # def populate_projects(self):
    #     self.projects_list.clear()
    #     icon = QIcon()
    #     icon.addFile(u":/icons/icons/classes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    #     projects = Utils().get_projects()
    #     for project in projects:
    #         self.projects_list.addItem(icon, project)


class Boarding(QMainWindow):
    create = Signal(tuple)

    def __init__(self):
        super().__init__()
        self.ui = ui_boarding.Ui_Boarding()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.institution = None

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.main_container.setGraphicsEffect(shadow)

        self.primary_school_btn = self.ui.primary_btn
        self.secondary_school_btn = self.ui.secondary_btn
        self.tertiary_school_btn = self.ui.tertiary_btn
        self.group = [self.primary_school_btn, self.secondary_school_btn,
                      self.tertiary_school_btn]
        self.ticks = [self.ui.tick_3, self.ui.tick_2, self.ui.tick]

        self.next_btn = self.ui.next_btn
        self.back_btn = self.ui.back_btn
        self.create_btn = self.ui.create_btn
        self.close_btn = self.ui.close_btn

        self.institution_name = self.ui.intitution_name_txt
        self.project_name = self.ui.timetable_name_txt
        self.daily_slots = self.ui.slots_per_day_txt
        self.days_per_cycle = self.ui.slots_per_cycle_txt
        self.slot_length = self.ui.slot_length_txt

        self.primary_school_btn.clicked.connect(self.mark_selection)
        self.secondary_school_btn.clicked.connect(self.mark_selection)
        self.tertiary_school_btn.clicked.connect(self.mark_selection)
        self.close_btn.clicked.connect(self.close)
        self.next_btn.clicked.connect(self.set_next)
        self.back_btn.clicked.connect(self.set_back)
        self.create_btn.clicked.connect(self.get_data)

        self.highlight(-1)

    def highlight(self, index):
        for tick in self.ticks:
            tick.hide()

        if index != -1:
            for button in self.group:
                button.setStyleSheet(f"QFrame#{button.objectName()}" + "{background: #F3F4F6;"
                                                                       "border: 1px solid #E3E4E6;"
                                                                       "border-radius: 10px;}")
            button = self.group[index]
            button.setStyleSheet(f"QFrame#{button.objectName()}" + "{background: #DBEAFE;"
                                                                   "border: 1px solid #E3E4E6;"
                                                                   "border-radius: 10px;}")
            self.ticks[index].show()

    def mark_selection(self, button: str):
        if button == "primary_btn":
            self.highlight(0)
            self.set_primary()
        if button == "secondary_btn":
            self.highlight(1)
            self.set_secondary()
        if button == "tertiary_btn":
            self.highlight(2)
            self.set_tertiary()

    def set_primary(self):
        self.institution = Types.INSTITUTION_PRIMARY

    def set_secondary(self):
        self.institution = Types.INSTITUTION_SECONDARY

    def set_tertiary(self):
        self.institution = Types.INSTITUTION_COLLEGE

    def set_next(self):
        if self.institution is not None:
            self.ui.container.setCurrentIndex(1)

    def set_back(self):
        self.ui.container.setCurrentIndex(0)

    def get_data(self):
        data = (
            self.institution, self.institution_name.text(),
            self.project_name.text(), int(self.daily_slots.text()),
            int(self.days_per_cycle.text()), int(self.slot_length.text())
        )
        institution, name, time_table_name, slots_per_day, days_per_cycle, slot_length = data

        if (institution and name and time_table_name and slots_per_day > 0
                and days_per_cycle > 0 and slot_length > 0):
            self.clear()
            self.create.emit(data)
        else:
            QMessageBox.warning(self, "Warning", "Please fill in all the fields.")

    def clear(self):
        self.institution = None
        self.institution_name.clear()
        self.project_name.clear()
        self.days_per_cycle.setValue(0)
        self.daily_slots.setValue(0)
        self.slot_length.setValue(0)


class StartUp(QMainWindow):
    project_open = Signal(str, str)
    project_create = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.ui = ui_startup.Ui_StartUp()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.boarding = Boarding()
        self.central_cnt = self.ui.central_container

        self.prefs_btn = self.ui.prefs_btn
        self.web_btn = self.ui.online_btn
        self.close_btn = self.ui.close_btn
        self.minimize_btn = self.ui.minimize_btn
        self.quit_btn = self.ui.quit_btn

        self.search_txt = self.ui.projects_search_txt
        self.projects_table = self.ui.recent_layout
        self.create_project_btn = self.ui.create_new_project_btn
        self.open_project_btn = self.ui.open_project_btn
        self.import_project_btn = self.ui.import_project_btn
        self.recent_refresh_btn = self.ui.recent_projects_refresh_btn
        self.recent_clear_btn = self.ui.recents_clear_btn

        self.close_btn.clicked.connect(self.close)
        self.quit_btn.clicked.connect(self.close)
        self.minimize_btn.clicked.connect(self.showMinimized)
        self.prefs_btn.clicked.connect(self.show_prefs)
        self.web_btn.clicked.connect(self.visit_web)
        self.search_txt.textChanged.connect(self.search_recent)
        self.create_project_btn.clicked.connect(self.boarding.show)
        self.import_project_btn.clicked.connect(self.import_project)
        self.recent_refresh_btn.clicked.connect(self.populate_recent)
        self.recent_clear_btn.clicked.connect(self.recent_clear)

        self.populate_recent()

    def show_prefs(self):
        pass

    def visit_web(self):
        pass

    def populate_recent(self):
        self.clear_recent_layout()
        recent = Settings().get_recent_files()

        if not len(recent) > 0:
            self.ui.recent_status_txt.show()
        else:
            self.ui.recent_status_txt.hide()
            for name, path in recent:
                self.show_recent(name, path)

    def manage_recent(self, name: str, action: str):
        ...

    def clear_recent_layout(self):
        for i in range(self.projects_table.count() - 1):
            w = self.projects_table.takeAt(1).widget()
            w.setParent(None)

    def show_recent(self, name: str, path: str):
        self.projects_table.addWidget(RecentItem(
            self.ui.recents_container, name, path, callback=self.manage_recent
        ))

    def search_recent(self):
        recent = []
        search_text = self.search_txt.text()
        self.clear_recent_layout()

        if len(recent) == 0:
            self.projects_table.hide()
            self.ui.recent_status_txt.show()
        else:

            if search_text:
                pass
            else:
                self.projects_table.show()
                self.ui.recent_status_txt.hide()

                for name, path in recent:
                    self.show_recent(name, path)

    def recent_clear(self):
        Settings().clear_recent()
        self.populate_recent()

    def import_project(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select the tbl project file", "",
                                              "Timetable (*tbl)")
        if file:
            self.project_open.emit(file)
