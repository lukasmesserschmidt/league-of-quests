# League of Quests gives players additional tasks in the game League of Legends for a greater challenge.
# Copyright (C) 2024  Lukas Jan Messerschmidt

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


def start():
    """
    Creates the app and starts the program by instantiating the main menu.
    """
    from .gui import app

    app.create_app()

    from .gui.main_menu import MainMenu

    MainMenu()

    app.start()
