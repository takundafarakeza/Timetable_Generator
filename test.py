import json
from utils import Types


with open("tbl.json", "r") as f:
    timetable = json.loads(f.read())

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QDialog, QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSplitter, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView, QHeaderView
)


def flatten_timetable(timetable_data, module_to_lecturer=None):
    module_to_lecturer = module_to_lecturer or {}
    records = []

    for day_id, slots in timetable_data.get("time_table", {}).items():
        for slot_id, modules in slots.items():
            for module_id, info in modules.items():
                records.append({
                    "day_id": str(day_id),
                    "slot_id": str(slot_id),
                    "module_id": str(module_id),
                    "venue_id": str(info.get("venue")) if info.get("venue") is not None else "",
                    "course_ids": [str(c) for c in info.get("courses", [])],
                    "lecturer_id": str(module_to_lecturer.get(str(module_id), "")),
                })

    return records


def record_matches(record, selected_courses=None, selected_lecturers=None, selected_venues=None):
    selected_courses = selected_courses or set()
    selected_lecturers = selected_lecturers or set()
    selected_venues = selected_venues or set()

    course_ok = True if not selected_courses else any(c in selected_courses for c in record["course_ids"])
    lecturer_ok = True if not selected_lecturers else record["lecturer_id"] in selected_lecturers
    venue_ok = True if not selected_venues else record["venue_id"] in selected_venues

    return course_ok and lecturer_ok and venue_ok


def apply_filters(records, selected_courses=None, selected_lecturers=None, selected_venues=None):
    return [
        r for r in records
        if record_matches(r, selected_courses, selected_lecturers, selected_venues)
    ]


def get_available_courses(records, selected_lecturers=None, selected_venues=None):
    filtered = apply_filters(records, set(), selected_lecturers, selected_venues)
    result = set()
    for r in filtered:
        result.update(r["course_ids"])
    return sorted(result)


def get_available_lecturers(records, selected_courses=None, selected_venues=None):
    filtered = apply_filters(records, selected_courses, set(), selected_venues)
    return sorted({r["lecturer_id"] for r in filtered if r["lecturer_id"]})


def get_available_venues(records, selected_courses=None, selected_lecturers=None):
    filtered = apply_filters(records, selected_courses, selected_lecturers, set())
    return sorted({r["venue_id"] for r in filtered if r["venue_id"]})


def get_course_counts(records, selected_lecturers=None, selected_venues=None):
    filtered = apply_filters(records, set(), selected_lecturers, selected_venues)
    counts = {}
    for r in filtered:
        for c in r["course_ids"]:
            counts[c] = counts.get(c, 0) + 1
    return counts


def get_lecturer_counts(records, selected_courses=None, selected_venues=None):
    filtered = apply_filters(records, selected_courses, set(), selected_venues)
    counts = {}
    for r in filtered:
        lid = r["lecturer_id"]
        if lid:
            counts[lid] = counts.get(lid, 0) + 1
    return counts


def get_venue_counts(records, selected_courses=None, selected_lecturers=None):
    filtered = apply_filters(records, selected_courses, selected_lecturers, set())
    counts = {}
    for r in filtered:
        vid = r["venue_id"]
        if vid:
            counts[vid] = counts.get(vid, 0) + 1
    return counts


class CheckListFilter(QFrame):
    def __init__(self, title, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Shape.StyledPanel)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("titleLabel")

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.list_widget)

    def populate(self, values, counts=None, selected=None, enabled_values=None, block_signals=True):
        counts = counts or {}
        selected = selected or set()
        enabled_values = enabled_values or set(values)

        if block_signals:
            self.list_widget.blockSignals(True)

        old_selected = selected.copy()
        self.list_widget.clear()

        for value in values:
            count = counts.get(value, 0)
            text = f"{value} ({count})"

            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, value)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)

            if value in old_selected:
                item.setCheckState(Qt.CheckState.Checked)
            else:
                item.setCheckState(Qt.CheckState.Unchecked)

            if value not in enabled_values:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)

            self.list_widget.addItem(item)

        if block_signals:
            self.list_widget.blockSignals(False)

    def selected_values(self):
        selected = set()
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected.add(str(item.data(Qt.ItemDataRole.UserRole)))
        return selected


