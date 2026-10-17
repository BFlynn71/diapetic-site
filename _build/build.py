import os, hashlib
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
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

def page(fname, title, desc, body):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
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
<link rel="stylesheet" href="style.css?v={CSSV}">
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
<p class="eyebrow">For diabetic dogs and cats</p>
<h1>Every shot, meal and vet visit, in one calm place.</h1>
<p class="lead">DiaPetic helps you give insulin on time, never twice, and hand your veterinarian a clear picture of how it's really going.</p>
<div class="cta">
<a class="btn btn-primary" href="#get">Coming soon to the App Store</a>
<a class="btn btn-ghost" href="help.html">See how it works</a>
</div>
<p class="note" style="margin-top:14px">Free to use · DiaPetic Pro is $9.99 once, no subscription</p>
</div>
<img class="hero-icon" src="img/icon-dog.png" alt="DiaPetic app icon: Obi, a curly-haired dog, with an orange collar and a red blood-drop tag" width="300" height="300">
</div>
</section>

<section>
<div class="wrap">
<div class="section-head">
<p class="eyebrow">What it does</p>
<h2>Built around a real diabetic dog's real days</h2>
<p>Twice-a-day insulin, meals that have to line up, and a vet who needs good notes. DiaPetic keeps it all together so nothing gets missed and nothing gets given twice.</p>
</div>
<div class="features">
{feature("syringe", "Log in a tap", "Record each shot with the time it was actually given, how much of each meal was eaten, and a quick daily check-in that starts at Normal.")}
{feature("bell", "Reminders that have your back", "Insulin time, a nudge if a shot wasn't logged, meals, medications, glucose checks and vet visits. Snooze when you need a minute.")}
{feature("doc", "Ready for your vet", "Clear reports for 7 to 180 days: shots, appetite, symptoms, weight, glucose curves and dose history. Share a PDF in seconds.")}
{feature("cross", "Help when something's wrong", "An emergency button on every screen with step-by-step help for low blood sugar, missed or doubled shots and more, plus one-tap calls.")}
{feature("box", "Supplies that don't run out", "Tracks the insulin bottle in use, spares in the fridge, syringes and food, and warns you before you run short.")}
{feature("mic", "A journal you can talk to", "Tap the microphone and describe the day. It's turned into text and kept with your records and reports.")}
</div>
</div>
</section>

<section>
<div class="wrap">
<div class="section-head">
<p class="eyebrow">A look inside</p>
<h2>Simple screens for stressful days</h2>
</div>
<div class="shots">
<figure class="shot"><img src="img/reports.jpg" alt="Reports screen showing food eaten, calories, shots given and weight" width="600" height="1304" loading="lazy"><figcaption>Reports your vet will actually read</figcaption></figure>
<div style="display:flex;flex-direction:column;gap:18px">
<figure class="shot"><img src="img/appointment.jpg" alt="Next vet appointment card with call, directions and calendar buttons" width="600" height="459" loading="lazy"><figcaption>Vet visits, synced to your calendar</figcaption></figure>
<figure class="shot"><img src="img/diet.jpg" alt="Diet summary with calories per pound and the morning and evening split" width="600" height="382" loading="lazy"><figcaption>Nutrition that adds up</figcaption></figure>
</div>
<figure class="shot"><img src="img/icons-grid.png" alt="Twelve app icons: Obi the dog and an orange kitty in regular and seasonal styles" width="596" height="804" loading="lazy"><figcaption>Dog or kitty, all year round (Pro)</figcaption></figure>
</div>
</div>
</section>

<section class="story">
<div class="wrap">
<img src="img/icon-dog.png" alt="" width="300" height="300" style="width:min(260px,70%);border-radius:22%;justify-self:center">
<div>
<p class="eyebrow">Why it exists</p>
<h2 style="margin-top:10px">Made for Obi</h2>
<p style="margin-top:14px">DiaPetic started as a tracker for Obi, a diabetic Sheepadoodle, built by his owner to keep his shots, meals and vet notes straight.</p>
<p>It turned out other families caring for a diabetic pet needed the same thing: something clear, calm and private that helps on the hard days and makes vet visits easier.</p>
</div>
</div>
</section>

