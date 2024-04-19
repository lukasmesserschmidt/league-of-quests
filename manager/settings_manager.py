import json


class Settings:
    all_settings: dict

    @classmethod
    def import_settings(cls):
        with open("lol_quest/settings.json", "r") as f:
            data = json.load(f)
        cls.all_settings = data

    @classmethod
    def update(cls, ui):
        def get_value(lineedit):
            text = lineedit.text()
            if text.isdigit():
                return int(text)
            else:
                return int(text[0:-1])

        # quest settings
        quest_settings = cls.all_settings["quest_settings"]

        # quest on death
        quest_settings["quest_on_death"] = ui.quest_on_death_checkbox.isChecked()

        # quest after time
        # is checked
        quest_settings["quest_after_time"][
            "ischecked"
        ] = ui.quest_after_time_checkbox.isChecked()

        # time
        quest_settings["quest_after_time"]["time"] = get_value(
            ui.quest_after_time_lineedit
        )

        # quest duration
        quest_settings["quest_duration"] = get_value(ui.quest_duration_lineedit)

        # quest rarity settings
        quest_rarity_settings = cls.all_settings["quest_rarity_settings"]

        # easy
        quest_rarity_settings["easy"]["quest"] = get_value(ui.easy_quest_lineedit)

        quest_rarity_settings["easy"]["restriction"] = get_value(
            ui.easy_restriction_lineedit
        )

        # mid
        quest_rarity_settings["mid"]["quest"] = get_value(ui.mid_quest_lineedit)

        quest_rarity_settings["mid"]["restriction"] = get_value(
            ui.mid_restriction_lineedit
        )

        # hard
        quest_rarity_settings["hard"]["quest"] = get_value(ui.hard_quest_lineedit)

        quest_rarity_settings["hard"]["restriction"] = get_value(
            ui.hard_restriction_lineedit
        )

        print(cls.all_settings)

    @classmethod
    def get_setting(cls, *args):
        setting = cls.all_settings
        for arg in args:
            setting = setting[arg]

        return setting
