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
    QFrame,
    QGridLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from ..manager.settings_manager import Settings


class Ui_QuestDisplay(object):
    def setupUi(self, QuestDisplay):
        if not QuestDisplay.objectName():
            QuestDisplay.setObjectName("QuestDisplay")
        QuestDisplay.resize(250, 280)
        self.base_layout = QVBoxLayout(QuestDisplay)
        self.base_layout.setSpacing(3)
        self.base_layout.setObjectName("base_layout")
        self.base_layout.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(QuestDisplay)
        self.info_frame.setObjectName("info_frame")
        self.info_frame.setMaximumSize(QSize(16777215, 30))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.info_frame.setStyleSheet(
            "background-color: rgb(51, 51, 51);\n" "border-radius:7px"
        )
        self.info_frame_layout = QGridLayout(self.info_frame)
        self.info_frame_layout.setObjectName("info_frame_layout")
        self.info_frame_layout.setHorizontalSpacing(3)
        self.info_frame_layout.setVerticalSpacing(0)
        self.info_frame_layout.setContentsMargins(3, 3, 3, 3)
        self.quest_count_title_label = QLabel(self.info_frame)
        self.quest_count_title_label.setObjectName("quest_count_title_label")
        self.quest_count_title_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.quest_count_title_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.info_frame_layout.addWidget(self.quest_count_title_label, 1, 0, 1, 1)

        self.quest_count_label = QLabel(self.info_frame)
        self.quest_count_label.setObjectName("quest_count_label")
        self.quest_count_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.quest_count_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.info_frame_layout.addWidget(self.quest_count_label, 1, 1, 1, 1)

        self.next_quest_time_label = QLabel(self.info_frame)
        self.next_quest_time_label.setObjectName("next_quest_time_label")
        self.next_quest_time_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.next_quest_time_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.info_frame_layout.addWidget(self.next_quest_time_label, 0, 1, 1, 1)

        self.next_quest_title_label = QLabel(self.info_frame)
        self.next_quest_title_label.setObjectName("next_quest_title_label")
        self.next_quest_title_label.setStyleSheet("color: rgb(235, 235, 235)")
        self.next_quest_title_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.info_frame_layout.addWidget(self.next_quest_title_label, 0, 0, 1, 1)

        self.base_layout.addWidget(self.info_frame, 0, Qt.AlignRight | Qt.AlignTop)

        self.quest_frame = QFrame(QuestDisplay)
        self.quest_frame.setObjectName("quest_frame")
        self.quest_frame.setFrameShape(QFrame.NoFrame)
        self.quest_frame.setFrameShadow(QFrame.Raised)
        self.quest_frame_layout = QVBoxLayout(self.quest_frame)
        self.quest_frame_layout.setSpacing(3)
        self.quest_frame_layout.setObjectName("quest_frame_layout")
        self.quest_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.base_layout.addWidget(self.quest_frame, 1, Qt.AlignTop)

        self.retranslateUi(QuestDisplay)

        QMetaObject.connectSlotsByName(QuestDisplay)

    # setupUi

    def retranslateUi(self, QuestDisplay):
        self.quest_count_title_label.setText(
            QCoreApplication.translate("QuestDisplay", "Quests:", None)
        )
        self.quest_count_label.setText(
            QCoreApplication.translate(
                "QuestDisplay", f"0/{Settings.get_quest_limit()}", None
            )
        )
        self.next_quest_time_label.setText(
            QCoreApplication.translate("QuestDisplay", "00:00", None)
        )
        self.next_quest_title_label.setText(
            QCoreApplication.translate("QuestDisplay", "Next Quest in:", None)
        )
        pass

    # retranslateUi
