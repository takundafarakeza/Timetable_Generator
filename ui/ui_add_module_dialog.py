# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_module_dialogUEgSXv.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_AddModule(object):
    def setupUi(self, AddModule):
        if not AddModule.objectName():
            AddModule.setObjectName(u"AddModule")
        AddModule.resize(540, 403)
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
        self.horizontalLayout_2 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(505, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(30, 30))
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(10, 10))

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.toolbar)

        self.container = QWidget(self.main_container)
        self.container.setObjectName(u"container")
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
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
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 315))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.session_length = QSpinBox(self.frame_2)
        self.session_length.setObjectName(u"session_length")
        self.session_length.setGeometry(QRect(10, 280, 101, 30))
        self.session_length.setMinimumSize(QSize(0, 30))
        self.session_length.setMinimum(1)
        self.title = QLabel(self.frame_2)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 180, 101, 20))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.module_name = QLineEdit(self.frame_2)
        self.module_name.setObjectName(u"module_name")
        self.module_name.setGeometry(QRect(10, 20, 231, 30))
        self.module_name.setMinimumSize(QSize(0, 30))
        self.module_lecturer = QComboBox(self.frame_2)
        self.module_lecturer.setObjectName(u"module_lecturer")
        self.module_lecturer.setGeometry(QRect(10, 130, 181, 30))
        self.module_lecturer.setMinimumSize(QSize(0, 30))
        self.title_3 = QLabel(self.frame_2)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(10, 250, 141, 20))
        self.title_3.setFont(font1)
        self.title_3.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.title_2 = QLabel(self.frame_2)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(120, 180, 121, 20))
        self.title_2.setFont(font1)
        self.title_2.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.slots_per_day = QSpinBox(self.frame_2)
        self.slots_per_day.setObjectName(u"slots_per_day")
        self.slots_per_day.setGeometry(QRect(120, 210, 111, 30))
        self.slots_per_day.setMinimumSize(QSize(0, 30))
        self.slots_per_day.setMinimum(0)
        self.module_save = QPushButton(self.frame_2)
        self.module_save.setObjectName(u"module_save")
        self.module_save.setGeometry(QRect(160, 280, 81, 30))
        self.module_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.module_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.module_code = QLineEdit(self.frame_2)
        self.module_code.setObjectName(u"module_code")
        self.module_code.setGeometry(QRect(10, 75, 121, 30))
        self.module_code.setMinimumSize(QSize(0, 30))
        self.slots_per_cycle = QSpinBox(self.frame_2)
        self.slots_per_cycle.setObjectName(u"slots_per_cycle")
        self.slots_per_cycle.setGeometry(QRect(10, 210, 101, 30))
        self.slots_per_cycle.setMinimumSize(QSize(0, 30))
        self.slots_per_cycle.setMinimum(0)

        self.horizontalLayout.addWidget(self.frame_2)

        self.lock_frame = QFrame(self.frame)
        self.lock_frame.setObjectName(u"lock_frame")
        self.lock_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lock_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.lock_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.locked_slots_table = QTableWidget(self.lock_frame)
        if (self.locked_slots_table.columnCount() < 1):
            self.locked_slots_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.locked_slots_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.locked_slots_table.setObjectName(u"locked_slots_table")
        self.locked_slots_table.horizontalHeader().setDefaultSectionSize(230)

        self.verticalLayout_4.addWidget(self.locked_slots_table)

        self.frame_4 = QFrame(self.lock_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.module_lock_btn = QPushButton(self.frame_4)
        self.module_lock_btn.setObjectName(u"module_lock_btn")
        self.module_lock_btn.setGeometry(QRect(210, 60, 30, 30))
        self.module_lock_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.module_lock_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.module_lock_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.module_lock_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.module_lock_btn.setIcon(icon1)
        self.module_lock_btn.setIconSize(QSize(14, 14))
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
        self.max_locks_txt = QLabel(self.frame_4)
        self.max_locks_txt.setObjectName(u"max_locks_txt")
        self.max_locks_txt.setGeometry(QRect(0, 0, 161, 16))

        self.verticalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.lock_frame)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)

        QWidget.setTabOrder(self.module_save, self.module_name)
        QWidget.setTabOrder(self.module_name, self.module_code)
        QWidget.setTabOrder(self.module_code, self.slots_per_cycle)
        QWidget.setTabOrder(self.slots_per_cycle, self.slots_per_day)
        QWidget.setTabOrder(self.slots_per_day, self.session_length)
        QWidget.setTabOrder(self.session_length, self.module_lecturer)
        QWidget.setTabOrder(self.module_lecturer, self.locked_slots_table)

        self.retranslateUi(AddModule)

        QMetaObject.connectSlotsByName(AddModule)
    # setupUi

    def retranslateUi(self, AddModule):
        AddModule.setWindowTitle(QCoreApplication.translate("AddModule", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("AddModule", u"Module", None))
        self.title.setText(QCoreApplication.translate("AddModule", u"Sessions Per Cycle", None))
        self.module_name.setPlaceholderText(QCoreApplication.translate("AddModule", u"Module name", None))
        self.module_lecturer.setPlaceholderText(QCoreApplication.translate("AddModule", u"Lecturer", None))
        self.title_3.setText(QCoreApplication.translate("AddModule", u"Session length (In periods)", None))
        self.title_2.setText(QCoreApplication.translate("AddModule", u"Max Sessions Per Day", None))
        self.module_save.setText(QCoreApplication.translate("AddModule", u"Save", None))
        self.module_code.setPlaceholderText(QCoreApplication.translate("AddModule", u"Module code", None))
        ___qtablewidgetitem = self.locked_slots_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddModule", u"Locked Slots", None));
        self.module_lock_btn.setText("")
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
        self.max_locks_txt.setText(QCoreApplication.translate("AddModule", u"Max locks:", None))
    # retranslateUi

