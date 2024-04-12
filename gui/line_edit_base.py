from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import (
    QFocusEvent,
    QIntValidator,
)


class LineEdit(QLineEdit):
    def __init__(self, parent, symbol: str):
        super().__init__(parent)

        self.symbol = symbol
        self.setValidator(QIntValidator())

    def focusInEvent(self, arg__1: QFocusEvent) -> None:
        self.setText(self.text()[0:-1])
        super().focusInEvent(arg__1)

    def focusOutEvent(self, arg__1: QFocusEvent) -> None:
        self.setText((self.text() or "0") + self.symbol)
        super().focusOutEvent(arg__1)
