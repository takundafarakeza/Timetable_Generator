# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startupMaTrrU.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

from widgets.custom_widgets import ButtonFrame
import icons_rc

class Ui_StartUp(object):
    def setupUi(self, StartUp):
        if not StartUp.objectName():
            StartUp.setObjectName(u"StartUp")
        StartUp.resize(930, 600)
        StartUp.setStyleSheet(u"* {\n"
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
"QWidget#window_container{\n"
"	background: #EBECEF;\n"
"	border-radius: 5px;\n"
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
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #141517;\n"
"	height:"
                        " 8px;\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background: #262a2e;\n"
"	min-width: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: #EBECEF;\n"
"	width: 8px;\n"
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
"}")
        self.window_container = QWidget(StartUp)
        self.window_container.setObjectName(u"window_container")
        self.verticalLayout = QVBoxLayout(self.window_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolbar = QWidget(self.window_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMaximumSize(QSize(16777215, 60))
        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(884, 20, 31, 24))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(10, 10))
        self.minimize_btn = QPushButton(self.toolbar)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(844, 20, 31, 24))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.minimize_btn.setIcon(icon2)
        self.title = QLabel(self.toolbar)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 20, 241, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(False)
        self.title.setFont(font)
        self.window_icon = QPushButton(self.toolbar)
        self.window_icon.setObjectName(u"window_icon")
        self.window_icon.setGeometry(QRect(10, 10, 41, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.window_icon.setIcon(icon3)
        self.window_icon.setIconSize(QSize(38, 39))

        self.verticalLayout.addWidget(self.toolbar)

        self.container = QWidget(self.window_container)
        self.container.setObjectName(u"container")
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 25, 50, 30)
        self.central_container = QWidget(self.container)
        self.central_container.setObjectName(u"central_container")
        self.central_container.setStyleSheet(u"")
        self.create_new_project_btn = ButtonFrame(self.central_container)
        self.create_new_project_btn.setObjectName(u"create_new_project_btn")
        self.create_new_project_btn.setGeometry(QRect(60, 40, 221, 81))
        self.create_new_project_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.create_new_project_btn.setStyleSheet(u"QFrame#create_new_project_btn{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#create_new_project_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_1 = QLabel(self.create_new_project_btn)
        self.head_1.setObjectName(u"head_1")
        self.head_1.setGeometry(QRect(50, 10, 151, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.head_1.setFont(font1)
        self.sub_head_1 = QLabel(self.create_new_project_btn)
        self.sub_head_1.setObjectName(u"sub_head_1")
        self.sub_head_1.setGeometry(QRect(50, 35, 151, 41))
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        self.sub_head_1.setFont(font2)
        self.sub_head_1.setStyleSheet(u"color: #818181;")
        self.sub_head_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_3 = QLabel(self.create_new_project_btn)
        self.coner_shadow_3.setObjectName(u"coner_shadow_3")
        self.coner_shadow_3.setGeometry(QRect(80, 20, 141, 61))
        self.coner_shadow_3.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_3.setScaledContents(True)
        self.icon_2 = QPushButton(self.create_new_project_btn)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setGeometry(QRect(10, 15, 31, 24))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_2.setIcon(icon4)
        self.icon_2.setIconSize(QSize(20, 20))
        self.open_project_btn = ButtonFrame(self.central_container)
        self.open_project_btn.setObjectName(u"open_project_btn")
        self.open_project_btn.setGeometry(QRect(310, 40, 221, 81))
        self.open_project_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.open_project_btn.setStyleSheet(u"QFrame#open_project_btn{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#open_project_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_2 = QLabel(self.open_project_btn)
        self.head_2.setObjectName(u"head_2")
        self.head_2.setGeometry(QRect(50, 10, 161, 21))
        self.head_2.setFont(font1)
        self.sub_head_2 = QLabel(self.open_project_btn)
        self.sub_head_2.setObjectName(u"sub_head_2")
        self.sub_head_2.setGeometry(QRect(50, 35, 151, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.sub_head_2.setFont(font3)
        self.sub_head_2.setStyleSheet(u"color: #818181;")
        self.sub_head_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_2 = QLabel(self.open_project_btn)
        self.coner_shadow_2.setObjectName(u"coner_shadow_2")
        self.coner_shadow_2.setGeometry(QRect(80, 20, 141, 61))
        self.coner_shadow_2.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_2.setScaledContents(True)
        self.icon = QPushButton(self.open_project_btn)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(10, 15, 31, 24))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon.setIcon(icon5)
        self.icon.setIconSize(QSize(20, 20))
        self.import_project_btn = ButtonFrame(self.central_container)
        self.import_project_btn.setObjectName(u"import_project_btn")
        self.import_project_btn.setGeometry(QRect(560, 40, 221, 81))
        self.import_project_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.import_project_btn.setStyleSheet(u"QFrame#import_project_btn{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#import_project_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_4 = QLabel(self.import_project_btn)
        self.head_4.setObjectName(u"head_4")
        self.head_4.setGeometry(QRect(50, 10, 161, 21))
        self.head_4.setFont(font1)
        self.sub_head_4 = QLabel(self.import_project_btn)
        self.sub_head_4.setObjectName(u"sub_head_4")
        self.sub_head_4.setGeometry(QRect(50, 35, 151, 41))
        self.sub_head_4.setFont(font2)
        self.sub_head_4.setStyleSheet(u"color: #818181;")
        self.sub_head_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow = QLabel(self.import_project_btn)
        self.coner_shadow.setObjectName(u"coner_shadow")
        self.coner_shadow.setGeometry(QRect(80, 20, 141, 61))
        self.coner_shadow.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow.setScaledContents(True)
        self.icon_3 = QPushButton(self.import_project_btn)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setGeometry(QRect(10, 15, 31, 24))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_3.setIcon(icon6)
        self.icon_3.setIconSize(QSize(20, 20))
        self.head_5 = QLabel(self.central_container)
        self.head_5.setObjectName(u"head_5")
        self.head_5.setGeometry(QRect(60, 142, 121, 21))
        self.head_5.setFont(font1)
        self.line_1 = QWidget(self.central_container)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(190, 150, 590, 5))
        self.line_1.setStyleSheet(u"border-bottom: 2px solid #E3E4E6;")
        self.projects_search_txt = QLineEdit(self.central_container)
        self.projects_search_txt.setObjectName(u"projects_search_txt")
        self.projects_search_txt.setGeometry(QRect(582, 172, 201, 30))
        self.projects_search_txt.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.projects_search_txt.setStyleSheet(u"padding-left: 20px;")
        self.projects_search_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.search_icon = QPushButton(self.central_container)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(590, 172, 21, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_icon.setIcon(icon7)
        self.search_container = QFrame(self.central_container)
        self.search_container.setObjectName(u"search_container")
        self.search_container.setGeometry(QRect(60, 222, 722, 170))
        self.search_container.setMinimumSize(QSize(722, 170))
        self.search_container.setStyleSheet(u"")
        self.search_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.search_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.recents_toolbar = QFrame(self.search_container)
        self.recents_toolbar.setObjectName(u"recents_toolbar")
        self.recents_toolbar.setMinimumSize(QSize(0, 30))
        self.recents_toolbar.setMaximumSize(QSize(16777215, 30))
        self.recents_toolbar.setStyleSheet(u"background-color: rgb(235, 236, 239);\n"
"border-bottom: 2px solid #E3E4E6;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;")
        self.recents_toolbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.recents_toolbar.setFrameShadow(QFrame.Shadow.Raised)
        self.recent_projects_refresh_btn = QPushButton(self.recents_toolbar)
        self.recent_projects_refresh_btn.setObjectName(u"recent_projects_refresh_btn")
        self.recent_projects_refresh_btn.setGeometry(QRect(20, 0, 111, 30))
        self.recent_projects_refresh_btn.setFont(font3)
        self.recent_projects_refresh_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        self.recent_projects_refresh_btn.setIcon(icon8)
        self.recent_projects_refresh_btn.setIconSize(QSize(12, 12))
        self.recents_clear_btn = QPushButton(self.recents_toolbar)
        self.recents_clear_btn.setObjectName(u"recents_clear_btn")
        self.recents_clear_btn.setGeometry(QRect(640, 0, 71, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.recents_clear_btn.setFont(font4)
        self.recents_clear_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.recents_clear_btn.setIconSize(QSize(12, 12))

        self.verticalLayout_3.addWidget(self.recents_toolbar)

        self.scrollArea = QScrollArea(self.search_container)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.recents_scroll_container = QWidget()
        self.recents_scroll_container.setObjectName(u"recents_scroll_container")
        self.recents_scroll_container.setGeometry(QRect(0, 0, 720, 138))
        self.recent_scroll_layout = QVBoxLayout(self.recents_scroll_container)
        self.recent_scroll_layout.setObjectName(u"recent_scroll_layout")
        self.recents_container = QWidget(self.recents_scroll_container)
        self.recents_container.setObjectName(u"recents_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recents_container.sizePolicy().hasHeightForWidth())
        self.recents_container.setSizePolicy(sizePolicy)
        self.recent_layout = QVBoxLayout(self.recents_container)
        self.recent_layout.setSpacing(0)
        self.recent_layout.setObjectName(u"recent_layout")
        self.recent_layout.setContentsMargins(0, 0, 0, 0)
        self.recent_status_txt = QLabel(self.recents_container)
        self.recent_status_txt.setObjectName(u"recent_status_txt")
        self.recent_status_txt.setMinimumSize(QSize(0, 120))
        self.recent_status_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.recent_layout.addWidget(self.recent_status_txt)


        self.recent_scroll_layout.addWidget(self.recents_container, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.recents_scroll_container)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.prefs_btn = QPushButton(self.central_container)
        self.prefs_btn.setObjectName(u"prefs_btn")
        self.prefs_btn.setGeometry(QRect(60, 420, 91, 31))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prefs_btn.setIcon(icon9)
        self.online_btn = QPushButton(self.central_container)
        self.online_btn.setObjectName(u"online_btn")
        self.online_btn.setGeometry(QRect(60, 420, 75, 31))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.online_btn.setIcon(icon10)
        self.quit_btn = QPushButton(self.central_container)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setGeometry(QRect(720, 420, 61, 31))
        self.quit_btn.setStyleSheet(u"color: rgb(129, 129, 129);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/logout.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quit_btn.setIcon(icon11)
        self.label = QLabel(self.central_container)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 838, 491))
        self.label.setPixmap(QPixmap(u":/icons/images/shadow.svg"))
        self.label.setScaledContents(True)
        self.prefs_btn.raise_()
        self.label.raise_()
        self.create_new_project_btn.raise_()
        self.open_project_btn.raise_()
        self.import_project_btn.raise_()
        self.head_5.raise_()
        self.line_1.raise_()
        self.projects_search_txt.raise_()
        self.search_icon.raise_()
        self.search_container.raise_()
        self.online_btn.raise_()
        self.quit_btn.raise_()

        self.verticalLayout_2.addWidget(self.central_container)


        self.verticalLayout.addWidget(self.container)

        StartUp.setCentralWidget(self.window_container)
        QWidget.setTabOrder(self.minimize_btn, self.window_icon)
        QWidget.setTabOrder(self.window_icon, self.close_btn)
        QWidget.setTabOrder(self.close_btn, self.icon)
        QWidget.setTabOrder(self.icon, self.icon_3)
        QWidget.setTabOrder(self.icon_3, self.icon_2)
        QWidget.setTabOrder(self.icon_2, self.projects_search_txt)
        QWidget.setTabOrder(self.projects_search_txt, self.search_icon)
        QWidget.setTabOrder(self.search_icon, self.recent_projects_refresh_btn)
        QWidget.setTabOrder(self.recent_projects_refresh_btn, self.recents_clear_btn)
        QWidget.setTabOrder(self.recents_clear_btn, self.prefs_btn)
        QWidget.setTabOrder(self.prefs_btn, self.online_btn)
        QWidget.setTabOrder(self.online_btn, self.quit_btn)

        self.retranslateUi(StartUp)

        QMetaObject.connectSlotsByName(StartUp)
    # setupUi

    def retranslateUi(self, StartUp):
        StartUp.setWindowTitle(QCoreApplication.translate("StartUp", u"MainWindow", None))
        self.close_btn.setText("")
        self.minimize_btn.setText("")
        self.title.setText(QCoreApplication.translate("StartUp", u"Smart Timetable Generator", None))
        self.window_icon.setText("")
        self.head_1.setText(QCoreApplication.translate("StartUp", u"Create New Project", None))
        self.sub_head_1.setText(QCoreApplication.translate("StartUp", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe Ui'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Create a new timetable</p>\n"
"<p align=\"justify\" style=\" margin-top:2px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">from scratch</p></body></html>", None))
        self.coner_shadow_3.setText("")
        self.icon_2.setText("")
        self.head_2.setText(QCoreApplication.translate("StartUp", u"Open Existing Project", None))
        self.sub_head_2.setText(QCoreApplication.translate("StartUp", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe Ui'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span>Browse for an existing</span></p>\n"
"<p align=\"justify\" style=\" margin-top:2px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span>timetable file</span></p></body></html>", None))
        self.coner_shadow_2.setText("")
        self.icon.setText("")
        self.head_4.setText(QCoreApplication.translate("StartUp", u"Import Timetable", None))
        self.sub_head_4.setText(QCoreApplication.translate("StartUp", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe Ui'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Import from another</p>\n"
"<p align=\"justify\" style=\" margin-top:2px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">system or format</p></body></html>", None))
        self.coner_shadow.setText("")
        self.icon_3.setText("")
        self.head_5.setText(QCoreApplication.translate("StartUp", u"Recent Projects", None))
        self.projects_search_txt.setPlaceholderText(QCoreApplication.translate("StartUp", u"Search Recent Projects", None))
        self.search_icon.setText("")
        self.recent_projects_refresh_btn.setText(QCoreApplication.translate("StartUp", u"  Recent Projects", None))
        self.recents_clear_btn.setText(QCoreApplication.translate("StartUp", u"Clear List", None))
        self.recent_status_txt.setText(QCoreApplication.translate("StartUp", u"No Recent Projects Are Available Yet...", None))
        self.prefs_btn.setText(QCoreApplication.translate("StartUp", u"  Preferences", None))
        self.online_btn.setText(QCoreApplication.translate("StartUp", u" Online", None))
        self.quit_btn.setText(QCoreApplication.translate("StartUp", u"  Quit", None))
        self.label.setText("")
    # retranslateUi

