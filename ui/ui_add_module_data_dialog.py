# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_module_data_dialognTyZjO.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_AddModule(object):
    def setupUi(self, AddModule):
        if not AddModule.objectName():
            AddModule.setObjectName(u"AddModule")
        AddModule.resize(917, 506)
        AddModule.setStyleSheet(u"* {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #414141;\n"
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
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;"
                        "\n"
"	background: #FBFCFE;\n"
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
"}")
        self.verticalLayout_2 = QVBoxLayout(AddModule)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(AddModule)
        self.main_container.setObjectName(u"main_container")
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.toolbar = QWidget(self.main_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.toolbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(657, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(35, 30))
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.toolbar)

        self.container = QWidget(self.main_container)
        self.container.setObjectName(u"container")
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.module_save = QPushButton(self.frame)
        self.module_save.setObjectName(u"module_save")
        self.module_save.setGeometry(QRect(810, 390, 81, 30))
        self.module_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.module_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.module_add_course_btn = QPushButton(self.frame)
        self.module_add_course_btn.setObjectName(u"module_add_course_btn")
        self.module_add_course_btn.setGeometry(QRect(280, 320, 30, 30))
        self.module_add_course_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.module_add_course_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.module_add_course_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.module_add_course_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.module_add_course_btn.setIcon(icon1)
        self.module_add_course_btn.setIconSize(QSize(14, 14))
        self.module_venue_select = QComboBox(self.frame)
        self.module_venue_select.setObjectName(u"module_venue_select")
        self.module_venue_select.setGeometry(QRect(330, 320, 251, 30))
        self.module_venue_select.setMinimumSize(QSize(0, 30))
        self.module_venue_select.setEditable(True)
        self.module_venues_table = QTableWidget(self.frame)
        if (self.module_venues_table.columnCount() < 1):
            self.module_venues_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.module_venues_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.module_venues_table.setObjectName(u"module_venues_table")
        self.module_venues_table.setGeometry(QRect(330, 30, 301, 261))
        self.module_venues_table.horizontalHeader().setDefaultSectionSize(260)
        self.module_courses_table = QTableWidget(self.frame)
        if (self.module_courses_table.columnCount() < 1):
            self.module_courses_table.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.module_courses_table.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.module_courses_table.setObjectName(u"module_courses_table")
        self.module_courses_table.setGeometry(QRect(30, 30, 301, 201))
        self.module_courses_table.horizontalHeader().setDefaultSectionSize(260)
        self.module_add_venue_btn = QPushButton(self.frame)
        self.module_add_venue_btn.setObjectName(u"module_add_venue_btn")
        self.module_add_venue_btn.setGeometry(QRect(600, 320, 30, 30))
        self.module_add_venue_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.module_add_venue_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.module_add_venue_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.module_add_venue_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.module_add_venue_btn.setIcon(icon1)
        self.module_add_venue_btn.setIconSize(QSize(14, 14))
        self.module_course_select = QComboBox(self.frame)
        self.module_course_select.setObjectName(u"module_course_select")
        self.module_course_select.setGeometry(QRect(30, 320, 201, 30))
        self.module_course_select.setMinimumSize(QSize(0, 30))
        self.module_course_select.setEditable(True)
        self.module_course_level_select = QComboBox(self.frame)
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.addItem("")
        self.module_course_level_select.setObjectName(u"module_course_level_select")
        self.module_course_level_select.setGeometry(QRect(30, 280, 201, 30))
        self.module_course_level_select.setEditable(True)
        self.module_name = QLabel(self.frame)
        self.module_name.setObjectName(u"module_name")
        self.module_name.setGeometry(QRect(30, 0, 261, 21))
        self.module_course_module_code = QLineEdit(self.frame)
        self.module_course_module_code.setObjectName(u"module_course_module_code")
        self.module_course_module_code.setGeometry(QRect(30, 240, 281, 30))
        self.lock_frame = QFrame(self.frame)
        self.lock_frame.setObjectName(u"lock_frame")
        self.lock_frame.setGeometry(QRect(640, 20, 261, 351))
        self.lock_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lock_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.lock_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.locked_slots_table = QTableWidget(self.lock_frame)
        if (self.locked_slots_table.columnCount() < 1):
            self.locked_slots_table.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.locked_slots_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.locked_slots_table.setObjectName(u"locked_slots_table")
        self.locked_slots_table.horizontalHeader().setDefaultSectionSize(230)

        self.verticalLayout_4.addWidget(self.locked_slots_table)

        self.frame_4 = QFrame(self.lock_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.module_add_lock_btn = QPushButton(self.frame_4)
        self.module_add_lock_btn.setObjectName(u"module_add_lock_btn")
        self.module_add_lock_btn.setGeometry(QRect(210, 60, 30, 30))
        self.module_add_lock_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.module_add_lock_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.module_add_lock_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.module_add_lock_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.module_add_lock_btn.setIcon(icon1)
        self.module_add_lock_btn.setIconSize(QSize(14, 14))
        self.module_lock_slot_select = QComboBox(self.frame_4)
        self.module_lock_slot_select.setObjectName(u"module_lock_slot_select")
        self.module_lock_slot_select.setGeometry(QRect(0, 60, 201, 30))
        self.module_lock_slot_select.setMinimumSize(QSize(0, 30))
        self.module_lock_slot_select.setEditable(False)
        self.module_lock_day_select = QComboBox(self.frame_4)
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.addItem("")
        self.module_lock_day_select.setObjectName(u"module_lock_day_select")
        self.module_lock_day_select.setGeometry(QRect(0, 20, 201, 30))
        self.module_lock_day_select.setEditable(False)

        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(AddModule)

        QMetaObject.connectSlotsByName(AddModule)
    # setupUi

    def retranslateUi(self, AddModule):
        AddModule.setWindowTitle(QCoreApplication.translate("AddModule", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("AddModule", u"Module Programs and Venues", None))
        self.module_save.setText(QCoreApplication.translate("AddModule", u"Close", None))
        self.module_add_course_btn.setText("")
        self.module_venue_select.setPlaceholderText("")
        ___qtablewidgetitem = self.module_venues_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddModule", u"Venues", None));
        ___qtablewidgetitem1 = self.module_courses_table.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddModule", u"Program", None));
        self.module_add_venue_btn.setText("")
        self.module_course_select.setPlaceholderText(QCoreApplication.translate("AddModule", u"Select Course", None))
        self.module_course_level_select.setItemText(0, QCoreApplication.translate("AddModule", u"1.1", None))
        self.module_course_level_select.setItemText(1, QCoreApplication.translate("AddModule", u"1.2", None))
        self.module_course_level_select.setItemText(2, QCoreApplication.translate("AddModule", u"2.1", None))
        self.module_course_level_select.setItemText(3, QCoreApplication.translate("AddModule", u"2.2", None))
        self.module_course_level_select.setItemText(4, QCoreApplication.translate("AddModule", u"3.1", None))
        self.module_course_level_select.setItemText(5, QCoreApplication.translate("AddModule", u"3.2", None))
        self.module_course_level_select.setItemText(6, QCoreApplication.translate("AddModule", u"4.1", None))
        self.module_course_level_select.setItemText(7, QCoreApplication.translate("AddModule", u"4.2", None))
        self.module_course_level_select.setItemText(8, QCoreApplication.translate("AddModule", u"5.1", None))
        self.module_course_level_select.setItemText(9, QCoreApplication.translate("AddModule", u"5.2", None))

        self.module_course_level_select.setCurrentText("")
        self.module_course_level_select.setPlaceholderText(QCoreApplication.translate("AddModule", u"Level", None))
        self.module_name.setText(QCoreApplication.translate("AddModule", u"Module name", None))
        self.module_course_module_code.setText("")
        self.module_course_module_code.setPlaceholderText(QCoreApplication.translate("AddModule", u"Program custom module code (Optional)", None))
        ___qtablewidgetitem2 = self.locked_slots_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddModule", u"Locked Slots", None));
        self.module_add_lock_btn.setText("")
        self.module_lock_slot_select.setPlaceholderText(QCoreApplication.translate("AddModule", u"Slot", None))
        self.module_lock_day_select.setItemText(0, QCoreApplication.translate("AddModule", u"1.1", None))
        self.module_lock_day_select.setItemText(1, QCoreApplication.translate("AddModule", u"1.2", None))
        self.module_lock_day_select.setItemText(2, QCoreApplication.translate("AddModule", u"2.1", None))
        self.module_lock_day_select.setItemText(3, QCoreApplication.translate("AddModule", u"2.2", None))
        self.module_lock_day_select.setItemText(4, QCoreApplication.translate("AddModule", u"3.1", None))
        self.module_lock_day_select.setItemText(5, QCoreApplication.translate("AddModule", u"3.2", None))
        self.module_lock_day_select.setItemText(6, QCoreApplication.translate("AddModule", u"4.1", None))
        self.module_lock_day_select.setItemText(7, QCoreApplication.translate("AddModule", u"4.2", None))
        self.module_lock_day_select.setItemText(8, QCoreApplication.translate("AddModule", u"5.1", None))
        self.module_lock_day_select.setItemText(9, QCoreApplication.translate("AddModule", u"5.2", None))

        self.module_lock_day_select.setCurrentText("")
        self.module_lock_day_select.setPlaceholderText(QCoreApplication.translate("AddModule", u"Day", None))
    # retranslateUi

