import ctypes
import ctypes.wintypes

from ..utils import SingletonMeta


class LiveClient(metaclass=SingletonMeta):
    def __init__(self):
        self._window_title = "League of Legends (TM) Client"
        self._window_class = "RiotWindowClass"

    def is_focused(self) -> bool:
        # Get the handle of the foreground window
        foreground_window = ctypes.windll.user32.GetForegroundWindow()

        # Get the window title
        window_title = ctypes.create_unicode_buffer(512)
        ctypes.windll.user32.GetWindowTextW(
            foreground_window,
            window_title,
            ctypes.sizeof(window_title) // ctypes.sizeof(ctypes.c_wchar),
        )

        # Get the window class name
        class_name = ctypes.create_unicode_buffer(256)
        ctypes.windll.user32.GetClassNameW(
            foreground_window,
            class_name,
            ctypes.sizeof(class_name) // ctypes.sizeof(ctypes.c_wchar),
        )

        return (
            window_title.value == self._window_title
            and class_name.value == self._window_class
        )

    def get_window_handle(self) -> int | None:
        """Find the LoL game window handle. Returns None if not found."""
        hwnd = ctypes.windll.user32.FindWindowW(self._window_class, self._window_title)
        return hwnd if hwnd else None

    def get_window_rect(self) -> tuple[int, int, int, int] | None:
        """Return (x, y, width, height) of the game window in screen pixels.

        Returns None if the window is not found.
        """
        hwnd = self.get_window_handle()
        if not hwnd:
            return None

        rect = ctypes.wintypes.RECT()
        if not ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect)):
            return None

        return (
            rect.left,
            rect.top,
            rect.right - rect.left,
            rect.bottom - rect.top,
        )