<section id="get">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Pricing</p>
<h2>Free to use. Pro is one price, once.</h2>
</div>
<div class="pricing">
<div class="plan">
<h3>Free</h3>
<p class="price">$0</p>
<ul>
<li>Daily logging of shots, meals and check-ins</li>
<li>Insulin reminders and missed-shot nudges</li>
<li>Emergency help on every screen</li>
<li>Vet tab, appointments and calendar sync</li>
<li>Supplies, journal, backups</li>
<li>The last 30 days of reports</li>
</ul>
</div>
<div class="plan pro">
<h3>DiaPetic Pro</h3>
<p class="price">$9.99 <span class="note">once</span></p>
<ul>
<li>PDF and CSV reports for your vet</li>
<li>90- and 180-day trends</li>
<li>More than one pet</li>
<li>Your own reminders (heartworm, refills, vaccines…)</li>
<li>Dog or kitty app icons with seasonal looks</li>
<li>Shared with your Family Sharing group</li>
</ul>
</div>
</div>
<p class="safety" style="margin-top:24px"><strong>Important:</strong> DiaPetic is a record-keeping tool. It never recommends insulin doses or changes to treatment, and it isn't a substitute for veterinary care. Always follow your veterinarian's instructions.</p>
</div>
</section>
'''
page("index.html", "DiaPetic: Pet Diabetes Log", "Track insulin, meals and glucose for your diabetic dog or cat, get reminders, and share clear reports with your veterinarian.", home)

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
''', "Enter the insulin and times exactly as your vet prescribed.", "Setup screen with the prescribed insulin, morning shot 8 units at 7 AM and evening shot 8 units at 7 PM"),

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
''', "Mark the meal, tap Give, then choose when the shot was given.", "Morning card with the meal marked All and a Give 8 units button, and the When was the shot given menu"),

"journal": fig('''
<div class="m-nav"><span>Cancel</span><b>Thu, Oct 15</b><span class="m-b">Save</span></div>
<div class="m-mic"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 17v5"/></svg></div>
<div style="text-align:center;font-weight:600;color:var(--m-indigo);font-size:14px">Tap to talk about the day</div>
<div class="m-card" style="margin-top:8px"><div class="m-row" style="display:block">Ate all his breakfast but seemed tired after our walk. Drinking a bit more water tonight. Ask Dr. about the new food.</div></div>
<div class="m-card"><div class="m-row"><span>Time</span><span class="m-v">8:40 PM</span></div></div>
''', "Tap the microphone and talk; your words become the entry.", "Journal editor with a large microphone button and a dictated entry"),

"reminders": fig('''
<div class="m-h" style="color:var(--m-indigo)">Insulin</div>
<div class="m-card"><div class="m-row"><span>Insulin time</span>''' + tog(True) + '''</div><div class="m-row"><span>Nudge if a shot isn't logged</span>''' + tog(True) + '''</div></div>
<div class="m-h" style="color:var(--m-orange)">Meals and care</div>
<div class="m-card"><div class="m-row"><span>Meals</span>''' + tog(True) + '''</div><div class="m-row"><span>Glucose checks</span>''' + tog(False) + '''</div></div>
<div class="m-h" style="color:var(--m-blue)">Supplies</div>
<div class="m-card"><div class="m-row"><span>Insulin running low</span>''' + tog(True) + '''</div><div class="m-row"><span>Time to open a new bottle</span>''' + tog(True) + '''</div></div>
''', "Turn on just the reminders you want.", "Reminders screen with switches for insulin time, missed-shot nudge, meals, glucose checks and supplies"),

"supplies": fig('''
<div class="m-h" style="color:var(--m-blue)">Supplies</div>
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
''', "See what's on hand and when it runs out.", "Supplies section showing the insulin bottle in use, a spare in the fridge, syringes and run-out dates"),

