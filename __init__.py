from .gui import app
from .manager.settings_manager import Settings


app.create_app()

Settings.import_settings()
