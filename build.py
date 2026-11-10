"""Builds the static pages for dpaconsult.com.

The header and footer live here once; run `uv run build.py` after editing
and the seven .html files next to this script are rewritten.
"""
from pathlib import Path

ROOT = Path(__file__).parent
PHONE = "(866) 294-2319"
PHONE_HREF = "tel:+18662942319"
EMAIL = "info@dpaconsult.com"
LINKEDIN = "https://www.linkedin.com/in/damonanderson"
WEBINAR = "https://www.jcooperjr.com/webinar-registration"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("coaching.html", "Coaching"),
    ("workforce.html", "Workforce"),
    ("security.html", "Security"),
]

ICONS = {
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "nodes": '<circle cx="5" cy="12" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 11l10-4M7 13l10 4"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
    "people": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.700 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.500 0 4.500 2 4.500 4.500"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.500-3.200 8-8 9-4.800-1-8-4.500-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "build": '<path d="M3 21h18M6 21V8l6-4 6 4v13M10 21v-5h4v5M10 11h4"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "heart": '<path d="M12 20s-7-4.400-7-10a4 4 0 017-2.600A4 4 0 0119 10c0 5.600-7 10-7 10z"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.500V16c0 1.500 2.700 3 6 3s6-1.500 6-3v-4.500"/>',
    "phone": '<path d="M5 3h4l2 5-2.500 1.500a11 11 0 006 6L16 13l5 2v4a2 2 0 01-2 2A16 16 0 013 5a2 2 0 012-2z"/>',
}


def icon(name):
    return f'<div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24">{ICONS[name]}</svg></div>'


def card(ic, title, text, link=None, label=None):
    more = f'<a class="more" href="{link}">{label} &rarr;</a>' if link else ""
    return f'<article class="card reveal">{icon(ic)}<h3>{title}</h3><p>{text}</p>{more}</article>'


def layout(slug, title, desc, body):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == slug else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://dpaconsult.com/assets/img/dpa-logo.jpg">
<meta property="og:type" content="website">
<meta name="theme-color" content="#060a12">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/favicon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,600..900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav-row">
    <a class="brand" href="index.html" aria-label="DP Anderson Consulting home">
      <img src="assets/img/compass-mark.png" alt="" width="44" height="44">
      <span><b>DP Anderson Consulting</b><small>Guiding Business. Driving Results.</small></span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a class="btn" href="contact.html">Book a consultation</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="index.html"><img src="assets/img/compass-mark.png" alt="" width="44" height="44"><span><b>DP Anderson Consulting</b><small>Guiding Business. Driving Results.</small></span></a>
        <p style="margin-top:16px;max-width:36ch">Business development, solutions architecture, and coaching for small businesses and mission-driven organizations, led by Damon P. Anderson.</p>
      </div>
      <div><h4>Work</h4><ul>
        <li><a href="services.html">Consulting services</a></li>
        <li><a href="coaching.html">Coaching</a></li>
        <li><a href="services.html#align">A.L.I.G.N. Framework</a></li>
      </ul></div>
      <div><h4>Mission</h4><ul>
        <li><a href="workforce.html">Rockton Hospital project</a></li>
        <li><a href="security.html">Security for the normal person</a></li>
        <li><a href="about.html">About Damon</a></li>
      </ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="{PHONE_HREF}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li>Lancaster, Pennsylvania</li>
      </ul></div>
    </div>
    <div class="foot-bottom"><span>&copy; <span id="year">2026</span> DP Anderson Consulting. All rights reserved.</span><span>Guiding Business. Driving Results.</span></div>
  </div>
</footer>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


def cta(title, text, primary=("contact.html", "Book a consultation"), secondary=None):
    second = f'<a class="btn ghost" href="{secondary[0]}">{secondary[1]}</a>' if secondary else ""
    return f"""<section class="cta">
  <div class="wrap reveal">
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    <div class="btn-row"><a class="btn" href="{primary[0]}">{primary[1]}</a>{second}</div>
  </div>
</section>"""


ALIGN = """<div class="align">
  <div class="reveal"><b>A</b><h3>Assess</h3><p>Test strategic fit, risk, and the balance of power before anything is signed.</p></div>
  <div class="reveal"><b>L</b><h3>Locate</h3><p>Find the partners who hold the assets, access, or skills you lack.</p></div>
  <div class="reveal"><b>I</b><h3>Integrate</h3><p>Line up operations, data, incentives, and meeting cadence.</p></div>
  <div class="reveal"><b>G</b><h3>Govern</h3><p>Set the rules, metrics, exits, and escalation paths up front.</p></div>
  <div class="reveal"><b>N</b><h3>Nurture</h3><p>Review the value created every quarter and adjust.</p></div>
</div>"""

