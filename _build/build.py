import os, hashlib
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# ---- App Store launch switch -------------------------------------------------
# Leave empty until Apple approves the app. Then paste the numeric App Store ID
# (App Store Connect › App Information › Apple ID, e.g. "6741234567") and rebuild:
# every page switches from "Coming soon" to the official badge, the Safari app banner
# and a QR code. Also set AppContact.appStoreID in the app (Feedback.swift).
APP_STORE_ID = ""

STORE_URL = f"https://apps.apple.com/app/id{APP_STORE_ID}" if APP_STORE_ID else ""
# Apple's official badge artwork, served by Apple Marketing Tools (must not be altered).
BADGE_BLACK = "https://tools.applemarketingtools.com/api/badges/download-on-the-app-store/black/en-us?size=250x83"
BADGE_WHITE = "https://tools.applemarketingtools.com/api/badges/download-on-the-app-store/white/en-us?size=250x83"

def store_badge(height=54):
    """The official Download on the App Store badge, or a Coming soon label before launch."""
    if not STORE_URL:
        return '<span class="soon">Coming soon to the App Store</span>'
    return (f'<a class="store-badge" href="{STORE_URL}" aria-label="Download DiaPetic on the App Store">'
            f'<picture><source srcset="{BADGE_WHITE}" media="(prefers-color-scheme: dark)">'
            f'<img src="{BADGE_BLACK}" alt="Download on the App Store" height="{height}" style="height:{height}px;width:auto"></picture></a>')

def store_qr():
    """QR code to the App Store page, for people reading on a computer (hidden on phones)."""
    if not STORE_URL:
        return ""
    import segno, io
    buf = io.BytesIO()
    segno.make(STORE_URL, error="m").save(buf, kind="svg", scale=4, border=2, dark="#1C1B2E", light="#FFFFFF", xmldecl=False, svgns=True)
    svg = buf.getvalue().decode()
    return f'<div class="store-qr"><div class="qr-img" role="img" aria-label="QR code linking to DiaPetic on the App Store">{svg}</div><p>Scan with your iPhone camera to open the App Store.</p></div>'

NOTIFY = ('<p class="note">To be notified when DiaPetic is available, email '
          '<a href="mailto:support@diapetic.com?subject=Notify%20me%20when%20DiaPetic%20is%20available">support@diapetic.com</a>.</p>')

NAV = [("index.html", "Home"), ("help.html", "How to use"), ("faq.html", "FAQ & support"), ("privacy.html", "Privacy")]

def icon(path):
    return f'<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

ICONS = {
 "syringe": '<path d="M18 2l4 4M17 7l3-3M19 9 9 19l-4 1 1-4L16 6zM7 13l4 4M10 10l4 4"/>',
 "bell": '<path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
 "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "cross": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M12 10.5v6M9 13.5h6"/>',
 "bowl": '<path d="M3 11h18a9 9 0 0 1-18 0zM8 7c0-1.5 1-2 1-3M12 7c0-1.5 1-2 1-3M16 7c0-1.5 1-2 1-3"/>',
 "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M8 7h8M8 11h6"/>',
 "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 17v5"/>',
}

CSSV = hashlib.md5(open(os.path.join(OUT, "style.css"), "rb").read()).hexdigest()[:8]

def page(fname, title, desc, body, nav_key=None):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == (nav_key or fname) else ""}>{t}</a>' for h, t in NAV)
    foot = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://diapetic.com/img/icon-dog.png">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="style.css?v={CSSV}">{f'\n<meta name="apple-itunes-app" content="app-id={APP_STORE_ID}">' if APP_STORE_ID else ""}
</head>
<body>
<header class="site-head">
<div class="wrap">
<a class="brand" href="index.html" aria-label="DiaPetic home"><img src="img/icon-dog.png" alt=""><span class="wordmark">Dia<b>PET</b>ic</span></a>
<nav class="nav" aria-label="Main">{nav}</nav>
</div>
</header>
<main>
{body}
</main>
<footer class="site-foot">
<div class="wrap">
<div class="foot-get">{store_badge(40)}</div>
<p>© 2026 Bryan Flynn · <a href="mailto:support@diapetic.com">support@diapetic.com</a></p>
<nav aria-label="Footer">{foot}</nav>
</div>
</footer>
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(html)

