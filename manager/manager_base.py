from random import randint, shuffle

from .settings_manager import Settings


class ManagerBase:
    object_type: str
    all_objects: list
    active_objects = []

    @classmethod
    def get_available_objects(cls):
        available_objects = [[], [], []]

        for object in cls.all_objects:
            if (
                object not in cls.active_objects
                and object.check_dependencies()
                and cls.check_attributes(object)
            ):
                available_objects[object.difficulty].append(object)

        for i in range(3):
            shuffle(available_objects[i])

        return available_objects

    @classmethod
    def check_attributes(cls, object):
        for active_object in cls.active_objects:
            for attribute in object.attributes:
                if attribute in active_object.attributes:
                    return False

        return True

    @classmethod
    def get_difficulty(cls, available_objects):
        rarity_settings = Settings.all_settings["quest_rarity_settings"]
        easy_chance = rarity_settings["easy"][cls.object_type]
        mid_chance = rarity_settings["mid"][cls.object_type]
        hard_chance = rarity_settings["hard"][cls.object_type]

        all_chances = easy_chance + mid_chance + hard_chance
        roll = randint(1, all_chances)

        # if len(available_objects[2]) > 0 and roll <= hard_chance:
        #     return 2
        # elif len(available_objects[1]) > 0 and roll <= mid_chance + hard_chance:
        #     return 1
        # elif len(available_objects[0]) > 0:
        #     return 0
        if roll <= hard_chance:
            return 2
        elif roll <= mid_chance + hard_chance:
            return 1
        else:
            return 0

        return None

    @classmethod
    def get_object(cls):
        available_objects = cls.get_available_objects()
        difficulty = cls.get_difficulty(available_objects)

        if difficulty != None:
            rand_idx = randint(0, len(available_objects[difficulty]) - 1)
            object = available_objects[difficulty][rand_idx]
            # object.start()
            # cls.active_objects.append(object)

            return object

        return None
