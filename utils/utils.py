import re

from PySide6.QtCore import QStandardPaths
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pathlib import Path
import json
import os
import math
import random
import shutil


class Utils:

    @staticmethod
    def get_projects():
        projects = {}
        path = Utils.get_timetables_path()
        projects_list = os.listdir(path)
        for project in projects_list:
            file = os.path.join(path, project)
            if os.path.isfile(file):
                projects[project.replace(".tbl", "").replace("_", " ")] = file
        return projects

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
            return []

    @staticmethod
    def get_appdata_path(app_name="Timetable_Generator"):
        base_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)

        if not base_path or not os.path.exists(base_path):
            base_path = os.getenv('APPDATA')

        app_path = os.path.join(base_path, app_name)
        Path(app_path).mkdir(parents=True, exist_ok=True)

        return app_path

    @staticmethod
    def get_timetables_path():
        app_path = os.path.join(Utils.get_appdata_path(), "timetables")
        Path(app_path).mkdir(parents=True, exist_ok=True)
        return app_path

    @staticmethod
    def get_log_path(app_name="Timetable_Generator"):
        base_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)

        if not base_path or not os.path.exists(base_path):
            base_path = os.getenv('APPDATA')

        app_path = os.path.join(base_path, app_name, "logs")
        Path(app_path).mkdir(parents=True, exist_ok=True)

        return app_path

    @staticmethod
    def view_portal():
        pass

    @staticmethod
    def save_file(file_path, parent):

        dest_path, _ = QFileDialog.getSaveFileName(parent, "Save as", os.path.basename(file_path), "All Files (*)")

        if file_path:
            try:
                if os.path.isdir(file_path):
                    if os.path.exists(dest_path):
                        QMessageBox.warning(parent, "Already exists", f"{dest_path} already exists")
                        return False
                    shutil.copytree(file_path, dest_path)
                else:
                    shutil.copy2(file_path, dest_path)
                return True
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))
        return False

    @staticmethod
    def project_path_to_name(path: str):
        return os.path.basename(path).replace(".tbl", "")

    @staticmethod
    def project_name_to_path(name: str):
        return os.path.join(Utils.get_timetables_path(), f"{name.replace(" ", "_")}.tbl")

    @staticmethod
    def scale_down(limit, num):
        return num - limit * (math.ceil(num / limit) - 1)

    @staticmethod
    def ordered_token_match(query: str, text: str) -> bool:
        q_tokens = re.sub(r'[^a-z0-9]', '', query.lower()).split()
        t = re.sub(r'[^a-z0-9]', '', text.lower())

        pos = 0

        for token in q_tokens:
            idx = t.find(token, pos)
            if idx == -1:
                return False
            pos = idx + len(token)

        return True

    def list_search(self, query: str, text: list) -> list:
        matches = []
        for i, text in enumerate(text):
            if self.ordered_token_match(query, text):
                matches.append(i)
        return matches

    def create_project_file(self, name: str, school: str) -> str:
        file_path = os.path.join(self.get_timetables_path(), f"{name}_{school}.tbl").replace(" ", "_")
        file = open(file_path, "w")
        file.close()
        return file_path


class Settings:
    def __init__(self, app_path=Utils.get_appdata_path()):
        self.db_file = os.path.join(app_path, "conf.tblc")
        if not os.path.exists(self.db_file):
            file_ = open(self.db_file, "w")
            file_.write(json.dumps({"recent": {}}))
            file_.close()

    def add(self, setting, value):

        file_data = {}

        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            file_data = json.loads(file_.read())
            file_.close()

        with open(self.db_file, "w") as settings:
            file_data[setting] = value
            file_data = json.dumps(file_data)
            settings.write(file_data)

    def add_recent_file(self, file, path):

        file_data = {}

        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            file_data = json.loads(file_.read())
            file_.close()

        recent = file_data["recent"]
        if file in recent:
            del recent[file]

        with open(self.db_file, "w") as settings:
            recent[file] = path
            file_data = json.dumps(file_data)
            settings.write(file_data)

    def get_recent_files(self):
        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            file_data = json.loads(file_.read())["recent"]
            file_.close()
            recent_files = [item for item in file_data.items()]
            recent_files.reverse()
            return recent_files
        else:
            return []

    def get_recent_file(self, name: str):
        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            file = None
            try:
                file = json.loads(file_.read())["recent"][name]
            except KeyError:
                pass
            file_.close()
            return file

    def remove_recent_file(self, file):
        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            file_data = json.loads(file_.read())
            file_.close()
            del file_data["recent"][file]

            with open(self.db_file, "w") as settings:
                file_data = json.dumps(file_data)
                settings.write(file_data)
        return self.get_recent_files()

    def clear_recent(self):
        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            file_data = json.loads(file_.read())
            file_data["recent"] = {}
            file_.close()

            with open(self.db_file, "w") as settings:
                file_data = json.dumps(file_data)
                settings.write(file_data)

    def get(self, setting):
        value = None
        if os.path.exists(self.db_file):
            file_ = open(self.db_file)
            try:
                value = json.loads(file_.read())[setting]
            except Exception:
                value = None
            finally:
                file_.close()
        return value

    def remove(self, setting):
        try:
            file_data = {}

            if os.path.exists(self.db_file):
                file_ = open(self.db_file)
                file_data = json.loads(file_.read())
                file_.close()

            if len(file_data) > 0:
                with open(self.db_file, "w") as settings:
                    del file_data[setting]
                    file_data = json.dumps(file_data)
                    settings.write(file_data)
            else:
                return
        except Exception:
            return