# ---------------- Home ----------------
def feature(ic, title, text):
    return f'<div class="feature"><span class="dot" style="color:var(--indigo)">{icon(ICONS[ic])}</span><h3>{title}</h3><p>{text}</p></div>'

home = f'''
<section class="hero">
<div class="wrap">
<div>
<p class="eyebrow">For dogs and cats with diabetes</p>
<h1>Diabetes care for your pet, organized in one place.</h1>
<p class="lead">DiaPetic helps you give insulin on schedule, avoid missed or repeated doses, and share accurate records with your veterinarian.</p>
<div class="cta">
{store_badge(54) if STORE_URL else '<a class="btn btn-primary" href="#get">Coming soon to the App Store</a>'}
<a class="btn btn-ghost" href="help.html">Read the guide</a>
</div>
<p class="note" style="margin-top:14px">Free to download. DiaPetic Pro is a one-time purchase of $9.99.</p>
</div>
<img class="hero-icon" src="img/icon-dog.png" alt="DiaPetic app icon: Obi, a curly-haired dog, with an orange collar and a red blood-drop tag" width="300" height="300">
</div>
</section>

<section>
<div class="wrap">
<div class="section-head">
<p class="eyebrow">What it does</p>
<h2>Designed for a real diabetic dog's needs</h2>
<p>Managing diabetes means insulin twice a day, carefully timed meals, and regular conversations with your veterinarian. DiaPetic keeps everything together, so nothing is missed and nothing is given twice.</p>
</div>
<div class="features">
{feature("syringe", "Quick daily logging", "Record each shot with the time it was given, how much of each meal was eaten, and a brief daily check-in that defaults to normal.")}
{feature("bell", "Dependable reminders", "Reminders for insulin, meals, medications, glucose checks and appointments, with a follow-up if a shot has not been recorded.")}
{feature("doc", "Reports for your veterinarian", "Clear summaries covering 7 to 180 days, including shots, appetite, symptoms, weight, glucose curves and dose history, ready to share as a PDF.")}
{feature("cross", "Help in an emergency", "An emergency button on every screen with step-by-step guidance for low blood sugar, missed or repeated doses and other urgent situations.")}
{feature("box", "Supply tracking", "Keeps track of the insulin bottle in use, spare bottles, syringes and food, and alerts you before anything runs low.")}
{feature("mic", "A daily journal", "Record observations by typing or speaking. Entries are saved with the day's records and included in your reports.")}
</div>
</div>
</section>

<section>
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Inside the app</p>
<h2>Clear screens for everyday care</h2>
</div>
<div class="shots">
<figure class="shot"><img src="img/reports.jpg" alt="Reports screen showing food eaten, calories, shots given and weight" width="600" height="1304" loading="lazy"><figcaption>Progress reports for your veterinarian</figcaption></figure>
<div style="display:flex;flex-direction:column;gap:18px">
<figure class="shot"><img src="img/appointment.jpg" alt="Next vet appointment card with call, directions and calendar buttons" width="600" height="459" loading="lazy"><figcaption>Appointments synced with your calendar</figcaption></figure>
<figure class="shot"><img src="img/diet.jpg" alt="Diet summary with calories per pound and the morning and evening split" width="600" height="382" loading="lazy"><figcaption>Detailed nutrition tracking</figcaption></figure>
</div>
<figure class="shot"><img src="img/icons-grid.png" alt="Twelve app icons: Obi the dog and an orange kitty in regular and seasonal styles" width="596" height="804" loading="lazy"><figcaption>Dog and cat app icons with seasonal designs (Pro)</figcaption></figure>
</div>
</div>
</section>

<section class="story">
<div class="wrap">
<img src="img/icon-dog.png" alt="" width="300" height="300" style="width:min(260px,70%);border-radius:22%;justify-self:center">
<div>
<p class="eyebrow">Our story</p>
<h2 style="margin-top:10px">Made for Obi</h2>
<p style="margin-top:14px">DiaPetic began as a tracker for Obi, a diabetic Sheepadoodle, created by his owner to keep his insulin, meals and veterinary notes in order.</p>
<p>It soon became clear that other families caring for a diabetic pet needed the same thing: a clear, private and dependable way to manage daily care and to make veterinary visits more productive.</p>
</div>
</div>
</section>

<section id="get">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Pricing</p>
<h2>Free to use, with an optional one-time upgrade</h2>
</div>
<div class="pricing">
<div class="plan">
<h3>Free</h3>
<p class="price">$0</p>
<ul>
<li>Daily logging of shots, meals and check-ins</li>
<li>Insulin reminders and follow-ups for unrecorded shots</li>
<li>Emergency guidance on every screen</li>
<li>Appointments with calendar sync</li>
<li>Supply tracking, journal and backups</li>
<li>Reports for the last 30 days</li>
</ul>
</div>
<div class="plan pro">
<h3>DiaPetic Pro</h3>
<p class="price">$9.99 <span class="note">one time</span></p>
<ul>
<li>PDF and CSV reports for your veterinarian</li>
<li>90- and 180-day trends</li>
<li>Multiple pets</li>
<li>Custom reminders, such as heartworm prevention, refills and vaccines</li>
<li>Dog and cat app icons with seasonal designs</li>
<li>Shared with your Family Sharing group</li>
</ul>
</div>
</div>
<div class="get-app">
<div>
<h3>{"Download DiaPetic" if STORE_URL else "Coming soon to the App Store"}</h3>
<p>{"Available for iPhone. Free to download, with an optional one-time upgrade." if STORE_URL else "DiaPetic for iPhone will be available on the App Store soon."}</p>
{store_badge(54) if STORE_URL else NOTIFY}
</div>
{store_qr()}
</div>
<p class="safety" style="margin-top:24px"><strong>Important:</strong> DiaPetic is a record-keeping tool. It does not recommend insulin doses or changes to treatment and is not a substitute for veterinary care. Always follow your veterinarian's instructions.</p>
</div>
</section>
'''
page("index.html", "DiaPetic: Pet Diabetes Log", "Track insulin, meals and glucose for your diabetic dog or cat, receive reminders, and share clear reports with your veterinarian.", home)