"vet": fig('''
<div class="m-h" style="color:var(--m-red)">Next appointment</div>
<div class="m-card">
<div class="m-row" style="display:block"><span class="m-b">Glucose curve</span><span class="m-sub" style="color:var(--m-fg)">Thu, Oct 22 · 8:00 AM – 4:00 PM</span><span class="m-sub">Bring: the insulin, a morning meal, your questions</span></div>
<div class="m-btns" style="display:grid;grid-template-columns:repeat(3,1fr)">''' + pill("Call", "--m-red") + pill("Directions", "--m-red") + pill("In Calendar", "--m-red") + '''</div>
</div>
''', "Appointments with times, what to bring, and one-tap actions.", "Next appointment card for a glucose curve with Call, Directions and In Calendar buttons"),

"reports": fig('''
<div class="m-title">Reports</div>
<div class="m-h">At a glance · 30 days</div>
<div class="m-tiles">
<div class="m-tile"><span class="m-sub" style="color:var(--m-green)">Food eaten</span><b>96%</b><span class="m-sub">of planned meals</span></div>
<div class="m-tile"><span class="m-sub" style="color:var(--m-orange)">Calories a day</span><b>712</b><span class="m-sub">97% of target</span></div>
<div class="m-tile"><span class="m-sub" style="color:var(--m-indigo)">Shots given</span><b>100%</b><span class="m-sub">0 not logged</span></div>
<div class="m-tile"><span class="m-sub" style="color:var(--m-blue)">Weight</span><b>48 lb</b><span class="m-sub">steady</span></div>
</div>
''', "A quick read on how the last weeks went.", "Reports at a glance: food eaten 96 percent, 712 calories a day, shots given 100 percent, weight 48 pounds"),

"emergency": fig('''
<div class="m-title" style="color:var(--m-red)">Emergency</div>
<div class="m-card"><div class="m-row" style="justify-content:center">''' + pill("Help me decide what to do", "--m-red", True) + '''</div></div>
<div class="m-h">Call now</div>
<div class="m-card"><div class="m-row"><span>Your veterinarian</span><span class="m-v" style="color:var(--m-red)">Call</span></div><div class="m-row"><span>Emergency clinic</span><span class="m-v" style="color:var(--m-red)">Call</span></div><div class="m-row"><span>Pet poison hotline</span><span class="m-v" style="color:var(--m-red)">Call</span></div></div>
<div class="m-h">Quick guides</div>
<div class="m-card"><div class="m-row"><span>Low blood sugar</span><span class="m-v">›</span></div><div class="m-row"><span>Unsure if the shot was given</span><span class="m-v">›</span></div></div>
''', "One tap from any screen: calls, triage and step-by-step guides.", "Emergency screen with a Help me decide button, call buttons and quick guides"),

"backup": fig('''
<div class="m-title">Backup and restore</div>
<div class="m-card"><div class="m-row" style="justify-content:center">''' + pill("Back up now", "--m-blue", True) + '''</div><div class="m-row"><span>Last backup</span><span class="m-v">Today, 7:10 AM</span></div><div class="m-row"><span>Weekly automatic copy</span><span class="m-v">Keeps 4</span></div></div>
<div class="m-card"><div class="m-row"><span style="color:var(--m-blue)">Restore from backup</span><span class="m-v">›</span></div></div>
<div class="m-foot">Save the file to iCloud Drive or anywhere in Files.</div>
''', "Back up to iCloud Drive or Files, and restore on a new iPhone.", "Backup and restore screen with Back up now and Restore from backup"),
}

