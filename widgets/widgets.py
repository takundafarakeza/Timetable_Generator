from PySide6.QtWidgets import (QFrame, QPushButton, QLabel,
                               QHBoxLayout, QWidget, QDialog,
                               QTableWidget, QVBoxLayout)
from PySide6.QtGui import QIcon, QPixmap, QCursor, QFont, QColor, QPainter
from PySide6.QtCore import QSize, Qt, QRect, QTimer
from utils import Utils
from functools import partial
from .custom_widgets import ButtonFrameSilent
from ui import ui_message_box
import os.path
import math

def_path = os.path.join(Utils.get_timetables_path(), "timetable.tbl")


class RecentItem(ButtonFrameSilent):

    def __init__(self, parent=None, name="Timetables",
                 path=def_path, callback=None):
        super().__init__(parent)
        path = path.replace(Utils.get_appdata_path(), "")
        path = path.replace(r"C:/Users/TAKUNDA/AppData/Roaming\Timetable_Generator", "")
        path = path.replace(r"C:/Users/TAKUNDA/AppData/Roaming/Timetable_Generator", "")
        self.setObjectName(u"recent_item")
        self.setMinimumSize(QSize(0, 50))
        self.setMaximumSize(QSize(16777215, 50))
        self.setStyleSheet(u"QFrame {\n"
                           "border-bottom: 1px solid #e3e4e6;\n"
                           "}\n"
                           "\n"
                           "QLabel, QPushButton{\n"
                           "	border: none;\n"
                           "}")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 0, 0)
        self.icon = QLabel(self)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(30, 30))
        self.icon.setTextFormat(Qt.TextFormat.AutoText)
        self.icon.setPixmap(QPixmap(u":/icons/images/icon.png"))
        self.icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.file_name = QLabel(name, parent=self.widget)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(10, 5, 531, 20))
        self.path = QLabel(f"~{path}", parent=self.widget)
        self.path.setObjectName(u"path")
        self.path.setStyleSheet(u"color: #818181;")
        self.path.setGeometry(QRect(10, 25, 531, 20))

        self.horizontalLayout.addWidget(self.widget)

        self.delete_btn = QPushButton(self)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(30, 30))
        self.delete_btn.setMaximumSize(QSize(30, 30))
        delete_func = partial(callback, name, "del")
        self.delete_btn.clicked.connect(delete_func)
        open_func = partial(callback, name, "open")
        self.clicked.connect(open_func)
        icon = QIcon()
        icon.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon)
        self.horizontalLayout.addWidget(self.delete_btn)


class IOSWhiteSpinner(QWidget):
    def __init__(self, w_size=100, dot_size=10, speed=80, parent=None):
        super().__init__(parent)
        self.w_size = w_size
        self.dot_size = dot_size
        self.speed = speed

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(self.speed)

        self.angle_index = 0
        self.setFixedSize(w_size + 10, w_size + 10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        center = self.rect().center()

        num_dots = 12
        radius = (self.w_size - self.dot_size) / 2

        for i in range(num_dots):
            fade = (i - self.angle_index) % num_dots
            alpha = int(40 + (215 * (num_dots - fade) / num_dots))

            color = QColor(255, 255, 255)  # white
            color.setAlpha(alpha)

            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)

            angle = (360 / num_dots) * i
            rad = math.radians(angle)

            x = center.x() + radius * math.cos(rad) - self.dot_size / 2
            y = center.y() + radius * math.sin(rad) - self.dot_size / 2

            painter.drawEllipse(int(x), int(y), self.dot_size, self.dot_size)

        self.angle_index = (self.angle_index + 1) % num_dots


