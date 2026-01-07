# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowoGwhCl.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

from widgets.custom_widgets import (ButtonFrame, SearchableComboBox)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setStyleSheet(u"* {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #414141;\n"
"}\n"
"\n"
"QPushButton#close_btn{\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#minimize_btn{\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#close_btn:hover{\n"
"	background: #D62626;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 1px solid #D3D4D6;\n"
"	background: #FBFCFE;\n"
"	padding-left:5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QWidget#main_container{\n"
"	background: #EBECEF;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #B1B1B1;\n"
"}\n"
"\n"
"QWidget#menu_container{\n"
"	background: #EBECEF;\n"
"	border-right: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QFrame#footer{\n"
"	background: #EBECEF;\n"
"	border-top: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QWidget#container{\n"
"	background: #F3F4F6;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QWidget#toolbar{\n"
"	border-bottom: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-"
                        "left: 5px;\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QPushButton#current_project {\n"
"	border: 1px solid #D3D4D6;\n"
"	background: #F3F4F6;\n"
"	padding-left:5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#search_container {\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#recent_status_txt{\n"
"	color: #818181;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #DBEAFE;\n"
"}\n"
"\n"
"QToolTip{\n"
"	background: #F3F4F6;\n"
"	border: 1px solid #E3E4E6;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #EBECEF;\n"
"	height: 8px;\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background: #B1B1B1;\n"
"	min-width: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"	background-color: #EBECEF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: #EBECEF;\n"
"	width: 8px"
                        ";\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background: #B1B1B1;\n"
"	min-height: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"	background-color: #EBECEF;\n"
"}\n"
"\n"
"QToolButton::menu-indicator{\n"
"	image: none;\n"
"	width: 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(':/icons/icons/drop_down.svg');\n"
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QSpinBox:down-button{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QSpinBox:up-button{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QSpinBox:down-arrow{\n"
"	image: url(':/icons/icons/drop_down.svg');\n"
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QSpinBox:up-arrow{\n"
"	image: url(':/icons/icons/drop_up.svg');\n"
"	height: "
                        "24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"                            QTableWidget {\n"
"                                border: none;\n"
"                            }\n"
"                            QHeaderView::section {\n"
"                                background-color: #EBECEF;\n"
"                                padding: 3px;\n"
"                                border: none;\n"
"                                font-weight: bold;\n"
"                            }\n"
"                            \n"
"                            QHeaderView::section:horizontal {\n"
"                                border-right: 1px solid #D3D4D6;\n"
"                                border-bottom: 1px solid #D3D4D6;\n"
"                            }\n"
"                            \n"
"                            QHeaderView::section:vertical {\n"
"                                border-right: 1px solid #D3D4D6;\n"
"                                border-bottom: 1px solid #D3D4D6;\n"
"                            }\n"
"      "
                        "                      \n"
"                            QTableWidget::item {\n"
"                                border-bottom: 1px solid #E3E4E6;\n"
"                                padding: 3px;\n"
"                            }")
        self.main_container = QWidget(MainWindow)
        self.main_container.setObjectName(u"main_container")
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.toolbar = QWidget(self.main_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 30))
        self.toolbar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.toolbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_icon = QPushButton(self.toolbar)
        self.window_icon.setObjectName(u"window_icon")
        self.window_icon.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.window_icon.setIcon(icon)
        self.window_icon.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.window_icon)

        self.frame_2 = QFrame(self.toolbar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.file_btn = QToolButton(self.frame_2)
        self.file_btn.setObjectName(u"file_btn")
        self.file_btn.setGeometry(QRect(40, 0, 40, 30))
        self.file_btn.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.file_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.file_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.edit_btn = QToolButton(self.frame_2)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setGeometry(QRect(80, 0, 40, 30))
        self.edit_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.edit_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.tools_btn = QToolButton(self.frame_2)
        self.tools_btn.setObjectName(u"tools_btn")
        self.tools_btn.setGeometry(QRect(160, 0, 40, 30))
        self.tools_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.tools_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.menu_btn = QPushButton(self.frame_2)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setGeometry(QRect(0, 0, 40, 30))
        self.timetable_btn = QToolButton(self.frame_2)
        self.timetable_btn.setObjectName(u"timetable_btn")
        self.timetable_btn.setGeometry(QRect(200, 0, 71, 30))
        self.timetable_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.timetable_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.view_btn = QToolButton(self.frame_2)
        self.view_btn.setObjectName(u"view_btn")
        self.view_btn.setGeometry(QRect(120, 0, 40, 30))
        self.view_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.view_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.generate_indicator = QWidget(self.frame_2)
        self.generate_indicator.setObjectName(u"generate_indicator")
        self.generate_indicator.setGeometry(QRect(260, 5, 10, 10))
        self.generate_indicator.setMaximumSize(QSize(10, 10))
        self.generate_indicator.setStyleSheet(u"QWidget#generate_indicator{\n"
"	background: #2F69B2;\n"
"	border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.toolbar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.save_btn = QPushButton(self.frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(200, 0, 30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QSize(22, 22))
        self.save_indicator = QWidget(self.frame)
        self.save_indicator.setObjectName(u"save_indicator")
        self.save_indicator.setGeometry(QRect(220, 3, 10, 10))
        self.save_indicator.setStyleSheet(u"QWidget#save_indicator{\n"
"	background: #DC2626;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.current_project = QPushButton(self.frame)
        self.current_project.setObjectName(u"current_project")
        self.current_project.setGeometry(QRect(250, 3, 281, 24))
        self.current_project.setStyleSheet(u"text-align: left;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/classes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.current_project.setIcon(icon2)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.toolbar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(120, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(80, 0, 40, 30))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(10, 10))
        self.minimize_btn = QPushButton(self.frame_3)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(0, 0, 40, 30))
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.minimize_btn.setIcon(icon4)
        self.maximize_btn = QPushButton(self.frame_3)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setGeometry(QRect(40, 0, 40, 30))
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.maximize_btn.setIcon(icon5)
        self.maximize_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.toolbar)

        self.container = QWidget(self.main_container)
        self.container.setObjectName(u"container")
        self.horizontalLayout_2 = QHBoxLayout(self.container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_container = QFrame(self.container)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setMinimumSize(QSize(42, 0))
        self.menu_container.setMaximumSize(QSize(42, 16777215))
        self.menu_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_container)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 30, 0, 0)
        self.middle = QFrame(self.menu_container)
        self.middle.setObjectName(u"middle")
        self.middle.setMinimumSize(QSize(160, 0))
        self.middle.setMaximumSize(QSize(160, 16777215))
        self.middle.setStyleSheet(u"QFrame#middle{\n"
"	border: 2px solid #E3E4E6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#middle QPushButton{\n"
"	border-bottom: 2px solid #E3E4E6;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.middle)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.middle)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 40))
        self.home_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_btn.setStyleSheet(u"background: #2F69B2;\n"
"color: #F3F4F6;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/home-white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn.setIcon(icon6)
        self.home_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.home_btn)

        self.modules_btn = QPushButton(self.middle)
        self.modules_btn.setObjectName(u"modules_btn")
        self.modules_btn.setMinimumSize(QSize(0, 40))
        self.modules_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.modules_btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/subject.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modules_btn.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.modules_btn)

        self.subjects_btn = QPushButton(self.middle)
        self.subjects_btn.setObjectName(u"subjects_btn")
        self.subjects_btn.setMinimumSize(QSize(0, 40))
        self.subjects_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.subjects_btn.setStyleSheet(u"")
        self.subjects_btn.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.subjects_btn)

        self.blocks_btn = QPushButton(self.middle)
        self.blocks_btn.setObjectName(u"blocks_btn")
        self.blocks_btn.setMinimumSize(QSize(0, 40))
        self.blocks_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.blocks_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/blocks.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.blocks_btn.setIcon(icon8)
        self.blocks_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.blocks_btn)

        self.lecturers_btn = QPushButton(self.middle)
        self.lecturers_btn.setObjectName(u"lecturers_btn")
        self.lecturers_btn.setMinimumSize(QSize(0, 40))
        self.lecturers_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lecturers_btn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/teacher.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lecturers_btn.setIcon(icon9)
        self.lecturers_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.lecturers_btn)

        self.teachers_btn = QPushButton(self.middle)
        self.teachers_btn.setObjectName(u"teachers_btn")
        self.teachers_btn.setMinimumSize(QSize(0, 40))
        self.teachers_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teachers_btn.setStyleSheet(u"")
        self.teachers_btn.setIcon(icon9)
        self.teachers_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.teachers_btn)

        self.courses_btn = QPushButton(self.middle)
        self.courses_btn.setObjectName(u"courses_btn")
        self.courses_btn.setMinimumSize(QSize(0, 40))
        self.courses_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.courses_btn.setStyleSheet(u"")
        self.courses_btn.setIcon(icon2)
        self.courses_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.courses_btn)

        self.classes_btn = QPushButton(self.middle)
        self.classes_btn.setObjectName(u"classes_btn")
        self.classes_btn.setMinimumSize(QSize(0, 40))
        self.classes_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.classes_btn.setStyleSheet(u"")
        self.classes_btn.setIcon(icon2)
        self.classes_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.classes_btn)

        self.venues_btn = QPushButton(self.middle)
        self.venues_btn.setObjectName(u"venues_btn")
        self.venues_btn.setMinimumSize(QSize(0, 40))
        self.venues_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.venues_btn.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/venues.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.venues_btn.setIcon(icon10)
        self.venues_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.venues_btn)


        self.verticalLayout_3.addWidget(self.middle, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.bottom = QFrame(self.menu_container)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(160, 80))
        self.bottom.setMaximumSize(QSize(160, 80))
        self.bottom.setStyleSheet(u"QFrame#bottom{\n"
"	border: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QFrame#bottom QPushButton{\n"
"	border-bottom: 2px solid #E3E4E6;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottom)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settings_btn = QPushButton(self.bottom)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 40))
        self.settings_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_btn.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon11)

        self.verticalLayout_4.addWidget(self.settings_btn)

        self.close_project_btn = QPushButton(self.bottom)
        self.close_project_btn.setObjectName(u"close_project_btn")
        self.close_project_btn.setMinimumSize(QSize(0, 40))
        self.close_project_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_project_btn.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_project_btn.setIcon(icon12)

        self.verticalLayout_4.addWidget(self.close_project_btn)


        self.verticalLayout_3.addWidget(self.bottom)


        self.horizontalLayout_2.addWidget(self.menu_container)

        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked_container = QStackedWidget(self.widget)
        self.stacked_container.setObjectName(u"stacked_container")
        self.home_window = QWidget()
        self.home_window.setObjectName(u"home_window")
        self.verticalLayout_27 = QVBoxLayout(self.home_window)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, -1, -1, 0)
        self.container_9 = QWidget(self.home_window)
        self.container_9.setObjectName(u"container_9")
        self.verticalLayout_28 = QVBoxLayout(self.container_9)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.container_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_28.addWidget(self.frame_4)

        self.middle_container = QFrame(self.container_9)
        self.middle_container.setObjectName(u"middle_container")
        self.middle_container.setMinimumSize(QSize(900, 470))
        self.middle_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.middle_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.middle_container)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.middle_container)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_8)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_5)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(280, 16777215))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_10)
        self.verticalLayout_34.setSpacing(20)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.venues_card = ButtonFrame(self.frame_10)
        self.venues_card.setObjectName(u"venues_card")
        self.venues_card.setMinimumSize(QSize(280, 50))
        self.venues_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.venues_card.setStyleSheet(u"QFrame#primary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#primary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_8 = QLabel(self.venues_card)
        self.head_8.setObjectName(u"head_8")
        self.head_8.setGeometry(QRect(60, 5, 151, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.head_8.setFont(font1)
        self.venues_count = QLabel(self.venues_card)
        self.venues_count.setObjectName(u"venues_count")
        self.venues_count.setGeometry(QRect(60, 30, 171, 21))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        self.venues_count.setFont(font2)
        self.venues_count.setStyleSheet(u"color: #818181;")
        self.venues_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_8 = QLabel(self.venues_card)
        self.coner_shadow_8.setObjectName(u"coner_shadow_8")
        self.coner_shadow_8.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_8.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_8.setScaledContents(True)
        self.icon_8 = QPushButton(self.venues_card)
        self.icon_8.setObjectName(u"icon_8")
        self.icon_8.setGeometry(QRect(10, 15, 31, 24))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/primary.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_8.setIcon(icon13)
        self.icon_8.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.venues_card)

        self.subjects_card = ButtonFrame(self.frame_10)
        self.subjects_card.setObjectName(u"subjects_card")
        self.subjects_card.setMinimumSize(QSize(280, 50))
        self.subjects_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.subjects_card.setStyleSheet(u"QFrame#secondary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#secondary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_9 = QLabel(self.subjects_card)
        self.head_9.setObjectName(u"head_9")
        self.head_9.setGeometry(QRect(60, 5, 161, 21))
        self.head_9.setFont(font1)
        self.subjects_count = QLabel(self.subjects_card)
        self.subjects_count.setObjectName(u"subjects_count")
        self.subjects_count.setGeometry(QRect(60, 30, 171, 21))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.subjects_count.setFont(font3)
        self.subjects_count.setStyleSheet(u"color: #818181;")
        self.subjects_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_9 = QLabel(self.subjects_card)
        self.coner_shadow_9.setObjectName(u"coner_shadow_9")
        self.coner_shadow_9.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_9.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_9.setScaledContents(True)
        self.icon_9 = QPushButton(self.subjects_card)
        self.icon_9.setObjectName(u"icon_9")
        self.icon_9.setGeometry(QRect(10, 15, 31, 24))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/secondary.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_9.setIcon(icon14)
        self.icon_9.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.subjects_card)

        self.modules_card = ButtonFrame(self.frame_10)
        self.modules_card.setObjectName(u"modules_card")
        self.modules_card.setMinimumSize(QSize(280, 50))
        self.modules_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.modules_card.setStyleSheet(u"QFrame#secondary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#secondary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_13 = QLabel(self.modules_card)
        self.head_13.setObjectName(u"head_13")
        self.head_13.setGeometry(QRect(60, 5, 161, 21))
        self.head_13.setFont(font1)
        self.modules_count = QLabel(self.modules_card)
        self.modules_count.setObjectName(u"modules_count")
        self.modules_count.setGeometry(QRect(60, 30, 171, 21))
        self.modules_count.setFont(font3)
        self.modules_count.setStyleSheet(u"color: #818181;")
        self.modules_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_13 = QLabel(self.modules_card)
        self.coner_shadow_13.setObjectName(u"coner_shadow_13")
        self.coner_shadow_13.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_13.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_13.setScaledContents(True)
        self.icon_13 = QPushButton(self.modules_card)
        self.icon_13.setObjectName(u"icon_13")
        self.icon_13.setGeometry(QRect(10, 15, 31, 24))
        self.icon_13.setIcon(icon14)
        self.icon_13.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.modules_card)

        self.courses_card = ButtonFrame(self.frame_10)
        self.courses_card.setObjectName(u"courses_card")
        self.courses_card.setMinimumSize(QSize(280, 50))
        self.courses_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.courses_card.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_7 = QLabel(self.courses_card)
        self.head_7.setObjectName(u"head_7")
        self.head_7.setGeometry(QRect(60, 5, 161, 21))
        self.head_7.setFont(font1)
        self.courses_count = QLabel(self.courses_card)
        self.courses_count.setObjectName(u"courses_count")
        self.courses_count.setGeometry(QRect(60, 30, 181, 21))
        self.courses_count.setFont(font2)
        self.courses_count.setStyleSheet(u"color: #818181;")
        self.courses_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_7 = QLabel(self.courses_card)
        self.coner_shadow_7.setObjectName(u"coner_shadow_7")
        self.coner_shadow_7.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_7.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_7.setScaledContents(True)
        self.icon_7 = QPushButton(self.courses_card)
        self.icon_7.setObjectName(u"icon_7")
        self.icon_7.setGeometry(QRect(10, 15, 31, 24))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/tertiary.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_7.setIcon(icon15)
        self.icon_7.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.courses_card)

        self.classes_card = ButtonFrame(self.frame_10)
        self.classes_card.setObjectName(u"classes_card")
        self.classes_card.setMinimumSize(QSize(280, 50))
        self.classes_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.classes_card.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_15 = QLabel(self.classes_card)
        self.head_15.setObjectName(u"head_15")
        self.head_15.setGeometry(QRect(60, 5, 161, 21))
        self.head_15.setFont(font1)
        self.classes_count = QLabel(self.classes_card)
        self.classes_count.setObjectName(u"classes_count")
        self.classes_count.setGeometry(QRect(60, 30, 181, 21))
        self.classes_count.setFont(font2)
        self.classes_count.setStyleSheet(u"color: #818181;")
        self.classes_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_15 = QLabel(self.classes_card)
        self.coner_shadow_15.setObjectName(u"coner_shadow_15")
        self.coner_shadow_15.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_15.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_15.setScaledContents(True)
        self.icon_15 = QPushButton(self.classes_card)
        self.icon_15.setObjectName(u"icon_15")
        self.icon_15.setGeometry(QRect(10, 15, 31, 24))
        self.icon_15.setIcon(icon15)
        self.icon_15.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.classes_card)

        self.lecturers_card = ButtonFrame(self.frame_10)
        self.lecturers_card.setObjectName(u"lecturers_card")
        self.lecturers_card.setMinimumSize(QSize(280, 50))
        self.lecturers_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lecturers_card.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_11 = QLabel(self.lecturers_card)
        self.head_11.setObjectName(u"head_11")
        self.head_11.setGeometry(QRect(60, 5, 161, 21))
        self.head_11.setFont(font1)
        self.lecturers_count = QLabel(self.lecturers_card)
        self.lecturers_count.setObjectName(u"lecturers_count")
        self.lecturers_count.setGeometry(QRect(60, 30, 181, 21))
        self.lecturers_count.setFont(font2)
        self.lecturers_count.setStyleSheet(u"color: #818181;")
        self.lecturers_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_11 = QLabel(self.lecturers_card)
        self.coner_shadow_11.setObjectName(u"coner_shadow_11")
        self.coner_shadow_11.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_11.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_11.setScaledContents(True)
        self.icon_11 = QPushButton(self.lecturers_card)
        self.icon_11.setObjectName(u"icon_11")
        self.icon_11.setGeometry(QRect(10, 15, 35, 24))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/lecturer.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_11.setIcon(icon16)
        self.icon_11.setIconSize(QSize(32, 32))
        self.tertiary_btn_5 = ButtonFrame(self.lecturers_card)
        self.tertiary_btn_5.setObjectName(u"tertiary_btn_5")
        self.tertiary_btn_5.setGeometry(QRect(90, 50, 281, 51))
        self.tertiary_btn_5.setMinimumSize(QSize(280, 50))
        self.tertiary_btn_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tertiary_btn_5.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_17 = QLabel(self.tertiary_btn_5)
        self.head_17.setObjectName(u"head_17")
        self.head_17.setGeometry(QRect(60, 5, 161, 21))
        self.head_17.setFont(font1)
        self.sub_head_17 = QLabel(self.tertiary_btn_5)
        self.sub_head_17.setObjectName(u"sub_head_17")
        self.sub_head_17.setGeometry(QRect(60, 30, 181, 21))
        self.sub_head_17.setFont(font2)
        self.sub_head_17.setStyleSheet(u"color: #818181;")
        self.sub_head_17.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_17 = QLabel(self.tertiary_btn_5)
        self.coner_shadow_17.setObjectName(u"coner_shadow_17")
        self.coner_shadow_17.setGeometry(QRect(80, 0, 201, 61))
        self.coner_shadow_17.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_17.setScaledContents(True)
        self.icon_17 = QPushButton(self.tertiary_btn_5)
        self.icon_17.setObjectName(u"icon_17")
        self.icon_17.setGeometry(QRect(10, 15, 35, 24))
        self.icon_17.setIcon(icon16)
        self.icon_17.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.lecturers_card)

        self.teachers_card = ButtonFrame(self.frame_10)
        self.teachers_card.setObjectName(u"teachers_card")
        self.teachers_card.setMinimumSize(QSize(280, 50))
        self.teachers_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teachers_card.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_18 = QLabel(self.teachers_card)
        self.head_18.setObjectName(u"head_18")
        self.head_18.setGeometry(QRect(60, 5, 161, 21))
        self.head_18.setFont(font1)
        self.teachers_count = QLabel(self.teachers_card)
        self.teachers_count.setObjectName(u"teachers_count")
        self.teachers_count.setGeometry(QRect(60, 30, 181, 21))
        self.teachers_count.setFont(font2)
        self.teachers_count.setStyleSheet(u"color: #818181;")
        self.teachers_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_18 = QLabel(self.teachers_card)
        self.coner_shadow_18.setObjectName(u"coner_shadow_18")
        self.coner_shadow_18.setGeometry(QRect(80, 0, 201, 51))
        self.coner_shadow_18.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_18.setScaledContents(True)
        self.icon_18 = QPushButton(self.teachers_card)
        self.icon_18.setObjectName(u"icon_18")
        self.icon_18.setGeometry(QRect(10, 15, 35, 24))
        self.icon_18.setIcon(icon16)
        self.icon_18.setIconSize(QSize(32, 32))
        self.tertiary_btn_7 = ButtonFrame(self.teachers_card)
        self.tertiary_btn_7.setObjectName(u"tertiary_btn_7")
        self.tertiary_btn_7.setGeometry(QRect(90, 50, 281, 51))
        self.tertiary_btn_7.setMinimumSize(QSize(280, 50))
        self.tertiary_btn_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tertiary_btn_7.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_19 = QLabel(self.tertiary_btn_7)
        self.head_19.setObjectName(u"head_19")
        self.head_19.setGeometry(QRect(60, 5, 161, 21))
        self.head_19.setFont(font1)
        self.sub_head_19 = QLabel(self.tertiary_btn_7)
        self.sub_head_19.setObjectName(u"sub_head_19")
        self.sub_head_19.setGeometry(QRect(60, 30, 181, 21))
        self.sub_head_19.setFont(font2)
        self.sub_head_19.setStyleSheet(u"color: #818181;")
        self.sub_head_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_19 = QLabel(self.tertiary_btn_7)
        self.coner_shadow_19.setObjectName(u"coner_shadow_19")
        self.coner_shadow_19.setGeometry(QRect(80, 0, 201, 61))
        self.coner_shadow_19.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_19.setScaledContents(True)
        self.icon_19 = QPushButton(self.tertiary_btn_7)
        self.icon_19.setObjectName(u"icon_19")
        self.icon_19.setGeometry(QRect(10, 15, 35, 24))
        self.icon_19.setIcon(icon16)
        self.icon_19.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.teachers_card)

        self.blocks_card = ButtonFrame(self.frame_10)
        self.blocks_card.setObjectName(u"blocks_card")
        self.blocks_card.setMinimumSize(QSize(280, 50))
        self.blocks_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.blocks_card.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_12 = QLabel(self.blocks_card)
        self.head_12.setObjectName(u"head_12")
        self.head_12.setGeometry(QRect(60, 5, 161, 21))
        self.head_12.setFont(font1)
        self.blocks_count = QLabel(self.blocks_card)
        self.blocks_count.setObjectName(u"blocks_count")
        self.blocks_count.setGeometry(QRect(60, 30, 181, 21))
        self.blocks_count.setFont(font2)
        self.blocks_count.setStyleSheet(u"color: #818181;")
        self.blocks_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_12 = QLabel(self.blocks_card)
        self.coner_shadow_12.setObjectName(u"coner_shadow_12")
        self.coner_shadow_12.setGeometry(QRect(90, 0, 191, 51))
        self.coner_shadow_12.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_12.setScaledContents(True)
        self.icon_12 = QPushButton(self.blocks_card)
        self.icon_12.setObjectName(u"icon_12")
        self.icon_12.setGeometry(QRect(10, 15, 31, 24))
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/blocks_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_12.setIcon(icon17)
        self.icon_12.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.blocks_card)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_2)


        self.verticalLayout_33.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.timetable_generate_btn = QPushButton(self.frame_9)
        self.timetable_generate_btn.setObjectName(u"timetable_generate_btn")
        self.timetable_generate_btn.setGeometry(QRect(140, 5, 121, 30))
        self.timetable_generate_btn.setStyleSheet(u"#timetable_generate_btn{padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;}")
        self.timetable_generate_btn.setIconSize(QSize(14, 14))
        self.timetable_generate_updates_btn = QPushButton(self.frame_9)
        self.timetable_generate_updates_btn.setObjectName(u"timetable_generate_updates_btn")
        self.timetable_generate_updates_btn.setGeometry(QRect(280, 5, 131, 30))
        self.timetable_generate_updates_btn.setStyleSheet(u"#timetable_generate_updates_btn{padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;}")
        self.timetable_generate_updates_btn.setIconSize(QSize(14, 14))
        self.timetable_view_btn = QPushButton(self.frame_9)
        self.timetable_view_btn.setObjectName(u"timetable_view_btn")
        self.timetable_view_btn.setGeometry(QRect(10, 5, 111, 31))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.timetable_view_btn.setFont(font4)
        self.timetable_view_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.timetable_view_btn.setStyleSheet(u"#timetable_view_btn{padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;}")

        self.verticalLayout_33.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.middle_container)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_5)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 9, 0, 9)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_2)

        self.cfg_cnt = QFrame(self.frame_5)
        self.cfg_cnt.setObjectName(u"cfg_cnt")
        self.cfg_cnt.setMaximumSize(QSize(457, 16777215))
        self.cfg_cnt.setStyleSheet(u"QFrame#cfg_cnt{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 5px;\n"
"	background: #EBECEF;\n"
"}")
        self.cfg_cnt.setFrameShape(QFrame.Shape.StyledPanel)
        self.cfg_cnt.setFrameShadow(QFrame.Shadow.Raised)
        self.cfg_days_per_cycle = QSpinBox(self.cfg_cnt)
        self.cfg_days_per_cycle.setObjectName(u"cfg_days_per_cycle")
        self.cfg_days_per_cycle.setGeometry(QRect(20, 370, 121, 30))
        self.cfg_daily_slots = QSpinBox(self.cfg_cnt)
        self.cfg_daily_slots.setObjectName(u"cfg_daily_slots")
        self.cfg_daily_slots.setGeometry(QRect(180, 370, 121, 30))
        self.label_3 = QLabel(self.cfg_cnt)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 345, 101, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_4 = QLabel(self.cfg_cnt)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 345, 101, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.slot_edit_table = QTableWidget(self.cfg_cnt)
        if (self.slot_edit_table.columnCount() < 2):
            self.slot_edit_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.slot_edit_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.slot_edit_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.slot_edit_table.setObjectName(u"slot_edit_table")
        self.slot_edit_table.setGeometry(QRect(20, 10, 201, 311))
        self.slot_edit_table.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.slot_edit_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.slot_edit_table.setShowGrid(False)
        self.slot_edit_table.horizontalHeader().setVisible(True)
        self.slot_edit_table.horizontalHeader().setDefaultSectionSize(95)
        self.slot_edit_table.verticalHeader().setVisible(False)
        self.day_edit_table = QTableWidget(self.cfg_cnt)
        if (self.day_edit_table.columnCount() < 2):
            self.day_edit_table.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.day_edit_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.day_edit_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.day_edit_table.setObjectName(u"day_edit_table")
        self.day_edit_table.setGeometry(QRect(230, 10, 201, 311))
        self.day_edit_table.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.day_edit_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.day_edit_table.setShowGrid(False)
        self.day_edit_table.horizontalHeader().setVisible(True)
        self.day_edit_table.horizontalHeader().setDefaultSectionSize(95)
        self.day_edit_table.verticalHeader().setVisible(False)
        self.add_break_btn = QPushButton(self.cfg_cnt)
        self.add_break_btn.setObjectName(u"add_break_btn")
        self.add_break_btn.setGeometry(QRect(320, 370, 101, 30))
        self.add_break_btn.setStyleSheet(u"#add_break_btn{padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_break_btn.setIcon(icon18)
        self.add_break_btn.setIconSize(QSize(14, 14))

        self.verticalLayout_32.addWidget(self.cfg_cnt)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_28.addWidget(self.middle_container, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.frame_6 = QFrame(self.container_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dash_timetable_status = QPushButton(self.frame_6)
        self.dash_timetable_status.setObjectName(u"dash_timetable_status")
        self.dash_timetable_status.setMinimumSize(QSize(400, 0))
        self.dash_timetable_status.setStyleSheet(u"text-align: left;")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dash_timetable_status.setIcon(icon19)

        self.horizontalLayout_3.addWidget(self.dash_timetable_status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(460, 0))
        self.frame_7.setMaximumSize(QSize(320, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_28.addWidget(self.frame_6)


        self.verticalLayout_27.addWidget(self.container_9)

        self.stacked_container.addWidget(self.home_window)
        self.modules_window = QWidget()
        self.modules_window.setObjectName(u"modules_window")
        self.verticalLayout_6 = QVBoxLayout(self.modules_window)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.container_2 = QWidget(self.modules_window)
        self.container_2.setObjectName(u"container_2")
        self.verticalLayout_10 = QVBoxLayout(self.container_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.title_container = QFrame(self.container_2)
        self.title_container.setObjectName(u"title_container")
        self.title_container.setMinimumSize(QSize(0, 40))
        self.title_container.setMaximumSize(QSize(16777215, 40))
        self.title_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container.setFrameShadow(QFrame.Shadow.Raised)
        self.modules_course_filter = SearchableComboBox(self.title_container)
        self.modules_course_filter.setObjectName(u"modules_course_filter")
        self.modules_course_filter.setGeometry(QRect(679, 5, 251, 30))
        self.modules_course_filter.setEditable(True)
        self.title = QLabel(self.title_container)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 251, 21))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.title.setFont(font5)

        self.verticalLayout_10.addWidget(self.title_container)

        self.modules_cnt = QFrame(self.container_2)
        self.modules_cnt.setObjectName(u"modules_cnt")
        self.modules_cnt.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.modules_cnt)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.module_header_cnt = QFrame(self.modules_cnt)
        self.module_header_cnt.setObjectName(u"module_header_cnt")
        self.module_header_cnt.setMinimumSize(QSize(0, 50))
        self.module_header_cnt.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt.setFrameShadow(QFrame.Shadow.Raised)
        self.modules_add_btn = QPushButton(self.module_header_cnt)
        self.modules_add_btn.setObjectName(u"modules_add_btn")
        self.modules_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.modules_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.modules_add_btn.setIcon(icon18)
        self.modules_add_btn.setIconSize(QSize(14, 14))
        self.modules_search = QLineEdit(self.module_header_cnt)
        self.modules_search.setObjectName(u"modules_search")
        self.modules_search.setGeometry(QRect(669, 10, 251, 30))

        self.verticalLayout_7.addWidget(self.module_header_cnt)

        self.modules_table_container = QFrame(self.modules_cnt)
        self.modules_table_container.setObjectName(u"modules_table_container")
        self.modules_table_container.setMinimumSize(QSize(920, 405))
        self.modules_table_container.setMaximumSize(QSize(920, 16777215))
        self.modules_table_container.setStyleSheet(u"QWidget#modules_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.modules_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.modules_table_layout = QVBoxLayout(self.modules_table_container)
        self.modules_table_layout.setSpacing(0)
        self.modules_table_layout.setObjectName(u"modules_table_layout")
        self.modules_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.modules_table_container)


        self.verticalLayout_10.addWidget(self.modules_cnt)


        self.verticalLayout_6.addWidget(self.container_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.modules_window)
        self.subjects_window = QWidget()
        self.subjects_window.setObjectName(u"subjects_window")
        self.verticalLayout_9 = QVBoxLayout(self.subjects_window)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.container_3 = QWidget(self.subjects_window)
        self.container_3.setObjectName(u"container_3")
        self.verticalLayout_11 = QVBoxLayout(self.container_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.title_container_2 = QFrame(self.container_3)
        self.title_container_2.setObjectName(u"title_container_2")
        self.title_container_2.setMinimumSize(QSize(0, 40))
        self.title_container_2.setMaximumSize(QSize(16777215, 40))
        self.title_container_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_2.setFrameShadow(QFrame.Shadow.Raised)
        self.subjects_class_filter = SearchableComboBox(self.title_container_2)
        self.subjects_class_filter.setObjectName(u"subjects_class_filter")
        self.subjects_class_filter.setGeometry(QRect(729, 5, 201, 30))
        self.subjects_class_filter.setEditable(True)
        self.title_2 = QLabel(self.title_container_2)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(10, 10, 251, 21))
        self.title_2.setFont(font5)

        self.verticalLayout_11.addWidget(self.title_container_2)

        self.modules_cnt_2 = QFrame(self.container_3)
        self.modules_cnt_2.setObjectName(u"modules_cnt_2")
        self.modules_cnt_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.modules_cnt_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.module_header_cnt_2 = QFrame(self.modules_cnt_2)
        self.module_header_cnt_2.setObjectName(u"module_header_cnt_2")
        self.module_header_cnt_2.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_2.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_2.setFrameShadow(QFrame.Shadow.Raised)
        self.subjects_add_btn = QPushButton(self.module_header_cnt_2)
        self.subjects_add_btn.setObjectName(u"subjects_add_btn")
        self.subjects_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.subjects_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.subjects_add_btn.setIcon(icon18)
        self.subjects_add_btn.setIconSize(QSize(14, 14))
        self.subjects_search = QLineEdit(self.module_header_cnt_2)
        self.subjects_search.setObjectName(u"subjects_search")
        self.subjects_search.setGeometry(QRect(719, 10, 201, 30))

        self.verticalLayout_8.addWidget(self.module_header_cnt_2)

        self.subjects_table_container = QFrame(self.modules_cnt_2)
        self.subjects_table_container.setObjectName(u"subjects_table_container")
        self.subjects_table_container.setMinimumSize(QSize(920, 405))
        self.subjects_table_container.setMaximumSize(QSize(910, 16777215))
        self.subjects_table_container.setStyleSheet(u"QWidget#subjects_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.subjects_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjects_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.subjects_table_layout = QVBoxLayout(self.subjects_table_container)
        self.subjects_table_layout.setSpacing(0)
        self.subjects_table_layout.setObjectName(u"subjects_table_layout")
        self.subjects_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.subjects_table_container)


        self.verticalLayout_11.addWidget(self.modules_cnt_2)


        self.verticalLayout_9.addWidget(self.container_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.subjects_window)
        self.blocks_page = QWidget()
        self.blocks_page.setObjectName(u"blocks_page")
        self.verticalLayout_31 = QVBoxLayout(self.blocks_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.container_10 = QWidget(self.blocks_page)
        self.container_10.setObjectName(u"container_10")
        self.verticalLayout_29 = QVBoxLayout(self.container_10)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.title_container_8 = QFrame(self.container_10)
        self.title_container_8.setObjectName(u"title_container_8")
        self.title_container_8.setMinimumSize(QSize(0, 40))
        self.title_container_8.setMaximumSize(QSize(16777215, 40))
        self.title_container_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_8.setFrameShadow(QFrame.Shadow.Raised)
        self.title_8 = QLabel(self.title_container_8)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setGeometry(QRect(10, 10, 251, 21))
        self.title_8.setFont(font5)

        self.verticalLayout_29.addWidget(self.title_container_8)

        self.modules_cnt_8 = QFrame(self.container_10)
        self.modules_cnt_8.setObjectName(u"modules_cnt_8")
        self.modules_cnt_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.modules_cnt_8)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.module_header_cnt_8 = QFrame(self.modules_cnt_8)
        self.module_header_cnt_8.setObjectName(u"module_header_cnt_8")
        self.module_header_cnt_8.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_8.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_8.setFrameShadow(QFrame.Shadow.Raised)
        self.blocks_add_btn = QPushButton(self.module_header_cnt_8)
        self.blocks_add_btn.setObjectName(u"blocks_add_btn")
        self.blocks_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.blocks_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.blocks_add_btn.setIcon(icon18)
        self.blocks_add_btn.setIconSize(QSize(14, 14))
        self.blocks_search = QLineEdit(self.module_header_cnt_8)
        self.blocks_search.setObjectName(u"blocks_search")
        self.blocks_search.setGeometry(QRect(719, 10, 201, 30))

        self.verticalLayout_30.addWidget(self.module_header_cnt_8)

        self.blocks_table_container = QFrame(self.modules_cnt_8)
        self.blocks_table_container.setObjectName(u"blocks_table_container")
        self.blocks_table_container.setMinimumSize(QSize(920, 405))
        self.blocks_table_container.setMaximumSize(QSize(910, 16777215))
        self.blocks_table_container.setStyleSheet(u"QWidget#blocks_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.blocks_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.blocks_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.blocks_table_layout = QVBoxLayout(self.blocks_table_container)
        self.blocks_table_layout.setSpacing(0)
        self.blocks_table_layout.setObjectName(u"blocks_table_layout")
        self.blocks_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_30.addWidget(self.blocks_table_container)


        self.verticalLayout_29.addWidget(self.modules_cnt_8)


        self.verticalLayout_31.addWidget(self.container_10, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.blocks_page)
        self.lecturers_window = QWidget()
        self.lecturers_window.setObjectName(u"lecturers_window")
        self.verticalLayout_14 = QVBoxLayout(self.lecturers_window)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.container_4 = QWidget(self.lecturers_window)
        self.container_4.setObjectName(u"container_4")
        self.verticalLayout_12 = QVBoxLayout(self.container_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.title_container_3 = QFrame(self.container_4)
        self.title_container_3.setObjectName(u"title_container_3")
        self.title_container_3.setMinimumSize(QSize(0, 40))
        self.title_container_3.setMaximumSize(QSize(16777215, 40))
        self.title_container_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_3.setFrameShadow(QFrame.Shadow.Raised)
        self.title_3 = QLabel(self.title_container_3)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 10, 251, 21))
        self.title_3.setFont(font5)

        self.verticalLayout_12.addWidget(self.title_container_3)

        self.modules_cnt_3 = QFrame(self.container_4)
        self.modules_cnt_3.setObjectName(u"modules_cnt_3")
        self.modules_cnt_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.modules_cnt_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.module_header_cnt_3 = QFrame(self.modules_cnt_3)
        self.module_header_cnt_3.setObjectName(u"module_header_cnt_3")
        self.module_header_cnt_3.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_3.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_3.setFrameShadow(QFrame.Shadow.Raised)
        self.lecturers_add_btn = QPushButton(self.module_header_cnt_3)
        self.lecturers_add_btn.setObjectName(u"lecturers_add_btn")
        self.lecturers_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.lecturers_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.lecturers_add_btn.setIcon(icon18)
        self.lecturers_add_btn.setIconSize(QSize(14, 14))
        self.lecturers_search = QLineEdit(self.module_header_cnt_3)
        self.lecturers_search.setObjectName(u"lecturers_search")
        self.lecturers_search.setGeometry(QRect(709, 10, 211, 30))

        self.verticalLayout_13.addWidget(self.module_header_cnt_3)

        self.lecturers_table_container = QFrame(self.modules_cnt_3)
        self.lecturers_table_container.setObjectName(u"lecturers_table_container")
        self.lecturers_table_container.setMinimumSize(QSize(920, 405))
        self.lecturers_table_container.setMaximumSize(QSize(920, 16777215))
        self.lecturers_table_container.setStyleSheet(u"QWidget#lecturers_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.lecturers_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.lecturers_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.lecturers_table_layout = QVBoxLayout(self.lecturers_table_container)
        self.lecturers_table_layout.setSpacing(0)
        self.lecturers_table_layout.setObjectName(u"lecturers_table_layout")
        self.lecturers_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.lecturers_table_container)


        self.verticalLayout_12.addWidget(self.modules_cnt_3)


        self.verticalLayout_14.addWidget(self.container_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.lecturers_window)
        self.teachers_window = QWidget()
        self.teachers_window.setObjectName(u"teachers_window")
        self.verticalLayout_17 = QVBoxLayout(self.teachers_window)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.container_5 = QWidget(self.teachers_window)
        self.container_5.setObjectName(u"container_5")
        self.verticalLayout_15 = QVBoxLayout(self.container_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.title_container_4 = QFrame(self.container_5)
        self.title_container_4.setObjectName(u"title_container_4")
        self.title_container_4.setMinimumSize(QSize(0, 40))
        self.title_container_4.setMaximumSize(QSize(16777215, 40))
        self.title_container_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_4.setFrameShadow(QFrame.Shadow.Raised)
        self.title_4 = QLabel(self.title_container_4)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(10, 10, 251, 21))
        self.title_4.setFont(font5)

        self.verticalLayout_15.addWidget(self.title_container_4)

        self.modules_cnt_4 = QFrame(self.container_5)
        self.modules_cnt_4.setObjectName(u"modules_cnt_4")
        self.modules_cnt_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.modules_cnt_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.module_header_cnt_4 = QFrame(self.modules_cnt_4)
        self.module_header_cnt_4.setObjectName(u"module_header_cnt_4")
        self.module_header_cnt_4.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_4.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_4.setFrameShadow(QFrame.Shadow.Raised)
        self.teachers_add_btn = QPushButton(self.module_header_cnt_4)
        self.teachers_add_btn.setObjectName(u"teachers_add_btn")
        self.teachers_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.teachers_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.teachers_add_btn.setIcon(icon18)
        self.teachers_add_btn.setIconSize(QSize(14, 14))
        self.teachers_search = QLineEdit(self.module_header_cnt_4)
        self.teachers_search.setObjectName(u"teachers_search")
        self.teachers_search.setGeometry(QRect(689, 10, 231, 30))

        self.verticalLayout_16.addWidget(self.module_header_cnt_4)

        self.teachers_table_container = QFrame(self.modules_cnt_4)
        self.teachers_table_container.setObjectName(u"teachers_table_container")
        self.teachers_table_container.setMinimumSize(QSize(920, 405))
        self.teachers_table_container.setMaximumSize(QSize(920, 16777215))
        self.teachers_table_container.setStyleSheet(u"QWidget#teachers_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.teachers_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.teachers_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.teachers_table_layout = QVBoxLayout(self.teachers_table_container)
        self.teachers_table_layout.setSpacing(0)
        self.teachers_table_layout.setObjectName(u"teachers_table_layout")
        self.teachers_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.teachers_table_container)


        self.verticalLayout_15.addWidget(self.modules_cnt_4)


        self.verticalLayout_17.addWidget(self.container_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.teachers_window)
        self.courses_window = QWidget()
        self.courses_window.setObjectName(u"courses_window")
        self.verticalLayout_23 = QVBoxLayout(self.courses_window)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.container_7 = QWidget(self.courses_window)
        self.container_7.setObjectName(u"container_7")
        self.verticalLayout_21 = QVBoxLayout(self.container_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.title_container_6 = QFrame(self.container_7)
        self.title_container_6.setObjectName(u"title_container_6")
        self.title_container_6.setMinimumSize(QSize(0, 40))
        self.title_container_6.setMaximumSize(QSize(16777215, 40))
        self.title_container_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_6.setFrameShadow(QFrame.Shadow.Raised)
        self.title_6 = QLabel(self.title_container_6)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setGeometry(QRect(10, 10, 251, 21))
        self.title_6.setFont(font5)

        self.verticalLayout_21.addWidget(self.title_container_6)

        self.modules_cnt_6 = QFrame(self.container_7)
        self.modules_cnt_6.setObjectName(u"modules_cnt_6")
        self.modules_cnt_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.modules_cnt_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.module_header_cnt_6 = QFrame(self.modules_cnt_6)
        self.module_header_cnt_6.setObjectName(u"module_header_cnt_6")
        self.module_header_cnt_6.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_6.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_6.setFrameShadow(QFrame.Shadow.Raised)
        self.courses_add_btn = QPushButton(self.module_header_cnt_6)
        self.courses_add_btn.setObjectName(u"courses_add_btn")
        self.courses_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.courses_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.courses_add_btn.setIcon(icon18)
        self.courses_add_btn.setIconSize(QSize(14, 14))
        self.courses_search = QLineEdit(self.module_header_cnt_6)
        self.courses_search.setObjectName(u"courses_search")
        self.courses_search.setGeometry(QRect(679, 10, 241, 30))

        self.verticalLayout_22.addWidget(self.module_header_cnt_6)

        self.courses_table_container = QFrame(self.modules_cnt_6)
        self.courses_table_container.setObjectName(u"courses_table_container")
        self.courses_table_container.setMinimumSize(QSize(920, 405))
        self.courses_table_container.setMaximumSize(QSize(920, 16777215))
        self.courses_table_container.setStyleSheet(u"QWidget#courses_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.courses_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.courses_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.courses_table_layout = QVBoxLayout(self.courses_table_container)
        self.courses_table_layout.setSpacing(0)
        self.courses_table_layout.setObjectName(u"courses_table_layout")
        self.courses_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.courses_table_container)


        self.verticalLayout_21.addWidget(self.modules_cnt_6)


        self.verticalLayout_23.addWidget(self.container_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.courses_window)
        self.classes_window = QWidget()
        self.classes_window.setObjectName(u"classes_window")
        self.verticalLayout_26 = QVBoxLayout(self.classes_window)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.container_8 = QWidget(self.classes_window)
        self.container_8.setObjectName(u"container_8")
        self.verticalLayout_24 = QVBoxLayout(self.container_8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.title_container_7 = QFrame(self.container_8)
        self.title_container_7.setObjectName(u"title_container_7")
        self.title_container_7.setMinimumSize(QSize(0, 40))
        self.title_container_7.setMaximumSize(QSize(16777215, 40))
        self.title_container_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_7.setFrameShadow(QFrame.Shadow.Raised)
        self.title_7 = QLabel(self.title_container_7)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setGeometry(QRect(10, 10, 251, 21))
        self.title_7.setFont(font5)

        self.verticalLayout_24.addWidget(self.title_container_7)

        self.modules_cnt_7 = QFrame(self.container_8)
        self.modules_cnt_7.setObjectName(u"modules_cnt_7")
        self.modules_cnt_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.modules_cnt_7)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.module_header_cnt_7 = QFrame(self.modules_cnt_7)
        self.module_header_cnt_7.setObjectName(u"module_header_cnt_7")
        self.module_header_cnt_7.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_7.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_7.setFrameShadow(QFrame.Shadow.Raised)
        self.classes_add_btn = QPushButton(self.module_header_cnt_7)
        self.classes_add_btn.setObjectName(u"classes_add_btn")
        self.classes_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.classes_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.classes_add_btn.setIcon(icon18)
        self.classes_add_btn.setIconSize(QSize(14, 14))
        self.classes_search = QLineEdit(self.module_header_cnt_7)
        self.classes_search.setObjectName(u"classes_search")
        self.classes_search.setGeometry(QRect(709, 10, 211, 30))

        self.verticalLayout_25.addWidget(self.module_header_cnt_7)

        self.classes_table_container = QFrame(self.modules_cnt_7)
        self.classes_table_container.setObjectName(u"classes_table_container")
        self.classes_table_container.setMinimumSize(QSize(920, 405))
        self.classes_table_container.setMaximumSize(QSize(920, 16777215))
        self.classes_table_container.setStyleSheet(u"QWidget#classes_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.classes_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.classes_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.classes_table_layout = QVBoxLayout(self.classes_table_container)
        self.classes_table_layout.setSpacing(0)
        self.classes_table_layout.setObjectName(u"classes_table_layout")
        self.classes_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_25.addWidget(self.classes_table_container)


        self.verticalLayout_24.addWidget(self.modules_cnt_7)


        self.verticalLayout_26.addWidget(self.container_8, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.classes_window)
        self.venues_window = QWidget()
        self.venues_window.setObjectName(u"venues_window")
        self.verticalLayout_20 = QVBoxLayout(self.venues_window)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.container_6 = QWidget(self.venues_window)
        self.container_6.setObjectName(u"container_6")
        self.verticalLayout_18 = QVBoxLayout(self.container_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.title_container_5 = QFrame(self.container_6)
        self.title_container_5.setObjectName(u"title_container_5")
        self.title_container_5.setMinimumSize(QSize(0, 40))
        self.title_container_5.setMaximumSize(QSize(16777215, 40))
        self.title_container_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_container_5.setFrameShadow(QFrame.Shadow.Raised)
        self.title_5 = QLabel(self.title_container_5)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setGeometry(QRect(10, 10, 251, 21))
        self.title_5.setFont(font5)

        self.verticalLayout_18.addWidget(self.title_container_5)

        self.modules_cnt_5 = QFrame(self.container_6)
        self.modules_cnt_5.setObjectName(u"modules_cnt_5")
        self.modules_cnt_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.modules_cnt_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.modules_cnt_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.module_header_cnt_5 = QFrame(self.modules_cnt_5)
        self.module_header_cnt_5.setObjectName(u"module_header_cnt_5")
        self.module_header_cnt_5.setMinimumSize(QSize(0, 50))
        self.module_header_cnt_5.setMaximumSize(QSize(16777215, 50))
        self.module_header_cnt_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.module_header_cnt_5.setFrameShadow(QFrame.Shadow.Raised)
        self.venues_add_btn = QPushButton(self.module_header_cnt_5)
        self.venues_add_btn.setObjectName(u"venues_add_btn")
        self.venues_add_btn.setGeometry(QRect(0, 10, 111, 30))
        self.venues_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.venues_add_btn.setIcon(icon18)
        self.venues_add_btn.setIconSize(QSize(14, 14))
        self.venues_search = QLineEdit(self.module_header_cnt_5)
        self.venues_search.setObjectName(u"venues_search")
        self.venues_search.setGeometry(QRect(719, 10, 201, 30))

        self.verticalLayout_19.addWidget(self.module_header_cnt_5)

        self.venues_table_container = QFrame(self.modules_cnt_5)
        self.venues_table_container.setObjectName(u"venues_table_container")
        self.venues_table_container.setMinimumSize(QSize(920, 405))
        self.venues_table_container.setMaximumSize(QSize(920, 16777215))
        self.venues_table_container.setStyleSheet(u"QWidget#venues_table_container{\n"
"background: #FBFCFE;\n"
"border-radius: 5px;\n"
"border: 1px solid #E3E4E6;\n"
"}")
        self.venues_table_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.venues_table_container.setFrameShadow(QFrame.Shadow.Raised)
        self.venues_table_layout = QVBoxLayout(self.venues_table_container)
        self.venues_table_layout.setSpacing(0)
        self.venues_table_layout.setObjectName(u"venues_table_layout")
        self.venues_table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_19.addWidget(self.venues_table_container)


        self.verticalLayout_18.addWidget(self.modules_cnt_5)


        self.verticalLayout_20.addWidget(self.container_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_container.addWidget(self.venues_window)

        self.verticalLayout_2.addWidget(self.stacked_container)

        self.footer = QFrame(self.widget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 25))
        self.footer.setMaximumSize(QSize(16777215, 25))
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.footer)


        self.horizontalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.main_container)

        self.retranslateUi(MainWindow)

        self.stacked_container.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_icon.setText("")
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.tools_btn.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.timetable_btn.setText(QCoreApplication.translate("MainWindow", u"Timetable", None))
        self.view_btn.setText(QCoreApplication.translate("MainWindow", u"View", None))
#if QT_CONFIG(tooltip)
        self.generate_indicator.setToolTip(QCoreApplication.translate("MainWindow", u"Changes not generated", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.save_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.save_btn.setText("")
#if QT_CONFIG(tooltip)
        self.save_indicator.setToolTip(QCoreApplication.translate("MainWindow", u"Unsaved changes", None))
#endif // QT_CONFIG(tooltip)
        self.current_project.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u" Home", None))
#if QT_CONFIG(tooltip)
        self.modules_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Modules", None))
#endif // QT_CONFIG(tooltip)
        self.modules_btn.setText(QCoreApplication.translate("MainWindow", u"   Modules", None))
#if QT_CONFIG(tooltip)
        self.subjects_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Subjects", None))
#endif // QT_CONFIG(tooltip)
        self.subjects_btn.setText(QCoreApplication.translate("MainWindow", u"   Subjects", None))
#if QT_CONFIG(tooltip)
        self.blocks_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Blocks", None))
#endif // QT_CONFIG(tooltip)
        self.blocks_btn.setText(QCoreApplication.translate("MainWindow", u"Blocks", None))
#if QT_CONFIG(tooltip)
        self.lecturers_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Lecturers", None))
#endif // QT_CONFIG(tooltip)
        self.lecturers_btn.setText(QCoreApplication.translate("MainWindow", u" Lecturers", None))
#if QT_CONFIG(tooltip)
        self.teachers_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Teachers", None))
#endif // QT_CONFIG(tooltip)
        self.teachers_btn.setText(QCoreApplication.translate("MainWindow", u" Teachers", None))
#if QT_CONFIG(tooltip)
        self.courses_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Courses", None))
#endif // QT_CONFIG(tooltip)
        self.courses_btn.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
#if QT_CONFIG(tooltip)
        self.classes_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Classes", None))
#endif // QT_CONFIG(tooltip)
        self.classes_btn.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
#if QT_CONFIG(tooltip)
        self.venues_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Venues", None))
#endif // QT_CONFIG(tooltip)
        self.venues_btn.setText(QCoreApplication.translate("MainWindow", u"  Venues", None))
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
#if QT_CONFIG(tooltip)
        self.close_project_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Project", None))
#endif // QT_CONFIG(tooltip)
        self.close_project_btn.setText(QCoreApplication.translate("MainWindow", u"  Close Project", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Smart Timetable Generator", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Timetable", None))
        self.head_8.setText(QCoreApplication.translate("MainWindow", u"Venues", None))
        self.venues_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.coner_shadow_8.setText("")
        self.icon_8.setText("")
        self.head_9.setText(QCoreApplication.translate("MainWindow", u"Subjects", None))
        self.subjects_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_9.setText("")
        self.icon_9.setText("")
        self.head_13.setText(QCoreApplication.translate("MainWindow", u"Modules", None))
        self.modules_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_13.setText("")
        self.icon_13.setText("")
        self.head_7.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.courses_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_7.setText("")
        self.icon_7.setText("")
        self.head_15.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
        self.classes_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_15.setText("")
        self.icon_15.setText("")
        self.head_11.setText(QCoreApplication.translate("MainWindow", u"Lecturers", None))
        self.lecturers_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_11.setText("")
        self.icon_11.setText("")
        self.head_17.setText(QCoreApplication.translate("MainWindow", u"Lecturers", None))
        self.sub_head_17.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_17.setText("")
        self.icon_17.setText("")
        self.head_18.setText(QCoreApplication.translate("MainWindow", u"Teachers", None))
        self.teachers_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_18.setText("")
        self.icon_18.setText("")
        self.head_19.setText(QCoreApplication.translate("MainWindow", u"Lecturers", None))
        self.sub_head_19.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_19.setText("")
        self.icon_19.setText("")
        self.head_12.setText(QCoreApplication.translate("MainWindow", u"Blocks", None))
        self.blocks_count.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">0</span></p></body></html>", None))
        self.coner_shadow_12.setText("")
        self.icon_12.setText("")
#if QT_CONFIG(tooltip)
        self.timetable_generate_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Generate or regenerate the entire timetable.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.timetable_generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.timetable_generate_updates_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Generate only the changes made to the school data without changing the existing timetable.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.timetable_generate_updates_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Updates", None))
#if QT_CONFIG(tooltip)
        self.timetable_view_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>View the existing timetable.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.timetable_view_btn.setText(QCoreApplication.translate("MainWindow", u"View Timetable", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Days per cycle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Periods per day", None))
        ___qtablewidgetitem = self.slot_edit_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Slot", None));
        ___qtablewidgetitem1 = self.slot_edit_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.day_edit_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Day", None));
        ___qtablewidgetitem3 = self.day_edit_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Name", None));
#if QT_CONFIG(tooltip)
        self.add_break_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add timetable Break, Lunch or Study.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_break_btn.setText(QCoreApplication.translate("MainWindow", u"Add Break", None))
        self.dash_timetable_status.setText(QCoreApplication.translate("MainWindow", u"There is nothing to generate from.", None))
        self.modules_course_filter.setCurrentText("")
        self.modules_course_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter Courses", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Manage Modules", None))
        self.modules_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Module", None))
        self.modules_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Module", None))
        self.subjects_class_filter.setCurrentText("")
        self.subjects_class_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter By Class", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Manage Subjects", None))
        self.subjects_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Subject", None))
        self.subjects_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Subject", None))
        self.title_8.setText(QCoreApplication.translate("MainWindow", u"Manage Blocks", None))
        self.blocks_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Block", None))
        self.blocks_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Block", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Manage Lecturers", None))
        self.lecturers_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Lecturer", None))
        self.lecturers_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Lecturer", None))
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"Manage Teachers", None))
        self.teachers_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Teacher", None))
        self.teachers_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Teacher", None))
        self.title_6.setText(QCoreApplication.translate("MainWindow", u"Manage Courses", None))
        self.courses_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Course", None))
        self.courses_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Courses", None))
        self.title_7.setText(QCoreApplication.translate("MainWindow", u"Manage Classes", None))
        self.classes_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Class", None))
        self.classes_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Class", None))
        self.title_5.setText(QCoreApplication.translate("MainWindow", u"Manage Venues", None))
        self.venues_add_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Venue", None))
        self.venues_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Venue", None))
    # retranslateUi