# ---------------- How to use ----------------
help_sections = [
("setup", "Set up your pet", '''
<p>The first time you open DiaPetic, you'll add your pet. Have your veterinarian's instructions and the insulin label nearby.</p>
<ul>
<li><strong>About your pet:</strong> name, dog or cat, breed, color, sex, weight and (optionally) the microchip number.</li>
<li><strong>Insulin:</strong> the insulin your vet prescribed, its strength (U-40 or U-100), and the units and time for the morning and evening shots. DiaPetic records what your vet prescribed. It never suggests a dose.</li>
<li><strong>Meals:</strong> the food and portions for each meal, and the daily calorie target if your vet gave you one.</li>
<li><strong>Your vet and an emergency clinic:</strong> names, phone numbers and addresses, so they're one tap away when you need them.</li>
</ul>
<p>You can change any of this later in the tab named after your pet (the last tab).</p>
'''),
("day", "Your daily routine", '''
<p>The <span class="path">Tracker</span> tab is where your day happens. Morning and evening each get a card with the meal, the shot and any medications.</p>
<h3>Logging a shot</h3>
<ol>
<li>Record how much of the meal was eaten: All, Most, Some or None.</li>
<li>Tap <strong>Give</strong> on the shot. DiaPetic asks when it was given: just now, at the usual time, or a different time.</li>
<li>The card shows the units and the time given, so anyone checking later knows it's done.</li>
</ol>
<div class="tip">Not sure whether a shot was given? Don't give another. Check the Tracker first, and if it isn't logged and no one remembers, call your veterinarian.</div>
<h3>The daily check-in</h3>
<p>Water, urine, energy, sleep, stool and vomiting all start at Normal and are saved that way. Just change anything that was different today.</p>
<h3>Moving between days</h3>
<p>Swipe left or right, use the arrows beside the date, or tap the <strong>calendar</strong> button to jump straight to any day. Tap the date to come back to today.</p>
'''),
("journal", "The journal", '''
<p>Under the check-in, the <span class="path">Journal</span> is for anything else worth remembering: how the day went, something new, a question for your vet.</p>
<ul>
<li>Tap <strong>Write about today</strong>, then tap the microphone and just talk. Your words appear as text. You can also type, or fix words afterward.</li>
<li>A day can have several entries, each with its own time.</li>
<li>Journal entries appear in History and in your reports, so your vet sees them too.</li>
</ul>
'''),
("reminders", "Reminders", '''
<p>Turn reminders on in <span class="path">your pet's tab › Reminders</span>. You can choose:</p>
<ul>
<li>Insulin time, and a nudge if a shot hasn't been logged</li>
<li>Meals, medications and glucose checks</li>
<li>Running low on insulin, syringes or food, and time to open a new insulin bottle</li>
<li>Vet appointments and checkups</li>
<li>Your own reminders, such as heartworm or flea and tick (Pro)</li>
</ul>
<p>When a reminder appears, press and hold it to snooze for 15 minutes or an hour. Tapping it opens the right pet and screen.</p>
<div class="tip">If reminders don't show up, check that notifications are allowed for DiaPetic in iPhone Settings, and that a Focus mode isn't silencing them.</div>
'''),
("supplies", "Insulin, syringes and food", '''
<p>The <span class="path">Supplies</span> section at the bottom of today's Tracker shows what's on hand and when it runs out.</p>
<ul>
<li><strong>Insulin:</strong> the bottle in use, how many days it's been open, and spare bottles in the fridge. When you start a new bottle, tap <strong>Open new bottle</strong>. Add bottles you pick up with <strong>Got a new bottle</strong>.</li>
<li><strong>Syringes:</strong> the box in use and unopened boxes. When you start a new box early, choose whether to keep the leftovers so the count stays right.</li>
<li><strong>Food:</strong> how much is left based on the meals you log.</li>
</ul>
<p>Prescription details from the label (refills left, Rx number, pharmacy) live in <span class="path">your pet's tab › Insulin bottles</span>.</p>
'''),
("vet", "Your veterinarian", '''
<p>The <span class="path">Vet</span> tab keeps appointments, what to bring, and questions you want to ask.</p>
<ul>
<li>Add an appointment with its start and end time. DiaPetic can add it to your iPhone calendar and keep it updated if you change or cancel it.</li>
<li>Jot down questions as they come up, then email your vet with a summary attached.</li>
<li>Call or get directions with one tap.</li>
</ul>
'''),
("reports", "Reports and sharing", '''
<p>The <span class="path">Reports</span> tab shows how things are going over 7 days to 6 months: shots given and missed, appetite, symptoms, weight, nutrition, glucose and your journal.</p>
<ul>
<li><strong>PDF report for your vet (Pro):</strong> in Reports, tap <em>Share a PDF report with your veterinarian</em>, pick a period, and send it by email, Messages or AirDrop, or print it.</li>
<li><strong>Info sheet:</strong> in your pet's tab, tap <strong>Share</strong> beside the name for a one-page sheet with your pet's details, insulin routine, meals, vet and emergency contacts. It's handy for pet sitters, boarding and emergency visits. Free.</li>
</ul>
'''),
("emergency", "When something seems wrong", '''
<p>The red <strong>emergency button</strong> at the top right of every screen opens help right away:</p>
<ul>
<li>One-tap calls to your vet, your emergency clinic and pet poison hotlines</li>
<li>Nearby emergency vets</li>
<li>Step-by-step guides for low blood sugar, too much insulin, an unsure or missed shot, not eating, vomiting and possible poisoning</li>
<li>A summary to read to the clinic: insulin, last shot, last meal and today's notes</li>
</ul>
<div class="tip">Signs of low blood sugar include weakness, wobbling, trembling, confusion and seizures. Rub honey or corn syrup on the gums and call your vet or an emergency clinic right away.</div>
'''),
("backup", "Backups and a new iPhone", '''
<p>Everything you enter is stored on your iPhone. To keep it safe:</p>
<ul>
<li>Go to <span class="path">your pet's tab › Backup and restore</span> and tap <strong>Back up now</strong>. Save the file to iCloud Drive or anywhere in Files.</li>
<li>DiaPetic also saves an automatic copy every week and keeps the last four.</li>
<li>On a new iPhone, install DiaPetic, open <span class="path">Backup and restore</span>, choose <strong>Restore from backup</strong> and pick your file.</li>
</ul>
'''),
]
toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t, _ in help_sections)
secs = "".join(f'<h2 id="{a}">{i}. {t}</h2>{b}{MOCKS.get(a, "")}' for i, (a, t, b) in enumerate(help_sections, 1))
help_body = f'''
<div class="wrap narrow">
<header class="page-head">
<p class="eyebrow">How to use</p>
<h1>Getting started with DiaPetic</h1>
<p>A short guide from setting up your pet to sharing reports with your veterinarian. New to pet diabetes? Take it one section at a time. The pictures show a sample pet, Biscuit.</p>
</header>
<nav class="toc" aria-label="Contents"><strong>Contents</strong><ol>{toc}</ol></nav>
<article class="article">
{secs}
<p class="safety" style="margin-top:36px"><strong>Remember:</strong> DiaPetic keeps records and reminds you. It never recommends insulin doses or changes to treatment. Always follow your veterinarian's instructions.</p>
<p style="margin-top:20px">Still have a question? See the <a href="faq.html">FAQ</a> or email <a href="mailto:support@diapetic.com">support@diapetic.com</a>.</p>
</article>
</div>
'''
page("help.html", "How to use DiaPetic", "A step-by-step guide to DiaPetic: setting up your pet, logging shots and meals, reminders, supplies, reports and backups.", help_body)

