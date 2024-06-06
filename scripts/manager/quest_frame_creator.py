from random import randint, shuffle, choice

from .settings_manager import SettingsManager
from ..quests import all_quests
from ..restrictions import all_restrictions
from ..common_classes.quest_restriction_base import QuestRestrictionBase
from ..gui.quest_frame import QuestFrame


class QuestFrameCreator:
    all_objects = {"quest": all_quests, "restriction": all_restrictions}

    @classmethod
    def _get_available_objects(cls, active_qust_frames: list[QuestFrame]):
        active_objects = cls._get_active_objects(active_qust_frames)

        available_objects = {
            "quest": list[list[QuestRestrictionBase],],
            "restriction": list[list[QuestRestrictionBase],],
        }

        for object_type in available_objects.keys():
            # remove objects that are already active
            all_objects = cls.all_objects[object_type].copy()
            all_objects = [
                object
                for object in all_objects
                if object not in active_objects[object_type]
            ]

            # check dependencies/attributes and sort by difficulty
            available_objects[object_type] = cls._filter_objects(
                object_type, all_objects, active_objects
            )

        # randomize object order
        available_objects = cls._shuffle_objects(available_objects)

        return available_objects

    @classmethod
    def _get_active_objects(cls, active_quest_frames: list[QuestFrame]):
        active_objects: dict[str, list[QuestRestrictionBase]] = {
            "quest": [],
            "restriction": [],
        }

        for active_quest_frame in active_quest_frames:
            active_objects["quest"].append(active_quest_frame.quest)
            active_objects["restriction"].append(active_quest_frame.restriction)

        return active_objects

    @classmethod
    def _filter_objects(
        cls,
        object_type: str,
        all_objects: list[QuestRestrictionBase],
        active_objects: dict[str, list[QuestRestrictionBase]],
    ):
        filtered_objects = [[], [], []]

        for object in all_objects:
            if object.check_dependencies() and cls._check_attributes(
                object_type, object, active_objects
            ):
                if type(object.alternating_difficulties) == tuple:
                    object.difficulty = choice(object.alternating_difficulties)
                filtered_objects[object.difficulty].append(object)

        return filtered_objects

    @classmethod
    def _check_attributes(
        cls,
        object_type: str,
        object: QuestRestrictionBase,
        active_objects: dict[str, list[QuestRestrictionBase]],
    ):
        if not SettingsManager.get_allow_similar():
            for active_object in active_objects[object_type]:
                for attribute in active_object.attributes:
                    if attribute in object.attributes:
                        return False

        return True

    @classmethod
    def _shuffle_objects(
        cls, available_objects: dict[str, list[list[QuestRestrictionBase]]]
    ):
        for available_object in available_objects.values():
            for i in range(3):
                shuffle(available_object[i])

        return available_objects

    @classmethod
    def _get_difficultys(cls):
        object_difficultys = {"quest": None, "restriction": None}

        for object_type in object_difficultys.keys():
            easy_chance = SettingsManager.get_easy_object(object_type)
            mid_chance = SettingsManager.get_mid_object(object_type)
            hard_chance = SettingsManager.get_hard_object(object_type)

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
        available_quests, available_restrictions = cls._get_available_objects(
            active_quest_frames
        ).values()
        quest_difficulty, restriction_difficulty = cls._get_difficultys().values()

        for q_diff_rotation in range(3):
            q_diff = (quest_difficulty + q_diff_rotation) % 3

            for quest in available_quests[q_diff]:
                quest: QuestRestrictionBase

                for r_diff_rotation in range(3):
                    r_diff = (restriction_difficulty + r_diff_rotation) % 3

                    for restriction in available_restrictions[r_diff]:
                        restriction: QuestRestrictionBase

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
