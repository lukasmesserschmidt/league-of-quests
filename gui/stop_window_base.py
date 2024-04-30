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
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_StopWindow(object):
    def setupUi(self, stop_window):
        if not stop_window.objectName():
            stop_window.setObjectName("bg_widget")
        stop_window.resize(200, 80)
        stop_window.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.bg_widget_layout = QVBoxLayout(stop_window)
        self.bg_widget_layout.setObjectName("bg_widget_layout")
        self.bg_widget_layout.setContentsMargins(5, 5, 5, 5)
        self.bg_frame = QFrame(stop_window)
        self.bg_frame.setObjectName("bg_frame")
        self.bg_frame.setStyleSheet(
            "background-color: rgb(43, 43, 43);\n" "border-radius: 10px"
        )
        self.bg_frame.setFrameShape(QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QFrame.Raised)
        self.bg_frame_layout = QVBoxLayout(self.bg_frame)
        self.bg_frame_layout.setSpacing(4)
        self.bg_frame_layout.setObjectName("bg_frame_layout")
        self.bg_frame_layout.setContentsMargins(6, 6, 6, 6)
        self.headline_frame = QLabel(self.bg_frame)
        self.headline_frame.setObjectName("headline_frame")
        self.headline_frame.setMinimumSize(QSize(100, 30))
        self.headline_frame.setMaximumSize(QSize(16777215, 30))
        self.headline_frame.setStyleSheet(
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(36, 36, 36);\n"
            "border-radius: 8px"
        )
        self.headline_frame.setAlignment(Qt.AlignCenter)

        self.bg_frame_layout.addWidget(self.headline_frame)

        self.stop_button = QPushButton(self.bg_frame)
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setMinimumSize(QSize(60, 20))
        self.stop_button.setStyleSheet(
            "QPushButton{\n"
            "color: rgb(235, 235, 235);\n"
            "background-color: rgb(214, 21, 24);\n"
            "border-radius: 5px\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: rgb(162, 23, 25);\n"
            "}"
        )

        self.bg_frame_layout.addWidget(self.stop_button)

        self.bg_widget_layout.addWidget(self.bg_frame)

        self.retranslateUi(stop_window)

        QMetaObject.connectSlotsByName(stop_window)

    # setupUi

    def retranslateUi(self, bg_widget):
        bg_widget.setWindowTitle(
            QCoreApplication.translate("bg_widget", "League of Quests", None)
        )
        self.headline_frame.setText(
            QCoreApplication.translate("bg_widget", "Game is Running", None)
        )
        self.stop_button.setText(QCoreApplication.translate("bg_widget", "Stop", None))

    # retranslateUi
