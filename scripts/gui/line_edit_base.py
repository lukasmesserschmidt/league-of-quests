from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import (
    QFocusEvent,
    QIntValidator,
)


class LineEdit(QLineEdit):
    def __init__(self, parent, symbol: str, max_num: int, min_num: int = 0):
        super().__init__(parent)

        self.symbol = symbol
        self.min_num = min_num
        self.max_num = max_num
        self.setValidator(QIntValidator(0, 1000000, self))

    def focusInEvent(self, arg__1: QFocusEvent) -> None:
        if self.symbol != "":
            self.setText(self.text()[0:-1])
        super().focusInEvent(arg__1)

    def focusOutEvent(self, arg__1: QFocusEvent) -> None:
        if self.text()[0:4] == "+000":
            self.setText(self.text()[4:])
        else:
            self.setText(self.text().replace("+", ""))

            if "-" in self.text():
                self.setText(str(self.min_num))

            self.set_min()
            self.set_max()

        while len(self.text()) > 1 and self.text()[0] == "0":
            self.setText(self.text()[1:])

        self.setText((self.text() or "0") + self.symbol)
        super().focusOutEvent(arg__1)

    def set_max(self):
        if self.text().isdigit():
            if int(self.text()) > self.max_num:
                self.setText(str(self.max_num))

    def set_min(self):
        if self.text().isdigit():
            if int(self.text()) < self.min_num:
                self.setText(str(self.min_num))
