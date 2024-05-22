from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import (
    QFocusEvent,
    QIntValidator,
)


class LineEdit(QLineEdit):
    def __init__(self, parent, symbol: str, max_num: int):
        super().__init__(parent)

        self.symbol = symbol
        self.max_num = max_num
        self.setValidator(QIntValidator())

        self.textChanged.connect(self.on_text_change)

    def focusInEvent(self, arg__1: QFocusEvent) -> None:
        if self.symbol != "":
            self.setText(self.text()[0:-1])
        super().focusInEvent(arg__1)

    def focusOutEvent(self, arg__1: QFocusEvent) -> None:
        self.setText((self.text() or "0") + self.symbol)
        self.setText(self.text().replace("-", ""))
        super().focusOutEvent(arg__1)

    def on_text_change(self, text):
        if text.isdigit() and int(text) > self.max_num:
            self.setText(str(self.max_num))
