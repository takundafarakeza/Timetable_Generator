from . import logger_config
from PySide6.QtCore import QStandardPaths
from pathlib import Path
import os
import math
import random


class Utils:

    @staticmethod
    def randomize_slots(slots_: list, block_size_, strict: bool = False):

        if len(slots_) < block_size_:
            return []
        elif len(slots_) == block_size_:
            return slots_

        try:
            iter_count = math.ceil(len(slots_) / block_size_)
            remaining_slots = len(slots_)
            random_slots = []
            extra_slots = []

            for _ in range(iter_count):
                slot = []
                for _ in range(min(block_size_, remaining_slots)):
                    slot.append(slots_[len(slots_) - remaining_slots])
                    remaining_slots -= 1
                if [str(sl) for sl in range(int(slot[0]), int(slot[0]) + len(slot))] == slot and len(slot) == block_size_:
                    random_slots.append(slot)
                elif [str(sl) for sl in range(int(slot[0]), int(slot[0]) + len(slot))] == slot:
                    extra_slots.append(slot)

            random.shuffle(random_slots)
            random_slots = [sl for sls in random_slots for sl in sls]

            if not strict:
                random.shuffle(extra_slots)
                extra_slots = [sl for sls in extra_slots for sl in sls]
                random_slots.extend(extra_slots)
            return random_slots
        except Exception as e:
            logger_config.logger.critical(f"Error: {str(e)}")
            return []

    @staticmethod
    def get_appdata_path(app_name="Timetable_Generator"):
        base_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)

        if not base_path or not os.path.exists(base_path):
            base_path = os.getenv('APPDATA')

        app_path = os.path.join(base_path, app_name, app_name)
        Path(app_path).mkdir(parents=True, exist_ok=True)

        return app_path