class TimetableExportFilterDialog(QDialog):
    def __init__(self, timetable_data, module_to_lecturer, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Export Timetable Filter")
        self.resize(1200, 700)

        self.records = flatten_timetable(timetable_data, module_to_lecturer)

        self.selected_courses = set()
        self.selected_lecturers = set()
        self.selected_venues = set()

        self.all_courses = sorted({
            c for r in self.records for c in r["course_ids"]
        })
        self.all_lecturers = sorted({
            r["lecturer_id"] for r in self.records if r["lecturer_id"]
        })
        self.all_venues = sorted({
            r["venue_id"] for r in self.records if r["venue_id"]
        })

        self.build_ui()
        self.refresh_ui()

    def build_ui(self):
        root_layout = QVBoxLayout(self)

        splitter = QSplitter()
        root_layout.addWidget(splitter)

        # Left panel
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        self.course_filter = CheckListFilter("Courses")
        self.lecturer_filter = CheckListFilter("Lecturers")
        self.venue_filter = CheckListFilter("Venues")

        left_layout.addWidget(self.course_filter)
        left_layout.addWidget(self.lecturer_filter)
        left_layout.addWidget(self.venue_filter)

        self.clear_btn = QPushButton("Clear Filters")
        left_layout.addWidget(self.clear_btn)

        # Right panel
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        self.result_label = QLabel("Showing 0 entries")

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Day", "Slot", "Module", "Lecturer", "Venue", "Courses"
        ])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)

        right_layout.addWidget(self.result_label)
        right_layout.addWidget(self.table)

        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([320, 880])

        # Signals
        self.course_filter.list_widget.itemChanged.connect(self.on_filters_changed)
        self.lecturer_filter.list_widget.itemChanged.connect(self.on_filters_changed)
        self.venue_filter.list_widget.itemChanged.connect(self.on_filters_changed)
        self.clear_btn.clicked.connect(self.clear_filters)

    def clear_filters(self):
        self.selected_courses.clear()
        self.selected_lecturers.clear()
        self.selected_venues.clear()
        self.refresh_ui()

    def on_filters_changed(self, _item=None):
        self.selected_courses = self.course_filter.selected_values()
        self.selected_lecturers = self.lecturer_filter.selected_values()
        self.selected_venues = self.venue_filter.selected_values()
        self.refresh_ui()

    def refresh_ui(self):
        filtered_records = apply_filters(
            self.records,
            self.selected_courses,
            self.selected_lecturers,
            self.selected_venues
        )

        available_courses = set(get_available_courses(
            self.records,
            self.selected_lecturers,
            self.selected_venues
        ))
        available_lecturers = set(get_available_lecturers(
            self.records,
            self.selected_courses,
            self.selected_venues
        ))
        available_venues = set(get_available_venues(
            self.records,
            self.selected_courses,
            self.selected_lecturers
        ))

        course_counts = get_course_counts(
            self.records,
            self.selected_lecturers,
            self.selected_venues
        )
        lecturer_counts = get_lecturer_counts(
            self.records,
            self.selected_courses,
            self.selected_venues
        )
        venue_counts = get_venue_counts(
            self.records,
            self.selected_courses,
            self.selected_lecturers
        )

        self.selected_courses &= set(self.all_courses)
        self.selected_lecturers &= set(self.all_lecturers)
        self.selected_venues &= set(self.all_venues)

        self.course_filter.populate(
            values=self.all_courses,
            counts=course_counts,
            selected=self.selected_courses,
            enabled_values=available_courses | self.selected_courses
        )
        self.lecturer_filter.populate(
            values=self.all_lecturers,
            counts=lecturer_counts,
            selected=self.selected_lecturers,
            enabled_values=available_lecturers | self.selected_lecturers
        )
        self.venue_filter.populate(
            values=self.all_venues,
            counts=venue_counts,
            selected=self.selected_venues,
            enabled_values=available_venues | self.selected_venues
        )

        self.populate_table(filtered_records)
        self.result_label.setText(f"Showing {len(filtered_records)} entries")

    def populate_table(self, records):
        self.table.setRowCount(len(records))

        for row, record in enumerate(records):
            values = [
                record["day_id"],
                record["slot_id"],
                record["module_id"],
                record["lecturer_id"],
                record["venue_id"],
                ", ".join(record["course_ids"]),
            ]

            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter if col != 5 else Qt.AlignLeft | Qt.AlignVCenter)
                self.table.setItem(row, col, item)


if __name__ == "__main__":
    import sys
    module_lecturer = {}
    app = QApplication(sys.argv)
    dlg = TimetableExportFilterDialog(timetable, module_lecturer)
    dlg.show()
    sys.exit(app.exec())
