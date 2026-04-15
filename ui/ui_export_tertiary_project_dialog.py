# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_tertiary_project_dialogSjObuM.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from widgets.widgets import CheckListFilter
import icons_rc

class Ui_Export(object):
    def setupUi(self, Export):
        if not Export.objectName():
            Export.setObjectName(u"Export")
        Export.resize(762, 424)
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
        self.toolbar.setMinimumSize(QSize(0, 30))
        self.toolbar.setMaximumSize(QSize(16777215, 30))
        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(730, 0, 30, 30))
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(10, 10))
        self.label = QLabel(self.toolbar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 0, 141, 31))

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
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sub_title_2 = QLabel(self.frame)
        self.sub_title_2.setObjectName(u"sub_title_2")
        self.sub_title_2.setMinimumSize(QSize(0, 30))
        self.sub_title_2.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.sub_title_2.setFont(font)
        self.sub_title_2.setStyleSheet(u"color: rgb(129, 129, 129);")

        self.verticalLayout_4.addWidget(self.sub_title_2)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.courses_checklist = CheckListFilter(self.widget_2)
        self.courses_checklist.setObjectName(u"courses_checklist")
        self.verticalLayout_5 = QVBoxLayout(self.courses_checklist)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout.addWidget(self.courses_checklist)

        self.lecturers_checklist = CheckListFilter(self.widget_2)
        self.lecturers_checklist.setObjectName(u"lecturers_checklist")
        self.verticalLayout_7 = QVBoxLayout(self.lecturers_checklist)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout.addWidget(self.lecturers_checklist)

        self.venues_checklist = CheckListFilter(self.widget_2)
        self.venues_checklist.setObjectName(u"venues_checklist")
        self.verticalLayout_6 = QVBoxLayout(self.venues_checklist)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout.addWidget(self.venues_checklist)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.timetable_export = QPushButton(self.widget)
        self.timetable_export.setObjectName(u"timetable_export")
        self.timetable_export.setGeometry(QRect(670, 0, 81, 30))
        self.timetable_export.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.timetable_export.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.cancel_btn = QPushButton(self.widget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(580, 0, 71, 30))
        self.cancel_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.cancel_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cancel_btn.setStyleSheet(u"padding: 5px;\n"
"background: #D3D4D6;\n"
"color: #414141;\n"
"border-radius: 3px;")
        self.cancel_btn.setIconSize(QSize(12, 12))
        self.clear_btn = QPushButton(self.widget)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(10, 0, 131, 30))
        self.clear_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clear_btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.clear_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.clear_btn.setStyleSheet(u"padding: 5px;\n"
"background: #D3D4D6;\n"
"color: #414141;\n"
"border-radius: 3px;")
        self.clear_btn.setIconSize(QSize(12, 12))
        self.export_codes = QCheckBox(self.widget)
        self.export_codes.setObjectName(u"export_codes")
        self.export_codes.setGeometry(QRect(170, 0, 171, 31))

        self.verticalLayout_4.addWidget(self.widget)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(Export)

        QMetaObject.connectSlotsByName(Export)
    # setupUi

    def retranslateUi(self, Export):
        Export.setWindowTitle(QCoreApplication.translate("Export", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("Export", u"Export Excel Timetable", None))
        self.sub_title_2.setText(QCoreApplication.translate("Export", u"   Filter", None))
        self.timetable_export.setText(QCoreApplication.translate("Export", u"Export", None))
        self.cancel_btn.setText(QCoreApplication.translate("Export", u"Cancel", None))
        self.clear_btn.setText(QCoreApplication.translate("Export", u"Clear Filters", None))
        self.export_codes.setText(QCoreApplication.translate("Export", u"Export modules using codes", None))
    # retranslateUi

