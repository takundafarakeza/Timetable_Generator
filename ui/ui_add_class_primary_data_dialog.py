# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_class_primary_data_dialogDbaqUk.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_AddClass(object):
    def setupUi(self, AddClass):
        if not AddClass.objectName():
            AddClass.setObjectName(u"AddClass")
        AddClass.resize(620, 439)
        AddClass.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(AddClass)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(AddClass)
        self.main_container.setObjectName(u"main_container")
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.toolbar = QWidget(self.main_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMaximumSize(QSize(16777215, 30))
        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(585, 0, 33, 30))
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(10, 10))

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
        self.class_save = QPushButton(self.frame)
        self.class_save.setObjectName(u"class_save")
        self.class_save.setGeometry(QRect(520, 320, 81, 30))
        self.class_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.class_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 105, 111, 20))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.class_subject_select = QComboBox(self.frame)
        self.class_subject_select.setObjectName(u"class_subject_select")
        self.class_subject_select.setGeometry(QRect(30, 55, 231, 30))
        self.class_subject_select.setMinimumSize(QSize(0, 30))
        self.class_subjects_table = QTableWidget(self.frame)
        if (self.class_subjects_table.columnCount() < 1):
            self.class_subjects_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.class_subjects_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.class_subjects_table.setObjectName(u"class_subjects_table")
        self.class_subjects_table.setGeometry(QRect(310, 20, 281, 281))
        self.class_subjects_table.horizontalHeader().setDefaultSectionSize(250)
        self.slots_per_cycle = QSpinBox(self.frame)
        self.slots_per_cycle.setObjectName(u"slots_per_cycle")
        self.slots_per_cycle.setGeometry(QRect(30, 130, 111, 30))
        self.slots_per_cycle.setMinimumSize(QSize(0, 30))
        self.slots_per_cycle.setMinimum(0)
        self.title_2 = QLabel(self.frame)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(160, 105, 91, 20))
        self.title_2.setFont(font1)
        self.title_2.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.class_add_subject_btn = QPushButton(self.frame)
        self.class_add_subject_btn.setObjectName(u"class_add_subject_btn")
        self.class_add_subject_btn.setGeometry(QRect(190, 205, 71, 30))
        self.class_add_subject_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.class_add_subject_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.class_add_subject_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.class_add_subject_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.class_add_subject_btn.setIcon(icon1)
        self.class_add_subject_btn.setIconSize(QSize(12, 12))
        self.slots_per_day = QSpinBox(self.frame)
        self.slots_per_day.setObjectName(u"slots_per_day")
        self.slots_per_day.setGeometry(QRect(160, 130, 101, 30))
        self.slots_per_day.setMinimumSize(QSize(0, 30))
        self.slots_per_day.setMinimum(0)
        self.class_name = QLabel(self.frame)
        self.class_name.setObjectName(u"class_name")
        self.class_name.setGeometry(QRect(30, 20, 241, 21))

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(AddClass)

        QMetaObject.connectSlotsByName(AddClass)
    # setupUi

    def retranslateUi(self, AddClass):
        AddClass.setWindowTitle(QCoreApplication.translate("AddClass", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("AddClass", u"Class Subjects", None))
        self.class_save.setText(QCoreApplication.translate("AddClass", u"Save", None))
        self.title.setText(QCoreApplication.translate("AddClass", u"Periods Per Cycle", None))
        self.class_subject_select.setPlaceholderText(QCoreApplication.translate("AddClass", u"Select Subject", None))
        ___qtablewidgetitem = self.class_subjects_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddClass", u"Subject", None));
        self.title_2.setText(QCoreApplication.translate("AddClass", u"Periods Per Day", None))
        self.class_add_subject_btn.setText(QCoreApplication.translate("AddClass", u" Add", None))
        self.class_name.setText(QCoreApplication.translate("AddClass", u"Class Name", None))
    # retranslateUi

