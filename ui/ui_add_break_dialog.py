# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_break_dialogkUgPDY.ui'
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
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_AddBreak(object):
    def setupUi(self, AddBreak):
        if not AddBreak.objectName():
            AddBreak.setObjectName(u"AddBreak")
        AddBreak.resize(465, 447)
        AddBreak.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(AddBreak)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(AddBreak)
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
        self.close_btn.setGeometry(QRect(430, 0, 35, 30))
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
        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.break_save = QPushButton(self.frame)
        self.break_save.setObjectName(u"break_save")
        self.break_save.setGeometry(QRect(350, 360, 81, 30))
        self.break_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.break_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.breaks_table = QTableWidget(self.frame)
        if (self.breaks_table.columnCount() < 1):
            self.breaks_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.breaks_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.breaks_table.setObjectName(u"breaks_table")
        self.breaks_table.setGeometry(QRect(50, 20, 381, 251))
        self.breaks_table.horizontalHeader().setDefaultSectionSize(350)
        self.break_add_btn = QPushButton(self.frame)
        self.break_add_btn.setObjectName(u"break_add_btn")
        self.break_add_btn.setGeometry(QRect(210, 360, 71, 30))
        self.break_add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.break_add_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.break_add_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.break_add_btn.setStyleSheet(u"padding: 5px;\n"
"background: #2F69B2;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.break_add_btn.setIcon(icon1)
        self.break_add_btn.setIconSize(QSize(12, 12))
        self.break_slot_select = QComboBox(self.frame)
        self.break_slot_select.setObjectName(u"break_slot_select")
        self.break_slot_select.setGeometry(QRect(50, 320, 231, 30))
        self.break_slot_select.setMinimumSize(QSize(0, 30))
        self.break_name = QLineEdit(self.frame)
        self.break_name.setObjectName(u"break_name")
        self.break_name.setGeometry(QRect(50, 280, 231, 30))
        self.break_name.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(AddBreak)

        QMetaObject.connectSlotsByName(AddBreak)
    # setupUi

    def retranslateUi(self, AddBreak):
        AddBreak.setWindowTitle(QCoreApplication.translate("AddBreak", u"Dialog", None))
        self.close_btn.setText("")
        self.break_save.setText(QCoreApplication.translate("AddBreak", u"Save", None))
        ___qtablewidgetitem = self.breaks_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddBreak", u"Breaks", None));
        self.break_add_btn.setText(QCoreApplication.translate("AddBreak", u" Add", None))
        self.break_slot_select.setPlaceholderText(QCoreApplication.translate("AddBreak", u"Select Period", None))
        self.break_name.setPlaceholderText(QCoreApplication.translate("AddBreak", u"Break name e.g (Lunch or Break, Study)", None))
    # retranslateUi

