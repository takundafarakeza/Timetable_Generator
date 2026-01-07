# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_project_dialogOUBZpE.ui'
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_Export(object):
    def setupUi(self, Export):
        if not Export.objectName():
            Export.setObjectName(u"Export")
        Export.resize(316, 298)
        Export.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(Export)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(Export)
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
        self.close_btn.setGeometry(QRect(280, 0, 35, 30))
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
        self.timetable_export = QPushButton(self.frame)
        self.timetable_export.setObjectName(u"timetable_export")
        self.timetable_export.setGeometry(QRect(200, 210, 81, 30))
        self.timetable_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.timetable_export.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(110, 210, 71, 30))
        self.cancel_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.cancel_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cancel_btn.setStyleSheet(u"padding: 5px;\n"
"background: #D3D4D6;\n"
"color: #414141;\n"
"border-radius: 3px;")
        self.cancel_btn.setIconSize(QSize(12, 12))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 141, 31))
        self.sub_title_2 = QLabel(self.frame)
        self.sub_title_2.setObjectName(u"sub_title_2")
        self.sub_title_2.setGeometry(QRect(30, 80, 160, 20))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.sub_title_2.setFont(font)
        self.sub_title_2.setStyleSheet(u"color: rgb(129, 129, 129);")
        self.timetable_filter = QComboBox(self.frame)
        self.timetable_filter.setObjectName(u"timetable_filter")
        self.timetable_filter.setGeometry(QRect(30, 120, 251, 30))
        self.timetable_filter.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(Export)

        QMetaObject.connectSlotsByName(Export)
    # setupUi

    def retranslateUi(self, Export):
        Export.setWindowTitle(QCoreApplication.translate("Export", u"Dialog", None))
        self.close_btn.setText("")
        self.timetable_export.setText(QCoreApplication.translate("Export", u"Export", None))
        self.cancel_btn.setText(QCoreApplication.translate("Export", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Export", u"Export Excel Timetable", None))
        self.sub_title_2.setText(QCoreApplication.translate("Export", u"Filter", None))
        self.timetable_filter.setPlaceholderText("")
    # retranslateUi

