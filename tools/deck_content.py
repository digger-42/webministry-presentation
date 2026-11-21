"""Slide text for the PCC WebMinistry Training deck (11/21/2026).

Each slide is a dict:
  master    one of the masters in build_template.py
  title     slide title
  subtitle  title and section slides only
  paragraphs  content slides; plain paragraphs, shown above any bullets
  bullets   content slides; a (text, [sub-bullets]) tuple nests one level
  icon      content slides; a Lucide icon name from assets/icons, shown as a brand-color sticker
  notes     speaker notes, one paragraph per string

No email addresses or phone numbers go on slides.
"""

GOLD = "PCC-Content-Gold"           # How we're organized
TEAL = "PCC-Content-Teal"           # The building
BURGUNDY = "PCC-Content-Burgundy"   # Services
WEB = "PCC-Content-DarkGreen"       # The website
GREEN = "PCC-Content"               # Everything else


def section(title, subtitle):
    return {"master": "PCC-Section", "title": title, "subtitle": subtitle}


DECK = [
    {"master": "PCC-Title", "title": "PCC WebMinistry Training", "subtitle": "11/21/2026"},

    {"master": GREEN, "title": "Today", "bullets": [
        "10:00  Welcome",
        "10:05  How we're organized: people and responsibilities",
        "10:15  The building: internet, network, phones, video, safety",
        "10:35  Services: Google Workspace, Breeze, Planning Center",
        "10:55  Break",
        "11:00  The website: Flex, menus, content, page types, live editing",
        "12:00  Lunch, then your turn: questions and ideas for the website",
    ], "notes": [
        "This session is being recorded with Pocket so we get a summary afterward.",
    ]},

    {"master": GREEN, "title": "Why we're here", "paragraphs": [
        "Everything we do is to serve Christ and bring Him glory. Together, we build a website that "
        "serves our church family and helps bring seekers to Christ, leading them to our doors with "
        "warm, inviting content.",
    ], "bullets": [
        "Know who looks after which system, and who to ask",
        "See how the building, our services and the website fit together",
        "Watch how the website is edited, so it feels less mysterious",
        "After lunch, tell us what you want the website to become",
    ]},

    section("How we're organized", "People and responsibilities"),

    {"master": GOLD, "title": "Who's responsible for what", "icon": "users", "bullets": [
        "Elders: the church as a whole",
        "Dan Raymond: hardware infrastructure (internet, network, phones, cameras)",
        "Dan Rittersdorf: web backend (website, Google Workspace, live stream)",
        "Web Ministry team and staff: the content",
    ]},

    {"master": GOLD, "title": "We build the shelves; you fill them", "icon": "layout-template", "paragraphs": [
        "The Dans provide the framework: accounts, systems, page templates and menus.",
        "Staff and ministry leaders bring it to life with words, photos, events, schedules and "
        "updates from your area.",
        "Together, the framework and your content make the website an appealing, effective ministry tool.",
    ], "notes": [
        "Core message of the day: structure versus content.",
    ]},

    {"master": GOLD, "title": "The Web Ministry team", "bullets": [
        "The Dans (Raymond and Rittersdorf): Super Admins",
        "Ken Stewart: art, design, branding",
        "Greg Fales: Breeze",
        "Christine Coggins: Missions",
        "David Schafer: back-up",
        "Steve Wellman: online advertising that drives visitors to the site",
        "Addie Snauko: rising star, constellation TBD",
    ], "notes": [
        "\"The Dans\": with apologies to The Bobs in Office Space.",
    ]},

    section("The building", "Internet, network, phones, video, safety"),

    {"master": TEAL, "title": "Internet and DNS", "icon": "globe", "bullets": [
        "Charter Spectrum Business cable internet",
        "Comes in near the brown staff door; modem is in the communication closet (conference room next to Steve's office)",
        "DNS for pccmi.org is hosted at Squarespace",
        "A UPS keeps the modem, network and cameras running through short outages",
        "Who: Dan Raymond and Gary Campbell manage the account",
    ]},

    {"master": TEAL, "title": "Network and Wi-Fi", "icon": "wifi", "bullets": [
        "Ubiquiti equipment: Dream Machine Pro and a 16-port PoE switch in the closet",
        "4 NanoHD Wi-Fi access points around the building, powered over the network cable",
        "Staff, sound and guest networks are separate subnets and Wi-Fi networks on this service",
        "Who: Dan Raymond",
    ]},

    {"master": TEAL, "title": "Phone system", "icon": "phone", "bullets": [
        "RingCentral internet phone system (replaced AT&T Merlin, then MiTel)",
        "Any phone can answer any incoming call",
        "Calls can be transferred to any extension, or to an outside number",
        "Who: Dan Raymond; Gary Campbell and Patti Krieger are also admins",
    ]},

    {"master": TEAL, "title": "Live-stream video", "bullets": [
        "3 PTZ cameras above the sound booth; Camera 3, in the center, also feeds the hallway TV outside the sanctuary directly",
        "They feed the \"PCC Video Beast\", a graphics powerhouse of a PC, much like a gaming computer",
        "vMix blends the camera feeds with the sound-board feed into one coherent video stream",
        "Streams to Facebook, YouTube and the Watch Live page on pccmi.org",
        "Who: Dan Rittersdorf (the system) and Katie Winstanley (the budget)",
    ], "notes": [
        "The Video Beast lives in the video production room, in the northeast corner of the sanctuary.",
    ]},

    {"master": TEAL, "title": "Building safety systems", "icon": "cctv", "bullets": [
        ("Security cameras: owned by the Security/Safety team", [
            "Speco system on its own separate network; recorder locked in the Hub",
            "Separate from the live-stream cameras",
        ]),
        "Burglar alarm: monitored and serviced by Johnson Controls / ADT",
        "Fire suppression system: monitored by Johnson Controls",
    ]},

    section("Services", "Google Workspace, Breeze, Planning Center"),

    {"master": BURGUNDY, "title": "Google Workspace for Nonprofits", "icon": "mail", "bullets": [
        "Our pccmi.org email accounts and email groups",
        "Shared folders in Google Drive",
        "Calendar, Docs, Sheets, Slides, Forms, Meet",
        "Free nonprofit edition, managed by the Dans",
    ]},

    {"master": BURGUNDY, "title": "Workspace: what we can and can't do", "bullets": [
        ("Included", [
            "Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Sites, Meet",
            "The Gemini app and NotebookLM",
        ]),
        ("Not included (paid editions, discounted for nonprofits)", [
            "Gemini inside Gmail, Docs and Meet",
            "Saving Meet recordings to Drive",
            "Vault for email retention and search",
        ]),
    ]},

    {"master": BURGUNDY, "title": "Breeze", "icon": "hand-heart", "bullets": [
        "Address book and member directory",
        "Giving: records donations, produces annual tax statements, supports financial reports",
        "Mass email",
        "Who: Greg Fales administers it; staff and the Financial Secretary contribute",
    ], "notes": [
        "The Financial Secretary counts the offering weekly and reports giving; that role is separate from Gary's Treasurer role.",
    ]},

    {"master": BURGUNDY, "title": "Planning Center", "icon": "calendar-days", "paragraphs": [
        "Katie uses Planning Center for worship, and Wade uses it for children's ministry.",
        "Katie and Wade: how do you use it?",
    ]},

    {"master": GREEN, "title": "Break", "icon": "coffee", "paragraphs": [
        "Stretch, grab a coffee. Back in 5 minutes for the website.",
    ]},

    section("The website", "PCCMI.org, Flex, menus, content"),

    {"master": WEB, "title": "PCCMI.org and Faith Connector", "icon": "church", "bullets": [
        "Faith Connector hosts the site",
        "Flex is their editor: where we build and change pages",
        "Admin pages at pccmi.org/admin; the Dans hold the master account",
        "Help: Faith Connector's help videos and Facebook support group",
    ], "notes": [
        "Live: log in to Flex.",
    ]},

    {"master": WEB, "title": "How a page is built", "icon": "blocks", "bullets": [
        "Most of our pages start as a blank template page",
        "We build them up with sections and blocks",
        "Blocks control the layout and hold the content: text, images, buttons, embeds",
        "The site's design can change without rebuilding pages",
    ]},

    {"master": WEB, "title": "Menu management", "icon": "list-tree", "bullets": [
        "Dropdown menus, up to three levels deep",
        "Drag and drop to reorder pages",
        "A page can be hidden from the menu and still be reached by its direct link",
        "Live: change a menu",
    ]},

    {"master": WEB, "title": "Content management", "icon": "image", "bullets": [
        "Image library and file manager",
        "Upload a file once, then link it from any page",
        "Keep file names clear so the next person can find them",
        "Live: upload an image and use it on a page",
    ]},

    {"master": WEB, "title": "Page types we use", "icon": "layout-template", "bullets": [
        "Blank template pages built up with blocks (most pages)",
        "Calendar",
        "Membership directory (in use, but very incomplete)",
        "Also available: forms, photo galleries, prayer requests, FAQ, blogs",
    ]},

    {"master": WEB, "title": "Safety net", "icon": "life-buoy", "paragraphs": [
        "Mistakes are easy to undo. Page rollback restores an earlier version of a page, and the "
        "change log shows who changed what.",
        "If something breaks, tell a Dan.",
    ]},

    {"master": WEB, "title": "Live: editing a page", "icon": "pen-line", "bullets": [
        "Log in to Flex",
        "Find the page and open it",
        "Edit a block, preview, save",
        "Roll it back",
    ]},

    {"master": GREEN, "title": "Who to ask", "icon": "message-circle-question", "bullets": [
        "Website, Google Workspace, live stream: Dan Rittersdorf",
        "Internet, network, phones: Dan Raymond",
        "Breeze: Greg Fales",
        "Design and branding: Ken Stewart",
        "Security cameras: the Security/Safety team",
    ]},

    section("Your turn", "Questions and ideas for the website"),

    {"master": GREEN, "title": "Who is our audience?", "icon": "user-round-search", "bullets": [
        "Picture someone visiting pccmi.org for the first time. Who are they?",
        "Is the site mainly for members, or for people looking for a church?",
        "Do teens and parents of young kids use the site?",
    ]},

    {"master": GREEN, "title": "What do they need to know?", "icon": "map-pin-house", "bullets": [
        "What must a newcomer know before their first Sunday?",
        "What questions come to the office that the site should answer?",
        "What do members look for and struggle to find?",
    ]},

    {"master": GREEN, "title": "What belongs on the front page?", "icon": "compass", "bullets": [
        "What should a visitor see in the first five seconds?",
        "What's there now that nobody would miss?",
        "If it could hold only three things, what are they?",
    ]},

    {"master": GREEN, "title": "Keeping them, and bringing them back", "icon": "sprout", "bullets": [
        "What stories from your ministry would make someone want more?",
        "What could your area post every week, and who would send it in?",
        "Why would a member visit every week?",
        "What would make you text a link to a friend?",
    ]},

    {"master": GREEN, "title": "If not Faith Connector, then what?", "icon": "route", "bullets": [
        "What frustrates you in Flex? Show us.",
        "What would an easy editing day look like?",
        "What must any replacement still do: giving, calendar, live stream?",
        "Who would edit week to week, and how much training would they need?",
    ]},

    {"master": WEB, "title": "Let's build one: a youth landing page", "icon": "rocket", "bullets": [
        "Who we are and why",
        "A 3-month calendar of programs and events, with registration and \"more info\" links",
        "One place to send parents for updates and cancellations",
        "Children's can reuse the same pattern",
    ], "notes": [
        "Requested by Josh; Wade wants the same for Children's.",
    ]},

    {"master": WEB, "title": "Brainstorm, plan, prototype, revise, publish", "icon": "lightbulb", "bullets": [
        "Brainstorm: who it's for and the three questions it must answer",
        "Plan: sections, blocks, where it sits in the menu, images needed",
        "Prototype: build it live, hidden from the menu",
        "Revise: check it on the screen and on a phone",
        "Publish: turn it on in the menu",
    ]},

    {"master": "PCC-Section", "title": "Thank you"},
]
