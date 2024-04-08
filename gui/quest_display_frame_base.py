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
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_QuestDisplayFrame(object):
    def setupUi(self, QuestDisplayFrame):
        if not QuestDisplayFrame.objectName():
            QuestDisplayFrame.setObjectName("QuestDisplayFrame")
        QuestDisplayFrame.resize(195, 84)
        QuestDisplayFrame.setStyleSheet(
            "background-color: rgb(66, 164, 89);\n" "border-radius:12px\n" "\n" ""
        )
        self.verticalLayout = QVBoxLayout(QuestDisplayFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(QuestDisplayFrame)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(
            "background-color: rgb(62, 155, 84);\n" "border-radius:7px\n" "\n" ""
        )
        self.title_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.title_label.setMargin(5)

        self.verticalLayout.addWidget(self.title_label)

        self.time_label = QLabel(QuestDisplayFrame)
        self.time_label.setObjectName("time_label")
        self.time_label.setMaximumSize(QSize(40, 16777215))
        self.time_label.setStyleSheet(
            "background-color: rgb(200, 200, 200);\n" "border-radius:5px\n" "\n" ""
        )
        self.time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.time_label)

        self.restriction_label = QLabel(QuestDisplayFrame)
        self.restriction_label.setObjectName("restriction_label")
        self.restriction_label.setStyleSheet(
            "background-color: rgb(62, 155, 84);\n" "border-radius:7px\n" "\n" ""
        )
        self.restriction_label.setMargin(5)

        self.verticalLayout.addWidget(self.restriction_label)

        self.retranslateUi(QuestDisplayFrame)

        QMetaObject.connectSlotsByName(QuestDisplayFrame)

    # setupUi

    def retranslateUi(self, QuestDisplayFrame):
        QuestDisplayFrame.setWindowTitle(
            QCoreApplication.translate("QuestDisplayFrame", "Frame", None)
        )
        self.title_label.setText(
            QCoreApplication.translate(
                "QuestDisplayFrame",
                "<html><head/><body><p>Kill Player X!</p></body></html>",
                None,
            )
        )
        self.time_label.setText(
            QCoreApplication.translate("QuestDisplayFrame", "00:00", None)
        )
        self.restriction_label.setText(
            QCoreApplication.translate(
                "QuestDisplayFrame",
                "<html><head/><body><p>Ability 1 locked!</p></body></html>",
                None,
            )
        )

    # retranslateUi
