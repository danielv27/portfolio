from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.colors import black, HexColor

OUTPUT = "./public/resume.pdf"

W, H = A4

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    topMargin=14*mm,
    bottomMargin=14*mm,
    leftMargin=18*mm,
    rightMargin=18*mm,
)

gray = HexColor('#555555')
blue = HexColor('#0055cc')

nameStyle     = ParagraphStyle('Name',     fontName='Helvetica-Bold', fontSize=20, alignment=TA_CENTER, leading=24, spaceAfter=4)
contactStyle  = ParagraphStyle('Contact',  fontName='Helvetica',      fontSize=9,  alignment=TA_CENTER, leading=13, spaceAfter=5, textColor=gray)
sectionStyle  = ParagraphStyle('Section',  fontName='Helvetica-Bold', fontSize=11, leading=14, spaceBefore=8, spaceAfter=3)
jobStyle      = ParagraphStyle('Job',      fontName='Helvetica-Bold', fontSize=9,  leading=12, spaceBefore=5, spaceAfter=2)
bulletStyle   = ParagraphStyle('Bullet',   fontName='Helvetica',      fontSize=8.5, leading=12, leftIndent=8, spaceAfter=1.5)
profileStyle  = ParagraphStyle('Profile',  fontName='Helvetica',      fontSize=9,  leading=13, spaceAfter=3)

def hr(color=black, thickness=0.8):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=1)

def section_hr():
    return HRFlowable(width="100%", thickness=0.4, color=HexColor('#aaaaaa'), spaceBefore=1, spaceAfter=1)

def b(text):
    return Paragraph(f"\u2022\u2003{text}", bulletStyle)

story = []

# ── Header ──────────────────────────────────────────────────────────────
story.append(Paragraph("Daniel Verner", nameStyle))
story.append(Paragraph("Software Engineer", ParagraphStyle('Sub', fontName='Helvetica', fontSize=11, alignment=TA_CENTER, leading=14, spaceAfter=4, textColor=gray)))
story.append(Paragraph(
    '<link href="https://danielv27.github.io/portfolio" color="#0055cc">Portfolio</link>'
    ' &nbsp;|&nbsp; '
    '<link href="https://github.com/danielv27" color="#0055cc">GitHub</link>'
    ' &nbsp;|&nbsp; '
    '<link href="https://linkedin.com/in/daniel-verner" color="#0055cc">LinkedIn</link>'
    ' &nbsp;|&nbsp; danielv2000@gmail.com &nbsp;|&nbsp; +31 06 15205800 &nbsp;|&nbsp; Amsterdam, Netherlands',
    contactStyle
))
story.append(hr())

# ── Profile ──────────────────────────────────────────────────────────────
story.append(Paragraph("Profile", sectionStyle))
story.append(Paragraph(
    "Full-stack software engineer with a strong focus on backend systems, microservice architecture, and end-to-end delivery. "
    "I enjoy owning features from system design to production — building reliable integrations, automating workflows, and "
    "collaborating closely with stakeholders to ship software that solves real problems.",
    profileStyle
))
story.append(section_hr())

# ── Experience ───────────────────────────────────────────────────────────
story.append(Paragraph("Experience", sectionStyle))

story.append(Paragraph("Software Engineer &nbsp;&mdash;&nbsp; MyParcel.com, Amsterdam &nbsp;&nbsp; <font color='#555555'>Jan 2025 – Present</font>", jobStyle))
story.append(b("Own features end-to-end: from system design and API contracts to backend logic, microservice implementation, and deployment."))
story.append(b("Built carrier, marketplace, and warehouse integrations from scratch, enabling automated shipment creation, tracking, and returns at scale."))
story.append(b("Drove CI/CD improvements with GitHub Actions and Docker, reducing friction in release and testing workflows."))
story.append(b("Collaborate directly with stakeholders and clients to refine requirements and deliver complex logistics processes on time."))

story.append(Paragraph("Software Engineer &nbsp;&mdash;&nbsp; DongIT, Leiden &nbsp;&nbsp; <font color='#555555'>Aug 2023 – Dec 2024</font>", jobStyle))
story.append(b("Modernized a legacy pentesting platform end-to-end: rebuilt the frontend (Vanilla JS to Vue.js) and extended backend APIs."))
story.append(b("Introduced a Vitest testing framework, raising reliability and giving the team confidence to iterate faster."))
story.append(b("Containerized the full stack with Docker, eliminating environment inconsistencies and cutting deployment overhead."))

story.append(Paragraph("Software Engineer &nbsp;&mdash;&nbsp; Capisoft B.V., Amsterdam &nbsp;&nbsp; <font color='#555555'>Feb 2022 – Aug 2023</font>", jobStyle))
story.append(b("Led project delivery across multiple client products, owning technical direction and team coordination."))
story.append(b("Owned the full-stack integration between backend services and client applications across web and mobile."))
story.append(b("Shipped cross-platform apps (mobile, desktop, web) using React Native, Flutter, and Firebase."))
story.append(b("Drove code quality standards, testing practices, and deployment processes in an Agile environment."))

story.append(Paragraph("Teaching Assistant &nbsp;&mdash;&nbsp; Vrije Universiteit Amsterdam &nbsp;&nbsp; <font color='#555555'>Sep 2021 – Feb 2023</font>", jobStyle))
story.append(b("Mentored CS and AI students in small groups, building their programming skills and problem-solving confidence."))

story.append(section_hr())

# ── Open Source & Research ───────────────────────────────────────────────
story.append(Paragraph("Open Source &amp; Research", sectionStyle))
story.append(b(
    '<b><link href="https://github.com/danielv27/ast-insight" color="#0055cc">AST Insight</link></b>: '
    'MSc thesis — an AST-based static analysis tool in Python that detects and automatically corrects security vulnerabilities in C code.'
))
story.append(b(
    '<b><link href="https://github.com/atlarge-research/continuum" color="#0055cc">TS EDSL (Continuum)</link></b>: '
    'Contributed a TypeScript embedded DSL for cloud simulation configuration to an open-source research project at atlarge-research.'
))
story.append(section_hr())

# ── Skills ───────────────────────────────────────────────────────────────
story.append(Paragraph("Skills", sectionStyle))
story.append(b("<b>Backend</b>: PHP (Laravel), Python (Django), Node.js (Express), Microservices, REST APIs, System Design"))
story.append(b("<b>Frontend</b>: Vue.js, React, TypeScript, TailwindCSS"))
story.append(b("<b>DevOps</b>: Docker, GitHub Actions, CI/CD, Linux, AWS"))
story.append(b("<b>Testing</b>: Vitest, Testing Library, Unit / Component / E2E"))
story.append(b("<b>Spoken</b>: English (fluent), Hebrew (native)"))
story.append(section_hr())

# ── Education ────────────────────────────────────────────────────────────
story.append(Paragraph("Education", sectionStyle))
story.append(b("<b>MSc Software Engineering</b> &nbsp;&mdash;&nbsp; University of Amsterdam (UvA) &nbsp;&nbsp; Sep 2023 – Aug 2024"))
story.append(b("<b>BSc Computer Science</b> (Cum Laude) &nbsp;&mdash;&nbsp; Vrije Universiteit Amsterdam (VU) &nbsp;&nbsp; Sep 2020 – Aug 2023"))

doc.build(story)
print(f"Done: {OUTPUT}")
