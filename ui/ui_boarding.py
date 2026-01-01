# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boardingpaDFGc.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget)

from widgets.custom_widgets import ButtonFrame
import icons_rc

class Ui_Boarding(object):
    def setupUi(self, Boarding):
        if not Boarding.objectName():
            Boarding.setObjectName(u"Boarding")
        Boarding.resize(360, 430)
        Boarding.setMinimumSize(QSize(360, 430))
        Boarding.setStyleSheet(u"* {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #414141;\n"
"}\n"
"\n"
"QWidget#main_container {\n"
"	background: #EBECEF;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #B1B1B1;\n"
"}\n"
"\n"
"QWidget#container {\n"
"	background: #F3F4F6;\n"
"}\n"
"\n"
"#close_btn:hover{\n"
"	background: #DC2626;\n"
"}\n"
"\n"
"#toolbar{\n"
"	border-bottom: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	outline: none;\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background: #FBFCFE;\n"
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
"	background"
                        ": transparent;\n"
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
"	height: 24px;\n"
"	width: 24px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Boarding)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(Boarding)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setMinimumSize(QSize(360, 430))
        self.verticalLayout_2 = QVBoxLayout(self.main_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.toolbar = QFrame(self.main_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 25))
        self.toolbar.setMaximumSize(QSize(16777215, 25))
        self.toolbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.toolbar.setFrameShadow(QFrame.Shadow.Raised)
        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(330, 0, 30, 24))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(10, 10))

        self.verticalLayout_2.addWidget(self.toolbar)

        self.container = QStackedWidget(self.main_container)
        self.container.setObjectName(u"container")
        self.board_page_1 = QWidget()
        self.board_page_1.setObjectName(u"board_page_1")
        self.title = QLabel(self.board_page_1)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(81, 20, 221, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        self.next_btn = QPushButton(self.board_page_1)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setGeometry(QRect(111, 350, 131, 30))
        self.next_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.next_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.next_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.next_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-right-long.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_btn.setIcon(icon1)
        self.next_btn.setIconSize(QSize(14, 14))
        self.sub_title = QLabel(self.board_page_1)
        self.sub_title.setObjectName(u"sub_title")
        self.sub_title.setGeometry(QRect(111, 45, 161, 20))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.sub_title.setFont(font1)
        self.sub_title.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.frame = QFrame(self.board_page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 80, 311, 251))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tertiary_btn = ButtonFrame(self.frame)
        self.tertiary_btn.setObjectName(u"tertiary_btn")
        self.tertiary_btn.setGeometry(QRect(10, 170, 281, 61))
        self.tertiary_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tertiary_btn.setStyleSheet(u"QFrame#tertiary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#tertiary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_7 = QLabel(self.tertiary_btn)
        self.head_7.setObjectName(u"head_7")
        self.head_7.setGeometry(QRect(60, 10, 161, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.head_7.setFont(font2)
        self.sub_head_7 = QLabel(self.tertiary_btn)
        self.sub_head_7.setObjectName(u"sub_head_7")
        self.sub_head_7.setGeometry(QRect(60, 35, 181, 21))
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        self.sub_head_7.setFont(font3)
        self.sub_head_7.setStyleSheet(u"color: #818181;")
        self.sub_head_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_7 = QLabel(self.tertiary_btn)
        self.coner_shadow_7.setObjectName(u"coner_shadow_7")
        self.coner_shadow_7.setGeometry(QRect(80, 0, 201, 61))
        self.coner_shadow_7.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_7.setScaledContents(True)
        self.icon_7 = QPushButton(self.tertiary_btn)
        self.icon_7.setObjectName(u"icon_7")
        self.icon_7.setGeometry(QRect(10, 20, 31, 24))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/tertiary.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_7.setIcon(icon2)
        self.icon_7.setIconSize(QSize(32, 32))
        self.selector_7 = QWidget(self.tertiary_btn)
        self.selector_7.setObjectName(u"selector_7")
        self.selector_7.setGeometry(QRect(250, 25, 15, 15))
        self.selector_7.setStyleSheet(u"border: 1px solid #B1B1B1;\n"
"border-radius: 7px;")
        self.verticalLayout_5 = QVBoxLayout(self.selector_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tick = QLabel(self.selector_7)
        self.tick.setObjectName(u"tick")
        self.tick.setPixmap(QPixmap(u":/icons/icons/tick.svg"))
        self.tick.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.tick)

        self.primary_btn = ButtonFrame(self.frame)
        self.primary_btn.setObjectName(u"primary_btn")
        self.primary_btn.setGeometry(QRect(10, 10, 281, 61))
        self.primary_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.primary_btn.setStyleSheet(u"QFrame#primary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#primary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_8 = QLabel(self.primary_btn)
        self.head_8.setObjectName(u"head_8")
        self.head_8.setGeometry(QRect(60, 10, 151, 21))
        self.head_8.setFont(font2)
        self.sub_head_8 = QLabel(self.primary_btn)
        self.sub_head_8.setObjectName(u"sub_head_8")
        self.sub_head_8.setGeometry(QRect(60, 35, 171, 21))
        self.sub_head_8.setFont(font3)
        self.sub_head_8.setStyleSheet(u"color: #818181;")
        self.sub_head_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_8 = QLabel(self.primary_btn)
        self.coner_shadow_8.setObjectName(u"coner_shadow_8")
        self.coner_shadow_8.setGeometry(QRect(80, 0, 201, 61))
        self.coner_shadow_8.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_8.setScaledContents(True)
        self.icon_8 = QPushButton(self.primary_btn)
        self.icon_8.setObjectName(u"icon_8")
        self.icon_8.setGeometry(QRect(10, 20, 31, 24))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/primary.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_8.setIcon(icon3)
        self.icon_8.setIconSize(QSize(32, 32))
        self.selector_8 = QWidget(self.primary_btn)
        self.selector_8.setObjectName(u"selector_8")
        self.selector_8.setGeometry(QRect(250, 25, 15, 15))
        self.selector_8.setStyleSheet(u"border: 1px solid #B1B1B1;\n"
"border-radius: 5px;")
        self.tick_3 = QLabel(self.selector_8)
        self.tick_3.setObjectName(u"tick_3")
        self.tick_3.setGeometry(QRect(0, 0, 15, 15))
        self.tick_3.setPixmap(QPixmap(u":/icons/icons/tick.svg"))
        self.tick_3.setScaledContents(True)
        self.secondary_btn = ButtonFrame(self.frame)
        self.secondary_btn.setObjectName(u"secondary_btn")
        self.secondary_btn.setGeometry(QRect(10, 90, 281, 61))
        self.secondary_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.secondary_btn.setStyleSheet(u"QFrame#secondary_btn{\n"
"	border: 1px solid #E3E4E6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#secondary_btn:hover{\n"
"	border: 3px solid #DBEAFE;\n"
"	background: #DBEAFE;\n"
"}")
        self.head_9 = QLabel(self.secondary_btn)
        self.head_9.setObjectName(u"head_9")
        self.head_9.setGeometry(QRect(60, 10, 161, 21))
        self.head_9.setFont(font2)
        self.sub_head_9 = QLabel(self.secondary_btn)
        self.sub_head_9.setObjectName(u"sub_head_9")
        self.sub_head_9.setGeometry(QRect(60, 35, 171, 21))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        self.sub_head_9.setFont(font4)
        self.sub_head_9.setStyleSheet(u"color: #818181;")
        self.sub_head_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.coner_shadow_9 = QLabel(self.secondary_btn)
        self.coner_shadow_9.setObjectName(u"coner_shadow_9")
        self.coner_shadow_9.setGeometry(QRect(80, 0, 201, 61))
        self.coner_shadow_9.setPixmap(QPixmap(u":/icons/images/corner_gradient.png"))
        self.coner_shadow_9.setScaledContents(True)
        self.icon_9 = QPushButton(self.secondary_btn)
        self.icon_9.setObjectName(u"icon_9")
        self.icon_9.setGeometry(QRect(10, 20, 31, 24))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/secondary.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_9.setIcon(icon4)
        self.icon_9.setIconSize(QSize(32, 32))
        self.selector_9 = QWidget(self.secondary_btn)
        self.selector_9.setObjectName(u"selector_9")
        self.selector_9.setGeometry(QRect(250, 25, 15, 15))
        self.selector_9.setStyleSheet(u"border: 1px solid #B1B1B1;\n"
"border-radius: 5px;")
        self.tick_2 = QLabel(self.selector_9)
        self.tick_2.setObjectName(u"tick_2")
        self.tick_2.setGeometry(QRect(0, 0, 15, 15))
        self.tick_2.setPixmap(QPixmap(u":/icons/icons/tick.svg"))
        self.tick_2.setScaledContents(True)
        self.container.addWidget(self.board_page_1)
        self.board_page_2 = QWidget()
        self.board_page_2.setObjectName(u"board_page_2")
        self.back_btn = QPushButton(self.board_page_2)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(20, 360, 75, 24))
        self.back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/arrow-left-long.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_btn.setIcon(icon5)
        self.back_btn.setIconSize(QSize(14, 14))
        self.create_btn = QPushButton(self.board_page_2)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setGeometry(QRect(220, 360, 121, 30))
        self.create_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.create_btn.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.title_2 = QLabel(self.board_page_2)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(40, 20, 251, 20))
        self.title_2.setFont(font)
        self.intitution_name_txt = QLineEdit(self.board_page_2)
        self.intitution_name_txt.setObjectName(u"intitution_name_txt")
        self.intitution_name_txt.setGeometry(QRect(40, 70, 200, 30))
        self.intitution_name_txt.setStyleSheet(u"border: 1px solid #D3D4D6;\n"
"border-radius: 5px;\n"
"padding-left: 5px;")
        self.timetable_name_txt = QLineEdit(self.board_page_2)
        self.timetable_name_txt.setObjectName(u"timetable_name_txt")
        self.timetable_name_txt.setGeometry(QRect(40, 120, 200, 30))
        self.timetable_name_txt.setStyleSheet(u"border: 1px solid #D3D4D6;\n"
"border-radius: 5px;\n"
"padding-left: 5px;")
        self.slots_per_cycle_txt = QSpinBox(self.board_page_2)
        self.slots_per_cycle_txt.setObjectName(u"slots_per_cycle_txt")
        self.slots_per_cycle_txt.setGeometry(QRect(40, 185, 100, 30))
        self.slots_per_cycle_txt.setStyleSheet(u"border: 1px solid #D3D4D6;\n"
"border-radius: 5px;\n"
"padding-left: 5px;")
        self.slots_per_cycle_txt.setMinimum(1)
        self.slots_per_cycle_txt.setMaximum(10000)
        self.sub_title_2 = QLabel(self.board_page_2)
        self.sub_title_2.setObjectName(u"sub_title_2")
        self.sub_title_2.setGeometry(QRect(40, 160, 160, 20))
        self.sub_title_2.setFont(font1)
        self.sub_title_2.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.slots_per_day_txt = QSpinBox(self.board_page_2)
        self.slots_per_day_txt.setObjectName(u"slots_per_day_txt")
        self.slots_per_day_txt.setGeometry(QRect(40, 250, 100, 30))
        self.slots_per_day_txt.setStyleSheet(u"border: 1px solid #D3D4D6;\n"
"border-radius: 5px;\n"
"padding-left: 5px;")
        self.slots_per_day_txt.setMinimum(1)
        self.slots_per_day_txt.setMaximum(1000000000)
        self.sub_title_3 = QLabel(self.board_page_2)
        self.sub_title_3.setObjectName(u"sub_title_3")
        self.sub_title_3.setGeometry(QRect(40, 225, 161, 20))
        self.sub_title_3.setFont(font1)
        self.sub_title_3.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.slot_length_txt = QSpinBox(self.board_page_2)
        self.slot_length_txt.setObjectName(u"slot_length_txt")
        self.slot_length_txt.setGeometry(QRect(40, 310, 100, 30))
        self.slot_length_txt.setStyleSheet(u"border: 1px solid #D3D4D6;\n"
"border-radius: 5px;\n"
"padding-left: 5px;")
        self.slot_length_txt.setMinimum(30)
        self.slot_length_txt.setMaximum(1000000000)
        self.sub_title_4 = QLabel(self.board_page_2)
        self.sub_title_4.setObjectName(u"sub_title_4")
        self.sub_title_4.setGeometry(QRect(40, 285, 161, 20))
        self.sub_title_4.setFont(font1)
        self.sub_title_4.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.container.addWidget(self.board_page_2)

        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout.addWidget(self.main_container)


        self.retranslateUi(Boarding)

        self.container.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Boarding)
    # setupUi

    def retranslateUi(self, Boarding):
        Boarding.setWindowTitle(QCoreApplication.translate("Boarding", u"Dialog", None))
        self.close_btn.setText("")
        self.title.setText(QCoreApplication.translate("Boarding", u"Smart Timetable Generator", None))
        self.next_btn.setText(QCoreApplication.translate("Boarding", u"Continue    ", None))
        self.sub_title.setText(QCoreApplication.translate("Boarding", u"Build Schedules Intelligently", None))
        self.head_7.setText(QCoreApplication.translate("Boarding", u"University or College", None))
        self.sub_head_7.setText(QCoreApplication.translate("Boarding", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe Ui'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Courses, lecturers and modules</p></body></html>", None))
        self.coner_shadow_7.setText("")
        self.icon_7.setText("")
        self.tick.setText("")
        self.head_8.setText(QCoreApplication.translate("Boarding", u"Primary School", None))
        self.sub_head_8.setText(QCoreApplication.translate("Boarding", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">Simple Class-based scheduling</span></p></body></html>", None))
        self.coner_shadow_8.setText("")
        self.icon_8.setText("")
        self.tick_3.setText("")
        self.head_9.setText(QCoreApplication.translate("Boarding", u"Secondary School", None))
        self.sub_head_9.setText(QCoreApplication.translate("Boarding", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Ui';\">Classes, Teachers and Subjects</span></p></body></html>", None))
        self.coner_shadow_9.setText("")
        self.icon_9.setText("")
        self.tick_2.setText("")
        self.back_btn.setText(QCoreApplication.translate("Boarding", u"  Back", None))
        self.create_btn.setText(QCoreApplication.translate("Boarding", u"Create Project", None))
        self.title_2.setText(QCoreApplication.translate("Boarding", u"Create New Timetable Project", None))
        self.intitution_name_txt.setPlaceholderText(QCoreApplication.translate("Boarding", u"Institution name", None))
        self.timetable_name_txt.setPlaceholderText(QCoreApplication.translate("Boarding", u"Project name", None))
        self.sub_title_2.setText(QCoreApplication.translate("Boarding", u"Days per cycle", None))
        self.sub_title_3.setText(QCoreApplication.translate("Boarding", u"Slots per day", None))
        self.sub_title_4.setText(QCoreApplication.translate("Boarding", u"Slot length (minutes)", None))
    # retranslateUi

