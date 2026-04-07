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
    def randomize_slots(slots_: list, block_size_, strict: bool = False, block: bool = False):

        if len(slots_) < block_size_:
            return []

        try:
            random_slots = []
            extra_slots = [sl for sl in slots_]
            slots = slots_
            while len(slots) > 0:
                slot = []
                remaining = block_size_
                while remaining > 0:
                    for slot_item in slots:
                        if len(slot) > 0 and int(slot_item)- 1 != int(slot[-1]):
                            break
                        slot.append(slot_item)
                        remaining -= 1
                        if remaining == 0:
                            break
                    if remaining != 0:
                        break
                if not block:
                    for item in slot:
                        slots.remove(item)
                else:
                    slots.remove(slots[0])
                if len(slot) == block_size_:
                    random_slots.append(slot)

            random.shuffle(random_slots)
            random_slots = [sl for slot in random_slots for sl in slot]
            if not strict:
                extra_slots = [sl for sl in extra_slots if sl not in random_slots]
                random.shuffle(extra_slots)
                extra_slots = [sl for sls in extra_slots for sl in sls]
                random_slots.extend(extra_slots)
            return random_slots
        except Exception:
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
    def save_file(file_path, parent=None, dest_path=None):

        if dest_path is None:
            dest_path, _ = QFileDialog.getSaveFileName(parent, "Save as", os.path.basename(file_path), "All Files (*)")

        if file_path:
            try:
                if os.path.isdir(file_path):
                    if os.path.exists(dest_path):
                        QMessageBox.warning(parent, "Already exists", f"This project file already exists")
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


class ExportUtils:
    @staticmethod
    def record_matches(record, selected_courses=None, selected_lecturers=None, selected_venues=None):
        selected_courses = selected_courses or set()
        selected_lecturers = selected_lecturers or set()
        selected_venues = selected_venues or set()

        course_ok = True if not selected_courses else any(c in selected_courses for c in record["course_ids"])
        lecturer_ok = True if not selected_lecturers else record["lecturer_id"] in selected_lecturers
        venue_ok = True if not selected_venues else record["venue_id"] in selected_venues

        return course_ok and lecturer_ok and venue_ok

    @staticmethod
    def flatten_timetable(builder):
        records = []
        timetable_data = builder.timetable_get()

        for day_id, slots in timetable_data.items():
            for slot_id, modules in slots.items():
                for module_id, info in modules.items():
                    records.append({
                        "day_id": str(day_id),
                        "slot_id": str(slot_id),
                        "module_id": str(module_id),
                        "venue_id": str(info.get("venue")) if info.get("venue") is not None else "",
                        "course_ids": [str(c) for c in info.get("courses", [])],
                        "lecturer_id": builder.module_get(module_id).lecturer
                    })

        return records

    @staticmethod
    def apply_filters(records, selected_courses=None, selected_lecturers=None, selected_venues=None):
        return [
            r for r in records
            if ExportUtils.record_matches(r, selected_courses, selected_lecturers, selected_venues)
        ]

    @staticmethod
    def get_available_courses(records, selected_lecturers=None, selected_venues=None):
        filtered = ExportUtils.apply_filters(records, set(), selected_lecturers, selected_venues)
        result = set()
        for r in filtered:
            result.update(r["course_ids"])
        return sorted(result)

    @staticmethod
    def get_available_lecturers(records, selected_courses=None, selected_venues=None):
        filtered = ExportUtils.apply_filters(records, selected_courses, set(), selected_venues)
        return sorted({r["lecturer_id"] for r in filtered if r["lecturer_id"]})

    @staticmethod
    def get_available_venues(records, selected_courses=None, selected_lecturers=None):
        filtered = ExportUtils.apply_filters(records, selected_courses, selected_lecturers, set())
        return sorted({r["venue_id"] for r in filtered if r["venue_id"]})

    @staticmethod
    def get_course_counts(records, selected_lecturers=None, selected_venues=None):
        filtered = ExportUtils.apply_filters(records, set(), selected_lecturers, selected_venues)
        counts = {}
        for r in filtered:
            for c in r["course_ids"]:
                counts[c] = counts.get(c, 0) + 1
        return counts

    @staticmethod
    def get_lecturer_counts(records, selected_courses=None, selected_venues=None):
        filtered = ExportUtils.apply_filters(records, selected_courses, set(), selected_venues)
        counts = {}
        for r in filtered:
            lid = r["lecturer_id"]
            if lid:
                counts[lid] = counts.get(lid, 0) + 1
        return counts

    @staticmethod
    def get_venue_counts(records, selected_courses=None, selected_lecturers=None):
        filtered = ExportUtils.apply_filters(records, selected_courses, selected_lecturers, set())
        counts = {}
        for r in filtered:
            vid = r["venue_id"]
            if vid:
                counts[vid] = counts.get(vid, 0) + 1
        return counts

