import random

from ..core.restrictions import Restriction
from ..core.quests import Quest
from ..core import GameContext
from ..core import Difficulty
from ..core import GameDisruptor
from ..content.quests import ALL_QUEST_CLASSES
from ..content.restrictions import ALL_RESTRICTION_CLASSES


class QuestCreator:
    def create_quest(
        self,
        existing_quests: list[Quest],
        game_context: GameContext,
        game_disruptor: GameDisruptor,
    ) -> Quest:
        available_quest_classes = self._get_available_quests(existing_quests, game_context)
        available_restriction_classes = self._get_available_restrictions(
            existing_quests, game_context
        )

        if not available_quest_classes or not available_restriction_classes:
            raise ValueError("No quests or restrictions available after filtering")

        quest_difficulty = self._get_weighted_difficulty(available_quest_classes)
        restriction_difficulty = self._get_weighted_difficulty(available_restriction_classes)

        quest_classes_with_difficulty = self._filter_by_difficulty(
            available_quest_classes, quest_difficulty
        )
        restriction_classes_with_difficulty = self._filter_by_difficulty(
            available_restriction_classes, restriction_difficulty
        )

        selected_quest_class = random.choice(quest_classes_with_difficulty)
        selected_restriction_class = random.choice(restriction_classes_with_difficulty)

        restriction_object = selected_restriction_class(game_disruptor)
        quest_object = selected_quest_class(restriction_object)

        return quest_object

    def _get_available_quests(
        self, existing_quests: list[Quest], game_context: GameContext
    ) -> list[type[Quest]]:
        filtered_by_duplicates = self._filter_duplicate_classes(ALL_QUEST_CLASSES, existing_quests)

        filtered_by_tags = self._filter_duplicate_tags(filtered_by_duplicates, existing_quests)

        filtered_by_requirements = self._filter_by_requirements(filtered_by_tags, game_context)

        return filtered_by_requirements

    def _get_available_restrictions(
        self, existing_quests: list[Quest], game_context: GameContext
    ) -> list[type[Restriction]]:
        existing_restriction_objects = [
            quest.get_restriction() for quest in existing_quests if quest.get_restriction()
        ]

        filtered_by_duplicates = self._filter_duplicate_classes(
            ALL_RESTRICTION_CLASSES, existing_restriction_objects
        )

        filtered_by_tags = self._filter_duplicate_tags(filtered_by_duplicates, existing_quests)

        filtered_by_requirements = self._filter_by_requirements(filtered_by_tags, game_context)

        return filtered_by_requirements

    def _filter_duplicate_classes(
        self,
        classes: list[type[Quest | Restriction]],
        existing_objects: list[Quest | Restriction],
    ) -> list[type[Quest | Restriction]]:
        existing_classes = {type(object) for object in existing_objects}
        return [cls for cls in classes if cls not in existing_classes]

    def _filter_duplicate_tags(
        self,
        classes: list[type[Quest | Restriction]],
        existing_quests: list[Quest],
    ) -> list[type[Quest | Restriction]]:
        existing_tags = {
            tag for quest in existing_quests for tag in quest.tags + quest.get_restriction().tags
        }

        return [cls for cls in classes if not existing_tags.intersection(cls.tags)]

    def _filter_by_requirements(
        self,
        classes: list[type[Quest | Restriction]],
        game_context: GameContext,
    ) -> list[type[Quest | Restriction]]:
        return [cls for cls in classes if cls.requirements_met(game_context)]

    def _get_weighted_difficulty(self, classes: list[type[Quest | Restriction]]) -> Difficulty:
        available_difficulties = set()
        for cls in classes:
            available_difficulties.add(cls.difficulty)

        available_difficulties = list(available_difficulties)

        weights = {
            Difficulty.EASY: 0.6,
            Difficulty.MEDIUM: 0.3,
            Difficulty.HARD: 0.1,
        }

        weights_list = [weights[diff] for diff in available_difficulties]

        return random.choices(available_difficulties, weights=weights_list, k=1)[0]

    def _filter_by_difficulty(
        self,
        classes: list[type[Quest | Restriction]],
        difficulty: Difficulty,
    ) -> list[type[Quest | Restriction]]:
        return [cls for cls in classes if cls.difficulty == difficulty]
