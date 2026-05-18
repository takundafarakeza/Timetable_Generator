class Developers:
    @staticmethod
    def get_timetable_html(timetable: dict):
        html_data = """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <title>Timetable Viewer</title>

        <style>
            body {
                font-family: "Segoe UI", Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: #eef2f7;
                color: #1e293b;
            }

            h1 {
                text-align: center;
                margin-bottom: 25px;
                font-size: 2rem;
                color: #0f172a;
            }

            .top-bar {
                display: flex;
                justify-content: center;
                gap: 12px;
                flex-wrap: wrap;
                margin-bottom: 25px;
            }

            select,
            input {
                padding: 12px 14px;
                border: none;
                border-radius: 12px;
                background: white;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
                font-size: 14px;
                min-width: 220px;
                outline: none;
                transition: 0.2s ease;
            }

            select:focus,
            input:focus {
                transform: translateY(-1px);
                box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
            }

            #schedule {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
                gap: 18px;
            }

            .card {
                background: white;
                border-radius: 18px;
                padding: 18px;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
                transition: 0.2s ease;
                position: relative;
                overflow: hidden;
            }

            .card:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 24px rgba(0, 0, 0, 0.12);
            }

            .card::before {
                content: "";
                position: absolute;
                left: 0;
                top: 0;
                width: 6px;
                height: 100%;
                background: #2563eb;
            }

            .card h3 {
                margin: 0 0 12px 0;
                font-size: 1.2rem;
                color: #0f172a;
            }

            .meta {
                margin-top: 8px;
                font-size: 14px;
                line-height: 1.5;
                color: #475569;
            }

            .meta strong {
                color: #0f172a;
            }

            .empty {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 18px;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
                color: #64748b;
                grid-column: 1/-1;
            }

            @media screen and (max-width: 700px) {
                body {
                    padding: 14px;
                }

                h1 {
                    font-size: 1.5rem;
                }

                select,
                input {
                    width: 100%;
                    min-width: unset;
                }

                #schedule {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>

    <body>
        <h1 id="tbl-title">Test University Timetable</h1>

        <div class="top-bar">
            <select id="daySelect"></select>

            <select id="courseFilter">
                <option value="">All Programs</option>
            </select>

            <select id="levelFilter">
                <option value="">All Levels</option>
            </select>

            <select id="lecturerFilter">
                <option value="">All Lecturers</option>
            </select>

            <input
                type="text"
                id="searchInput"
                placeholder="Search module, lecturer, venue..."
            />
        </div>

        <div id="schedule"></div>

        <script>
            /*
    POPULATE COURSE AND LECTURER FILTERS
*/

            function populateFilters() {
                /*
        COURSES
    */

                const courseSelect = document.getElementById("courseFilter");

                for (const id in timetableData.courses) {
                    const course = timetableData.courses[id];

                    const option = document.createElement("option");

                    option.value = id;

                    option.textContent = `${course.short_name} - ${course.name}`;

                    courseSelect.appendChild(option);
                }

                if (Object.keys(timetableData.days).length === 0) {
                    for (const day in timetableData.time_table) {
                        const option = document.createElement("option");

                        option.value = day;

                        option.textContent = `Day ${day}`;
                        document
                            .getElementById("daySelect")
                            .appendChild(option);
                    }
                } else {
                    for (const day in timetableData.days) {
                        const dayData = timetableData.days[day];

                        const option = document.createElement("option");

                        option.value = day;

                        option.textContent = dayData;

                        document
                            .getElementById("daySelect")
                            .appendChild(option);
                    }
                }
                /*
        LECTURERS
    */

                const lecturerSelect =
                    document.getElementById("lecturerFilter");

                for (const id in timetableData.lecturers) {
                    if (id === "unavailable") {
                        continue;
                    }

                    const lecturer = timetableData.lecturers[id];

                    const option = document.createElement("option");

                    option.value = id;

                    option.textContent = lecturer.name;

                    lecturerSelect.appendChild(option);
                }
            }

            function populateLevels() {
                const levelSelect = document.getElementById("levelFilter");

                const levels = new Set();

                for (const day in timetableData.time_table) {
                    const dayData = timetableData.time_table[day];

                    for (const slot in dayData) {
                        const slotData = dayData[slot];

                        for (const moduleId in slotData) {
                            const entry = slotData[moduleId];

                            entry.courses.forEach((course) => {
                                const [, level] = course.split("-");

                                levels.add(level);
                            });
                        }
                    }
                }

                [...levels].sort().forEach((level) => {
                    const option = document.createElement("option");

                    option.value = level;

                    option.textContent = level;

                    levelSelect.appendChild(option);
                });
            }

/*
    EMBEDDED TIMETABLE DATA
*/
        """

        html_data += f"const timetableData = {timetable}; \n"

        html_data += """
/*
    SLOT LABELS
*/

            const slotLabels = timetableData.slots;
            document.getElementById("tbl-title").textContent =
                `${timetableData.time_table_name}`;

            /*
    MAIN RENDER FUNCTION
*/

            function renderDayFromData(day, data) {
                const container = document.getElementById("schedule");

                container.innerHTML = "";

                const searchText = document
                    .getElementById("searchInput")
                    .value.toLowerCase();

                const dayData = data[day];

                if (!dayData) {
                    container.innerHTML = `
                        <div class="empty">
                            No timetable data available.
                        </div>
                    `;

                    return;
                }

                let found = false;

                for (const slot in dayData) {
                    const slotData = dayData[slot];

                    for (const moduleId in slotData) {
                        const entry = slotData[moduleId];

                        const module = timetableData.modules[moduleId];

                        const lecturer =
                            timetableData.lecturers[module.lecturer];

                        const venue = timetableData.venues[entry.venue];

                        module_courses = module.courses;
                        var modules_names = "";
                        var modules_codes = "";

                        for (courseId in module_courses) {
                            var course_module_code =
                                module_courses[courseId].course_module_code;
                            if (course_module_code != module.code) {
                                m_id =
                                    TimetableAPI.getModuleByCode(
                                        course_module_code,
                                    );
                                m_name = TimetableAPI.getModule(m_id);
                                modules_names += m_name.name + ", and ";
                                modules_codes += m_name.code + ", ";
                            }
                        }

                        const textBlob = `
                            ${modules_names + module.name}
                            ${module.code}
                            ${lecturer.name}
                            ${venue.name}
                        `.toLowerCase();

                        if (searchText && !textBlob.includes(searchText)) {
                            continue;
                        }

                        found = true;

                        const card = document.createElement("div");

                        card.className = "card";

                        card.innerHTML = `

                        <h3>${modules_names + module.name}</h3>

                        <div class="meta">
                            <strong>Code:</strong>
                            ${modules_codes + module.code}
                        </div>

                        <div class="meta">
                            <strong>Time:</strong>
                            ${slotLabels[slot] || "Slot " + slot}
                        </div>

                        <div class="meta">
                            <strong>Venue:</strong>
                            ${venue.name}
                        </div>

                        <div class="meta">
                            <strong>Lecturer:</strong>
                            ${lecturer.name}
                        </div>

                        <div class="meta">
                            <strong>Programs:</strong>

                            ${entry.courses
                                .map((course) => {
                                    const [courseId, level] = course.split("-");

                                    const courseInfo =
                                        timetableData.courses[courseId];

                                    return `
                                    ${courseInfo.short_name}
                                    ${level}
                                `;
                                })
                                .join(", ")}

                        </div>

                        `;

                        container.appendChild(card);
                    }
                }

                if (!found) {
                    container.innerHTML = `
            <div class="empty">
                No matching schedule found.
            </div>
        `;
                }
            }

            function renderDay(day) {
                const container = document.getElementById("schedule");

                container.innerHTML = "";

                const searchText = document
                    .getElementById("searchInput")
                    .value.toLowerCase();

                const dayData = timetableData.time_table[day];

                if (!dayData) {
                    container.innerHTML = `
            <div class="empty">
                No timetable data available.
            </div>
        `;

                    return;
                }

                let found = false;

                for (const slot in dayData) {
                    const slotData = dayData[slot];

                    for (const moduleId in slotData) {
                        const entry = slotData[moduleId];

                        const module = timetableData.modules[moduleId];

                        const lecturer =
                            timetableData.lecturers[module.lecturer];

                        const venue = timetableData.venues[entry.venue];

                        module_courses = module.courses;
                        var modules_names = "";
                        var modules_codes = "";

                        for (courseId in module_courses) {
                            var course_module_code =
                                module_courses[courseId].course_module_code;
                            if (course_module_code != module.code) {
                                m_id =
                                    TimetableAPI.getModuleByCode(
                                        course_module_code,
                                    );
                                m_name = TimetableAPI.getModule(m_id);
                                modules_names += m_name.name + ", and ";
                                modules_codes += m_name.code + ", ";
                            }
                        }

                        const textBlob = `
                            ${modules_names + module.name}
                            ${module.code}
                            ${lecturer.name}
                            ${venue.name}
                        `.toLowerCase();

                        if (searchText && !textBlob.includes(searchText)) {
                            continue;
                        }

                        found = true;

                        const card = document.createElement("div");

                        card.className = "card";

                        card.innerHTML = `

                        <h3>${modules_names + module.name}</h3>

                        <div class="meta">
                            <strong>Code:</strong>
                            ${modules_codes + module.code}
                        </div>

                <div class="meta">
                    <strong>Time:</strong>
                    ${slotLabels[slot]}
                </div>

                <div class="meta">
                    <strong>Venue:</strong>
                    ${venue.name}
                </div>

                <div class="meta">
                    <strong>Lecturer:</strong>
                    ${lecturer.name}
                </div>

                <div class="meta">
                    <strong>Programs:</strong>

                    ${entry.courses
                        .map((course) => {
                            const [courseId, level] = course.split("-");

                            const courseInfo = timetableData.courses[courseId];

                            return `
                            ${courseInfo.short_name}
                            ${level}
                        `;
                        })
                        .join(", ")}

                </div>

            `;

                        container.appendChild(card);
                    }
                }

                if (!found) {
                    container.innerHTML = `
            <div class="empty">
                No matching schedule found.
            </div>
        `;
                }
            }

            /*
    API FOR DEVELOPERS
*/

            /*
================================================================

    TIMETABLE API

    This API provides lightweight access to timetable data embedded
    within this exported HTML document. It is intended for timetable
    viewing, filtering, iframe embedding, and frontend integrations.

    IMPORTANT:
    - All data is publicly accessible on the client side.
    - This is NOT a secure backend service.
    - No authentication or encryption is implemented.
    - The API is designed for read-only operations only.
    - Data validity depends on the exported timetable source.

    Recommended usage:
    - Student timetable lookup
    - Lecturer schedule lookup
    - Institutional timetable portals
    - Embedded timetable viewers

================================================================
*/

            window.TimetableAPI = {
                // GET FULL DAY SCHEDULE

                getDaySchedule(day) {
                    return timetableData.time_table[day] || {};
                },

                // GET MODULE INFO

                getModule(moduleId) {
                    return timetableData.modules[moduleId];
                },

                getModuleByCode(module_code) {
                    for (moduleId in timetableData.modules) {
                        module_det = timetableData.modules[moduleId];
                        if (module_det.code == module_code) {
                            return moduleId;
                        }
                    }
                },

                // GET VENUE INFO
                getVenue(venueId) {
                    return timetableData.venues[venueId];
                },

                // GET LECTURER INFO
                getLecturer(lecturerId) {
                    return timetableData.lecturers[lecturerId];
                },

                /*
        GET COURSE TIMETABLE

        Example:
        TimetableAPI.getCourseSchedule("1")
    */
                getCourseSchedule(courseId, level = null) {
                    const filtered = {};

                    for (const day in timetableData.time_table) {
                        const dayData = timetableData.time_table[day];

                        const filteredDay = {};

                        for (const slot in dayData) {
                            const slotData = dayData[slot];

                            const filteredSlot = {};

                            for (const moduleId in slotData) {
                                const entry = slotData[moduleId];

                                const found = entry.courses.some((course) => {
                                    const [id, lvl] = course.split("-");

                                    if (level) {
                                        return id === courseId && lvl === level;
                                    }

                                    return id === courseId;
                                });

                                if (found) {
                                    filteredSlot[moduleId] = entry;
                                }
                            }

                            if (Object.keys(filteredSlot).length) {
                                filteredDay[slot] = filteredSlot;
                            }
                        }

                        if (Object.keys(filteredDay).length) {
                            filtered[day] = filteredDay;
                        }
                    }

                    return filtered;
                },

                /*
        GET LECTURER TIMETABLE

        Example:
        TimetableAPI.getLecturerSchedule("3")
    */
                getLecturerSchedule(lecturerId) {
                    const filtered = {};

                    for (const day in timetableData.time_table) {
                        const dayData = timetableData.time_table[day];

                        const filteredDay = {};

                        for (const slot in dayData) {
                            const slotData = dayData[slot];

                            const filteredSlot = {};

                            for (const moduleId in slotData) {
                                const module = timetableData.modules[moduleId];

                                if (module.lecturer === lecturerId) {
                                    filteredSlot[moduleId] = slotData[moduleId];
                                }
                            }

                            if (Object.keys(filteredSlot).length) {
                                filteredDay[slot] = filteredSlot;
                            }
                        }

                        if (Object.keys(filteredDay).length) {
                            filtered[day] = filteredDay;
                        }
                    }

                    return filtered;
                },
            };

            /*
    EVENTS

    Dropdown change events trigger a re-render of the timetable 
    based on the selected filters. The search input triggers a re-render on every 
    input to filter the displayed schedule in real-time.
*/

            document
                .getElementById("courseFilter")
                .addEventListener("change", renderCurrentView);

            document
                .getElementById("levelFilter")
                .addEventListener("change", renderCurrentView);

            document
                .getElementById("lecturerFilter")
                .addEventListener("change", renderCurrentView);

            document
                .getElementById("daySelect")
                .addEventListener("change", (e) => renderCurrentView());

            document
                .getElementById("searchInput")
                .addEventListener("input", () => {
                    renderCurrentView();
                });

            /*
    INITIAL RENDER
*/
            function renderCurrentView() {
                const day = document.getElementById("daySelect").value;

                const courseId = document.getElementById("courseFilter").value;

                const level = document.getElementById("levelFilter").value;

                const lecturerId =
                    document.getElementById("lecturerFilter").value;

                let data = timetableData.time_table;

                if (courseId) {
                    data = TimetableAPI.getCourseSchedule(
                        courseId,
                        level || null,
                    );
                }

                if (lecturerId) {
                    data = TimetableAPI.getLecturerSchedule(lecturerId);
                    document.getElementById("courseFilter").selectedIndex = 0;
                    document.getElementById("levelFilter").selectedIndex = 0;
                }

                renderDayFromData(day, data);
            }

            populateLevels();
            populateFilters();
            renderDay("1");
        </script>
    </body>
</html>

        """
        return html_data\


    @staticmethod
    def get_js_api(timetable: dict):
        js_api = f"const timetableData = {timetable};" + """
window.TimetableAPI = {
    version: "1.0.0",

    // RAW DATA ACCESS (ADVANCED USERS)
    data: timetableData,

    // =========================
    // METADATA
    // =========================

    getMetadata() {
        return {
            name: timetableData.time_table_name,
            institution: timetableData.institution_name,
            type: timetableData.institution_type,
            slot_length: timetableData.time_slot_length,
            days_per_cycle: timetableData.days_per_cycle,
            slots_per_day: timetableData.slots_per_day,
        };
    },

    // =========================
    // BASIC LOOKUPS
    // =========================

    getDay(dayId) {
        return timetableData.days[dayId];
    },

    getSlot(slotId) {
        return timetableData.slots[slotId];
    },

    getCourse(courseId) {
        return timetableData.courses[courseId];
    },

    getModule(moduleId) {
        return timetableData.modules[moduleId];
    },

    getVenue(venueId) {
        return timetableData.venues[venueId];
    },

    getLecturer(lecturerId) {
        return timetableData.lecturers[lecturerId];
    },

    getModuleByCode(moduleCode) {
        for (const moduleId in timetableData.modules) {
            const module = timetableData.modules[moduleId];

            if (module.code === moduleCode) {
                return moduleId;
            }
        }

        return null;
    },

    // =========================
    // SCHEDULE GETTERS
    // =========================

    getDaySchedule(day) {
        return timetableData.time_table[day] || {};
    },

    getSlotSchedule(day, slot) {
        return timetableData.time_table?.[day]?.[slot] || {};
    },

    getCourseSchedule(courseId, level = null) {
        const filtered = {};

        for (const day in timetableData.time_table) {
            const dayData = timetableData.time_table[day];

            const filteredDay = {};

            for (const slot in dayData) {
                const slotData = dayData[slot];

                const filteredSlot = {};

                for (const moduleId in slotData) {
                    const entry = slotData[moduleId];

                    const found = entry.courses.some((course) => {
                        const [id, lvl] = course.split("-");

                        if (level) {
                            return id === courseId && lvl === level;
                        }

                        return id === courseId;
                    });

                    if (found) {
                        filteredSlot[moduleId] = entry;
                    }
                }

                if (Object.keys(filteredSlot).length) {
                    filteredDay[slot] = filteredSlot;
                }
            }

            if (Object.keys(filteredDay).length) {
                filtered[day] = filteredDay;
            }
        }

        return filtered;
    },

    getLecturerSchedule(lecturerId) {
        const filtered = {};

        for (const day in timetableData.time_table) {
            const dayData = timetableData.time_table[day];

            const filteredDay = {};

            for (const slot in dayData) {
                const slotData = dayData[slot];

                const filteredSlot = {};

                for (const moduleId in slotData) {
                    const module = timetableData.modules[moduleId];

                    if (module.lecturer === lecturerId) {
                        filteredSlot[moduleId] = slotData[moduleId];
                    }
                }

                if (Object.keys(filteredSlot).length) {
                    filteredDay[slot] = filteredSlot;
                }
            }

            if (Object.keys(filteredDay).length) {
                filtered[day] = filteredDay;
            }
        }

        return filtered;
    },

    getVenueSchedule(venueId) {
        const filtered = {};

        for (const day in timetableData.time_table) {
            const dayData = timetableData.time_table[day];

            const filteredDay = {};

            for (const slot in dayData) {
                const slotData = dayData[slot];

                const filteredSlot = {};

                for (const moduleId in slotData) {
                    const entry = slotData[moduleId];

                    if (entry.venue === venueId) {
                        filteredSlot[moduleId] = entry;
                    }
                }

                if (Object.keys(filteredSlot).length) {
                    filteredDay[slot] = filteredSlot;
                }
            }

            if (Object.keys(filteredDay).length) {
                filtered[day] = filteredDay;
            }
        }

        return filtered;
    },

    // =========================
    // FREE VENUES
    // =========================

    getFreeVenues(day, slot) {
        const usedVenues = new Set();

        const slotData = timetableData.time_table?.[day]?.[slot] || {};

        for (const moduleId in slotData) {
            usedVenues.add(slotData[moduleId].venue);
        }

        const freeVenues = {};

        for (const venueId in timetableData.venues) {
            if (!usedVenues.has(venueId)) {
                freeVenues[venueId] = timetableData.venues[venueId];
            }
        }

        return freeVenues;
    },

    // =========================
    // COURSE MODULES
    // =========================

    getCourseModules(courseId, level = null) {
        const modules = {};

        for (const moduleId in timetableData.modules) {
            const module = timetableData.modules[moduleId];

            for (const cid in module.courses) {
                const details = module.courses[cid];

                if (cid === courseId) {
                    if (!level || details.level === level) {
                        modules[moduleId] = module;
                    }
                }
            }
        }

        return modules;
    },

    // =========================
    // SEARCH
    // =========================

    searchModules(query) {
        const results = {};

        query = query.toLowerCase();

        for (const moduleId in timetableData.modules) {
            const module = timetableData.modules[moduleId];

            if (
                module.name.toLowerCase().includes(query) ||
                module.code.toLowerCase().includes(query)
            ) {
                results[moduleId] = module;
            }
        }

        return results;
    },

    // =========================
    // FORMATTERS
    // =========================

    formatEntry(moduleId, entry) {
        const module = timetableData.modules[moduleId];

        const lecturer = timetableData.lecturers[module.lecturer];

        const venue = timetableData.venues[entry.venue];

        return {
            module_id: moduleId,
            module_name: module.name,
            module_code: module.code,
            lecturer: lecturer?.name || "Unknown",
            venue: venue?.name || "Unknown",
            courses: entry.courses,
        };
    },

    // =========================
    // FLAT SCHEDULE
    // =========================

    getFlatSchedule() {
        const output = [];

        for (const day in timetableData.time_table) {
            const dayData = timetableData.time_table[day];

            for (const slot in dayData) {
                const slotData = dayData[slot];

                for (const moduleId in slotData) {
                    const entry = slotData[moduleId];

                    const module = timetableData.modules[moduleId];

                    const lecturer = timetableData.lecturers[module.lecturer];

                    const venue = timetableData.venues[entry.venue];

                    output.push({
                        day_id: day,
                        day: timetableData.days[day],

                        slot_id: slot,
                        slot: timetableData.slots[slot],

                        module_id: moduleId,
                        module_name: module.name,
                        module_code: module.code,

                        lecturer_id: module.lecturer,
                        lecturer: lecturer?.name || "Unknown",

                        venue_id: entry.venue,
                        venue: venue?.name || "Unknown",

                        courses: entry.courses,
                    });
                }
            }
        }

        return output;
    },
};
        """
        return js_api