class LoadingDialog(QDialog):
    def __init__(self, parent=None, text: str = "Please wait for a moment!"):
        super().__init__(parent)

        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setMinimumWidth(350)
        self.setMinimumHeight(100)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(u"color: #ffffff; background: transparent;")

        dialog_layout = QHBoxLayout(self)
        dialog_layout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget()
        self.widget.setObjectName(u"loading_dialog_container")
        self.widget.setStyleSheet(u"QWidget#loading_dialog_container {"
                                  u"background: #313131; "
                                  u"border-radius: 10px; "
                                  u"border: 2px solid #414141;"
                                  u"}")
        dialog_layout.addWidget(self.widget)
        layout = QHBoxLayout(self.widget)
        layout.setContentsMargins(20, 20, 20, 20)

        self.spinner = IOSWhiteSpinner(w_size=50, dot_size=7, speed=70)
        self.loading_label = QLabel(text)
        self.loading_label.setMinimumWidth(220)
        font = QFont()
        font.setPointSize(9)
        self.loading_label.setFont(font)
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.spinner, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loading_label)

    def showEvent(self, event):
        self.spinner.timer.start()
        super().showEvent(event)

    def closeEvent(self, event):
        self.spinner.timer.stop()
        super().closeEvent(event)


class MessageBox(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_message_box.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.cancel_btn = self.ui.cancel_btn
        self.ok_btn = self.ui.ok_btn
        self.icon = self.ui.icon
        self.title = self.ui.title
        self.text = self.ui.text

        self.cancel_btn.clicked.connect(self.close)
        self.ok_btn.clicked.connect(self.close)

    def information(self, parent, title, text):
        self.icon.setPixmap(QPixmap(u":/icons/icons/success.svg"))
        self.setParent(parent)
        self.title.setText(title)
        self.text.setText(text)
        self.show()

    def warning(self, parent, title, text):
        self.icon.setPixmap(QPixmap(u":/icons/icons/warning.svg"))
        self.setParent(parent)
        self.title.setText(title)
        self.text.setText(text)
        self.show()

    def critical(self, parent, title, text):
        self.icon.setPixmap(QPixmap(u":/icons/icons/error.svg"))
        self.setParent(parent)
        self.title.setText(title)
        self.text.setText(text)
        self.show()


class ModulesTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 7)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Module", "Lecturer", "Courses",
                                        "Venues", "Time Slots", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 190)
        self.setColumnWidth(2, 160)
        self.setColumnWidth(3, 160)
        self.setColumnWidth(4, 100)
        self.setColumnWidth(5, 80)
        self.setColumnWidth(6, 160)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }
                            
                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }
                            
                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }
                            
                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, module_id, name, code, lecturer, courses, venues, time_slots, slots_per_day):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        module = QWidget()
        module_layout = QVBoxLayout(module)
        module_layout.setContentsMargins(0, 0, 0, 0)
        module_layout.setSpacing(3)
        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        code = QLabel(f"<font color='gray'>{code}</font>")
        module_layout.addWidget(name)
        module_layout.addWidget(code)
        self.setCellWidget(row, 1, module)

        lecturer = QLabel(f"{lecturer}")
        self.setCellWidget(row, 2, lecturer)

        courses = "\n".join(courses)
        courses = QLabel(f"{courses}")
        self.setCellWidget(row, 3, courses)

        venues = "\n".join(venues)
        venues = QLabel(f"{venues}")
        self.setCellWidget(row, 4, venues)

        time_slots = QLabel(f"Slots: {time_slots}\nDaily: {slots_per_day}")
        self.setCellWidget(row, 5, time_slots)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        module_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        module_edit_btn.setIcon(edit_icon)
        module_edit_btn.setToolTip("Edit")
        module_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        module_edit_btn.setFlat(True)
        module_edit_btn.clicked.connect(partial(self._handle_action, module_id, "edit"))

        module_add_data_btn = QPushButton()
        add_data_icon = QIcon()
        add_data_icon.addFile(u":/icons/icons/courses-add.svg")
        module_add_data_btn.setIcon(add_data_icon)
        module_add_data_btn.setToolTip("Add Courses and Venues")
        module_add_data_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        module_add_data_btn.setFlat(True)
        module_add_data_btn.clicked.connect(partial(self._handle_action, module_id, "add_data"))

        module_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        module_delete_btn.setIcon(delete_icon)
        module_delete_btn.setToolTip("Delete")
        module_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        module_delete_btn.setFlat(True)
        module_delete_btn.clicked.connect(partial(self._handle_action, module_id, "delete"))

        for btn in [module_edit_btn, module_add_data_btn, module_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 6, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)


class SubjectsTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 4)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Subject", "Primary Venue", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 410)
        self.setColumnWidth(2, 320)
        self.setColumnWidth(3, 120)

        self.setStyleSheet("""
                                    QTableWidget {
                                        border: none;
                                    }
                                    QHeaderView::section {
                                        background-color: #EBECEF;
                                        padding: 3px;
                                        border: none;
                                        font-weight: bold;
                                    }

                                    QHeaderView::section:horizontal {
                                        border-right: 1px solid #D3D4D6;
                                        border-bottom: 1px solid #D3D4D6;
                                    }

                                    QHeaderView::section:vertical {
                                        border-right: 1px solid #D3D4D6;
                                        border-bottom: 1px solid #D3D4D6;
                                    }

                                    QTableWidget::item {
                                        border-bottom: 1px solid #E3E4E6;
                                        padding: 3px;
                                    }
                                """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, subject_id, name, venue):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        self.setCellWidget(row, 1, name)

        venue = QLabel(f"{venue}")
        self.setCellWidget(row, 2, venue)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        subject_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        subject_edit_btn.setIcon(edit_icon)
        subject_edit_btn.setToolTip("Edit")
        subject_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        subject_edit_btn.setFlat(True)
        subject_edit_btn.clicked.connect(partial(self._handle_action, subject_id, "edit"))

        subject_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        subject_delete_btn.setIcon(delete_icon)
        subject_delete_btn.setToolTip("Delete")
        subject_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        subject_delete_btn.setFlat(True)
        subject_delete_btn.clicked.connect(partial(self._handle_action, subject_id, "delete"))

        for btn in [subject_edit_btn, subject_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 3, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)


class LecturersTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Name", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 740)
        self.setColumnWidth(2, 120)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }
    
                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }
    
                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }
    
                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, lecturer_id, name):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        self.setCellWidget(row, 1, name)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        subject_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        subject_edit_btn.setIcon(edit_icon)
        subject_edit_btn.setToolTip("Edit")
        subject_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        subject_edit_btn.setFlat(True)
        subject_edit_btn.clicked.connect(partial(self._handle_action, lecturer_id, "edit"))

        subject_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        subject_delete_btn.setIcon(delete_icon)
        subject_delete_btn.setToolTip("Delete")
        subject_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        subject_delete_btn.setFlat(True)
        subject_delete_btn.clicked.connect(partial(self._handle_action, lecturer_id, "delete"))

        for btn in [subject_edit_btn, subject_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 2, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)


class TeachersTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Name", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 740)
        self.setColumnWidth(2, 120)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }

                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, teacher_id, name):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        self.setCellWidget(row, 1, name)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        subject_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        subject_edit_btn.setIcon(edit_icon)
        subject_edit_btn.setToolTip("Edit")
        subject_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        subject_edit_btn.setFlat(True)
        subject_edit_btn.clicked.connect(partial(self._handle_action, teacher_id, "edit"))

        subject_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        subject_delete_btn.setIcon(delete_icon)
        subject_delete_btn.setToolTip("Delete")
        subject_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        subject_delete_btn.setFlat(True)
        subject_delete_btn.clicked.connect(partial(self._handle_action, teacher_id, "delete"))

        for btn in [subject_edit_btn, subject_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 2, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)


class CoursesTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 4)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Name", "Short Name", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 620)
        self.setColumnWidth(2, 140)
        self.setColumnWidth(3, 120)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }
    
                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }
    
                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }
    
                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, course_id, name, shortname):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        self.setCellWidget(row, 1, name)

        shortname = QLabel(f"{shortname}")
        self.setCellWidget(row, 2, shortname)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        course_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        course_edit_btn.setIcon(edit_icon)
        course_edit_btn.setToolTip("Edit")
        course_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        course_edit_btn.setFlat(True)
        course_edit_btn.clicked.connect(partial(self._handle_action, course_id, "edit"))

        course_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        course_delete_btn.setIcon(delete_icon)
        course_delete_btn.setToolTip("Delete")
        course_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        course_delete_btn.setFlat(True)
        course_delete_btn.clicked.connect(partial(self._handle_action, course_id, "delete"))

        for btn in [course_edit_btn, course_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 3, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)


class ClassesTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 5)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Name", "Primary Venue", "Subjects", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 260)
        self.setColumnWidth(2, 160)
        self.setColumnWidth(3, 280)
        self.setColumnWidth(4, 160)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }

                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, class_id, name, venue, subjects):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        self.setCellWidget(row, 1, name)

        venue = QLabel(f"{venue}")
        self.setCellWidget(row, 2, venue)

        subjects = "\n".join(subjects)
        subjects = QLabel(f"{subjects}")
        self.setCellWidget(row, 3, subjects)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        class_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        class_edit_btn.setIcon(edit_icon)
        class_edit_btn.setToolTip("Edit")
        class_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        class_edit_btn.setFlat(True)
        class_edit_btn.clicked.connect(partial(self._handle_action, class_id, "edit"))

        class_add_subjects_btn = QPushButton()
        add_subjects_icon = QIcon()
        add_subjects_icon.addFile(u":/icons/icons/courses-add.svg")
        class_add_subjects_btn.setIcon(add_subjects_icon)
        class_add_subjects_btn.setToolTip("Add Subjects")
        class_add_subjects_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        class_add_subjects_btn.setFlat(True)
        class_add_subjects_btn.clicked.connect(partial(self._handle_action, class_id, "add_subjects"))

        class_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        class_delete_btn.setIcon(delete_icon)
        class_delete_btn.setToolTip("Delete")
        class_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        class_delete_btn.setFlat(True)
        class_delete_btn.clicked.connect(partial(self._handle_action, class_id, "delete"))

        for btn in [class_edit_btn, class_add_subjects_btn, class_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 4, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)


class VenuesTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 5)
        self.colors = ["#4785cf", "#63b542", "#d3cb4a",
                       "#cb4550", "#de8a40", "#4456b0"]

        self.setHorizontalHeaderLabels(["", "Name", "Location", "Location Description", "Actions"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 15)
        self.setColumnWidth(1, 320)
        self.setColumnWidth(2, 200)
        self.setColumnWidth(3, 220)
        self.setColumnWidth(4, 120)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }

                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)

    def set_action_handler(self, handler):
        self.parent_callback = handler

    def add_item(self, class_id, name, location, location_description):
        row = self.rowCount()
        color = self.colors[Utils.scale_down(6, row) - 1]
        self.insertRow(row)
        self.setRowHeight(row, 50)

        color_container = QWidget()
        layout = QVBoxLayout(color_container)
        color_item = QWidget()
        color_item.setMaximumSize(QSize(10, 10))
        color_item.setMinimumSize(QSize(10, 10))
        color_item.setStyleSheet(f"background: {color};\n"
                                 "border-radius: 5px;\n")
        layout.addWidget(color_item)
        self.setCellWidget(row, 0, color_container)

        name = QLabel(f"<font color='#414141'><b>{name}</b></font>")
        self.setCellWidget(row, 1, name)

        location = f"Latitude: {location[0]}\nLongitude: {location[1]}"
        location = QLabel(f"{location}")
        self.setCellWidget(row, 2, location)

        location_description = QLabel(f"{location_description}")
        self.setCellWidget(row, 3, location_description)

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.setContentsMargins(0, 0, 0, 0)

        class_edit_btn = QPushButton()
        edit_icon = QIcon()
        edit_icon.addFile(u":/icons/icons/pencil.svg")
        class_edit_btn.setIcon(edit_icon)
        class_edit_btn.setToolTip("Edit")
        class_edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        class_edit_btn.setFlat(True)
        class_edit_btn.clicked.connect(partial(self._handle_action, class_id, "edit"))

        class_delete_btn = QPushButton()
        delete_icon = QIcon()
        delete_icon.addFile(u":/icons/icons/trash-2.svg")
        class_delete_btn.setIcon(delete_icon)
        class_delete_btn.setToolTip("Delete")
        class_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        class_delete_btn.setFlat(True)
        class_delete_btn.clicked.connect(partial(self._handle_action, class_id, "delete"))

        for btn in [class_edit_btn, class_delete_btn]:
            btn.setStyleSheet("padding: 2px;")
            action_layout.addWidget(btn)
        self.setCellWidget(row, 4, action_widget)

    def _handle_action(self, _id, action):
        if self.parent_callback:
            self.parent_callback(_id, action)
