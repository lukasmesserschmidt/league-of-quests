from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget

from ..platform import LiveClient, User
from ..data import LiveClientConfigMonitor
from ..utils.calculations import interpolate, map_value


class GameOverlayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
            | Qt.WindowTransparentForInput
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.live_client = LiveClient()
        self.user = User()
        self.live_client_config_monitor = LiveClientConfigMonitor()

        style = "background-color: rgba(255, 0, 0, 0.5);"

        self.ability_1 = QWidget(self)
        self.ability_1.setStyleSheet(style)

        self.ability_2 = QWidget(self)
        self.ability_2.setStyleSheet(style)

        self.ability_3 = QWidget(self)
        self.ability_3.setStyleSheet(style)

        self.ability_4 = QWidget(self)
        self.ability_4.setStyleSheet(style)

        self.summoner_spell_1 = QWidget(self)
        self.summoner_spell_1.setStyleSheet(style)

        self.summoner_spell_2 = QWidget(self)
        self.summoner_spell_2.setStyleSheet(style)

        self.trinket = QWidget(self)
        self.trinket.setStyleSheet(style)

        self.recall = QWidget(self)
        self.recall.setStyleSheet(style)

        self.health = QWidget(self)
        self.health.setStyleSheet(style)

        self.resource = QWidget(self)
        self.resource.setStyleSheet(style)

        self.map = QWidget(self)
        self.map.setStyleSheet("background-color: rgba(0, 0, 0, 1);")

        self.update()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.timer.start(200)

    def _update_geometry(self):
        window_rect = self.live_client.get_window_rect()
        if window_rect is None:
            self.hide()
            return

        dpi = self.user.get_dpi_scale()
        x, y, width, height = window_rect
        self.setGeometry(int(x / dpi), int(y / dpi), int(width / dpi), int(height / dpi))

    def _update(self):
        config = self.live_client_config_monitor.get_config()

        if config is None or not self.live_client.is_focused():
            self.hide()
            return

        self.show()
        self._update_geometry()

        window_width = self.width()
        window_height = self.height()
        global_scale = config.game.GlobalScale

        scale_factor = window_height / 2160
        horizontal_center = window_width / 2

        # Ability bar positioning
        x = horizontal_center + interpolate(
            (-303.4 * scale_factor), (-460.8 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.919, 0.877, global_scale)
        size = window_height * interpolate(0.038, 0.057, global_scale)
        space = window_height * interpolate(0.0025, 0.0045, global_scale)

        # Move ability 1
        self.ability_1.setGeometry(x, y, size, size)

        # Move ability 2
        self.ability_2.setGeometry(x + size + space, y, size, size)

        # Move ability 3
        self.ability_3.setGeometry(x + (size + space) * 2, y, size, size)

        # Move ability 4
        self.ability_4.setGeometry(x + (size + space) * 3, y, size, size)

        # Summoner spells positioning
        x = horizontal_center + interpolate((59 * scale_factor), (90 * scale_factor), global_scale)
        y = window_height * interpolate(0.919, 0.878, global_scale)
        size = window_height * interpolate(0.027, 0.041, global_scale)
        space = window_height * interpolate(0.0034, 0.0052, global_scale)

        # Move summoner spell 1
        self.summoner_spell_1.setGeometry(x, y, size, size)

        # Move summoner spell 2
        self.summoner_spell_2.setGeometry(x + size + space, y, size, size)

        # Move trinket
        x = horizontal_center + interpolate(
            (418 * scale_factor), (634 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.919, 0.878, global_scale)
        size = window_height * interpolate(0.026, 0.039, global_scale)

        self.trinket.setGeometry(x, y, size, size)

        # Move recall
        x = horizontal_center + interpolate(
            (420 * scale_factor), (636 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.948, 0.921, global_scale)
        size = window_height * interpolate(0.023, 0.036, global_scale)

        self.recall.setGeometry(x, y, size, size)

        # Move health and resource
        x = horizontal_center + interpolate(
            (-367.1 * scale_factor), (-556 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.969, 0.9528, global_scale)
        width = window_height * interpolate(0.254, 0.384, global_scale)
        height = window_height * interpolate(0.0106, 0.0162, global_scale)
        space = window_height * interpolate(0.0022, 0.0024, global_scale)

        # Move health
        self.health.setGeometry(x, y, width, height)

        # Move resource
        self.resource.setGeometry(x, y + height + space, width, height)

        # Move map
        map_scale = config.game.MinimapScale
        is_flipped = config.game.FlipMiniMap
        size = map_value(map_scale, 0, 3, 400 * scale_factor, 800 * scale_factor)
        x = 0 if is_flipped else window_width - size
        y = window_height - size
        self.map.setGeometry(x, y, size, size)
