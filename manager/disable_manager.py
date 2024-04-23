import keyboard

from ..lol_data.lol_settings import LolSettings
from ..gui.game_overlay.game_overlay_window import game_overlay
from ..utils.top_window_is_lol import get_top_window_is_lol


class DisableManager:
    hotkey_dict = {
        "ability": {0: None, 1: None, 2: None, 3: None},
        "summoner_spell": {0: None, 1: None},
        "trinket": {0: None},
        "teleport": {0: None},
    }

    @classmethod
    def enable_key(cls, enable: bool, overlay_type: str, *args: int):
        hotkeys = cls.hotkey_dict[overlay_type]

        for arg in args:
            hotkey = hotkeys[arg]

            if hotkey == None:
                cls.update_hotkeys(overlay_type, *args)

            try:
                if enable:
                    keyboard.unblock_key(hotkey)
                else:
                    keyboard.block_key(hotkey)
            except:
                pass

    @classmethod
    def update_hotkeys(cls, overlay_type: str, *args: int):
        get_hotkey = getattr(LolSettings, f"get_{overlay_type}_hotkey")
        hotkeys = cls.hotkey_dict[overlay_type]

        for arg in args:
            hotkey = get_hotkey(arg)
            hotkeys[arg] = hotkey

    @classmethod
    def enable_type(cls, enable: bool, overlay_type: str, *args: int):
        if get_top_window_is_lol():
            cls.enable_key(True, overlay_type, *args)
            cls.update_hotkeys(overlay_type, *args)

            cls.enable_key(enable, overlay_type, *args)
            game_overlay.disable_cover(enable, overlay_type, *args)
            # if enable:
            #     cls.enable_key(True, overlay_type, args)
            #     game_overlay.disable_cover(True, overlay_type, args)
            # else:
            #     cls.enable_key(True, overlay_type, args)
            #     cls.update_hotkeys(overlay_type, args)

            #     cls.enable_key(False, overlay_type, args)
            #     game_overlay.disable_cover(False, overlay_type, args)
        else:
            keyboard.unhook_all()
            game_overlay.disable_cover(True, overlay_type, *args)

    @classmethod
    def enable_ability(cls, enable: bool, *args: int):
        for arg in args:
            if get_top_window_is_lol():
                if enable:
                    keyboard.unhook_all()
                    game_overlay.ability_cover.deactivate_cover(arg)
                else:
                    type = "ability"
                    cls.unblock_key(type, arg)
                    hotkey = LolSettings.get_ability_hotkey(arg)
                    cls.hotkey_dict[type][arg] = hotkey

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
                    type = "summonerspell"
                    cls.unblock_key(type, arg)
                    hotkey = LolSettings.get_summoner_spell_hotkey(arg)
                    cls.hotkey_dict[type][arg] = hotkey

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
                type = "trinket"
                cls.unblock_key(type)
                hotkey = LolSettings.get_trinket_hotkey()
                cls.hotkey_dict[type] = hotkey

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
                type = "teleport"
                cls.unblock_key(type)
                hotkey = LolSettings.get_teleport_hotkey()
                cls.hotkey_dict[type] = hotkey

                keyboard.block_key(hotkey)
                game_overlay.teleport_cover.show()
        else:
            keyboard.unhook_all()
            game_overlay.teleport_cover.hide()

    @classmethod
    def enable_map(cls, enable: bool):
        if get_top_window_is_lol:
            if enable:
                game_overlay.map_cover.show()
            else:
                game_overlay.map_cover.hide()
        else:
            game_overlay.map_cover.hide()
