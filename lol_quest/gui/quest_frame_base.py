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
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from ..utils.colors import difficulty_colors


class Ui_QuestFrame(object):
    def setupUi(self, QuestDisplayFrame):
        quest_bg = difficulty_colors[QuestDisplayFrame.quest.difficulty]["bg"]
        quest_fg = difficulty_colors[QuestDisplayFrame.quest.difficulty]["fg"]
        restriction_fg = difficulty_colors[QuestDisplayFrame.restriction.difficulty][
            "fg"
        ]

        if not QuestDisplayFrame.objectName():
            QuestDisplayFrame.setObjectName("QuestDisplayFrame")
        QuestDisplayFrame.resize(111, 49)
        QuestDisplayFrame.setMaximumHeight(50)
        QuestDisplayFrame.setStyleSheet(
            f"background-color: {quest_bg};\n" "border-radius:7px"
        )
        self.verticalLayout = QVBoxLayout(QuestDisplayFrame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.title_frame = QFrame(QuestDisplayFrame)
        self.title_frame.setObjectName("frame")
        self.title_frame.setStyleSheet(
            f"background-color: {quest_bg};\n" "border-radius:4px"
        )
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.time_label = QLabel(self.title_frame)
        self.time_label.setObjectName("time_label")
        self.time_label.setMinimumSize(QSize(35, 0))
        self.time_label.setMaximumSize(QSize(35, 16777215))
        self.time_label.setStyleSheet(
            "background-color: rgb(235, 235, 235);\n" "border-radius:5px"
        )
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setMargin(1)

        self.horizontalLayout.addWidget(self.time_label)

        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(
            f"background-color: {quest_bg};\n" "border-radius:7px\n" ""
        )
        self.title_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.title_label.setMargin(0)

        self.horizontalLayout.addWidget(self.title_label)

        self.verticalLayout.addWidget(self.title_frame)

        self.restriction_label = QLabel(QuestDisplayFrame)
        self.restriction_label.setObjectName("restriction_label")
        self.restriction_label.setStyleSheet(
            f"background-color: {restriction_fg};\n" "border-radius:4px"
        )
        self.restriction_label.setAlignment(Qt.AlignCenter)
        self.restriction_label.setMargin(2)

        self.verticalLayout.addWidget(self.restriction_label)

        self.retranslateUi(QuestDisplayFrame)

        QMetaObject.connectSlotsByName(QuestDisplayFrame)

    # setupUi

    def retranslateUi(self, QuestDisplayFrame):
        self.time_label.setText(
            QCoreApplication.translate("QuestDisplayFrame", "00:00", None)
        )
        self.title_label.setText(
            QCoreApplication.translate(
                "QuestDisplayFrame",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Kill Player X!</p></body></html>',
                None,
            )
        )
        self.restriction_label.setText(
            QCoreApplication.translate(
                "QuestDisplayFrame",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Ability 1 locked!</p></body></html>',
                None,
            )
        )
        pass

    # retranslateUi