# ---------------- Screen illustrations (demo pet "Biscuit") ----------------
def tog(on): return f'<span class="m-tog{" on" if on else ""}"></span>'
def pill(t, color, fill=False):
    return (f'<span class="m-pill m-fill" style="background:var({color})">{t}</span>' if fill
            else f'<span class="m-pill" style="color:var({color});background:color-mix(in srgb, var({color}) 15%, transparent)">{t}</span>')
def fig(body, cap, alt):
    return f'<figure class="shotfig"><div class="mock" role="img" aria-label="{alt}">{body}</div><figcaption>{cap}</figcaption></figure>'

MOCKS = {
"setup": fig('''
<div class="m-h">Insulin prescribed by your veterinarian</div>
<div class="m-card"><div class="m-row"><span>Insulin</span><span class="m-v">Vetsulin · U-40 ›</span></div></div>
<div class="m-h" style="color:var(--m-orange)">Morning shot</div>
<div class="m-card"><div class="m-row"><span>Units</span><span class="m-v">8</span></div><div class="m-row"><span>Time</span><span class="m-v">7:00 AM</span></div></div>
<div class="m-h" style="color:var(--m-indigo)">Evening shot</div>
<div class="m-card"><div class="m-row"><span>Units</span><span class="m-v">8</span></div><div class="m-row"><span>Time</span><span class="m-v">7:00 PM</span></div></div>
<div class="m-foot">Set units to 0 for a shot your pet doesn't get. DiaPetic records doses; it never recommends one.</div>
''', "Enter the insulin, doses and times exactly as prescribed.", "Setup screen with the prescribed insulin, morning shot 8 units at 7 AM and evening shot 8 units at 7 PM"),

"day": fig('''
<div class="m-h" style="color:var(--m-orange)">☀︎ Morning</div>
<div class="m-card">
<div class="m-row" style="border:0"><span><span class="m-b">Meal</span><span class="m-sub">1 cup kibble · ≈390 kcal</span></span></div>
<div class="m-seg"><span style="background:var(--m-orange);color:#fff">All</span><span>Most</span><span>Some</span><span>None</span></div>
<div class="m-row"><span><span class="m-b">Insulin</span><span class="m-sub">8 units of Vetsulin</span></span>''' + pill("Give 8 u", "--m-orange", True) + '''</div>
</div>
<div class="m-sheet" style="margin-top:10px">
<div><b>When was the shot given?</b>Record the time Biscuit actually got the insulin.</div>
<div>Just now (7:04 AM)</div><div>At the scheduled time (7:00 AM)</div><div>A different time…</div>
</div>
''', "Record the meal, tap Give, and choose when the shot was given.", "Morning card with the meal marked All and a Give 8 units button, and the When was the shot given menu"),

"journal": fig('''
<div class="m-nav"><span>Cancel</span><b>Thu, Oct 15</b><span class="m-b">Save</span></div>
<div class="m-mic"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 17v5"/></svg></div>
<div style="text-align:center;font-weight:600;color:var(--m-indigo);font-size:14px">Tap to talk about the day</div>
<div class="m-card" style="margin-top:8px"><div class="m-row" style="display:block">Ate all his breakfast but seemed tired after our walk. Drinking a bit more water tonight. Ask the vet about the new food.</div></div>
<div class="m-card"><div class="m-row"><span>Time</span><span class="m-v">8:40 PM</span></div></div>
''', "Tap the microphone to dictate a journal entry.", "Journal editor with a large microphone button and a dictated entry"),

"reminders": fig('''
<div class="m-h" style="color:var(--m-indigo)">Insulin</div>
<div class="m-card"><div class="m-row"><span>Insulin time</span>''' + tog(True) + '''</div><div class="m-row"><span>Nudge if a shot isn't logged</span>''' + tog(True) + '''</div></div>
<div class="m-h" style="color:var(--m-orange)">Meals and care</div>
<div class="m-card"><div class="m-row"><span>Meals</span>''' + tog(True) + '''</div><div class="m-row"><span>Glucose checks</span>''' + tog(False) + '''</div></div>
<div class="m-h" style="color:var(--m-blue)">Supplies</div>
<div class="m-card"><div class="m-row"><span>Insulin running low</span>''' + tog(True) + '''</div><div class="m-row"><span>Time to open a new bottle</span>''' + tog(True) + '''</div></div>
''', "Choose the reminders that suit your routine.", "Reminders screen with switches for insulin time, missed-shot nudge, meals, glucose checks and supplies"),

"supplies": fig('''
<div class="m-h" style="color:var(--m-blue)">Insulin Supplies</div>
<div class="m-card">
<div class="m-row" style="display:block"><span class="m-b">Insulin</span>
<span class="m-sub" style="color:var(--m-fg)">In use · day 12 of 42 · about 210 units left</span>
<span class="m-sub">Use by Nov 22 · In the fridge: 1 unopened bottle</span>
<span class="m-sub" style="color:var(--m-blue);font-weight:600">Supply lasts until about Dec 30</span></div>
<div class="m-btns">''' + pill("Open new bottle", "--m-blue", True) + pill("Manage", "--m-blue") + '''</div>
<div class="m-row" style="display:block"><span class="m-b">Syringes</span>
<span class="m-sub" style="color:var(--m-fg)">In use · about 64 left</span>
<span class="m-sub">Unopened: 1 box (100 syringes)</span>
<span class="m-sub" style="color:var(--m-blue);font-weight:600">Supply lasts until about Feb 10</span></div>
<div class="m-btns">''' + pill("Start new box", "--m-blue", True) + pill("Manage", "--m-blue") + '''</div>
</div>
''', "Supplies on hand and their expected run-out dates.", "Supplies section showing the insulin bottle in use, a spare in the fridge, syringes and run-out dates"),

"vet": fig('''
<div class="m-h" style="color:var(--m-red)">Next appointment</div>
<div class="m-card">
<div class="m-row" style="display:block"><span class="m-b">Glucose curve</span><span class="m-sub" style="color:var(--m-fg)">Thu, Oct 22 · 8:00 AM – 4:00 PM</span><span class="m-sub">Bring: the insulin, a morning meal, your questions</span></div>
<div class="m-btns" style="display:grid;grid-template-columns:repeat(3,1fr)">''' + pill("Call", "--m-red") + pill("Directions", "--m-red") + pill("In Calendar", "--m-red") + '''</div>
</div>
''', "Each appointment shows the time, what to bring, and quick actions.", "Next appointment card for a glucose curve with Call, Directions and In Calendar buttons"),

"reports": fig('''
<div class="m-title">Reports</div>
<div class="m-h">At a glance · 30 days</div>
<div class="m-tiles">
<div class="m-tile"><span class="m-sub" style="color:var(--m-green)">Food eaten</span><b>96%</b><span class="m-sub">of planned meals</span></div>
<div class="m-tile"><span class="m-sub" style="color:var(--m-orange)">Calories a day</span><b>712</b><span class="m-sub">97% of target</span></div>
<div class="m-tile"><span class="m-sub" style="color:var(--m-indigo)">Shots given</span><b>100%</b><span class="m-sub">0 not logged</span></div>
<div class="m-tile"><span class="m-sub" style="color:var(--m-blue)">Weight</span><b>48 lb</b><span class="m-sub">steady</span></div>
</div>
''', "A summary of recent weeks at a glance.", "Reports at a glance: food eaten 96 percent, 712 calories a day, shots given 100 percent, weight 48 pounds"),

"emergency": fig('''
<div class="m-title" style="color:var(--m-red)">Emergency</div>
<div class="m-card"><div class="m-row" style="justify-content:center">''' + pill("Help me decide what to do", "--m-red", True) + '''</div></div>
<div class="m-h">Call now</div>
<div class="m-card"><div class="m-row"><span>Your veterinarian</span><span class="m-v" style="color:var(--m-red)">Call</span></div><div class="m-row"><span>Emergency clinic</span><span class="m-v" style="color:var(--m-red)">Call</span></div><div class="m-row"><span>Pet poison hotline</span><span class="m-v" style="color:var(--m-red)">Call</span></div></div>
<div class="m-h">Quick guides</div>
<div class="m-card"><div class="m-row"><span>Low blood sugar</span><span class="m-v">›</span></div><div class="m-row"><span>Unsure if the shot was given</span><span class="m-v">›</span></div></div>
''', "Calls, guided questions and step-by-step guides, available from every screen.", "Emergency screen with a Help me decide button, call buttons and quick guides"),

"backup": fig('''
<div class="m-title">Backup and restore</div>
<div class="m-card"><div class="m-row" style="justify-content:center">''' + pill("Back up now", "--m-blue", True) + '''</div><div class="m-row"><span>Last backup</span><span class="m-v">Today, 7:10 AM</span></div><div class="m-row"><span>Weekly automatic copy</span><span class="m-v">Keeps 4</span></div></div>
<div class="m-card"><div class="m-row"><span style="color:var(--m-blue)">Restore from backup</span><span class="m-v">›</span></div></div>
<div class="m-foot">Save the file to iCloud Drive or anywhere in Files.</div>
''', "Back up to iCloud Drive or Files, and restore on a new iPhone.", "Backup and restore screen with Back up now and Restore from backup"),
}

