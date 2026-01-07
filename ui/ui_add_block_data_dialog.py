# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_block_data_dialoggsfWiR.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_AddBlock(object):
    def setupUi(self, AddBlock):
        if not AddBlock.objectName():
            AddBlock.setObjectName(u"AddBlock")
        AddBlock.resize(694, 526)
        AddBlock.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(AddBlock)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(AddBlock)
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
        self.block_save = QPushButton(self.frame)
        self.block_save.setObjectName(u"block_save")
        self.block_save.setGeometry(QRect(590, 410, 81, 30))
        self.block_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.block_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.subject_add_btn = QPushButton(self.frame)
        self.subject_add_btn.setObjectName(u"subject_add_btn")
        self.subject_add_btn.setGeometry(QRect(280, 360, 30, 30))
        self.subject_add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.subject_add_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.subject_add_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.subject_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.subject_add_btn.setIcon(icon1)
        self.subject_add_btn.setIconSize(QSize(14, 14))
        self.class_select = QComboBox(self.frame)
        self.class_select.setObjectName(u"class_select")
        self.class_select.setGeometry(QRect(380, 360, 211, 30))
        self.class_select.setMinimumSize(QSize(0, 30))
        self.class_select.setEditable(True)
        self.classes_table = QTableWidget(self.frame)
        if (self.classes_table.columnCount() < 1):
            self.classes_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.classes_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.classes_table.setObjectName(u"classes_table")
        self.classes_table.setGeometry(QRect(370, 30, 281, 261))
        self.classes_table.horizontalHeader().setDefaultSectionSize(260)
        self.subjects_table = QTableWidget(self.frame)
        if (self.subjects_table.columnCount() < 1):
            self.subjects_table.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.subjects_table.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.subjects_table.setObjectName(u"subjects_table")
        self.subjects_table.setGeometry(QRect(30, 30, 281, 231))
        self.subjects_table.horizontalHeader().setDefaultSectionSize(260)
        self.class_add_btn = QPushButton(self.frame)
        self.class_add_btn.setObjectName(u"class_add_btn")
        self.class_add_btn.setGeometry(QRect(610, 360, 30, 30))
        self.class_add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.class_add_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.class_add_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.class_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.class_add_btn.setIcon(icon1)
        self.class_add_btn.setIconSize(QSize(14, 14))
        self.teacher_select = QComboBox(self.frame)
        self.teacher_select.setObjectName(u"teacher_select")
        self.teacher_select.setGeometry(QRect(30, 360, 231, 30))
        self.teacher_select.setMinimumSize(QSize(0, 30))
        self.teacher_select.setEditable(True)
        self.venue_select = QComboBox(self.frame)
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.addItem("")
        self.venue_select.setObjectName(u"venue_select")
        self.venue_select.setGeometry(QRect(30, 320, 231, 30))
        self.venue_select.setEditable(True)
        self.block_name = QLabel(self.frame)
        self.block_name.setObjectName(u"block_name")
        self.block_name.setGeometry(QRect(30, 0, 261, 21))
        self.subject_select = QComboBox(self.frame)
        self.subject_select.setObjectName(u"subject_select")
        self.subject_select.setGeometry(QRect(30, 280, 231, 30))
        self.subject_select.setMinimumSize(QSize(0, 30))
        self.subject_select.setEditable(True)

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(AddBlock)

        QMetaObject.connectSlotsByName(AddBlock)
    # setupUi

    def retranslateUi(self, AddBlock):
        AddBlock.setWindowTitle(QCoreApplication.translate("AddBlock", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("AddBlock", u"Block Classes, Subjects and Venues", None))
        self.block_save.setText(QCoreApplication.translate("AddBlock", u"Close", None))
        self.subject_add_btn.setText("")
        self.class_select.setPlaceholderText("")
        ___qtablewidgetitem = self.classes_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddBlock", u"Classes", None));
        ___qtablewidgetitem1 = self.subjects_table.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddBlock", u"Subjects", None));
        self.class_add_btn.setText("")
        self.teacher_select.setPlaceholderText(QCoreApplication.translate("AddBlock", u"Select Course", None))
        self.venue_select.setItemText(0, QCoreApplication.translate("AddBlock", u"1.1", None))
        self.venue_select.setItemText(1, QCoreApplication.translate("AddBlock", u"1.2", None))
        self.venue_select.setItemText(2, QCoreApplication.translate("AddBlock", u"2.1", None))
        self.venue_select.setItemText(3, QCoreApplication.translate("AddBlock", u"2.2", None))
        self.venue_select.setItemText(4, QCoreApplication.translate("AddBlock", u"3.1", None))
        self.venue_select.setItemText(5, QCoreApplication.translate("AddBlock", u"3.2", None))
        self.venue_select.setItemText(6, QCoreApplication.translate("AddBlock", u"4.1", None))
        self.venue_select.setItemText(7, QCoreApplication.translate("AddBlock", u"4.2", None))
        self.venue_select.setItemText(8, QCoreApplication.translate("AddBlock", u"5.1", None))
        self.venue_select.setItemText(9, QCoreApplication.translate("AddBlock", u"5.2", None))

        self.venue_select.setCurrentText("")
        self.venue_select.setPlaceholderText(QCoreApplication.translate("AddBlock", u"Level", None))
        self.block_name.setText(QCoreApplication.translate("AddBlock", u"Block name", None))
        self.subject_select.setPlaceholderText("")
    # retranslateUi

