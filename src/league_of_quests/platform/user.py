import ctypes


class User:
    """Provides system-level info: screen resolution, DPI scaling."""

    def get_screen_resolution(self) -> tuple[int, int]:
        """Return primary monitor resolution (width, height) in physical pixels."""
        # SM_CXSCREEN = 0, SM_CYSCREEN = 1
        width = ctypes.windll.user32.GetSystemMetrics(0)
        height = ctypes.windll.user32.GetSystemMetrics(1)
        return width, height

    def get_dpi_scale(self) -> float:
        """Return DPI scaling factor (e.g. 1.0 = 100%, 1.5 = 150%, 2.0 = 200%)."""
        try:
            # SetProcessDpiAwareness must be called before querying DPI
            ctypes.windll.shcore.SetProcessDpiAwareness(2)  # PROCESS_PER_MONITOR_DPI_AWARE
        except (AttributeError, OSError):
            pass

        try:
            dpi = ctypes.windll.user32.GetDpiForSystem()
            return dpi / 96.0
        except AttributeError:
            # Fallback for older Windows versions
            hdc = ctypes.windll.user32.GetDC(0)
            dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return dpi / 96.0


if __name__ == "__main__":
    user = User()
    print(f"Screen resolution: {user.get_screen_resolution()}")
    print(f"DPI scale: {user.get_dpi_scale()}")
    print(
        f"Screen resolution scaled: {user.get_screen_resolution()[0] / user.get_dpi_scale()}, {user.get_screen_resolution()[1] / user.get_dpi_scale()}"
    )