# ---------------- Guide (How to use hub + chapters) ----------------
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "guide_content.py")).read())

def chapter_file(slug): return f"guide-{slug}.html"

cards = "".join(
    f'<a class="chapter" href="{chapter_file(slug)}"><span class="num">{i}</span><span><strong>{title}</strong><span>{summary}</span></span></a>'
    for i, (slug, title, summary, _intro, _secs, _mocks) in enumerate(CHAPTERS, 1))
hub = f'''
<div class="wrap">
<header class="page-head narrow">
<p class="eyebrow">How to use</p>
<h1>The DiaPetic guide</h1>
<p>This guide explains each part of DiaPetic in detail. If you are new to the app, begin with <a href="{chapter_file("getting-started")}">Getting started</a> and then read <a href="{chapter_file("tracker")}">The Daily Tracker</a>. You can open the guide from within the app at any time under your pet\u2019s tab \u203a Help and support. The illustrations show a sample pet named Biscuit.</p>
</header>
<nav class="chapters" aria-label="Guide chapters">{cards}</nav>
<p class="safety" style="margin-top:32px"><strong>Please note:</strong> DiaPetic keeps records and sends reminders. It does not recommend insulin doses or changes to treatment. Always follow your veterinarian\u2019s instructions.</p>
<p style="margin:20px 0 56px">If you cannot find what you need, see the <a href="faq.html">FAQ</a> or email <a href="mailto:support@diapetic.com">support@diapetic.com</a>.</p>
</div>
'''
page("help.html", "How to use DiaPetic", "The complete DiaPetic guide: setup, daily logging, food, medications, glucose, reminders, supplies, vet visits, reports, emergencies and backups.", hub)