PAGES = {}

# ---------------------------------------------------------------- Home
PAGES["index.html"] = (
    "DP Anderson Consulting | Guiding Business. Driving Results.",
    "Damon P. Anderson helps small and mid-sized businesses grow through business development, solutions architecture, coaching, workforce development, and everyday security.",
    f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Guiding Business. Driving Results.</span>
      <h1>Hard problems solved. <span class="gold">Then automated.</span></h1>
      <p class="lead">DP Anderson Consulting is the practice of Damon P. Anderson: business developer, solutions architect, and coach for small and mid-sized businesses that need a clear direction and systems that run without constant attention.</p>
      <div class="btn-row">
        <a class="btn" href="contact.html">Book a consultation</a>
        <a class="btn ghost" href="workforce.html">See the Rockton Hospital project</a>
      </div>
    </div>
    <div class="hero-art"><img src="assets/img/compass.jpg" alt="DP Anderson Consulting gold compass emblem" width="640" height="560"></div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">What Damon does</span>
      <h2>One practice, four kinds of work</h2>
      <p class="lead">Each one comes from the same habit: find the real problem, design the fix, and make it repeatable.</p>
    </div>
    <div class="grid g4">
      {card("nodes", "Solutions architecture", "Technology, process, and people decisions designed together so the fix holds up after the consultant leaves.", "services.html", "Services")}
      {card("chat", "Coaching for SMB leaders", "One-on-one work with owners and managers who are carrying too much and need a thinking partner.", "coaching.html", "Coaching")}
      {card("people", "Workforce development", "Community-led projects that turn idle assets into training, jobs, and services.", "workforce.html", "Current project")}
      {card("shield", "Security for the normal person", "Products in development to protect everyday people from scams and cyberbullying.", "security.html", "What is coming")}
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="photo reveal"><img src="assets/img/rockton-hospital.jpg" alt="The former hospital campus in Rockford, Illinois" width="1600" height="800" loading="lazy"></div>
    <div class="reveal">
      <span class="tag">Current main project</span>
      <h2>Rockton Hospital Repurposing Project</h2>
      <p class="lead">A community-led network working to bring needed resources and services to Rockford, Illinois, by giving a former hospital a new mission. Damon leads workforce development with J. Cooper Jr. LLC.</p>
      <div class="btn-row">
        <a class="btn" href="{WEBINAR}" target="_blank" rel="noopener">Save my spot for the webinar</a>
        <a class="btn ghost" href="workforce.html">About the project</a>
      </div>
    </div>
  </div>
</section>

<section class="stat-band">
  <div class="wrap split">
    <div>
      <div class="stat reveal" data-count="7.7" data-prefix="$" data-suffix="B">$7.7B</div>
      <p class="stat-note">Reported stolen from Americans aged 60 and older in a single year (FBI Internet Crime Complaint Center, 2025). That is one age group.</p>
    </div>
    <div class="reveal">
      <span class="eyebrow">Launching soon</span>
      <h2>Security for the normal person</h2>
      <p class="lead">Corporations have security teams. Retirees, parents, and teenagers face the same scammers and bullies with nothing. Damon is preparing a set of security products built for them.</p>
      <div class="btn-row"><a class="btn" href="security.html">See what is coming</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">The A.L.I.G.N. Framework</span>
      <h2>From broken partnerships to repeatable growth</h2>
      <p class="lead">Five stages for building alliances that keep producing value, and for repairing the ones that stopped.</p>
    </div>
    {ALIGN}
    <div class="btn-row"><a class="btn ghost" href="services.html#align">How the framework is used</a></div>
  </div>
</section>

<section class="cream">
  <div class="wrap split">
    <div class="reveal">
      <img class="avatar" src="assets/img/damon-anderson.jpg" alt="Damon P. Anderson" width="640" height="635" loading="lazy">
      <span class="eyebrow">About Damon</span>
      <h2>Public-sector technology leader, now building for small business and community</h2>
      <p>Damon P. Anderson gave 29&frac12; years to the Commonwealth of Pennsylvania. He was the first Chief Information Officer of the Department of Conservation and Natural Resources, then CIO and acting Chief Information Security Officer of the Pennsylvania Public Utility Commission, before retiring in January 2026.</p>
      <p>Today he runs DP Anderson Consulting, serves on the transition team at J. Cooper Jr. LLC, and is pursuing a Ph.D. in cybersecurity leadership.</p>
      <div class="btn-row"><a class="btn" href="about.html">Read his story</a><a class="btn ghost" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn profile</a></div>
    </div>
    <div class="grid reveal">
      <div class="card">{icon("bolt")}<h3>Automate everything</h3><p>If a task repeats, it should run itself. People are for judgment.</p></div>
      <div class="card">{icon("heart")}<h3>Give back</h3><p>Board service, advocacy, and community projects are part of the job.</p></div>
      <div class="card">{icon("cap")}<h3>Keep learning</h3><p>Doctoral research in cybersecurity leadership feeds directly into client work.</p></div>
    </div>
  </div>
</section>

{cta("Tell Damon what is stuck", "A first conversation costs nothing. Bring the problem; leave with a clearer picture of what to do next.", secondary=(PHONE_HREF, "Call " + PHONE))}
""",
)

# ---------------------------------------------------------------- About
PAGES["about.html"] = (
    "About Damon P. Anderson | DP Anderson Consulting",
    "Damon P. Anderson is a former Pennsylvania state CIO and acting CISO with 29 years of public service, now a consultant, coach, workforce development leader, and doctoral researcher in cybersecurity leadership.",
    f"""<section class="hero page-hero">
  <div class="wrap">
    <span class="eyebrow">About</span>
    <h1>Damon P. Anderson</h1>
    <p class="lead">A transformational change agent with more than 25 years of executive and on-the-ground experience across the public, military, and private sectors. Based in Lancaster, Pennsylvania.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap split top">
    <div class="reveal">
      <h2>&ldquo;I retired, led a lot, built some firsts, lifted leaders. I'm just getting started.&rdquo;</h2>
      <p>Damon started as a programmer analyst in the U.S. Army and went on to give 29&frac12; years to the Commonwealth of Pennsylvania. At the Department of Community Affairs he partnered with IBM to install the agency's first network and computer systems. At the Department of Conservation and Natural Resources he was appointed the first Chief Information Officer, built the IT organization from the ground up, and launched Pennsylvania's first Parks Reservation and Revenue System.</p>
      <p>He retired early in 2010 to found DP Anderson Consulting and to build The Strategic Alliance Experts with one of his mentors, then returned to state service in 2014 as CIO of the Pennsylvania Public Utility Commission, where he also served as acting Chief Information Security Officer. There he built the information security team, set up Commission-wide IT governance, and started an AI and emerging technologies practice.</p>
      <p>He retired from public service in January 2026. What he says he is proudest of is the leaders he developed, many of whom now serve as CIOs and executives across the Commonwealth.</p>
      <p>Now he does business development and works as a solutions architect and problem solver for small and mid-sized businesses, nonprofits, houses of worship, and community organizations. He serves on the transition team at J. Cooper Jr. LLC, leading workforce development on the Rockton Hospital Repurposing Project. He is pursuing a Ph.D. in cybersecurity leadership and preparing security products for ordinary people. He is also a minister, presenter, advocate, counselor, and musician.</p>
      <div class="btn-row"><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">Connect on LinkedIn</a><a class="btn ghost" href="contact.html">Get in touch</a></div>
    </div>
    <div class="reveal">
      <div class="photo" style="max-width:420px;margin-inline:auto"><img src="assets/img/damon-anderson.jpg" alt="Damon P. Anderson" width="640" height="635" style="aspect-ratio:auto"></div>
      <p style="text-align:center;margin-top:14px;color:var(--muted);font-size:.9rem">Damon P. Anderson<br>Manager, DP Anderson Consulting, LLC</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap split top">
    <div>
      <div class="section-head reveal" style="margin-bottom:1.6rem">
        <span class="eyebrow">Career</span>
        <h2>Four decades of building</h2>
      </div>
      <ol class="timeline">
        <li class="reveal"><span>2026 to present</span><h3>Transition Team Member, J. Cooper Jr. LLC</h3><p>Workforce development, grant strategy, and pathways to opportunity through the TECI2 platform.</p></li>
        <li class="reveal"><span>2010 to present</span><h3>Manager, DP Anderson Consulting, LLC</h3><p>Ideation, problem-solving frameworks, innovation platforms, and digital presence for small businesses and mission-driven organizations.</p></li>
        <li class="reveal"><span>2014 to 2026</span><h3>CIO and Acting CISO, Pennsylvania Public Utility Commission</h3><p>Technology strategy, security, and continuity for a 500-person agency regulating electricity, natural gas, water, transportation, and telecommunications. Launched the Data Management Office, Project Management Office, Architecture Review Board, and technology governance councils.</p></li>
        <li class="reveal"><span>2013 to 2026</span><h3>Strategic Industry Consultant, The Strategic Alliance Experts</h3><p>Alliances among nonprofits, industry, and government to design and improve workforce and technology programs.</p></li>
        <li class="reveal"><span>1997 to 2010</span><h3>First Chief Information Officer, PA Department of Conservation and Natural Resources</h3><p>Built the IT organization from scratch and delivered Pennsylvania's first Parks Reservation and Revenue System.</p></li>
        <li class="reveal"><span>1992 to 1997</span><h3>Technology Director, PA Department of Community Affairs (now DCED)</h3><p>Installed the agency's first network and computer systems with IBM and trained the staff to use them.</p></li>
        <li class="reveal"><span>1985 to 1992</span><h3>Programmer Analyst, U.S. Army</h3></li>
      </ol>
    </div>
    <div>
      <div class="reveal">
        <span class="eyebrow">Education and credentials</span>
        <ul class="checks">
          <li><strong>Ph.D., Cybersecurity Leadership</strong> (in progress), Capitol Technology University</li>
          <li><strong>Certified Government Chief Information Officer (CGCIO)</strong>, Harrisburg University of Science and Technology</li>
          <li><strong>M.A., Leadership Studies</strong>, Lancaster Bible College</li>
          <li><strong>B.A., Communications</strong>, Slippery Rock University</li>
        </ul>
      </div>
      <div class="reveal" style="margin-top:2.6rem">
        <span class="eyebrow">National and inter-agency work</span>
        <ul class="checks">
          <li><strong>NARUC Critical Infrastructure Committee</strong>: member and presenter</li>
          <li><strong>Cyber-Informed Engineering Workgroup</strong>, led by Idaho National Laboratory</li>
          <li><strong>NextGen IT Workforce Development Workgroup</strong></li>
          <li><strong>Multi-Agency Black History Celebration Committee</strong>: long-standing member, 2024 chair</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">What he is working on now</span>
      <h2>Four tracks</h2>
    </div>
    <div class="grid g2">
      {card("compass", "DP Anderson Consulting", "Business development, solutions architecture, and coaching for small and mid-sized businesses.", "services.html", "Services")}
      {card("build", "J. Cooper Jr. LLC", "Workforce development for the Rockton Hospital Repurposing Project, a community-led network in Rockford, Illinois.", "workforce.html", "The project")}
      {card("cap", "Ph.D. in cybersecurity leadership", "Doctoral research on how leaders make security decisions, applied directly to client and product work.")}
      {card("shield", "Security products", "A product line described as security for the normal person, aimed at scams and cyberbullying.", "security.html", "What is coming")}
    </div>
  </div>
</section>

<section class="cream">
  <div class="wrap split top">
    <div class="reveal">
      <span class="eyebrow">Giving back</span>
      <h2>Service is part of the work</h2>
      <p>Damon says he looks forward to giving back what he can. His record shows he started a long time ago. He and his wife, Jeania, have been domestic violence advocates for many years, presenting at schools, colleges, and churches.</p>
      <ul class="checks">
        <li><strong>Domestic Violence Services</strong>, Community Action Partnership of Lancaster County: since 2011</li>
        <li><strong>Technology Council of Central Pennsylvania</strong>: board member since 2018</li>
        <li><strong>Military Cyber Professional Association</strong>: member and volunteer since 2020</li>
      </ul>
    </div>
    <div class="reveal">
      <span class="eyebrow">Professional community</span>
      <h2>Affiliations</h2>
      <ul class="checks">
        <li><strong>AABE</strong> (American Association of Blacks in Energy), Harrisburg chapter: secretary</li>
        <li><strong>BDPA</strong>, Pittsburgh chapter: technology and STEM professional development</li>
        <li><strong>NSBE</strong> (National Society of Black Engineers), Philadelphia chapter</li>
        <li><strong>Toastmasters International</strong>: former vice president of public relations</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">How he works</span>
      <h2>Three principles</h2>
    </div>
    <div class="grid g3">
      {card("bolt", "Automate everything", "Repeating work belongs to systems. That frees people for the decisions only people can make.")}
      {card("heart", "Leave it better", "Every engagement should leave the client more capable, and every project should return something to its community.")}
      {card("shield", "Protect the people nobody is protecting", "Security has to work for a retiree with a phone as well as it works for a company with a budget.")}
    </div>
  </div>
</section>

{cta("Work with Damon", "Consulting, coaching, speaking, or the Rockton project: start with a conversation.")}
""",
)

# ---------------------------------------------------------------- Services
PAGES["services.html"] = (
    "Consulting Services | DP Anderson Consulting",
    "Business development, solutions architecture, alliance strategy, operational governance, and automation for small and mid-sized businesses.",
    f"""<section class="hero page-hero">
  <div class="wrap">
    <span class="eyebrow">Services</span>
    <h1>A problem solver for organizations without a spare executive</h1>
    <p class="lead">Small and mid-sized businesses, nonprofits, houses of worship, and community organizations hit the same walls as large enterprises, with fewer people to climb them. Damon brings CIO-level experience, practical tools, and AI to the problem in front of you and stays until the fix works.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="grid g3">
      {card("chart", "Business development", "Find the next customers, partners, and funding sources, and build a pipeline process your team can run every week.")}
      {card("nodes", "Solutions architecture", "Map the problem, choose the technology and process that fit your size and budget, and design how they connect.")}
      {card("bolt", "Automation", "Identify the work that repeats and hand it to software, so your people spend their time on customers and decisions.")}
      {card("people", "Strategic alliance revival", "Diagnose partnerships that have stalled, then reset the terms, incentives, and cadence or exit cleanly.")}
      {card("compass", "Growth blueprinting and digital presence", "A practical plan for getting off a growth plateau, including the social media and marketing that get you seen.")}
      {card("gear", "Adaptive PMO and operational governance", "Light project management and decision rules that keep work moving without adding bureaucracy, from someone who stood up a PMO and governance councils for a state commission.")}
      {card("shield", "Security and risk leadership", "Plain-language guidance on protecting your business, your customers, and your staff from fraud and attack.")}
      {card("build", "AI and emerging technology", "Sort what is useful from what is noise in AI and new tools, then pilot it on a real problem. Damon started the AI and emerging technologies practice at the Pennsylvania PUC.")}
      {card("chat", "Coaching", "Ongoing one-on-one support for the owner or leader responsible for making all of it happen.", "coaching.html", "About coaching")}
    </div>
  </div>
</section>

<section id="align">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Signature method</span>
      <h2>The A.L.I.G.N. Framework</h2>
      <p class="lead">Most growth for a small business comes through other organizations: suppliers, referral partners, funders, agencies. A.L.I.G.N. is the five-stage method Damon uses to build those relationships and to rescue the ones that have gone wrong.</p>
    </div>
    {ALIGN}
  </div>
</section>

<section class="cream">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">How an engagement works</span>
      <h2>Three steps, no surprises</h2>
    </div>
    <div class="steps">
      <div class="reveal"><h3>Listen and diagnose</h3><p>A free first conversation, followed by a short assessment of what is stuck and why.</p></div>
      <div class="reveal"><h3>Design the fix</h3><p>A written plan with scope, owners, and what success looks like, sized to your business.</p></div>
      <div class="reveal"><h3>Build, automate, hand over</h3><p>Damon works alongside your team, automates what can be automated, and leaves you able to run it.</p></div>
    </div>
  </div>
</section>

{cta("Have a problem that keeps coming back?", "Describe it in a few sentences and Damon will tell you whether he can help.", primary=("contact.html", "Describe your problem"))}
""",
)

# ---------------------------------------------------------------- Coaching
PAGES["coaching.html"] = (
    "Coaching for Small Business Leaders | DP Anderson Consulting",
    "One-on-one coaching from Damon P. Anderson for small and mid-sized business owners, managers, and emerging technology and security leaders.",
    f"""<section class="hero page-hero">
  <div class="wrap">
    <span class="eyebrow">Coaching</span>
    <h1>A thinking partner who has sat in the chair</h1>
    <p class="lead">Coaching came out of the consulting work. Owners would ask for a solution, and partway through it became clear they also needed someone to think with: someone outside the business who has carried executive responsibility.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap split top">
    <div class="reveal">
      <h2>Who it is for</h2>
      <ul class="checks">
        <li>Owners of small and mid-sized businesses who make every major decision alone</li>
        <li>Managers stepping into their first leadership role</li>
        <li>Technology and security professionals moving toward CIO or CISO responsibility</li>
        <li>Founders preparing for a partnership, a new market, or a hard conversation</li>
      </ul>
    </div>
    <div class="reveal">
      <h2>What you work on</h2>
      <ul class="checks">
        <li>Deciding what matters this quarter and dropping the rest</li>
        <li>Delegating and automating so the business does not depend on your hours</li>
        <li>Building partnerships and a business development habit</li>
        <li>Leading people through change</li>
        <li>Making sound technology and security decisions without a technical background</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Formats</span>
      <h2>Three ways to work together</h2>
    </div>
    <div class="grid g3">
      {card("chat", "One-on-one coaching", "Regular private sessions built around your goals, with direct feedback and accountability between sessions.")}
      {card("people", "Leadership team sessions", "Facilitated working sessions that get a small leadership team aligned on priorities and roles.")}
      {card("compass", "Coaching with consulting", "Coaching paired with hands-on solutions work, so the plan and the person carrying it out develop together.")}
    </div>
  </div>
</section>

<section class="cream">
  <div class="wrap">
    <div class="callout reveal" style="background:#fff;border-color:rgba(12,22,38,.12)">
      <h2>What to expect from Damon</h2>
      <p>Straight answers, practical next steps, and experience from decades of leading technology organizations. He will ask what you are trying to build, tell you what he sees, and help you put a system behind it so progress does not rely on willpower.</p>
      <div class="btn-row"><a class="btn" href="contact.html">Ask about coaching</a></div>
    </div>
  </div>
</section>
""",
)

# ---------------------------------------------------------------- Workforce
PAGES["workforce.html"] = (
    "Rockton Hospital Repurposing Project | DP Anderson Consulting",
    "Damon P. Anderson leads workforce development for the Rockton Hospital Repurposing Project in Rockford, Illinois, with J. Cooper Jr. LLC. Register for the webinar.",
    f"""<section class="hero page-hero">
  <div class="wrap split">
    <div>
      <span class="eyebrow">Workforce development &middot; Current main project</span>
      <h1>Rockton Hospital Repurposing Project</h1>
      <p class="lead">Transforming what it is now into what it can be. A community-led network to bring needed resources and services to the Rockford, Illinois community.</p>
      <div class="btn-row">
        <a class="btn" href="{WEBINAR}" target="_blank" rel="noopener">Save my spot for the webinar</a>
        <a class="btn ghost" href="#pillars">The three pillars</a>
      </div>
    </div>
    <div class="photo"><img src="assets/img/rockton-aerial.jpg" alt="Aerial view of the former hospital campus in Rockford, Illinois" width="1280" height="720"></div>
  </div>
</section>

<section class="alt">
  <div class="wrap split top">
    <div class="reveal">
      <span class="eyebrow">The project</span>
      <h2>A closed hospital is a building full of possibility</h2>
      <p>The project is led by J. Cooper Jr. LLC (JCJ), a coalition of development consultants that identifies and secures the developers, contractors, investors, financing, and partners a project like this needs. The work is organized as a community-led network, so the people of Rockford shape what the campus becomes.</p>
      <p>Damon joined JCJ's transition team in January 2026. His part is workforce development: making sure the repurposed campus produces training, employment services, and real jobs for the people who live around it, supported by JCJ's TECI2 platform (Talent and Employment Connections through Innovation).</p>
      <div class="partner" style="margin-top:1.6rem">
        <img src="assets/img/jcj-logo.png" alt="J. Cooper Jr. LLC logo" width="479" height="207" loading="lazy">
        <span>In partnership with <a href="https://www.jcooperjr.com/" target="_blank" rel="noopener">J. Cooper Jr. LLC</a><br><em>&ldquo;Your partner for the possible&rdquo;</em></span>
      </div>
    </div>
    <div class="reveal">
      <span class="eyebrow">JCJ's four core principles</span>
      <div class="grid g2">
        <div class="card"><h3>Identify</h3><p>Find the needs, the assets, and the key relationships.</p></div>
        <div class="card"><h3>Connect</h3><p>Bring the right people and organizations to the table.</p></div>
        <div class="card"><h3>Collaborate</h3><p>Work as one network toward a shared plan.</p></div>
        <div class="card"><h3>Innovate</h3><p>Design solutions the old model never considered.</p></div>
      </div>
    </div>
  </div>
</section>

<section id="pillars">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">&ldquo;Together we can make it&rdquo;</span>
      <h2>Three pillars for repurposing success</h2>
    </div>
    <div class="grid g3">
      {card("build", "Scalability and sustainability", "Repurposing is more than renovation. It means reimagining the infrastructure to serve new missions for every member of the Rockford community for years to come.")}
      {card("people", "Community investment and engagement", "Contributors receive a return on their investment and a service dividend: free access to wellness services, information and training, employment services, and healthy food.")}
      {card("chart", "Revenue driven, ensuring reinvestment", "Community investment programs are joined by other investment sources, fundraising, and revenue so the project keeps funding itself.")}
    </div>
  </div>
</section>

<section class="cream">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">Get involved</span>
      <h2>Join the community-led network</h2>
      <p>Churches, houses of worship, businesses, organizations, and residents are all invited. Register for the webinar, share your ideas, or ask to be kept up to date. Registration is handled on the J. Cooper Jr. LLC website.</p>
      <ul class="checks">
        <li>Hear the full plan for the campus</li>
        <li>Share ideas, questions, and concerns</li>
        <li>Learn how community investment and the service dividend work</li>
      </ul>
      <div class="btn-row">
        <a class="btn" href="{WEBINAR}" target="_blank" rel="noopener">Save my spot</a>
        <a class="btn ghost" href="tel:+18774019191">Call JCJ: (877) 401-9191</a>
      </div>
    </div>
    <a class="photo reveal" href="http://uidcdevelopment.org" target="_blank" rel="noopener" style="max-width:440px;margin-inline:auto">
      <img src="assets/img/rockton-presentation.png" alt="Unity in the Community Development Center: view the presentation and donate at uidcdevelopment.org" width="712" height="690" style="aspect-ratio:auto" loading="lazy">
    </a>
  </div>
</section>

{cta("Why this project matters to Damon", "Workforce development is how a community turns a closed building into careers. If your organization wants to help in Rockford, or has a similar site elsewhere, he would like to hear from you.", primary=("contact.html", "Contact Damon"), secondary=(WEBINAR, "Webinar registration"))}
""",
)

# ---------------------------------------------------------------- Security
PAGES["security.html"] = (
    "Security for the Normal Person | DP Anderson Consulting",
    "Americans 60 and older reported $7.7 billion stolen in one year. Damon P. Anderson is launching security products to protect everyday people from scams and cyberbullying.",
    f"""<section class="hero page-hero">
  <div class="wrap">
    <span class="eyebrow">Launching soon</span>
    <h1>Security for the <span class="gold">normal person</span></h1>
    <p class="lead">Corporations and companies have to deal with cyberbullying and scamming. People do too, and they do it without a security team. Damon is preparing several products to change that.</p>
    <div class="btn-row"><a class="btn" href="#notify">Tell me when they launch</a><a class="btn ghost" href="#redflags">Scam red flags</a></div>
  </div>
</section>

<section class="stat-band">
  <div class="wrap split">
    <div>
      <div class="stat reveal" data-count="7.7" data-prefix="$" data-suffix="B">$7.7B</div>
      <p class="stat-note">Source: FBI Internet Crime Complaint Center (IC3), losses reported by people aged 60 and older, 2025.</p>
    </div>
    <div class="reveal">
      <h2>Stolen from retirees in one year</h2>
      <p class="lead">That is only what people aged 60 and above reported, and it is one age group. The rest of the numbers are worse, and many victims never report at all.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Who it is for</span>
      <h2>The people attackers count on being unprotected</h2>
    </div>
    <div class="grid g3">
      {card("heart", "Retirees and their families", "Tech-support scams, fake investment offers, romance scams, and impostors posing as banks, agencies, or grandchildren.")}
      {card("people", "Parents, kids, and teens", "Cyberbullying, harassment, and extortion that follow young people home through their phones.")}
      {card("build", "Small businesses and their staff", "The invoice fraud, account takeovers, and impersonation that large companies pay teams to stop.")}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split top">
    <div class="reveal">
      <span class="eyebrow">The approach</span>
      <h2>Built by a former CIO and acting CISO, written for your grandmother</h2>
      <p>Damon built the information security team at the Pennsylvania Public Utility Commission, served on the NARUC Critical Infrastructure Committee, and is researching cybersecurity leadership at the doctoral level. The products he is preparing take what works for large organizations and make it usable for one person with a phone.</p>
      <p>He is also a longtime domestic violence advocate, and he sees one word connecting that work to cybersecurity: victimization. In both, power is being abused, and the person causing the harm is responsible, never the victim.</p>
      <ul class="checks">
        <li>Plain language, with no jargon and no assumption of technical skill</li>
        <li>Automated wherever possible, so protection does not depend on remembering to do something</li>
        <li>Focused on the two threats ordinary people face most: scams and cyberbullying</li>
      </ul>
      <p style="margin-top:1.4rem;color:var(--muted)">Product names and launch dates will be announced here.</p>
    </div>
    <div class="callout reveal" id="notify">
      <h2>Be first to know</h2>
      <p>Leave your email and Damon will let you know when the first product is available.</p>
      <form data-mailto="{EMAIL}" data-subject="Notify me: security products">
        <label>Name<input name="Name" autocomplete="name" required></label>
        <label>Email<input name="Email" type="email" autocomplete="email" required></label>
        <label>I am interested for
          <select name="Interested for"><option>Myself</option><option>A parent or older relative</option><option>My children</option><option>My business</option></select>
        </label>
        <button class="btn" type="submit">Notify me</button>
        <p class="form-note">This opens your email app with the message filled in.</p>
      </form>
    </div>
  </div>
</section>

<section class="cream" id="redflags">
  <div class="wrap split top">
    <div class="reveal">
      <span class="eyebrow">Use this today</span>
      <h2>Five red flags of a scam</h2>
      <ul class="checks">
        <li><strong>Urgency.</strong> You are told to act right now or something bad will happen.</li>
        <li><strong>Unusual payment.</strong> Gift cards, cryptocurrency, wire transfers, or cash by courier.</li>
        <li><strong>Secrecy.</strong> You are told not to tell your family or your bank.</li>
        <li><strong>Unexpected contact.</strong> A call, text, or pop-up you did not ask for, wanting information or remote access.</li>
        <li><strong>Too good to be true.</strong> Guaranteed returns, surprise prizes, or a new online friend who needs money.</li>
      </ul>
    </div>
    <div class="reveal">
      <span class="eyebrow">If it happens to you</span>
      <h2>Stop, verify, report</h2>
      <ul class="checks">
        <li><strong>Stop.</strong> Hang up or close the window. A real organization will let you call back.</li>
        <li><strong>Verify.</strong> Call the number on your card or statement, never one the caller gives you.</li>
        <li><strong>Report.</strong> File with the FBI at <a href="https://www.ic3.gov/" target="_blank" rel="noopener">ic3.gov</a> and the FTC at <a href="https://reportfraud.ftc.gov/" target="_blank" rel="noopener">reportfraud.ftc.gov</a>.</li>
        <li><strong>Age 60 or older?</strong> The National Elder Fraud Hotline is <a href="tel:+18333728311">833-372-8311</a>.</li>
        <li><strong>Call your bank</strong> immediately if money has moved. Speed matters.</li>
      </ul>
    </div>
  </div>
</section>

{cta("Want Damon to speak to your group?", "He recently spoke to the Pennsylvania Association of Retired State Employees about protecting their retirements from cyber scammers. Senior centers, churches, schools, and business associations are welcome to ask.", primary=("contact.html", "Request a talk"))}
""",
)

# ---------------------------------------------------------------- Contact
PAGES["contact.html"] = (
    "Contact | DP Anderson Consulting",
    "Contact Damon P. Anderson at DP Anderson Consulting: (866) 294-2319 or info@dpaconsult.com.",
    f"""<section class="hero page-hero">
  <div class="wrap split top">
    <div>
      <span class="eyebrow">Contact</span>
      <h1>Start with a conversation</h1>
      <p class="lead">Tell Damon what you are working on. The first conversation is free and there is no obligation.</p>
      <ul class="contact-list">
        <li><span>Phone</span><a href="{PHONE_HREF}">{PHONE}</a></li>
        <li><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span>LinkedIn</span><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/damonanderson</a></li>
        <li><span>Based in</span><b>Lancaster, Pennsylvania</b></li>
      </ul>
    </div>
    <div class="callout">
      <h2>Send a message</h2>
      <form data-mailto="{EMAIL}" data-subject="Inquiry from dpaconsult.com">
        <div class="row2">
          <label>Name<input name="Name" autocomplete="name" required></label>
          <label>Organization<input name="Organization" autocomplete="organization"></label>
        </div>
        <div class="row2">
          <label>Email<input name="Email" type="email" autocomplete="email" required></label>
          <label>Phone<input name="Phone" type="tel" autocomplete="tel"></label>
        </div>
        <label>I am interested in
          <select name="Interested in">
            <option>Consulting or solutions architecture</option>
            <option>Coaching</option>
            <option>Rockton Hospital Repurposing Project</option>
            <option>Security products</option>
            <option>Speaking</option>
            <option>Something else</option>
          </select>
        </label>
        <label>How can Damon help?<textarea name="Message" required></textarea></label>
        <button class="btn" type="submit">Send message</button>
        <p class="form-note">This opens your email app with the message filled in.</p>
      </form>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap callout reveal">
    <span class="tag">Rockton Hospital Repurposing Project</span>
    <h2>Looking for webinar registration?</h2>
    <p class="lead">Registration and the community sign-up form are on the J. Cooper Jr. LLC website.</p>
    <div class="btn-row"><a class="btn" href="{WEBINAR}" target="_blank" rel="noopener">Save my spot</a><a class="btn ghost" href="workforce.html">About the project</a></div>
  </div>
</section>
""",
)

if __name__ == "__main__":
    for slug, (title, desc, body) in PAGES.items():
        (ROOT / slug).write_text(layout(slug, title, desc, body), encoding="utf-8", newline="\n")
        print("wrote", slug)