# ---------------- FAQ ----------------
faq_groups = [
("Using the app", [
("I forgot to log a shot. Can I add it later?", "<p>Yes. Go to that day on the Tracker (swipe back or use the calendar button), tap <strong>Give</strong> on the shot, and choose <strong>A different time</strong> to enter when it was actually given.</p>"),
("What does \"Not logged\" mean?", "<p>The shot's usual time has passed and nothing has been recorded yet. It doesn't mean the shot was missed, only that DiaPetic doesn't know. If reminders are on, you'll get a nudge.</p><p>If you're not sure whether it was given, don't give another. Call your veterinarian.</p>"),
("Does DiaPetic tell me how much insulin to give?", "<p>No, and it never will. Insulin doses must come from your veterinarian. DiaPetic records the dose your vet prescribed and what was actually given, so your vet has accurate information to make those decisions.</p>"),
("Can I track a cat? More than one pet?", "<p>Yes to both. DiaPetic works for dogs and cats. Your first pet is free; adding more pets is part of DiaPetic Pro.</p>"),
("Can two people use it for the same pet?", "<p>Not yet. Today each iPhone keeps its own records. Sharing between family members is planned for a future update.</p>"),
("Why didn't my reminder go off?", "<p>Check iPhone <strong>Settings › Notifications › DiaPetic</strong> and make sure notifications are allowed, then check that a Focus mode (like Sleep or Do Not Disturb) isn't silencing them. In DiaPetic, open your pet's tab › Reminders to confirm the reminder is on.</p>"),
("Can I talk instead of typing?", "<p>Yes. In the journal and the suggestion box, tap the large microphone and speak. The first time, iPhone asks permission to use the microphone and speech recognition.</p>"),
]),
("Your data and privacy", [
("Where is my information stored?", "<p>Only on your iPhone. DiaPetic has no account, no ads, no analytics and no servers. Nothing leaves your phone unless you choose to share it, such as sending a report or saving a backup.</p>"),
("Can my veterinarian see my data?", "<p>Only what you send them, like a PDF report or an email from the Vet tab. There's no portal or automatic sharing.</p>"),
("How do I move to a new iPhone or restore a backup?", "<p>On your old iPhone, go to your pet's tab › Backup and restore › <strong>Back up now</strong> and save the file to iCloud Drive. On the new iPhone, install DiaPetic, open Backup and restore, choose <strong>Restore from backup</strong> and pick that file.</p>"),
("If I delete the app, is my data gone?", "<p>Yes, unless you have a backup. Deleting an app removes its data from the iPhone. Make a backup first.</p>"),
]),
("Pro and purchases", [
("What does DiaPetic Pro include? Is it a subscription?", "<p>Pro is a one-time purchase of $9.99, not a subscription. It adds PDF and CSV reports, 90- and 180-day trends, more than one pet, your own reminders, and dog or kitty app icons with seasonal looks. It's shared with your Family Sharing group.</p>"),
("I bought Pro on another iPhone. How do I get it back?", "<p>Open the Pro screen in your pet's tab and tap <strong>Restore purchases</strong>, signed in with the same Apple Account.</p>"),
("What are tips?", "<p>Optional thank-yous in <em>Support DiaPetic</em> that help cover the cost of keeping the app on the App Store. Tips don't unlock anything. Everything that keeps your pet safe is always free.</p>"),
("How do I change the app icon?", "<p>With Pro, go to your pet's tab › App settings › App icon. Pick Obi the dog or the kitty, and a style: automatic seasons, always regular, or one theme all year.</p>"),
]),
]
groups = ""
for g, items in faq_groups:
    groups += f"<h2>{g}</h2>" + "".join(f"<details><summary>{q}</summary><div>{a}</div></details>" for q, a in items)
