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
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QLabel,
)


class Ui_QuestDisplay(object):
    def setupUi(self, QuestDisplay):
        if not QuestDisplay.objectName():
            QuestDisplay.setObjectName("QuestDisplay")
        QuestDisplay.resize(250, 300)
        self.display_vertical_Layout = QVBoxLayout(QuestDisplay)
        self.display_vertical_Layout.setSpacing(0)
        self.display_vertical_Layout.setObjectName("display_vertical_Layout")
        self.display_vertical_Layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area = QScrollArea(QuestDisplay)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_container = QWidget()
        self.scroll_area_container.setObjectName("scroll_area_container")
        self.scroll_area_vertical_Layout = QVBoxLayout(self.scroll_area_container)
        self.scroll_area_vertical_Layout.setSpacing(4)
        self.scroll_area_vertical_Layout.setObjectName("scroll_area_vertical_Layout")
        self.scroll_area_vertical_Layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.scroll_area_container)

        self.display_vertical_Layout.addWidget(self.scroll_area)

        self.retranslateUi(QuestDisplay)

        QMetaObject.connectSlotsByName(QuestDisplay)

    # setupUi

    def retranslateUi(self, QuestDisplay):
        pass

    # retranslateUi