for i, (slug, title, summary, intro, secs, mocks) in enumerate(CHAPTERS):
    toc = "".join(f'<li><a href="#{a}">{h}</a></li>' for a, h, _ in secs)
    # place each illustration after the section it belongs to
    placed = {"setup": "insulin", "day": "shots", "journal": "journal", "reminders": "insulin",
              "supplies": "syringes", "vet": "appointments", "reports": "progress", "emergency": "summary", "backup": "restore"}
    body_secs = ""
    for a, h, html in secs:
        body_secs += f'<h2 id="{a}">{h}</h2>{html}'
        for m in mocks:
            if placed.get(m) == a:
                body_secs += MOCKS[m]
    prev_link = f'<a href="{chapter_file(CHAPTERS[i-1][0])}">\u2039 {CHAPTERS[i-1][1]}</a>' if i > 0 else '<a href="help.html">\u2039 All chapters</a>'
    next_link = f'<a href="{chapter_file(CHAPTERS[i+1][0])}">{CHAPTERS[i+1][1]} \u203a</a>' if i < len(CHAPTERS) - 1 else '<a href="faq.html">FAQ \u203a</a>'
    body = f'''
<div class="wrap narrow">
<header class="page-head">
<p class="eyebrow"><a href="help.html">Guide</a> \u00b7 Chapter {i + 1} of {len(CHAPTERS)}</p>
<h1>{title}</h1>
{intro}
</header>
<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>{toc}</ol></nav>
<article class="article">
{body_secs}
<nav class="pager" aria-label="Chapters">{prev_link}{next_link}</nav>
</article>
</div>
'''
    page(chapter_file(slug), f"{title} \u00b7 DiaPetic guide", summary, body, nav_key="help.html")

