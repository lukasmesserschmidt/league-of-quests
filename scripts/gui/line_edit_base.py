"""
Base class for LineEdit widgets.
"""

from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import (
    QFocusEvent,
    QIntValidator,
)

from ..utils.constants import Constants


class LineEdit(QLineEdit):
    """
    Base class for LineEdit widgets.
    """

    def __init__(self, parent, symbol: str, max_num: int, min_num: int = 0):
        super().__init__(parent)

        self._symbol = symbol
        self._min_num = min_num
        self._max_num = max_num
        self.setValidator(QIntValidator(0, Constants.MAX_DURATION, self))

    def focusInEvent(self, arg__1: QFocusEvent) -> None:
        if self._symbol != "":
            self.setText(self.text()[0:-1])
        super().focusInEvent(arg__1)

    def focusOutEvent(self, arg__1: QFocusEvent) -> None:
        if self.text()[0:4] == "+000":
            self.setText(self.text()[4:])
        else:
            self.setText(self.text().replace("+", ""))

            if "-" in self.text():
                self.setText(str(self._min_num))

            self._set_min()
            self._set_max()

        while len(self.text()) > 1 and self.text()[0] == "0":
            self.setText(self.text()[1:])

        self.setText((self.text() or "0") + self._symbol)
        super().focusOutEvent(arg__1)

    def _set_max(self):
        if self.text().isdigit():
            if int(self.text()) > self._max_num:
                self.setText(str(self._max_num))

    def _set_min(self):
        if self.text().isdigit():
            if int(self.text()) < self._min_num:
                self.setText(str(self._min_num))
