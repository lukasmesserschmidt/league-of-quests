from random import randint, shuffle

from .settings_manager import SettingsManager
from ..quests import all_quests
from ..restrictions import all_restrictions
from ..gui.quest_frame import QuestFrame


class QuestFrameCreator:

    @classmethod
    def get_available_objects(cls, active_quest_frames: list[QuestFrame]):
        available_objects = {"quest": [[], [], []], "restriction": [[], [], []]}

        for object_type, all_objects in zip(
            available_objects.keys(), (all_quests, all_restrictions)
        ):
            for object in all_objects:
                for quest_frame in active_quest_frames:
                    if object is getattr(quest_frame, object_type):
                        break
                else:
                    if object.check_dependencies() and cls.check_attributes(
                        object_type, object, active_quest_frames
                    ):
                        available_objects[object_type][object.difficulty].append(object)

        for objects in available_objects.values():
            for i in range(3):
                shuffle(objects[i])

        return available_objects

    @classmethod
    def check_attributes(
        cls, object_type: str, object: object, active_quest_frames: list[QuestFrame]
    ):
        if not SettingsManager.get_allow_similar():
            for quest_frame in active_quest_frames:
                for attribute in object.attributes:
                    if attribute in getattr(quest_frame, object_type).attributes:
                        return False

        return True

    @classmethod
    def get_difficultys(cls):
        object_difficultys = {"quest": None, "restriction": None}

        for object_type in object_difficultys.keys():
            rarity_settings = SettingsManager.all_settings["quest_rarity_settings"]
            easy_chance = rarity_settings["easy"][object_type] or 1
            mid_chance = rarity_settings["mid"][object_type] or 1
            hard_chance = rarity_settings["hard"][object_type] or 1

            all_chances = easy_chance + mid_chance + hard_chance
            roll = randint(1, all_chances)

            if roll <= hard_chance:
                difficulty = 2
            elif roll <= mid_chance + hard_chance:
                difficulty = 1
            else:
                difficulty = 0

            object_difficultys[object_type] = difficulty

        return object_difficultys

    @classmethod
    def get_compatible(cls, active_quest_frames: list[QuestFrame]):
        available_quests, available_restrictions = cls.get_available_objects(
            active_quest_frames
        ).values()
        quest_difficulty, restriction_difficulty = cls.get_difficultys().values()

        for q_diff_rotation in range(3):
            q_diff = (quest_difficulty + q_diff_rotation) % 3

            for quest in available_quests[q_diff]:
                for r_diff_rotation in range(3):
                    r_diff = (restriction_difficulty + r_diff_rotation) % 3

                    for restriction in available_restrictions[r_diff]:
                        if not SettingsManager.get_allow_similar():
                            for attribute in quest.attributes:
                                if attribute in restriction.attributes:
                                    break
                            else:
                                return quest, restriction
                        else:
                            return quest, restriction

    @classmethod
    def get_quest_frame(cls, active_quest_frames: list[QuestFrame]):
        compatible_objects = cls.get_compatible(active_quest_frames)
        if compatible_objects:
            quest, restriction = compatible_objects

            quest.start()
            restriction.start()
            quest_frame = QuestFrame(quest, restriction)

            return quest_frame