# ---------------- FAQ ----------------
faq_groups = [
("Using the app", [
("I forgot to record a shot. Can I add it later?", "<p>Yes. Go to that day on the Tracker by swiping back or using the calendar button, tap <strong>Give</strong> on the shot, and choose <strong>A different time…</strong> to enter when it was given.</p>"),
("What does \"Not logged\" mean?", "<p>It means the scheduled time has passed and no shot has been recorded yet. It does not necessarily mean the shot was missed. If reminders are on, DiaPetic will send a follow-up.</p><p>If you are unsure whether the shot was given, do not give another one. Call your veterinarian.</p>"),
("Does DiaPetic recommend insulin doses?", "<p>No. Insulin doses must always come from your veterinarian. DiaPetic records the prescribed dose and what was actually given, so your veterinarian has accurate information for making those decisions.</p>"),
("Can I use DiaPetic for a cat, or for more than one pet?", "<p>Yes. DiaPetic works for both dogs and cats. Your first pet is free, and additional pets are included with DiaPetic Pro.</p>"),
("Can two people use DiaPetic for the same pet?", "<p>Not yet. Each iPhone currently keeps its own records. Sharing between family members is planned for a future update.</p>"),
("Why are reminders not appearing?", "<p>First, go to iPhone <strong>Settings › Notifications › DiaPetic</strong> and make sure notifications are allowed. Then check that a Focus mode, such as Sleep or Do Not Disturb, is not silencing them. In DiaPetic, open your pet's tab › Reminders to confirm that the reminder is turned on.</p>"),
("Can I speak instead of typing?", "<p>Yes. In the journal and the suggestion box, tap the microphone and speak. The first time, your iPhone will ask for permission to use the microphone and speech recognition.</p>"),
]),
("Your data and privacy", [
("Where is my information stored?", "<p>Your information is stored only on your iPhone. DiaPetic has no accounts, advertising, analytics or servers. Information leaves your phone only when you choose to share it, for example by sending a report or saving a backup.</p>"),
("Can my veterinarian see my records?", "<p>Your veterinarian sees only what you send, such as a PDF report or an email from the Vet tab. There is no online portal or automatic sharing.</p>"),
("How do I move to a new iPhone?", "<p>On your current iPhone, go to your pet's tab › Backup and restore, tap <strong>Back up now</strong> and save the file to iCloud Drive. On the new iPhone, install DiaPetic, open Backup and restore, tap <strong>Restore from backup…</strong> and select the file.</p>"),
("What happens to my records if I delete the app?", "<p>Deleting the app removes its data from your iPhone. Your records can be recovered only from a backup, so be sure to make one first.</p>"),
]),
("DiaPetic Pro and purchases", [
("What does DiaPetic Pro include? Is it a subscription?", "<p>DiaPetic Pro is a one-time purchase of $9.99, not a subscription. It adds PDF and CSV reports, 90- and 180-day trends, multiple pets, custom reminders, and dog and cat app icons with seasonal designs. It is shared with your Family Sharing group.</p>"),
("How do I restore DiaPetic Pro on another iPhone?", "<p>Open the Pro screen in your pet's tab and tap <strong>Restore purchase</strong> while signed in with the same Apple Account.</p>"),
("What are tips?", "<p>Tips are optional contributions, available under <em>Support DiaPetic</em>, that help cover the cost of maintaining the app. They do not unlock any features. Everything related to your pet's safety is always free.</p>"),
("How do I change the app icon?", "<p>With DiaPetic Pro, go to your pet's tab › App settings › App icon. Choose Obi the dog or Kitty, then choose whether the icon changes with the seasons, stays the same all year, or keeps one seasonal theme.</p>"),
]),
]
groups = ""
for g, items in faq_groups:
    groups += f"<h2>{g}</h2>" + "".join(f"<details><summary>{q}</summary><div>{a}</div></details>" for q, a in items)
