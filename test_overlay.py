from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from src.league_of_quests.platform.live_client import LiveClient
from src.league_of_quests.data.live_client_config_monitor import LiveClientConfigMonitor
from src.league_of_quests.ui.game_overlay import GameOverlay


def test_overlay():
    print("Initializing GameOverlay test...")
    app = QApplication([])

    # Simple test: create a basic red window to verify Qt works
    test_window = QWidget()
    test_window.setWindowTitle("Test Window")
    test_window.setStyleSheet("background-color: red;")
    test_window.setGeometry(100, 100, 400, 300)
    test_window.show()
    print("Test window shown at (100, 100, 400, 300)")

    live_client = LiveClient()
    config_monitor = LiveClientConfigMonitor()

    # Debug: Check if we can find the window
    print(f"Window handle: {live_client.get_window_handle()}")
    print(f"Window rect: {live_client.get_window_rect()}")
    print(f"Is focused: {live_client.is_focused()}")
    print(f"Config: {config_monitor.get_config()}")

    overlay = GameOverlay(live_client, config_monitor)
    overlay.start()

    print("Overlay started. Waiting for League of Legends window...")

    # Enable a bunch of overlays with different colors
    overlay.show_ability(1, "#FF0000", 0.5)  # Q (Red)
    overlay.show_ability(4, "#FF00FF", 0.5)  # R (Magenta)

    overlay.show_summoner_spell(1, "#FFFF00", 0.5)  # D (Yellow)

    overlay.show_health(0.0, 0.5, "#00FF00", 0.5)  # Health 0-50% (Green)
    overlay.show_resource(0.5, 1.0, "#0000FF", 0.5)  # Mana 50-100% (Blue)

    overlay.show_minimap("#FFFFFF", 0.3)  # Minimap (White)
    overlay.show_recall("#00FFFF", 0.5)  # Recall (Cyan)

    print("Overlays activated! Focus the League of Legends window to see them.")
    print("Close the command prompt or press Ctrl+C to exit.")

    app.exec()


if __name__ == "__main__":
    test_overlay()
