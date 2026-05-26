import ctypes


class LiveClient:
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
