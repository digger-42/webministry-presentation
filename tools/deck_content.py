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

    {"master": BURGUNDY, "title": "Breeze: our people", "bullets": [
        ("People database: address book and member directory", [
            "It needs updating: when people leave PCC, their entries aren't always changed",
            "Hard to track, because sometimes they come back",
        ]),
        "Calendar: several ministries use it for scheduling and reminders",
        "Forms for our event sign-up lists, and mass email",
        "Who: Greg Fales administers it; staff and the Financial Secretary contribute",
    ]},

    {"master": BURGUNDY, "title": "Breeze: giving", "icon": "hand-heart", "paragraphs": [
        "Breeze is where all our online giving support lives.",
        "Automatic donations and electronic gifts to PCC are easy to set up, on a regular "
        "schedule or as a one-time gift.",
        "Breeze records donations, produces annual tax statements and supports our financial reports.",
    ], "notes": [
        "The Financial Secretary counts the offering weekly and reports giving; that role is separate from Gary's Treasurer role.",
    ]},

    {"master": BURGUNDY, "title": "Planning Center: how we use it", "bullets": [
        ("Katie, Worship: Planning Center Services", [
            "Manages the Worship Team and schedules team members each week",
            "Shares music and sound samples with the band and vocalists",
        ]),
        ("Wade, Children's: Services, Check-Ins and Registrations", [
            "Services: volunteers, scheduling and reminders",
            "Check-Ins: runs the check-in stations and matches children back up with parents",
            "Registrations: VBS sign-ups each year",
        ]),
    ]},

    {"master": BURGUNDY, "title": "Planning Center: the bigger picture", "icon": "calendar-days", "paragraphs": [
        "Planning Center offers many more modules, and some overlap with what Faith Connector "
        "and Breeze already do for us.",
        "Adding more of them is possible, but the cost is a real challenge compared to the "
        "services we use now.",
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

    {"master": GREEN, "title": "Lunch", "icon": "pizza", "paragraphs": [
        "Pizza time. Pizza fuels tech work. It's a rule.",
        "After lunch it's your turn: questions and ideas for the website.",
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

    {"master": WEB, "title": "Resources: Faith Connector", "bullets": [
        "Home: https://www.faithconnector.com/",
        "YouTube, Flex 2 training and examples: https://www.youtube.com/@faithconnector",
        "Designs: https://www.faithconnector.com/our-church-website-designs",
        "Real sites: https://www.faithconnector.com/best-church-websites",
        "Features: https://www.faithconnector.com/church-websites-features",
        "Stock graphics: in Flex's image selector pop-up",
    ]},

    {"master": WEB, "title": "Resources: PCC website and media", "bullets": [
        "Our site: https://pccmi.org/",
        "Web admin: https://www.pccmi.org/admin/",
        "Live edit (Flex 2): https://www.pccmi.org/edit",
        "Watch Live: https://www.pccmi.org/WatchLive",
        "YouTube: https://www.pccmi.org/YouTube",
        "Facebook: https://www.pccmi.org/FaceBook",
        "Linktree (TapDot): https://linktr.ee/pccmi",
    ]},

    {"master": WEB, "title": "Resources: PCC tools", "bullets": [
        "Breeze dashboard: https://pccmi.breezechms.com/r/dashboard",
        "Breeze admin: https://www.pccmi.org/i/breezechms",
        "Planning Center Services: https://login.planningcenteronline.com/login/new?return=Services%2Fdashboard%2F0",
        ("Google Workspace admin portal: https://www.pccmi.org/i/google-admin", [
            "Needs an admin login: ask Dan Rittersdorf to help you",
        ]),
    ]},

    {"master": WEB, "title": "Brand guidelines and logos", "icon": "palette", "paragraphs": [
        "The brand guidelines and logo source files are on Google Drive. For access, ask Ken, "
        "Katie or Dan Rittersdorf; any of them can share it with you.",
        "Please don't copy a low-resolution JPG of the logo, and never enlarge one. Ask for the "
        "source files so the logo always looks crisp and clean.",
    ]},

    {"master": WEB, "title": "Let's build one: a new front page", "icon": "rocket", "paragraphs": [
        "We want to refresh the website's design, and Flex 2 makes that easy.",
        "Let's build a new main page, live, that serves the purposes we just talked about.",
    ], "notes": [
        "Build it hidden from the menu so nothing changes for visitors today.",
    ]},

    {"master": WEB, "title": "Step 1: choose a look", "icon": "palette", "bullets": [
        "Browse the designs on the main site",
        "Set up fonts and colors, or change them on our current design",
        "Notice how little it takes",
    ], "notes": [
        "Live: open the Flex 2 design gallery, pick one, then adjust fonts and brand colors.",
    ]},

    {"master": WEB, "title": "Step 2: just what we said it needs", "icon": "blocks", "bullets": [
        "What a visitor should see in the first five seconds",
        "The three things the front page must hold",
        "Clear paths for newcomers and for members",
    ], "notes": [
        "Use the answers from the front-page and audience questions we just discussed.",
    ]},

    {"master": WEB, "title": "Step 3: compare", "icon": "scale", "paragraphs": [
        "Put the new page beside today's front page.",
        "Do we like it?",
    ]},

    {"master": WEB, "title": "What do we hang on the framework?", "icon": "image", "bullets": [
        "What content does it need?",
        "What assets do we need to go get: photos, videos, documents?",
        "What makes it the best site it can be for PCC and those we serve?",
    ]},

    {"master": WEB, "title": "Stand back", "icon": "lightbulb", "paragraphs": [
        "How hard was that?",
        "Is the new page better?",
        "We'll keep working on it in our regular meetings, to be sure it's right before we go live, "
        "if that's what we decide we want.",
    ]},

    {"master": "PCC-Section", "title": "Thank you",
     "subtitle": "“God doesn’t call the equipped; He equips the called.” Roll out!"},
]
