from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFrame,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from .line_edit_base import LineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        MainWindow.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.main_window_centralwidget = QWidget(MainWindow)
        self.main_window_centralwidget.setObjectName("main_window_centralwidget")
        self.main_window_layout = QVBoxLayout(self.main_window_centralwidget)
        self.main_window_layout.setSpacing(10)
        self.main_window_layout.setObjectName("main_window_layout")
        self.bg_frame = QFrame(self.main_window_centralwidget)
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(
            "background-color: rgb(43, 43, 43);\n" "border-radius: 10px"
        )
        self.bg_frame.setFrameShape(QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bg_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quest_settings_base_layout = QVBoxLayout()
        self.quest_settings_base_layout.setSpacing(2)
        self.quest_settings_base_layout.setObjectName("quest_settings_base_layout")
        self.quest_settings_label = QLabel(self.bg_frame)
        self.quest_settings_label.setObjectName("quest_settings_label")
        self.quest_settings_label.setMinimumSize(QSize(0, 30))
        self.quest_settings_label.setMaximumSize(QSize(16777215, 30))
        self.quest_settings_label.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(36, 36, 36);\n"
            "border-radius: 10px"
        )
        self.quest_settings_label.setAlignment(Qt.AlignCenter)

        self.quest_settings_base_layout.addWidget(self.quest_settings_label)

        self.quest_settings_frame = QFrame(self.bg_frame)
        self.quest_settings_frame.setObjectName("quest_settings_frame")
        self.quest_settings_frame.setStyleSheet(
            "background-color: rgb(51, 51, 51);\n" "border-radius: 10px"
        )
        self.quest_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.quest_settings_frame.setFrameShadow(QFrame.Raised)
        self.quest_settings_frame_layout = QGridLayout(self.quest_settings_frame)
        self.quest_settings_frame_layout.setObjectName("quest_settings_frame_layout")
        self.quest_after_time_label = QLabel(self.quest_settings_frame)
        self.quest_after_time_label.setObjectName("quest_after_time_label")
        self.quest_after_time_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.quest_after_time_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.quest_settings_frame_layout.addWidget(
            self.quest_after_time_label, 5, 0, 1, 1
        )

        self.quest_on_death_checkbox = QCheckBox(self.quest_settings_frame)
        self.quest_on_death_checkbox.setObjectName("quest_on_death_checkbox")
        self.quest_on_death_checkbox.setChecked(True)

        self.quest_settings_frame_layout.addWidget(
            self.quest_on_death_checkbox, 2, 1, 1, 1, Qt.AlignHCenter
        )

        self.quest_after_time_checkbox = QCheckBox(self.quest_settings_frame)
        self.quest_after_time_checkbox.setObjectName("quest_after_time_checkbox")

        self.quest_settings_frame_layout.addWidget(
            self.quest_after_time_checkbox, 5, 1, 1, 1, Qt.AlignHCenter
        )

        self.quest_on_death_label = QLabel(self.quest_settings_frame)
        self.quest_on_death_label.setObjectName("quest_on_death_label")
        self.quest_on_death_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.quest_on_death_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.quest_settings_frame_layout.addWidget(
            self.quest_on_death_label, 2, 0, 1, 1
        )

        self.label_10 = QLabel(self.quest_settings_frame)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color: rgb(235, 235, 235)")
        self.label_10.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.quest_settings_frame_layout.addWidget(self.label_10, 7, 0, 1, 1)

        self.quest_after_time_lineedit = LineEdit(self.quest_settings_frame, "s", 36000)
        self.quest_after_time_lineedit.setObjectName("quest_after_time_lineedit")
        self.quest_after_time_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_settings_frame_layout.addWidget(
            self.quest_after_time_lineedit, 5, 2, 1, 1
        )

        self.quest_duration_lineedit = LineEdit(self.quest_settings_frame, "s", 36000)
        self.quest_duration_lineedit.setObjectName("quest_duration_lineedit")
        self.quest_duration_lineedit.setEnabled(True)
        self.quest_duration_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_settings_frame_layout.addWidget(
            self.quest_duration_lineedit, 7, 2, 1, 1
        )

        self.quest_settings_base_layout.addWidget(self.quest_settings_frame)

        self.verticalLayout_2.addLayout(self.quest_settings_base_layout)

        self.quest_rarity_settings_base_layout = QVBoxLayout()
        self.quest_rarity_settings_base_layout.setSpacing(2)
        self.quest_rarity_settings_base_layout.setObjectName(
            "quest_rarity_settings_base_layout"
        )
        self.quest_rarity_settings_label = QLabel(self.bg_frame)
        self.quest_rarity_settings_label.setObjectName("quest_rarity_settings_label")
        self.quest_rarity_settings_label.setMinimumSize(QSize(0, 30))
        self.quest_rarity_settings_label.setMaximumSize(QSize(16777215, 30))
        self.quest_rarity_settings_label.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(36, 36, 36);\n"
            "border-radius: 10px"
        )
        self.quest_rarity_settings_label.setAlignment(Qt.AlignCenter)

        self.quest_rarity_settings_base_layout.addWidget(
            self.quest_rarity_settings_label
        )

        self.quest_rarity_settings_frame = QFrame(self.bg_frame)
        self.quest_rarity_settings_frame.setObjectName("quest_rarity_settings_frame")
        self.quest_rarity_settings_frame.setStyleSheet(
            "background-color: rgb(51, 51, 51);\n" "border-radius: 10px"
        )
        self.quest_rarity_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.quest_rarity_settings_frame.setFrameShadow(QFrame.Raised)
        self.quest_rarity_settings_frame_layout = QGridLayout(
            self.quest_rarity_settings_frame
        )
        self.quest_rarity_settings_frame_layout.setObjectName(
            "quest_rarity_settings_frame_layout"
        )
        self.mid_restriction_lineedit = LineEdit(
            self.quest_rarity_settings_frame, "%", 100
        )
        self.mid_restriction_lineedit.setObjectName("mid_restriction_lineedit")
        self.mid_restriction_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_rarity_settings_frame_layout.addWidget(
            self.mid_restriction_lineedit, 2, 3, 1, 1
        )

        self.restriction_label = QLabel(self.quest_rarity_settings_frame)
        self.restriction_label.setObjectName("restriction_label")
        self.restriction_label.setStyleSheet("color: rgb(235, 235, 235)")

        self.quest_rarity_settings_frame_layout.addWidget(
            self.restriction_label, 0, 3, 1, 1
        )

        self.quest_label = QLabel(self.quest_rarity_settings_frame)
        self.quest_label.setObjectName("quest_label")
        self.quest_label.setStyleSheet("color: rgb(235, 235, 235)")

        self.quest_rarity_settings_frame_layout.addWidget(self.quest_label, 0, 2, 1, 1)

        self.hard_label = QLabel(self.quest_rarity_settings_frame)
        self.hard_label.setObjectName("hard_label")
        self.hard_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.hard_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.quest_rarity_settings_frame_layout.addWidget(self.hard_label, 3, 1, 1, 1)

        self.easy_quest_lineedit = LineEdit(self.quest_rarity_settings_frame, "%", 100)
        self.easy_quest_lineedit.setObjectName("easy_quest_lineedit")
        self.easy_quest_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_rarity_settings_frame_layout.addWidget(
            self.easy_quest_lineedit, 1, 2, 1, 1
        )

        self.mid_label = QLabel(self.quest_rarity_settings_frame)
        self.mid_label.setObjectName("mid_label")
        self.mid_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.mid_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.quest_rarity_settings_frame_layout.addWidget(self.mid_label, 2, 1, 1, 1)

        self.easy_label = QLabel(self.quest_rarity_settings_frame)
        self.easy_label.setObjectName("easy_label")
        self.easy_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.easy_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.quest_rarity_settings_frame_layout.addWidget(self.easy_label, 1, 1, 1, 1)

        self.easy_restriction_lineedit = LineEdit(
            self.quest_rarity_settings_frame, "%", 100
        )
        self.easy_restriction_lineedit.setObjectName("easy_restriction_lineedit")
        self.easy_restriction_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_rarity_settings_frame_layout.addWidget(
            self.easy_restriction_lineedit, 1, 3, 1, 1
        )

        self.mid_quest_lineedit = LineEdit(self.quest_rarity_settings_frame, "%", 100)
        self.mid_quest_lineedit.setObjectName("mid_quest_lineedit")
        self.mid_quest_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_rarity_settings_frame_layout.addWidget(
            self.mid_quest_lineedit, 2, 2, 1, 1
        )

        self.hard_restriction_lineedit = LineEdit(
            self.quest_rarity_settings_frame, "%", 100
        )
        self.hard_restriction_lineedit.setObjectName("hard_restriction_lineedit")
        self.hard_restriction_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_rarity_settings_frame_layout.addWidget(
            self.hard_restriction_lineedit, 3, 3, 1, 1
        )

        self.hard_quest_lineedit = LineEdit(self.quest_rarity_settings_frame, "%", 100)
        self.hard_quest_lineedit.setObjectName("hard_quest_lineedit")
        self.hard_quest_lineedit.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(52, 54, 56);\n"
            "border: 2px solid rgb(86, 91, 94);\n"
            "border-radius: 5px"
        )

        self.quest_rarity_settings_frame_layout.addWidget(
            self.hard_quest_lineedit, 3, 2, 1, 1
        )

        self.placeholder_lineedit = QLineEdit(self.quest_rarity_settings_frame)
        self.placeholder_lineedit.setObjectName("placeholder_lineedit")
        self.placeholder_lineedit.setEnabled(False)
        self.placeholder_lineedit.setMaximumSize(QSize(10, 10))
        self.placeholder_lineedit.setStyleSheet("")

        self.quest_rarity_settings_frame_layout.addWidget(
            self.placeholder_lineedit, 0, 1, 1, 1
        )

        self.quest_rarity_settings_base_layout.addWidget(
            self.quest_rarity_settings_frame
        )

        self.verticalLayout_2.addLayout(self.quest_rarity_settings_base_layout)

        self.main_window_layout.addWidget(self.bg_frame)

        self.start_button = QPushButton(self.main_window_centralwidget)
        self.start_button.setObjectName("start_button")
        self.start_button.setMinimumSize(QSize(60, 20))
        self.start_button.setMaximumSize(QSize(60, 16777215))
        self.start_button.setStyleSheet(
            "QPushButton{\n"
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(31, 106, 165);\n"
            "border-radius: 5px\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: rgb(20, 72, 112);\n"
            "}"
        )

        self.main_window_layout.addWidget(self.start_button, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.main_window_centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "League of Quests", None)
        )
        self.quest_settings_label.setText(
            QCoreApplication.translate("MainWindow", "Quest Settings", None)
        )
        self.quest_after_time_label.setText(
            QCoreApplication.translate("MainWindow", "Get quest every x seconds", None)
        )
        self.quest_on_death_checkbox.setText("")
        self.quest_after_time_checkbox.setText("")
        self.quest_on_death_label.setText(
            QCoreApplication.translate("MainWindow", "Get quest on death", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Quest duration in seconds", None)
        )
        self.quest_after_time_lineedit.setText(
            QCoreApplication.translate("MainWindow", "240s", None)
        )
        self.quest_after_time_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "seconds", None)
        )
        self.quest_duration_lineedit.setText(
            QCoreApplication.translate("MainWindow", "360s", None)
        )
        self.quest_duration_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "seconds", None)
        )
        self.quest_rarity_settings_label.setText(
            QCoreApplication.translate("MainWindow", "Quest Rarity Settings", None)
        )
        self.mid_restriction_lineedit.setText(
            QCoreApplication.translate("MainWindow", "30%", None)
        )
        self.mid_restriction_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.restriction_label.setText(
            QCoreApplication.translate("MainWindow", "Restriction", None)
        )
        self.quest_label.setText(
            QCoreApplication.translate("MainWindow", "Quest", None)
        )
        self.hard_label.setText(QCoreApplication.translate("MainWindow", "Hard", None))
        self.easy_quest_lineedit.setText(
            QCoreApplication.translate("MainWindow", "60%", None)
        )
        self.easy_quest_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.mid_label.setText(QCoreApplication.translate("MainWindow", "Mid", None))
        self.easy_label.setText(QCoreApplication.translate("MainWindow", "Easy", None))
        self.easy_restriction_lineedit.setText(
            QCoreApplication.translate("MainWindow", "60%", None)
        )
        self.easy_restriction_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.mid_quest_lineedit.setText(
            QCoreApplication.translate("MainWindow", "30%", None)
        )
        self.mid_quest_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.hard_restriction_lineedit.setText(
            QCoreApplication.translate("MainWindow", "10%", None)
        )
        self.hard_restriction_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.hard_quest_lineedit.setText(
            QCoreApplication.translate("MainWindow", "10%", None)
        )
        self.hard_quest_lineedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.placeholder_lineedit.setText("")
        self.start_button.setText(
            QCoreApplication.translate("MainWindow", "Start", None)
        )

    # retranslateUi
