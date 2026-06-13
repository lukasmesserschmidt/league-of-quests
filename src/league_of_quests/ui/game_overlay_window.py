from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget

from ..platform import LiveClient, User
from ..data import LiveClientConfigFetcher, LiveClientConfig
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
        self.live_client_config_fetcher = LiveClientConfigFetcher()

        style = "background-color: rgba(255, 0, 0, 0.5);"

        self.ability_1 = QWidget(self)
        self.ability_1.setStyleSheet(style)
        self.ability_1.hide()

        self.ability_2 = QWidget(self)
        self.ability_2.setStyleSheet(style)
        self.ability_2.hide()

        self.ability_3 = QWidget(self)
        self.ability_3.setStyleSheet(style)
        self.ability_3.hide()

        self.ability_4 = QWidget(self)
        self.ability_4.setStyleSheet(style)
        self.ability_4.hide()

        self.summoner_spell_1 = QWidget(self)
        self.summoner_spell_1.setStyleSheet(style)
        self.summoner_spell_1.hide()

        self.summoner_spell_2 = QWidget(self)
        self.summoner_spell_2.setStyleSheet(style)
        self.summoner_spell_2.hide()

        self.trinket = QWidget(self)
        self.trinket.setStyleSheet(style)
        self.trinket.hide()

        self.recall = QWidget(self)
        self.recall.setStyleSheet(style)
        self.recall.hide()

        self.health = QWidget(self)
        self.health.setStyleSheet(style)
        self.health.hide()
        self._health_span = [0, 1]

        self.resource = QWidget(self)
        self.resource.setStyleSheet(style)
        self.resource.hide()
        self._resource_span = [0, 1]

        self.map = QWidget(self)
        self.map.setStyleSheet("background-color: rgba(0, 0, 0, 1);")
        self.map.hide()

        self.hide()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update)
        self.timer.start(200)

    def set_health_span(self, from_pct: float, to_pct: float):
        self._health_span = [from_pct, to_pct]

    def set_resource_span(self, from_pct: float, to_pct: float):
        self._resource_span = [from_pct, to_pct]

    def _update(self):
        config = self.live_client_config_fetcher.fetch()

        if config is None or not self.live_client.is_focused():
            self.hide()
            return

        self._update_geometry()

        window_width = self.width()
        window_height = self.height()
        global_scale = config.game.GlobalScale

        scale_factor = window_height / 2160
        horizontal_center = window_width / 2

        self._update_abilities(horizontal_center, window_height, global_scale, scale_factor)

        self._update_summoner_spells(horizontal_center, window_height, global_scale, scale_factor)

        self._update_trinket(horizontal_center, window_height, global_scale, scale_factor)

        self._update_recall(horizontal_center, window_height, global_scale, scale_factor)

        self._update_health_and_resource(
            horizontal_center, window_height, global_scale, scale_factor
        )
        self._update_map(config, window_height, window_width, scale_factor)

        self.show()

    def _update_geometry(self):
        window_rect = self.live_client.get_window_rect()
        if window_rect is None:
            self.hide()
            return

        dpi = self.user.get_dpi_scale()
        x, y, width, height = window_rect
        self.setGeometry(int(x / dpi), int(y / dpi), int(width / dpi), int(height / dpi))

    def _update_abilities(
        self,
        horizontal_center: float,
        window_height: float,
        global_scale: float,
        scale_factor: float,
    ):
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

    def _update_summoner_spells(
        self,
        horizontal_center: float,
        window_height: float,
        global_scale: float,
        scale_factor: float,
    ):
        # Summoner spells positioning
        x = horizontal_center + interpolate((59 * scale_factor), (90 * scale_factor), global_scale)
        y = window_height * interpolate(0.919, 0.878, global_scale)
        size = window_height * interpolate(0.027, 0.041, global_scale)
        space = window_height * interpolate(0.0034, 0.0052, global_scale)

        # Move summoner spell 1
        self.summoner_spell_1.setGeometry(x, y, size, size)

        # Move summoner spell 2
        self.summoner_spell_2.setGeometry(x + size + space, y, size, size)

    def _update_trinket(
        self,
        horizontal_center: float,
        window_height: float,
        global_scale: float,
        scale_factor: float,
    ):
        # Move trinket
        x = horizontal_center + interpolate(
            (418 * scale_factor), (634 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.919, 0.878, global_scale)
        size = window_height * interpolate(0.026, 0.039, global_scale)

        self.trinket.setGeometry(x, y, size, size)

    def _update_recall(
        self,
        horizontal_center: float,
        window_height: float,
        global_scale: float,
        scale_factor: float,
    ):
        # Move recall
        x = horizontal_center + interpolate(
            (420 * scale_factor), (636 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.948, 0.921, global_scale)
        size = window_height * interpolate(0.023, 0.036, global_scale)

        self.recall.setGeometry(x, y, size, size)

    def _update_health_and_resource(
        self,
        horizontal_center: float,
        window_height: float,
        global_scale: float,
        scale_factor: float,
    ):
        # Move health and resource
        x = horizontal_center + interpolate(
            (-367.1 * scale_factor), (-556 * scale_factor), global_scale
        )
        y = window_height * interpolate(0.969, 0.9528, global_scale)
        width = window_height * interpolate(0.254, 0.384, global_scale)
        height = window_height * interpolate(0.0106, 0.0162, global_scale)
        space = window_height * interpolate(0.002, 0.0024, global_scale)

        health_x = x + width * self._health_span[0]
        health_width = width * (self._health_span[1] - self._health_span[0])
        resource_x = x + width * self._resource_span[0]
        resource_width = width * (self._resource_span[1] - self._resource_span[0])

        # Move health
        self.health.setGeometry(health_x, y, health_width, height)

        # Move resource
        self.resource.setGeometry(resource_x, y + height + space, resource_width, height)

    def _update_map(
        self,
        config: LiveClientConfig,
        window_height: float,
        window_width: float,
        scale_factor: float,
    ):
        # Move map
        map_scale = config.game.MinimapScale
        is_flipped = config.game.FlipMiniMap
        size = map_value(map_scale, 0, 3, 400 * scale_factor, 800 * scale_factor)
        x = 0 if is_flipped else window_width - size
        y = window_height - size
        self.map.setGeometry(x, y, size, size)