faq_body = f'''
<div class="wrap narrow">
<header class="page-head">
<p class="eyebrow">FAQ &amp; support</p>
<h1>Questions and answers</h1>
<p>Quick answers to the most common questions. For step-by-step help, see <a href="help.html">How to use</a>.</p>
</header>
<div class="faq article">
{groups}
<div class="contact">
<h2 style="color:#FFFFFF">Still need help?</h2>
<p>Email us and include your iPhone model and what you were doing. Suggestions are very welcome too. You can also send one from the app: your pet's tab › App settings › Suggestion box.</p>
<a href="mailto:support@diapetic.com">support@diapetic.com</a>
</div>
<p class="safety" style="margin-top:28px"><strong>In an emergency</strong>, call your veterinarian or nearest emergency clinic. For possible poisoning, the ASPCA Animal Poison Control Center is (888) 426-4435 (a fee may apply).</p>
</div>
</div>
'''
page("faq.html", "DiaPetic FAQ and support", "Answers to common questions about DiaPetic, plus how to contact support.", faq_body)

# ---------------- Privacy ----------------
privacy_body = '''
<div class="wrap narrow">
<header class="page-head">
<p class="eyebrow">Privacy</p>
<h1>Privacy policy</h1>
<p>Effective October 17, 2026</p>
</header>
<article class="article">
<p><strong>The short version:</strong> DiaPetic doesn't collect your data. What you enter stays on your iPhone. There's no account, no advertising, no analytics and no tracking, and the developer has no server that receives your information.</p>

<h2>Who we are</h2>
<p>DiaPetic is an iPhone app made by Bryan Flynn ("we", "us"). Contact: <a href="mailto:support@diapetic.com">support@diapetic.com</a>.</p>

<h2>Information you enter</h2>
<p>Your pet's details, shots, meals, check-ins, glucose readings, journal entries, supplies, appointments and settings are stored only on your iPhone, in the app's own storage. We can't see them.</p>

<h2>When information leaves your iPhone</h2>
<p>Only when you choose:</p>
<ul>
<li><strong>Sharing:</strong> reports, the pet info sheet and CSV files go wherever you send them (email, Messages, AirDrop, Files, a printer).</li>
<li><strong>Email:</strong> emails to your veterinarian and messages from the suggestion box are sent from your own email app, and you see them before they're sent. Messages you send to us are used only to reply and improve the app.</li>
<li><strong>Backups:</strong> backup files are saved where you choose, such as iCloud Drive or Files. If they're in iCloud, they're stored in your own iCloud account under Apple's terms.</li>
</ul>

<h2>Permissions the app may ask for</h2>
<ul>
<li><strong>Notifications:</strong> to show the reminders you turn on.</li>
<li><strong>Calendar:</strong> to add your pet's appointments to your calendar and update or remove them when you change them in the app. DiaPetic doesn't read or share your other events.</li>
<li><strong>Camera:</strong> only to read calorie information from pet food labels. Nothing is photographed or saved.</li>
<li><strong>Location:</strong> only to find veterinarians and emergency clinics near you, using Apple Maps. It isn't stored.</li>
<li><strong>Microphone and speech recognition:</strong> only while you dictate a journal entry or suggestion. Recordings aren't saved; only the text is kept. Speech is recognized on your iPhone when it supports that; otherwise Apple processes it under Apple's privacy policy.</li>
</ul>
<p>You can turn any of these off in iPhone Settings › DiaPetic.</p>

<h2>Purchases and ratings</h2>
<p>DiaPetic Pro and tips are handled by Apple through the App Store. We don't receive your payment details. Apple may share anonymous sales information with us, such as the number of purchases. Rating prompts are shown by Apple.</p>

<h2>Children</h2>
<p>DiaPetic is meant for adults caring for a pet and isn't directed at children. We don't knowingly collect information from anyone.</p>

<h2>This website</h2>
<p>diapetic.com doesn't use cookies, analytics or tracking. It's hosted by GitHub Pages, which may keep standard server logs (such as IP addresses) for security, under GitHub's privacy statement.</p>

<h2>Not veterinary advice</h2>
<p>DiaPetic is a record-keeping tool. It never recommends insulin doses or changes to treatment and isn't a substitute for veterinary care.</p>

<h2>Changes to this policy</h2>
<p>If this policy changes, we'll update it here and change the effective date. If a change affects how your information is handled, we'll also note it in the app's update notes.</p>

<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:support@diapetic.com">support@diapetic.com</a></p>
</article>
</div>
'''
page("privacy.html", "DiaPetic privacy policy", "DiaPetic doesn't collect your data. Everything you enter stays on your iPhone.", privacy_body)

# 404 and custom domain
page("404.html", "Page not found · DiaPetic", "That page doesn't exist.", '<div class="wrap narrow"><header class="page-head"><h1>That page isn\'t here</h1><p>Try the <a href="index.html">home page</a>, <a href="help.html">How to use</a> or the <a href="faq.html">FAQ</a>.</p></header></div>')
open(os.path.join(OUT, "CNAME"), "w").write("diapetic.com\n")
open(os.path.join(OUT, "README.md"), "w").write("# diapetic.com\n\nThe DiaPetic website: home, how to use, FAQ & support, privacy policy. Plain HTML and CSS, hosted on GitHub Pages.\n\nThe pages are generated from `build.py` in the app project; edit there or edit the HTML directly.\n")
print("built")
