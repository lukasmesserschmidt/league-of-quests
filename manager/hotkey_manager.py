import keyboard

from ..lol_data.lol_settings import LolSettings
from ..gui.game_overlay.game_overlay_window import game_overlay
from ..utils.top_window import get_top_window_is_lol


class HotkeyManager:

    @classmethod
    def enable_ability(cls, enable: bool, *args: int):
        for arg in args:
            if get_top_window_is_lol():
                if enable:
                    keyboard.unhook_all()
                    game_overlay.ability_cover.deactivate_cover(arg)
                else:
                    hotkey = LolSettings.get_ability_hotkey(arg)
                    keyboard.block_key(hotkey)
                    game_overlay.ability_cover.activate_cover(arg)
            else:
                keyboard.unhook_all()
                game_overlay.ability_cover.deactivate_cover(arg)

    @classmethod
    def enable_summoner_spell(cls, enable: bool, *args: int):
        for arg in args:
            if get_top_window_is_lol():
                if enable:
                    keyboard.unhook_all()
                    game_overlay.summoner_spell_cover.deactivate_cover(arg)
                else:
                    hotkey = LolSettings.get_summoner_spell_hotkey(arg)
                    keyboard.block_key(hotkey)
                    game_overlay.summoner_spell_cover.activate_cover(arg)
            else:
                keyboard.unhook_all()
                game_overlay.summoner_spell_cover.deactivate_cover(arg)

    @classmethod
    def enable_trinket(cls, enable: bool):
        if get_top_window_is_lol():
            if enable:
                keyboard.unhook_all()
                game_overlay.trinket_cover.hide()
            else:
                hotkey = LolSettings.get_trinket_hotkey()
                keyboard.block_key(hotkey)
                game_overlay.trinket_cover.show()
        else:
            keyboard.unhook_all()
            game_overlay.trinket_cover.hide()

    @classmethod
    def enable_teleport(cls, enable: bool):
        if get_top_window_is_lol():
            if enable:
                keyboard.unhook_all()
                game_overlay.teleport_cover.hide()
            else:
                hotkey = LolSettings.get_teleport_hotkey()
                keyboard.block_key(hotkey)
                game_overlay.teleport_cover.show()
        else:
            keyboard.unhook_all()
            game_overlay.teleport_cover.hide()