faq_body = f'''
<div class="wrap narrow">
<header class="page-head">
<p class="eyebrow">FAQ &amp; support</p>
<h1>Frequently asked questions</h1>
<p>Answers to common questions about DiaPetic. For step-by-step instructions, see the <a href="help.html">guide</a>.</p>
</header>
<div class="faq article">
{groups}
<div class="contact">
<h2 style="color:#FFFFFF">Still need help?</h2>
<p>Please email us with your iPhone model and a description of what happened. We also welcome suggestions, which you can send from within the app under your pet's tab › Help and support › Suggestion box.</p>
<a href="mailto:support@diapetic.com">support@diapetic.com</a>
</div>
<p class="safety" style="margin-top:28px"><strong>In an emergency</strong>, call your veterinarian or the nearest emergency clinic. For possible poisoning, contact the ASPCA Animal Poison Control Center at (888) 426-4435. A consultation fee may apply.</p>
</div>
</div>
'''
page("faq.html", "DiaPetic FAQ and support", "Answers to common questions about DiaPetic and how to contact support.", faq_body)

# ---------------- Privacy ----------------
privacy_body = f'''
<div class="wrap narrow">
<header class="page-head">
<p class="eyebrow">Privacy</p>
<h1>Privacy policy</h1>
<p>Effective October 17, 2026</p>
</header>
<article class="article">
<p><strong>Summary:</strong> DiaPetic does not collect your data. The information you enter remains on your iPhone. The app has no accounts, advertising, analytics or tracking, and the developer operates no server that receives your information.</p>

<h2>Who we are</h2>
<p>DiaPetic is an iPhone app developed by Bryan Flynn ("we," "us"). You can contact us at <a href="mailto:support@diapetic.com">support@diapetic.com</a>.</p>

<h2>Information you enter</h2>
<p>Your pet's details, shots, meals, check-ins, glucose readings, journal entries, supplies, appointments and settings are stored only on your iPhone, in the app's private storage. We have no access to them.</p>

<h2>When information leaves your iPhone</h2>
<p>Information leaves your iPhone only when you choose to share it:</p>
<ul>
<li><strong>Sharing:</strong> reports, the pet information sheet and CSV files are sent only to the destinations you choose, such as email, Messages, AirDrop, Files or a printer.</li>
<li><strong>Email:</strong> emails to your veterinarian and messages from the suggestion box are sent from your own email app, and you can review them before sending. Messages sent to us are used only to respond and to improve the app.</li>
<li><strong>Backups:</strong> backup files are saved to the location you choose, such as iCloud Drive or Files. Backups stored in iCloud are kept in your own iCloud account under Apple's terms.</li>
</ul>

<h2>Permissions the app may ask for</h2>
<ul>
<li><strong>Notifications:</strong> to deliver the reminders you turn on.</li>
<li><strong>Calendar:</strong> to add your pet's appointments to your calendar and update or remove them when you change them in the app. DiaPetic does not read or share your other events.</li>
<li><strong>Camera:</strong> only to read calorie information from pet food labels. No photos are taken or saved.</li>
<li><strong>Location:</strong> only to find veterinarians and emergency clinics near you, using Apple Maps. Your location is not stored.</li>
<li><strong>Microphone and speech recognition:</strong> only while you dictate a journal entry or suggestion. Recordings are not saved; only the resulting text is kept. Speech is processed on your iPhone when supported; otherwise it is processed by Apple under Apple's privacy policy.</li>
</ul>
<p>You can change any of these permissions in iPhone Settings › DiaPetic.</p>

<h2>Purchases and ratings</h2>
<p>Purchases of DiaPetic Pro and tips are processed by Apple through the App Store. We do not receive your payment information. Apple may provide us with anonymous sales information, such as the number of purchases. Rating requests are displayed by Apple.</p>

<h2>Children</h2>
<p>DiaPetic is intended for adults caring for a pet and is not directed at children. We do not knowingly collect information from anyone.</p>

<h2>This website</h2>
<p>diapetic.com does not use cookies, analytics or tracking.{" The App Store badge image is loaded from Apple." if STORE_URL else ""} The site is hosted by GitHub Pages, which may keep standard server logs, such as IP addresses, for security purposes under GitHub's privacy statement.</p>

<h2>Not veterinary advice</h2>
<p>DiaPetic is a record-keeping tool. It does not recommend insulin doses or changes to treatment and is not a substitute for veterinary care.</p>

<h2>Changes to this policy</h2>
<p>If this policy changes, we will update this page and its effective date. If a change affects how your information is handled, we will also describe it in the app's release notes.</p>

<h2>Contact</h2>
<p>For questions about this policy, email <a href="mailto:support@diapetic.com">support@diapetic.com</a>.</p>
</article>
</div>
'''
page("privacy.html", "DiaPetic privacy policy", "DiaPetic does not collect your data. Everything you enter remains on your iPhone.", privacy_body)

# 404 and custom domain
page("404.html", "Page not found · DiaPetic", "The page you requested does not exist.", '<div class="wrap narrow"><header class="page-head"><h1>Page not found</h1><p>The page you requested does not exist. Please visit the <a href="index.html">home page</a>, the <a href="help.html">guide</a> or the <a href="faq.html">FAQ</a>.</p></header></div>')
open(os.path.join(OUT, "CNAME"), "w").write("diapetic.com\n")
open(os.path.join(OUT, "README.md"), "w").write("# diapetic.com\n\nThe DiaPetic website: home, how to use, FAQ & support, privacy policy. Plain HTML and CSS, hosted on GitHub Pages.\n\nThe pages are generated from `build.py` in the app project; edit there or edit the HTML directly.\n")
print("built")
