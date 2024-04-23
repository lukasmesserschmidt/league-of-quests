from PySide6.QtCore import QTimer
import threading
import time

from .quest_manager import QuestManager
from .restriction_manager import RestrictionManager
from .settings_manager import Settings
from ..gui.quest_display import quest_display
from ..gui.quest_display_frame import QuestDisplayFrame
from ..lol_data.active_player_data import AcitvePlayerData
from ..utils.time import convert_time


class MainManager:
    receive_enabled: bool
    restart_timer: bool
    create_quest_amount: int
    quest_on_death: bool
    quest_after_time: dict
    activation_time: float
    remaining_time: float

    terminat_flag: bool
    check_loop_timer: QTimer
    main_loop_thread: threading.Thread

    active_quest_frames = []

    @classmethod
    def start(cls):
        cls.receive_enabled = True
        cls.restart_timer = False
        cls.create_quest_amount = 0

        cls.quest_on_death = Settings.all_settings["quest_settings"]["quest_on_death"]
        cls.player_name = AcitvePlayerData.get_summoner_name()
        cls.last_death_count = AcitvePlayerData.get_death_count()

        cls.quest_after_time = Settings.all_settings["quest_settings"][
            "quest_after_time"
        ]
        cls.activation_time = time.time() + cls.quest_after_time["time"]
        cls.activation_time = time.time() + 10
        cls.remaining_time = 0

        cls.terminat_flag = False
        cls.check_loop_timer = QTimer()
        cls.check_loop_timer.timeout.connect(cls.check_loop)
        cls.check_loop_timer.start(100)
        cls.main_loop_thread = threading.Thread(target=cls.main_loop, daemon=True)
        cls.main_loop_thread.start()

    @classmethod
    def check_loop(cls):
        if cls.create_quest_amount:
            for _ in range(cls.create_quest_amount):
                cls.create_quest()
                cls.create_quest_amount -= 1

        if cls.terminat_flag:
            cls.check_loop_timer.deleteLater()

    @classmethod
    def main_loop(cls):
        while True:
            cls.update_quest_frames()
            cls.receive_quests()
            cls.update_quest_available()

            if cls.terminat_flag:
                break

    @classmethod
    def receive_quests(cls):
        if cls.receive_enabled:
            if cls.quest_on_death:
                death_count = AcitvePlayerData.get_death_count()

                if cls.last_death_count < death_count:
                    # cls.create_quest()
                    cls.create_quest_amount += 1

                cls.last_death_count = death_count

            if cls.quest_after_time["ischecked"]:
                if cls.restart_timer:
                    cls.activation_time = time.time() + cls.quest_after_time["time"]
                    cls.restart_timer = False

                cls.remaining_time = cls.activation_time - time.time()

                if cls.remaining_time <= 0:
                    cls.activation_time = time.time() + cls.quest_after_time["time"]
                    # cls.create_quest()
                    cls.create_quest_amount += 1
                else:
                    quest_display.set_timer_text(convert_time(cls.remaining_time))
            else:
                quest_display.set_timer_text("Not Active")

    @classmethod
    def create_quest(cls):
        compatible = cls.get_compatible()
        if compatible:
            quest, restriction = compatible
            quest.start()
            QuestManager.active_objects.append(quest)
            restriction.start()
            RestrictionManager.active_objects.append(restriction)

            quest_frame = QuestDisplayFrame(quest, restriction)
            quest_display.add_widget(quest_frame)
            cls.active_quest_frames.append(quest_frame)

            cls.update_quest_count()

    @classmethod
    def get_compatible(cls):
        quests = QuestManager.get_available_objects()
        quest_difficulty = QuestManager.get_difficulty(quests)
        restrictions = RestrictionManager.get_available_objects()
        restriction_difficulty = RestrictionManager.get_difficulty(restrictions)

        for diff1 in range(3):
            q_diff = (quest_difficulty + diff1) % 3

            for quest in quests[q_diff]:
                for diff2 in range(3):
                    r_diff = (restriction_difficulty + diff2) % 3

                    for restriction in restrictions[r_diff]:
                        for attribute in quest.attributes:
                            if attribute in restriction.attributes:
                                break
                        else:
                            return quest, restriction

        return None

    @classmethod
    def update_quest_frames(cls):
        for quest_frame in cls.active_quest_frames:
            quest_frame: QuestDisplayFrame
            if quest_frame.quest.terminate_flag:
                cls.delete_quest_frame(quest_frame)

                cls.receive_enabled = True

                cls.update_quest_count()

    @classmethod
    def delete_quest_frame(cls, quest_frame):
        quest_frame.quest.terminate_flag = True
        quest_frame.restriction.terminate_flag = True
        QuestManager.active_objects.remove(quest_frame.quest)
        RestrictionManager.active_objects.remove(quest_frame.restriction)
        quest_frame.deleteLater()
        cls.active_quest_frames.remove(quest_frame)

    @classmethod
    def update_quest_count(cls):
        quest_display.set_quest_count(len(cls.active_quest_frames))

        if len(cls.active_quest_frames) >= 5:
            cls.receive_enabled = False
            cls.restart_timer = True
            quest_display.set_timer_text("Max Quests")

    @classmethod
    def update_quest_available(cls):
        if cls.get_compatible():
            cls.receive_enabled = True
        else:
            cls.receive_enabled = False
            cls.restart_timer = True
            quest_display.set_timer_text("No Quest Available")
