const timetableData = {
    time_table_name: "First Semester",
    institution_type: "college",
    institution_name: "Midlands State University",
    time_slot_length: 120,
    days_per_cycle: 5,
    slots_per_day: 4,
    slots: {
        1: "08:00 - 10:00",
        2: "10:00 - 12:00",
        3: "12:00 - 14:00",
        4: "14:00 - 16:00",
    },
    days: {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
    },
    break_slots: [],
    sequence: { courses: 4, modules: 62, venues: 10, lecturers: 28, blocks: 0 },
    courses: {
        1: { name: "Computer Science", short_name: "CS" },
        2: { name: "Computer Systems Engineering", short_name: "CSE" },
        3: { name: "Cybersecurity", short_name: "CSC" },
        4: { name: "Software Engineering", short_name: "SWE" },
    },
    modules: {
        1: {
            name: "Basics of Communication Skills",
            code: "CS131",
            lecturer: "1",
            courses: {
                2: { level: "1.1", course_module_code: "CS131" },
                1: { level: "1.1", course_module_code: "CS131" },
                4: { level: "1.1", course_module_code: "CS131" },
                3: { level: "1.1", course_module_code: "CS131" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        2: {
            name: "Gender Studies",
            code: "GS231",
            lecturer: "2",
            courses: {
                2: { level: "2.1", course_module_code: "GS231" },
                1: { level: "2.1", course_module_code: "GS231" },
                4: { level: "2.1", course_module_code: "GS231" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        3: {
            name: "Principles of Programming Languages",
            code: "HCSCI132",
            lecturer: "3",
            courses: {
                2: { level: "1.1", course_module_code: "HCSCI132" },
                1: { level: "1.1", course_module_code: "HCSCI132" },
                4: { level: "1.1", course_module_code: "HCSCI132" },
                3: { level: "1.1", course_module_code: "HCSCI132" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        4: {
            name: "Operating Systems",
            code: "HCSCI133",
            lecturer: "4",
            courses: {
                1: { level: "1.1", course_module_code: "HCSCI133" },
                4: { level: "1.1", course_module_code: "HCSCI133" },
                3: { level: "1.1", course_module_code: "HCSCI133" },
                2: { level: "2.1", course_module_code: "HCSCI133" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        5: {
            name: "Fundamentals of Digital Electronics",
            code: "HCSCI134",
            lecturer: "5",
            courses: { 1: { level: "1.1", course_module_code: "HCSCI134" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        6: {
            name: "Computer Architecture and Organization",
            code: "HCSCI135",
            lecturer: "6",
            courses: {
                1: { level: "1.2", course_module_code: "HCSCI135" },
                4: { level: "1.2", course_module_code: "HCSCI135" },
                3: { level: "1.2", course_module_code: "HCSCI135" },
                2: { level: "2.1", course_module_code: "HCSCI135" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        7: {
            name: "Data Structures and Algorithms",
            code: "HCSCI136",
            lecturer: "7",
            courses: {
                2: { level: "1.2", course_module_code: "HCSCI136" },
                1: { level: "1.2", course_module_code: "HCSCI136" },
                4: { level: "1.2", course_module_code: "HCSCI136" },
                3: { level: "1.2", course_module_code: "HCSCI136" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        8: {
            name: "Software Engineering",
            code: "HCSCI137",
            lecturer: "8",
            courses: { 1: { level: "1.2", course_module_code: "HCSCI137" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        9: {
            name: "Fundamentals of Digital Technologies and Artificial Intelligence",
            code: "HCSCI138",
            lecturer: "9",
            courses: {
                2: { level: "1.1", course_module_code: "HCSCI138" },
                1: { level: "1.1", course_module_code: "HCSCI138" },
                4: { level: "1.1", course_module_code: "HCSCI138" },
                3: { level: "1.1", course_module_code: "HCSCI138" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        10: {
            name: "Web Development",
            code: "HCSCI231",
            lecturer: "7",
            courses: { 1: { level: "2.1", course_module_code: "HCSCI231" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        11: {
            name: "Systems Analysis and Design",
            code: "HCSCI232",
            lecturer: "10",
            courses: { 1: { level: "2.1", course_module_code: "HCSCI232" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        12: {
            name: "Computer Security",
            code: "HCSCI233",
            lecturer: "7",
            courses: { 1: { level: "2.1", course_module_code: "HCSCI233" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        13: {
            name: "Research Methods",
            code: "HCSCI234",
            lecturer: "11",
            courses: {
                1: { level: "2.1", course_module_code: "HCSCI234" },
                4: { level: "2.1", course_module_code: "HCSCI234" },
                2: { level: "4.1", course_module_code: "HCSCI234" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        14: {
            name: "Software Project Management",
            code: "HCSCI235",
            lecturer: "11",
            courses: {
                4: { level: "2.1", course_module_code: "HCSCI235" },
                1: { level: "2.2", course_module_code: "HCSCI235" },
                2: { level: "4.2", course_module_code: "HCSE437" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        15: {
            name: "Data Communications and Computer Networks",
            code: "HCSCI237",
            lecturer: "10",
            courses: {
                2: { level: "2.2", course_module_code: "HCSCI237" },
                1: { level: "2.2", course_module_code: "HCSCI237" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        16: {
            name: "Design and Analysis of Algorithms",
            code: "HCSCI238",
            lecturer: "12",
            courses: {
                2: { level: "2.2", course_module_code: "HCSCI238" },
                1: { level: "2.2", course_module_code: "HCSCI238" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        17: {
            name: "Digital Image Processing",
            code: "HCSCI239",
            lecturer: "13",
            courses: { 1: { level: "2.2", course_module_code: "HCSCI239" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        18: {
            name: "Theory of Computation",
            code: "HCSCI431",
            lecturer: "4",
            courses: { 1: { level: "4.1", course_module_code: "HCSCI431" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        19: {
            name: "Simulation and Modelling",
            code: "HCSCI432",
            lecturer: "7",
            courses: { 1: { level: "4.1", course_module_code: "HCSCI432" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        20: {
            name: "Parallel and Distributed Computing",
            code: "HCSCI433",
            lecturer: "4",
            courses: {
                2: { level: "4.1", course_module_code: "HCSCI433" },
                1: { level: "4.1", course_module_code: "HCSCI433" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        21: {
            name: "Artificial Intelligence",
            code: "HCSCI434",
            lecturer: "14",
            courses: { 1: { level: "4.1", course_module_code: "HCSCI434" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        22: {
            name: "Computer Graphics",
            code: "HCSCI435",
            lecturer: "14",
            courses: { 1: { level: "4.2", course_module_code: "HCSCI435" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        23: {
            name: "Human Computer Interaction",
            code: "HCSCI437",
            lecturer: "14",
            courses: { 1: { level: "4.2", course_module_code: "HCSCI437" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        24: {
            name: "Fundamentals of Data Science and Big Data",
            code: "HCSCI439",
            lecturer: "15",
            courses: {
                2: { level: "4.2", course_module_code: "HCSCI439" },
                1: { level: "4.2", course_module_code: "HCSCI439" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        25: {
            name: "Introduction to Computer Engineering",
            code: "HCSE131",
            lecturer: "3",
            courses: { 2: { level: "1.1", course_module_code: "HCSE131" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        26: {
            name: "Ethics and Professionalism",
            code: "HCSE133",
            lecturer: "16",
            courses: {
                1: { level: "1.1", course_module_code: "HCSE133" },
                2: { level: "1.2", course_module_code: "HCSE133" },
                4: { level: "1.2", course_module_code: "HCSE133" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        27: {
            name: "Electrical and Electronic Principles",
            code: "HCSE134",
            lecturer: "17",
            courses: { 2: { level: "1.2", course_module_code: "HCSE134" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        28: {
            name: "Database Systems",
            code: "HCSE135",
            lecturer: "4",
            courses: {
                1: { level: "1.2", course_module_code: "HCSE135" },
                4: { level: "1.2", course_module_code: "HCSE135" },
                3: { level: "1.2", course_module_code: "HCSE135" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        29: {
            name: "Digital Electronics and Logic Design",
            code: "HCSE137",
            lecturer: "5",
            courses: { 2: { level: "1.2", course_module_code: "HCSE137" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        30: {
            name: "Discrete Mathematics",
            code: "HCSE138",
            lecturer: "18",
            courses: {
                4: { level: "1.1", course_module_code: "HCSE138" },
                3: { level: "1.1", course_module_code: "HCSE138" },
                2: { level: "1.2", course_module_code: "HCSE138" },
                1: { level: "1.2", course_module_code: "HCSE138" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        31: {
            name: "Object Oriented Programming",
            code: "HCSE224",
            lecturer: "12",
            courses: {
                4: { level: "2.1", course_module_code: "HCSE224" },
                2: { level: "2.2", course_module_code: "HCSE224" },
                1: { level: "2.2", course_module_code: "HCSE224" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        32: {
            name: "Object Oriented Analysis and Design",
            code: "HCSE231",
            lecturer: "9",
            courses: { 2: { level: "2.1", course_module_code: "HCSE231" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        33: {
            name: "Engineering Statistics",
            code: "HCSE232",
            lecturer: "23",
            courses: { 2: { level: "2.1", course_module_code: "HCSE232" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        34: {
            name: "Linear Algebra",
            code: "HCSE233",
            lecturer: "27",
            courses: { 2: { level: "2.1", course_module_code: "HCSE233" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        35: {
            name: "Web and Mobile Application Development",
            code: "HCSE235",
            lecturer: "12",
            courses: { 2: { level: "2.2", course_module_code: "HCSE235" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        36: {
            name: "Microprocessors and Microcontroller Systems",
            code: "HCSE431",
            lecturer: "24",
            courses: { 2: { level: "4.1", course_module_code: "HCSE431" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        37: {
            name: "Embedded Systems",
            code: "HCSE432",
            lecturer: "5",
            courses: { 2: { level: "4.1", course_module_code: "HCSE432" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        38: {
            name: "IoT and Cloud Systems Engineering",
            code: "HCSE433",
            lecturer: "24",
            courses: {
                2: { level: "4.1", course_module_code: "HCSE433" },
                1: { level: "4.1", course_module_code: "HCSE433" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        39: {
            name: "Control System Engineering",
            code: "HCSE436",
            lecturer: "24",
            courses: { 2: { level: "4.2", course_module_code: "HCSE436" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        40: {
            name: "Project Management",
            code: "HCSE437",
            lecturer: "11",
            courses: {},
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        41: {
            name: "Network Security and Cryptography",
            code: "HCSE439",
            lecturer: "11",
            courses: {
                2: { level: "4.2", course_module_code: "HCSE439" },
                1: { level: "4.2", course_module_code: "HCSE439" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        42: {
            name: "Introduction to Information Security",
            code: "HCSEC111",
            lecturer: "6",
            courses: { 3: { level: "1.1", course_module_code: "HCSEC111" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        43: {
            name: "Cyberspace Ethics and Laws",
            code: "HCSEC122",
            lecturer: "13",
            courses: { 3: { level: "1.2", course_module_code: "HCSEC122" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        44: {
            name: "Principles of Secure Coding",
            code: "HCSEC123",
            lecturer: "19",
            courses: { 3: { level: "1.2", course_module_code: "HCSEC123" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        45: {
            name: "Forensics and Incident Response",
            code: "HCSEC125",
            lecturer: "20",
            courses: { 3: { level: "1.2", course_module_code: "HCSEC125" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        46: {
            name: "Network Programming",
            code: "HCSEC221",
            lecturer: "19",
            courses: { 3: { level: "2.2", course_module_code: "HCSEC221" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        47: {
            name: "Cryptography",
            code: "HCSEC222",
            lecturer: "20",
            courses: { 3: { level: "2.2", course_module_code: "HCSEC222" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        48: {
            name: "Ethical Hacking",
            code: "HCSEC223",
            lecturer: "20",
            courses: { 3: { level: "2.2", course_module_code: "HCSEC223" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        49: {
            name: "Calculus 1",
            code: "HMAT131",
            lecturer: "22",
            courses: { 2: { level: "1.1", course_module_code: "HMAT131" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        50: {
            name: "Applied Statistics",
            code: "HSTA132",
            lecturer: "23",
            courses: {
                4: { level: "1.2", course_module_code: "HSTA132" },
                1: { level: "2.1", course_module_code: "HSTA132" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        51: {
            name: "Software Engineering Fundamentals",
            code: "HSWE111",
            lecturer: "8",
            courses: {
                4: { level: "1.1", course_module_code: "HSWE111" },
                3: { level: "1.2", course_module_code: "HSWE111" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        52: {
            name: "Visual Programming",
            code: "HSWE121",
            lecturer: "12",
            courses: { 4: { level: "1.2", course_module_code: "HSWE121" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        53: {
            name: "Computer Networks and Information Security",
            code: "HSWE122",
            lecturer: "10",
            courses: { 4: { level: "1.2", course_module_code: "HSWE122" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        54: {
            name: "Requirements Engineering",
            code: "HSWE212",
            lecturer: "20",
            courses: { 4: { level: "2.1", course_module_code: "HSWE212" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        55: {
            name: "Web Technologies",
            code: "HSWE221",
            lecturer: "7",
            courses: {
                4: { level: "2.2", course_module_code: "HSWE221" },
                3: { level: "2.2", course_module_code: "HSWE221" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        56: {
            name: "Software Architecture and Design",
            code: "HSWE222",
            lecturer: "8",
            courses: { 4: { level: "2.2", course_module_code: "HSWE222" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        57: {
            name: "Advanced Database Systems",
            code: "HSWE223",
            lecturer: "19",
            courses: { 4: { level: "2.2", course_module_code: "HSWE223" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        58: {
            name: "Mobile Application Development",
            code: "HSWE225",
            lecturer: "19",
            courses: { 4: { level: "2.2", course_module_code: "HSWE225" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        59: {
            name: "Physics for Engineers",
            code: "HTENG133",
            lecturer: "28",
            courses: {
                2: { level: "1.1", course_module_code: "HTENG133" },
                1: { level: "1.2", course_module_code: "HTENG133" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        60: {
            name: "Digital Signal Processing",
            code: "HTENG237",
            lecturer: "26",
            courses: { 2: { level: "2.2", course_module_code: "HTENG237" } },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        61: {
            name: "Communications Network Design",
            code: "HTENG432",
            lecturer: "25",
            courses: {
                2: { level: "4.1", course_module_code: "HTENG432" },
                1: { level: "4.1", course_module_code: "HTENG432" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
        62: {
            name: "Technopreneurship",
            code: "TCNP201",
            lecturer: "21",
            courses: {
                2: { level: "2.1", course_module_code: "TCNP201" },
                1: { level: "2.1", course_module_code: "TCNP201" },
                4: { level: "2.1", course_module_code: "TCNP201" },
            },
            venues: [],
            time_slots: 2,
            slots_per_day: 1,
            duration: 1,
        },
    },
    venues: {
        unavailable: {
            name: "Unavailable",
            capacity: 0,
            special: "Yes",
            location: [0, 0],
            location_description: "Unavailable",
        },
        1: {
            name: "Science Lab",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        2: {
            name: "Lab 30",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        3: {
            name: "Lab 1",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        4: {
            name: "Lab 2",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        5: {
            name: "RSSB 4",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        6: {
            name: "RSSB 6",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        7: {
            name: "RSSB 9",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        8: {
            name: "RSSB 15",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        9: {
            name: "ELT",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
        10: {
            name: "Physics Lab 1",
            capacity: 60,
            special: "No",
            location: [0, 0],
            location_description: "Na",
        },
    },
    lecturers: {
        unavailable: { name: "Unavailable" },
        1: { name: "Dr F. Mutema" },
        2: { name: "Dr J. Katsande" },
        3: { name: "Mrs N. Sarai" },
        4: { name: "Mr O. Muzurura" },
        5: { name: "Mr P. Mbire" },
        6: { name: "Mr A. Mukwembi" },
        7: { name: "Mr D. Mpini" },
        8: { name: "Mr S. Kativu" },
        9: { name: "Ms C. Ngwenya" },
        10: { name: "Mr T. Mzikamwi" },
        11: { name: "Mr T.G. Rebanowako" },
        12: { name: "Mr A. Tigere" },
        13: { name: "Ms A.K. Sibanda" },
        14: { name: "Mr P.S. Mupfiga" },
        15: { name: "Mr H. Mafukidze" },
        16: { name: "Miss A.K. Sibanda" },
        17: { name: "Mr B. Siyachingoma" },
        18: { name: "Mrs L. Gonzo" },
        19: { name: "Mr D. Mashoko" },
        20: { name: "Mr T. Nemaramba" },
        21: { name: "Mr Mveku" },
        22: { name: "Mr Tapedzisa" },
        23: { name: "Ms Chipumuro" },
        24: { name: "Mr K. Moyo" },
        25: { name: "Mr Ndondo" },
        26: { name: "Mr L.T. Dube" },
        27: { name: "Mrs P. Mukwembi" },
        28: { name: "Dr V.E. Gora" },
    },
    capacities: {
        1: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        2: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        3: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        4: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        5: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        6: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        7: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        8: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        9: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
        10: {
            1.1: { capacity: 0 },
            1.2: { capacity: 0 },
            2.1: { capacity: 0 },
            2.2: { capacity: 0 },
            3.1: { capacity: 0 },
            3.2: { capacity: 0 },
            4.1: { capacity: 0 },
            4.2: { capacity: 0 },
            5.1: { capacity: 0 },
            5.2: { capacity: 0 },
        },
    },
    time_table: {
        1: {
            1: {
                2: { venue: "1", courses: ["2-2.1", "1-2.1", "4-2.1"] },
                30: {
                    venue: "3",
                    courses: ["4-1.1", "3-1.1", "2-1.2", "1-1.2"],
                },
                38: { venue: "7", courses: ["2-4.1", "1-4.1"] },
                47: { venue: "2", courses: ["3-2.2"] },
                52: { venue: "4", courses: ["4-1.2"] },
            },
            2: {
                4: {
                    venue: "9",
                    courses: ["1-1.1", "4-1.1", "3-1.1", "2-2.1"],
                },
                14: { venue: "8", courses: ["4-2.1", "1-2.2", "2-4.2"] },
                23: { venue: "5", courses: ["1-4.2"] },
                36: { venue: "4", courses: ["2-4.1"] },
                46: { venue: "2", courses: ["3-2.2"] },
                49: { venue: "10", courses: ["2-1.1"] },
            },
            3: {
                5: { venue: "2", courses: ["1-1.1"] },
                10: { venue: "9", courses: ["1-2.1"] },
                15: { venue: "5", courses: ["2-2.2", "1-2.2"] },
                22: { venue: "6", courses: ["1-4.2"] },
                27: { venue: "10", courses: ["2-1.2"] },
                33: { venue: "1", courses: ["2-2.1"] },
                61: { venue: "7", courses: ["2-4.1", "1-4.1"] },
            },
            4: {
                7: {
                    venue: "9",
                    courses: ["2-1.2", "1-1.2", "4-1.2", "3-1.2"],
                },
                9: {
                    venue: "7",
                    courses: ["2-1.1", "1-1.1", "4-1.1", "3-1.1"],
                },
                11: { venue: "10", courses: ["1-2.1"] },
                17: { venue: "2", courses: ["1-2.2"] },
                20: { venue: "5", courses: ["2-4.1", "1-4.1"] },
            },
        },
        2: {
            1: {
                2: { venue: "1", courses: ["2-2.1", "1-2.1", "4-2.1"] },
                51: { venue: "2", courses: ["4-1.1", "3-1.2"] },
                53: { venue: "6", courses: ["4-1.2"] },
                57: { venue: "10", courses: ["4-2.2"] },
                59: { venue: "5", courses: ["2-1.1", "1-1.2"] },
                60: { venue: "9", courses: ["2-2.2"] },
            },
            2: {
                10: { venue: "7", courses: ["1-2.1"] },
                25: { venue: "2", courses: ["2-1.1"] },
                27: { venue: "9", courses: ["2-1.2"] },
                42: { venue: "8", courses: ["3-1.1"] },
                43: { venue: "4", courses: ["3-1.2"] },
            },
            3: {
                3: {
                    venue: "1",
                    courses: ["2-1.1", "1-1.1", "4-1.1", "3-1.1"],
                },
                8: { venue: "10", courses: ["1-1.2"] },
                20: { venue: "5", courses: ["2-4.1", "1-4.1"] },
                31: { venue: "8", courses: ["4-2.1", "2-2.2", "1-2.2"] },
                34: { venue: "3", courses: ["2-2.1"] },
                39: { venue: "6", courses: ["2-4.2"] },
                50: { venue: "7", courses: ["4-1.2", "1-2.1"] },
            },
            4: {
                19: { venue: "7", courses: ["1-4.1"] },
                26: { venue: "6", courses: ["1-1.1", "2-1.2", "4-1.2"] },
                35: { venue: "10", courses: ["2-2.2"] },
                44: { venue: "4", courses: ["3-1.2"] },
                48: { venue: "2", courses: ["3-2.2"] },
                56: { venue: "9", courses: ["4-2.2"] },
                62: { venue: "8", courses: ["2-2.1", "1-2.1", "4-2.1"] },
            },
        },
        3: {
            1: {
                17: { venue: "6", courses: ["1-2.2"] },
                24: { venue: "1", courses: ["2-4.2", "1-4.2"] },
                30: {
                    venue: "10",
                    courses: ["4-1.1", "3-1.1", "2-1.2", "1-1.2"],
                },
                49: { venue: "3", courses: ["2-1.1"] },
                58: { venue: "8", courses: ["4-2.2"] },
                61: { venue: "9", courses: ["2-4.1", "1-4.1"] },
            },
            2: {
                9: {
                    venue: "3",
                    courses: ["2-1.1", "1-1.1", "4-1.1", "3-1.1"],
                },
                12: { venue: "5", courses: ["1-2.1"] },
                15: { venue: "1", courses: ["2-2.2", "1-2.2"] },
                21: { venue: "4", courses: ["1-4.1"] },
                28: { venue: "7", courses: ["1-1.2", "4-1.2", "3-1.2"] },
                57: { venue: "9", courses: ["4-2.2"] },
            },
            3: {
                6: {
                    venue: "6",
                    courses: ["1-1.2", "4-1.2", "3-1.2", "2-2.1"],
                },
                29: { venue: "2", courses: ["2-1.2"] },
                38: { venue: "10", courses: ["2-4.1", "1-4.1"] },
                41: { venue: "1", courses: ["2-4.2", "1-4.2"] },
                46: { venue: "7", courses: ["3-2.2"] },
                54: { venue: "9", courses: ["4-2.1"] },
                60: { venue: "5", courses: ["2-2.2"] },
            },
            4: {
                1: {
                    venue: "10",
                    courses: ["2-1.1", "1-1.1", "4-1.1", "3-1.1"],
                },
                7: {
                    venue: "6",
                    courses: ["2-1.2", "1-1.2", "4-1.2", "3-1.2"],
                },
                13: { venue: "5", courses: ["1-2.1", "4-2.1", "2-4.1"] },
                16: { venue: "8", courses: ["2-2.2", "1-2.2"] },
                23: { venue: "9", courses: ["1-4.2"] },
                32: { venue: "4", courses: ["2-2.1"] },
                48: { venue: "2", courses: ["3-2.2"] },
            },
        },
        4: {
            1: {
                18: { venue: "7", courses: ["1-4.1"] },
                25: { venue: "4", courses: ["2-1.1"] },
                29: { venue: "8", courses: ["2-1.2"] },
                31: { venue: "9", courses: ["4-2.1", "2-2.2", "1-2.2"] },
                32: { venue: "3", courses: ["2-2.1"] },
                44: { venue: "2", courses: ["3-1.2"] },
            },
            2: {
                8: { venue: "2", courses: ["1-1.2"] },
                41: { venue: "8", courses: ["2-4.2", "1-4.2"] },
                42: { venue: "6", courses: ["3-1.1"] },
                52: { venue: "9", courses: ["4-1.2"] },
            },
            3: {
                4: {
                    venue: "2",
                    courses: ["1-1.1", "4-1.1", "3-1.1", "2-2.1"],
                },
                37: { venue: "9", courses: ["2-4.1"] },
                45: { venue: "3", courses: ["3-1.2"] },
                50: { venue: "6", courses: ["4-1.2", "1-2.1"] },
                55: { venue: "4", courses: ["4-2.2", "3-2.2"] },
            },
            4: {
                3: {
                    venue: "1",
                    courses: ["2-1.1", "1-1.1", "4-1.1", "3-1.1"],
                },
                12: { venue: "5", courses: ["1-2.1"] },
                24: { venue: "7", courses: ["2-4.2", "1-4.2"] },
                34: { venue: "8", courses: ["2-2.1"] },
                36: { venue: "2", courses: ["2-4.1"] },
                43: { venue: "6", courses: ["3-1.2"] },
                54: { venue: "4", courses: ["4-2.1"] },
            },
        },
        5: {
            1: {
                1: {
                    venue: "10",
                    courses: ["2-1.1", "1-1.1", "4-1.1", "3-1.1"],
                },
                6: {
                    venue: "7",
                    courses: ["1-1.2", "4-1.2", "3-1.2", "2-2.1"],
                },
                11: { venue: "1", courses: ["1-2.1"] },
                14: { venue: "5", courses: ["4-2.1", "1-2.2", "2-4.2"] },
                21: { venue: "4", courses: ["1-4.1"] },
                35: { venue: "6", courses: ["2-2.2"] },
                55: { venue: "9", courses: ["4-2.2", "3-2.2"] },
            },
            2: {
                13: { venue: "8", courses: ["1-2.1", "4-2.1", "2-4.1"] },
                28: { venue: "2", courses: ["1-1.2", "4-1.2", "3-1.2"] },
                33: { venue: "5", courses: ["2-2.1"] },
                47: { venue: "4", courses: ["3-2.2"] },
            },
            3: {
                18: { venue: "1", courses: ["1-4.1"] },
                26: { venue: "4", courses: ["1-1.1", "2-1.2", "4-1.2"] },
                37: { venue: "7", courses: ["2-4.1"] },
                39: { venue: "9", courses: ["2-4.2"] },
                51: { venue: "3", courses: ["4-1.1", "3-1.2"] },
                58: { venue: "6", courses: ["4-2.2"] },
                62: { venue: "5", courses: ["2-2.1", "1-2.1", "4-2.1"] },
            },
            4: {
                5: { venue: "7", courses: ["1-1.1"] },
                16: { venue: "5", courses: ["2-2.2", "1-2.2"] },
                19: { venue: "3", courses: ["1-4.1"] },
                22: { venue: "4", courses: ["1-4.2"] },
                45: { venue: "9", courses: ["3-1.2"] },
                53: { venue: "6", courses: ["4-1.2"] },
                56: { venue: "10", courses: ["4-2.2"] },
                59: { venue: "2", courses: ["2-1.1", "1-1.2"] },
            },
        },
    },
}; 



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

