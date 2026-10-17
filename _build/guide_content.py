# Content for the DiaPetic guide (help.html hub + one page per area).
# Each chapter: slug, title, one-line summary, intro, list of (anchor, heading, html), and which illustrations to show.
# Keep in step with the app: when a screen or feature changes, update the matching chapter here.

P = lambda s: f'<span class="path">{s}</span>'   # an in-app location, e.g. P("Vet tab › Contacts")

CHAPTERS = [
# ------------------------------------------------------------------
("getting-started", "Getting started", "Install, add your pet and set things up in about 10 minutes.",
"""<p>This chapter walks you through your first ten minutes with DiaPetic. Have your veterinarian's instructions, the insulin bottle or box, and your pet's food bag nearby.</p>""",
[
("layout", "How the app is laid out", f"""
<p>DiaPetic has five tabs along the bottom:</p>
<ul>
<li><strong>Tracker:</strong> today's page, where you log shots, meals, the check-in and the journal.</li>
<li><strong>Reports:</strong> how things are going over 7 days to 6 months, plus glucose charts and PDF reports.</li>
<li><strong>Vet:</strong> appointments, questions for your veterinarian, contacts and email.</li>
<li><strong>History:</strong> every day you've logged, newest first. Tap a day to see or fix it.</li>
<li><strong>Your pet's name:</strong> your pet's details, insulin, food, medications, reminders, supplies and app settings.</li>
</ul>
<p>Two things are on every screen: the <strong>pet menu</strong> at the top left (switch pets or add one) and the red <strong>emergency button</strong> at the top right.</p>
"""),
("first-launch", "First launch", """
<ol>
<li>Read the short note on the welcome screen and tap <strong>I understand</strong>. DiaPetic is a record-keeping tool. It never recommends doses, and it isn't a substitute for your veterinarian.</li>
<li>The pet setup screen opens. Everything on it can be changed later, so don't worry about getting it perfect.</li>
</ol>
"""),
("pet", "Your pet", """
<ul>
<li><strong>Name and species:</strong> dog, cat or other.</li>
<li><strong>Breed:</strong> pick from the list, or type your own.</li>
<li><strong>Color:</strong> choose from common colors for dogs or cats, or pick <em>Other…</em> and describe the color or markings.</li>
<li><strong>Sex</strong> and whether your pet is spayed or neutered. (Hormone cycles in unspayed females can change how insulin works, so your vet may want to talk about spaying.)</li>
<li><strong>Current weight</strong> in lb or kg.</li>
<li><strong>Microchip #</strong> (optional). It appears on the info sheet you can share, which helps if your pet is ever lost.</li>
</ul>
"""),
("insulin", "Insulin", f"""
<ol>
<li>Choose your insulin from the list, and check that the strength matches the bottle: <strong>U-40</strong> or <strong>U-100</strong>. Use syringes that match the insulin's strength.</li>
<li>Enter the <strong>units</strong> and <strong>time</strong> for the morning and evening shots, exactly as your vet prescribed. If your pet only gets one shot a day, leave the other one blank.</li>
<li>Leave <strong>Remind me at each shot time</strong> on, unless you'd rather not have reminders.</li>
</ol>
<div class="tip">DiaPetic records the dose your vet prescribed. It never suggests or changes a dose. When your vet changes the dose, update it in {P("your pet's tab")} and the change is recorded in your reports automatically.</div>
"""),
("meals", "Meals and treats", """
<ol>
<li>Choose a <strong>feeding style</strong>: set meals (the usual for pets on insulin) or free feeding.</li>
<li>Tap <strong>Add meal food</strong> for each food your pet eats: the type (dry kibble, wet, fresh, raw, topper), brand, how much, and which meal it's fed at. You can add calories now or later. The <a href="guide-food.html">Food and nutrition</a> chapter has the details.</li>
<li>Add favorite <strong>treats</strong> the same way, so they're one tap to log.</li>
<li>If your vet gave you a <strong>daily calorie target</strong>, enter it.</li>
</ol>
"""),
("vet", "Your vet and an emergency clinic", f"""
<p>Add your veterinarian's clinic and phone, plus an after-hours <strong>emergency clinic</strong>. These make the call and directions buttons work, including on the emergency screen.</p>
<p>Later, in {P("Vet tab › Contacts › Edit or find clinics")}, you can add the doctor's name, email and address, or search for clinics near you.</p>
"""),
("permissions", "Allow notifications", """
<p>Tap <strong>Save</strong>. When iPhone asks whether DiaPetic can send notifications, tap <strong>Allow</strong>, or reminders can't appear. DiaPetic only asks for other permissions (calendar, camera, location, microphone) when you first use a feature that needs one.</p>
"""),
("first-week", "Your first week: a checklist", f"""
<ul class="checklist">
<li>Log every shot and meal on the <a href="guide-tracker.html">Tracker</a> for a few days to build the habit.</li>
<li>Check that reminders arrive at the right times. Adjust them in {P("your pet's tab › Reminders")}.</li>
<li>Add any other medications or supplements in {P("your pet's tab › Other medications and supplements")}.</li>
<li>Record the insulin bottle you're using and any spares in {P("your pet's tab › Insulin bottles")}.</li>
<li>Add your next vet appointment in the {P("Vet tab")}.</li>
<li>Make your first backup: {P("your pet's tab › Backup and restore › Back up now")}.</li>
</ul>
"""),
], ["setup"]),

# ------------------------------------------------------------------
("tracker", "The Daily Tracker", "Logging shots, meals, the check-in, weight, glucose and the journal.",
"""<p>The Tracker tab is where each day happens. It opens on today. If you come back after more than five minutes away, or the next day, it jumps back to today on its own.</p>""",
[
("days", "Moving between days", """
<ul>
<li><strong>Swipe</strong> left or right across the page, or tap the <strong>‹ ›</strong> arrows beside the date.</li>
<li>Tap the <strong>calendar</strong> button beside "Daily Tracker" to jump straight to any day, or use the quick jumps: today, one week, two weeks or one month ago.</li>
<li>Tap the <strong>date</strong> to come back to today.</li>
<li>When you change days, you stay at the same spot on the page, so you can compare the same section day to day.</li>
</ul>
"""),
("glance", "At a glance and alerts", """
<p>The top of the page shows today's calories against the target, the latest glucose reading, and how many meals are logged. Banners appear when something needs attention:</p>
<ul>
<li><strong>Eating less than usual</strong> when recent meals were small.</li>
<li><strong>Low reading</strong> when a glucose reading is below your low number, with buttons to call your vet or emergency clinic.</li>
<li><strong>An upcoming appointment</strong> the day before and the day of a visit, with what to bring.</li>
</ul>
"""),
("meals", "Logging a meal", """
<p>Each morning and evening card starts with the meal.</p>
<ul>
<li>Tap <strong>All</strong>, <strong>Most</strong>, <strong>Some</strong> or <strong>None</strong> for how much was eaten. Tap the same button again to clear it.</li>
<li>For exact amounts, tap the meal row to open the meal details. Enter the amount offered and the amount left over in the same unit (grams are the most accurate), and add a note such as "picky" or "vomited".</li>
<li>If less than half the meal was eaten, DiaPetic reminds you to check your veterinarian's instructions before giving insulin.</li>
</ul>
"""),
("shots", "Logging a shot", """
<ol>
<li>Tap <strong>Give</strong> on the Insulin row. It shows the prescribed units, for example "Give 8 u".</li>
<li>Choose when it was given: <strong>Just now</strong>, <strong>At the scheduled time</strong>, or <strong>A different time…</strong> to pick the exact time.</li>
<li>The row then shows, for example, "8 units given at 7:04 AM", so anyone checking later knows it's done.</li>
</ol>
<p>Tap the <strong>details</strong> button beside the shot to change the time or units, add a note, mark the shot as <strong>skipped</strong> (for example when your pet didn't eat and your vet said to skip), or delete an entry made by mistake.</p>
<div class="tip">Not sure whether a shot was given? <strong>Don't give another.</strong> Check the Tracker first. If it isn't logged and no one remembers giving it, call your veterinarian. The emergency screen has a guide for this.</div>
"""),
("meds", "Medications, supplements and treats", """
<ul>
<li><strong>Morning and evening medications</strong> appear in the matching card. Tap to check one off; tap its time to change when it was given.</li>
<li><strong>As-needed medications</strong> have their own section. Tap <strong>Give</strong> each time one is given.</li>
<li><strong>Supplements</strong> show as a simple daily checkbox.</li>
<li><strong>Meals and treats:</strong> tap <strong>Add a treat</strong> to log a treat from your list (with how many), or <strong>Something else</strong> for food outside the plan, like table scraps or a stolen snack. Extra food can raise blood sugar, so it helps your vet to know.</li>
</ul>
"""),
("weight", "Weight", """
<p>Tap the Weight section to log a weight for the day. Weigh at about the same time of day on the same scale for the most useful trend. At checkups, your vet may give a <strong>body condition score</strong> from 1 to 9 (4 to 5 is usually ideal); you can record that here too.</p>
"""),
("checkin", "The daily check-in", """
<p>Water, urine, stool, energy and sleep all start at <strong>Normal</strong> and are saved that way, so you only change what was different. Turn on <strong>Vomited</strong> if it happened. If you measure water, enter the amount under <strong>Water amount</strong>. Drinking and urinating more than usual can be a sign that blood sugar is running high.</p>
"""),
("journal", "The journal", """
<p>Under the check-in, the Journal is for anything else worth remembering: how the day went, something new, a question for your vet.</p>
<ol>
<li>Tap <strong>Write about today</strong> (or <strong>Add another entry</strong>).</li>
<li>Tap the big <strong>microphone</strong> and just talk; your words appear as text, with punctuation. Tap again to stop. Or type, or fix words afterward.</li>
<li>Check the time and tap <strong>Save</strong>.</li>
</ol>
<p>A day can have several entries. Tap one to edit it; swipe left to delete it. Journal entries appear in History, in Reports, in the PDF report, and in the clinic summary on the emergency screen.</p>
"""),
("glucose", "Glucose readings", f"""
<p>If you check glucose at home, add readings in the Blood glucose section. See <a href="guide-glucose.html">Glucose and lab results</a>. If you don't, the section stays small and out of the way.</p>
"""),
("supplies", "Supplies", f"""
<p>At the bottom of today's page, <strong>Supplies</strong> shows what runs out next, with the insulin bottle, syringes and food on hand. See <a href="guide-supplies.html">Insulin, syringes and food</a>.</p>
"""),
("history", "Fixing an earlier day (History)", """
<p>Go back with the calendar or a swipe, or open the <strong>History</strong> tab. It lists every logged day with the shots (a filled icon for given, an X for skipped, an empty circle for not logged), the glucose range, and the first journal entry. Tap a day to open it and add or fix anything, just like today.</p>
"""),
], ["day", "journal"]),

# ------------------------------------------------------------------
("food", "Food and nutrition", "Meal plans, calories, the label scanner, food on hand and diet changes.",
f"""<p>Consistent meals help keep glucose steady. Set up the meal plan in {P("your pet's tab › Meals and treats")}.</p>""",
[
("add", "Adding a food", """
<ol>
<li>Tap <strong>Add meal food</strong> (or <strong>Add treat</strong>).</li>
<li>Pick the type: dry kibble, wet or canned, fresh or cooked, raw, topper or mix-in, treat, or other.</li>
<li>Enter the brand and product, the unit (cups, grams, cans and so on), <strong>how much</strong> is fed, and which meal it's <strong>fed at</strong>.</li>
<li>Add the <strong>calories</strong>. Tap <strong>Scan the label</strong> to point the camera at the calorie statement on the bag or can and tap the number to use it.</li>
</ol>
<div class="tip">Weighing food in grams on a kitchen scale is the most accurate. A level measuring cup can vary by 20% or more.</div>
"""),
("facts", "Nutrition facts (optional)", """
<p>Enter the guaranteed analysis from the label (protein, fat, fiber, moisture and ash) and DiaPetic shows the values on a <strong>dry-matter basis</strong>, including estimated carbohydrate. This lets your vet compare foods with different moisture, like kibble and canned. Carbohydrate and fiber matter most for diabetic pets.</p>
"""),
("onhand", "Food on hand", """
<p>Turn on <strong>Track how much is left</strong>, then enter how it's sold (bags, cans, trays…), the size of each and how many you have. DiaPetic counts down as you log meals, shows when it will run out, and can remind you before it does.</p>
"""),
("target", "Calorie target and portions", """
<ul>
<li>Enter the <strong>daily calorie target</strong> from your veterinarian. If you don't have one, DiaPetic shows what the meal plan adds up to, and you can tap <strong>Use as target</strong>.</li>
<li><strong>Portion estimates</strong> set how much "Most" and "Some" count for when you tap them on the Tracker. For exact numbers, log a meal with the amount offered and the amount left over.</li>
<li>Treats and "something else" entries count toward the day's calories when you include calories for them.</li>
</ul>
"""),
("changes", "Diet changes", """
<p>Changes to the meal plan are recorded automatically. Reports mark each diet change on the charts and compare average glucose, calories and weight before and after, so your vet can see whether a new food made a difference.</p>
"""),
], []),

# ------------------------------------------------------------------
("medications", "Medications and supplements", "Other medicines, supplements, schedules and doses.",
f"""<p>Add everything your pet takes besides insulin in {P("your pet's tab › Other medications and supplements")}.</p>""",
[
("add", "Adding a medication", """
<ol>
<li>Tap <strong>Add medication or supplement</strong> and choose which it is.</li>
<li>Enter the name (for example Vetoryl), the <strong>dose as prescribed</strong> (for example 60 mg capsule) and, if you like, what it's for.</li>
<li>Choose the schedule: <strong>with the morning routine</strong>, <strong>with the evening routine</strong>, <strong>morning and evening</strong>, <strong>once a day</strong>, or <strong>as needed</strong>.</li>
<li>If a dose has calories (fish oil, chews, pastes), enter them so the day's calories add up.</li>
<li>Set when it <strong>started</strong> and add notes such as "give with food".</li>
</ol>
"""),
("tracker", "On the Tracker", """
<p>Scheduled medications appear in the morning or evening card to check off; once-a-day supplements show as a daily checkbox; as-needed medications have a <strong>Give</strong> button. Reports show the percent of scheduled doses checked off.</p>
"""),
("stop", "Stopping a medication", """
<p>When your pet stops a medication, turn on <strong>Stopped</strong> and set the date rather than deleting it. That keeps its history in reports. Delete only something added by mistake.</p>
"""),
("reminders", "Reminders", f"""
<p>Morning and evening medications are listed in the shot reminder. Once-a-day medications can have their own reminder, and you can be reminded before a course ends. Set these in {P("your pet's tab › Reminders › Medications and supplements")}.</p>
"""),
], []),

# ------------------------------------------------------------------
("glucose", "Glucose and lab results", "Home readings, curves, time in range and lab work.",
f"""<p>Only check glucose at home if your veterinarian asked you to. Turn it on in {P("your pet's tab › Home glucose monitoring › I check glucose at home")}.</p>""",
[
("numbers", "Your highlight numbers", """
<p>Set <strong>Highlight readings below</strong> and <strong>Highlight readings above</strong> to the numbers your veterinarian gives you. They only change how readings are colored, when the low-reading alert shows, and the time-in-range figure. Choose mg/dL or mmol/L in App settings.</p>
"""),
("add", "Adding a reading", """
<p>On the Tracker, tap <strong>Add reading</strong> in Blood glucose. Enter the value, the time, and the source: <strong>glucose meter</strong>, <strong>CGM sensor</strong>, or <strong>at the vet</strong>. Add a note if anything was unusual. A reading below your low number shows a warning with call buttons, and you can turn on a reminder to check on your pet afterward.</p>
"""),
("curves", "Glucose curves", """
<p>A curve is a series of readings over a day. Open <strong>Reports</strong> and switch to <strong>Glucose</strong> to see your readings as a curve, glucose by week, time in range, eating and glucose, and low readings.</p>
<p>Tap <strong>Compare curves</strong> to overlay up to three days. Your veterinarian looks at the lowest point of the curve and when it happens to judge how well the insulin is working.</p>
"""),
("labs", "Lab results", f"""
<p>Record blood work such as fructosamine in {P("Reports › Lab results › Add lab result")}, or after a vet visit. Enter the test, result, unit and date, plus what the veterinarian said. Lab results are included in reports.</p>
"""),
], []),

# ------------------------------------------------------------------
("reminders", "Reminders", "Shots, missed-shot nudges, meals, medications, supplies, checkups and your own.",
f"""<p>Set everything up in {P("your pet's tab › Reminders")}. The top of the screen shows what's <strong>coming up</strong>, so you can check reminders are set the way you want.</p>""",
[
("insulin", "Insulin", """
<ul>
<li><strong>At each shot time:</strong> a reminder at the morning and evening shot times.</li>
<li><strong>Nudge if a shot isn't logged:</strong> a follow-up if nothing has been logged, after 15 minutes to 2 hours (you choose). It helps prevent both a missed dose and a double dose.</li>
</ul>
"""),
("meals", "Meals", """
<p>A meal reminder with the shot, or 15, 30 or 45 minutes before it. <strong>Fill the bowl</strong> lists the planned portions, so whoever feeds your pet knows exactly what to give.</p>
"""),
("care", "Medications, glucose and logging", """
<ul>
<li>Morning and evening medications, once-a-day medications and supplements, and a heads-up before a course ends.</li>
<li><strong>Glucose checks</strong> before each shot, and a reminder to <strong>check on your pet after a low reading</strong>.</li>
<li>A <strong>daily log</strong> reminder and a <strong>weekly weigh-in</strong>.</li>
</ul>
"""),
("supplies", "Supplies", """
<p>Warnings before insulin, syringes or food run low (you choose how many days ahead), and <strong>Time to open a new bottle</strong> based on how long an opened bottle is good for. Unopened bottles and boxes you've recorded are counted, so you won't be told to order more when spares are waiting.</p>
"""),
("checkups", "Checkups", """
<p><strong>Remind me to book a checkup</strong> every 3, 6 or 12 months, counted from your last completed visit, and only when nothing is already scheduled. Reminders for booked appointments are set on each appointment in the Vet tab.</p>
"""),
("custom", "Your own reminders (Pro)", """
<p>Tap <strong>Add a reminder</strong> for anything else. Presets include heartworm prevention, flea and tick prevention, refilling the insulin prescription, a fructosamine or glucose curve, vaccines, nail trims, grooming, brushing teeth and cleaning the water bowl, or choose <strong>Something else…</strong>. Set the first reminder and how often it repeats: once, daily, weekly, every 2 weeks, monthly, every 3 or 6 months, or yearly.</p>
"""),
("snooze", "Snoozing and troubleshooting", """
<p>Each reminder has buttons to snooze for 15 minutes or an hour. Tapping a reminder opens the right pet and screen.</p>
<div class="tip">If reminders don't appear, open iPhone <strong>Settings › Notifications › DiaPetic</strong> and allow notifications, and check that a Focus mode such as Sleep isn't silencing them. If notifications are off, the Reminders screen shows an <strong>Open Settings</strong> button.</div>
"""),
], ["reminders"]),

# ------------------------------------------------------------------
("supplies", "Insulin, syringes and food", "Bottles in use and in the fridge, prescriptions, syringe boxes and food on hand.",
"""<p>DiaPetic keeps track of supplies from the shots and meals you log, and warns you before anything runs out.</p>""",
[
("bottles", "Insulin bottles", f"""
<p>Open {P("your pet's tab › Insulin bottles")}, or tap <strong>Manage</strong> in Supplies on the Tracker.</p>
<ul>
<li><strong>In use:</strong> turn on <strong>Bottle opened</strong>, set the date you opened it, the units in the bottle, and the expiration date on the label. Set how many days an <strong>opened bottle is good for</strong>; check the insulin's label or ask your vet. A 10 mL bottle holds 400 units of U-40 insulin or 1,000 units of U-100.</li>
<li><strong>In the fridge:</strong> tap <strong>Got a new bottle</strong> to add unopened bottles, with the expiration date and lot number. Bottles are opened in order of expiration date, earliest first, and you're warned if one will expire before its turn.</li>
<li><strong>Starting the next bottle:</strong> tap <strong>Open new bottle</strong>. The old bottle moves to history and the next spare becomes the one in use. Tapped it by mistake? <strong>Undo</strong> is there for the rest of the day.</li>
</ul>
"""),
("rx", "Prescription details", """
<p>In the same screen, record the date filled, <strong>refills left</strong>, the Rx number (tap to copy it when you call) and the pharmacy. When no refills are left, you'll get a reminder to ask your vet for a new prescription before the insulin runs out.</p>
"""),
("syringes", "Syringes", f"""
<p>Open {P("your pet's tab › Syringes")}. Set when you started the box in use and how many it holds; DiaPetic counts one syringe per shot. Tap <strong>Got new syringes</strong> to add unopened boxes.</p>
<p>When you start a new box, tap <strong>Start new box</strong>. If there are syringes left in the old box, choose whether you're <strong>keeping the leftovers</strong> (they're added to the new count) or threw them away, so the count stays right even when boxes overlap.</p>
"""),
("food", "Food on hand", """
<p>Track bags and cans in each food's settings (see <a href="guide-food.html#onhand">Food on hand</a>). The Supplies section shows when each food runs out.</p>
"""),
], ["supplies"]),

# ------------------------------------------------------------------
("vet", "Your veterinarian", "Contacts, appointments, visit notes, questions and email.",
"""<p>The Vet tab keeps everything about your pet's veterinary care in one place.</p>""",
[
("contacts", "Contacts and finding clinics", f"""
<p>In {P("Vet tab › Contacts › Edit or find clinics")}, enter your vet's clinic, the doctor's name, phone, email and address, plus an emergency clinic for after-hours problems such as very low blood sugar. Tap <strong>Find veterinarians near me</strong> or <strong>Find emergency clinics near me</strong> to search with your location or a city or ZIP code, then choose <strong>Use as my veterinarian</strong> or <strong>Use as my emergency clinic</strong>. Your location is only used for the search.</p>
"""),
("appointments", "Appointments", """
<ol>
<li>Tap <strong>Schedule an appointment</strong>.</li>
<li>Choose the type: checkup, glucose curve, blood work or fructosamine, recheck, dental, vaccines, emergency visit, or other.</li>
<li>Set when it <strong>starts</strong> and <strong>ends</strong> (drop-off and pick-up for a day stay), where it is, and any instructions from the clinic, such as "drop off by 8 AM".</li>
<li>List <strong>what to bring</strong>. It's shown in the reminders and on the Tracker the day before.</li>
<li>Choose reminders, and tap <strong>Add to Calendar</strong> to put it on your iPhone calendar. If you change or cancel the appointment in DiaPetic, the calendar event is updated or removed too.</li>
</ol>
<div class="tip">Ask the clinic whether to feed and give insulin as usual that morning, and write their answer in the instructions.</div>
"""),
("after", "After the visit", """
<p>After an appointment, DiaPetic asks how it went. Tap <strong>Add visit notes</strong> to record what the veterinarian said and the next steps (dose changes, rechecks, diet), add a lab result, or schedule a follow-up. If it didn't happen, tap <strong>It didn't happen</strong>. If the insulin dose changed, update it in your pet's tab so reports show the change.</p>
"""),
("questions", "Questions for your vet", """
<p>Jot questions down as they come up under <strong>Questions for your veterinarian</strong>. Open questions are printed at the top of the PDF report and can be included when you email your vet. Tap the circle when one is answered, and add the answer if you like.</p>
"""),
("email", "Emailing your vet", """
<p>Tap <strong>Ask your vet</strong> to write an email: choose questions to include, add a message, and optionally include a summary of the last 7 days, 2 weeks or 30 days. With Pro you can attach the PDF report. Tap <strong>Preview</strong> to see it, then send from your own email, or choose <strong>Share another way</strong> for Gmail or Messages.</p>
"""),
], ["vet"]),

# ------------------------------------------------------------------
("reports", "Reports and sharing", "Progress, glucose, PDF and CSV reports, and the pet info sheet.",
"""<p>The Reports tab shows how things are going. Choose a period at the top: 7 days, 2 weeks or 30 days (free), or 90 and 180 days (Pro). Switch between <strong>Progress</strong> and <strong>Glucose</strong>.</p>""",
[
("progress", "Progress", """
<ul>
<li><strong>At a glance:</strong> food eaten, calories, shots given and weight, compared with the period before.</li>
<li><strong>Routine at a glance:</strong> typical meal and shot times worked out from your log, and how complete the log is, so your vet knows how much to rely on it.</li>
<li><strong>Insulin dose:</strong> every change to the prescribed dose, recorded automatically.</li>
<li><strong>Symptoms</strong> and <strong>shot consistency:</strong> day-by-day grids, plus shot time against planned time. Shots about 12 hours apart, at the same times each day, help keep glucose steady.</li>
<li><strong>Journal:</strong> your latest entries, with all of them a tap away.</li>
<li><strong>Nutrition:</strong> calories per day, appetite, meals and insulin timing, calories and weight, treats, water intake and diet changes.</li>
<li><strong>Medications</strong>, <strong>weight</strong> and <strong>lab results</strong>.</li>
</ul>
"""),
("pdf", "PDF report for your vet (Pro)", """
<p>Tap <strong>Share a PDF report with your veterinarian</strong>, choose the period, and tap <strong>Create PDF report</strong>, then share it by email, Messages or AirDrop, save it to Files, or print it. The report starts with your open questions and the routine at a glance, then progress, glucose and curves, symptoms and shot consistency, nutrition and diet details, episodes and changes (low readings, small meals, missed shots, medications), a day-by-day log, and your journal in full.</p>
<p><strong>CSV file (Pro)</strong> exports every entry for Numbers or Excel.</p>
"""),
("infosheet", "Pet info sheet (free)", """
<p>In your pet's tab, tap <strong>Share</strong> beside the name for a one-page sheet with your pet's details, microchip, insulin routine, other medications, meals, vet and emergency contacts, supplies, and low-blood-sugar signs. It's ideal for pet sitters, boarding, family and emergency visits.</p>
"""),
], ["reports"]),

# ------------------------------------------------------------------
("emergency", "When something seems wrong", "The emergency button, triage questions, guides and clinic summary.",
"""<p>The red <strong>emergency button</strong> at the top right of every screen opens <strong>Emergency help</strong>. It's always OK to call your veterinarian or an emergency clinic.</p>""",
[
("now", "Go to an emergency vet now if your pet is:", """
<p>Collapsed or won't wake up, having a seizure, struggling to breathe, bleeding heavily, or very weak, wobbly or trembling. Use the call and directions buttons for your emergency clinic, or <strong>Find nearby</strong>.</p>
"""),
("decide", "Help me decide what to do", """
<p>Answer a few yes-or-no questions (for example whether your pet is weak or wobbly, could have eaten something harmful, isn't eating, is vomiting, or there's a problem with the insulin) and DiaPetic suggests next steps: <strong>act now</strong>, <strong>call your veterinarian today</strong>, or <strong>call your veterinarian soon</strong>. If it's an emergency, don't wait to finish the questions.</p>
"""),
("guides", "Quick guides", """
<p>Step-by-step guides for: going to an emergency vet now, possible low blood sugar, possible poisoning, needing to be seen today, not eating while on insulin, vomiting or diarrhea, too much insulin, not sure the shot was given, a missed dose, insulin that may be damaged, drinking and peeing more, a high glucose reading, serious and minor injuries, and when something seems off.</p>
"""),
("summary", "Information for the clinic", """
<p>A summary built from what you've logged: your pet's details and microchip, insulin and dose, the last shot, last meal and last glucose reading, other medications, today's notes and your regular vet. Read it over the phone, or tap <strong>Share</strong> or <strong>Copy</strong>.</p>
"""),
("poison", "Poison control", """
<p>The screen has one-tap calls to the <strong>ASPCA Animal Poison Control Center, (888) 426-4435</strong>, and the <strong>Pet Poison Helpline, (855) 764-7661</strong>, for anything your pet may have swallowed. A consultation fee may apply.</p>
<div class="tip">Signs of low blood sugar include weakness, wobbling, trembling, twitching, confusion and seizures. Rub honey or corn syrup on the gums and call your vet or an emergency clinic right away.</div>
"""),
], ["emergency"]),

# ------------------------------------------------------------------
("pet-tab", "Your pet's tab and settings", "Pet details, weight, more than one pet, app settings and the app icon.",
"""<p>The last tab is named after your pet. It holds everything you set up, plus the app's settings.</p>""",
[
("details", "Pet details", """
<p>Change your pet's name, species, breed, color, sex and microchip number. The <strong>Weight</strong> section shows the weight trend and body condition score, plus the starting and target weight from your vet. Below that are the meal plan, insulin and shot times, other medications, reminders, supplies and home glucose settings.</p>
"""),
("pets", "More than one pet", """
<p>Tap the <strong>pet menu</strong> at the top left of any tab to switch pets or <strong>Add a pet</strong>. Your first pet is free; more pets are part of DiaPetic Pro. Each pet has its own log, reminders, reports and supplies.</p>
"""),
("settings", "App settings", """
<ul>
<li><strong>Appearance:</strong> match iPhone, light or dark.</li>
<li><strong>Glucose units</strong> (mg/dL or mmol/L) and <strong>weight units</strong> (lb or kg).</li>
<li><strong>App icon (Pro):</strong> Obi the dog or Kitty, with automatic seasonal looks (fall, Halloween, Thanksgiving, holiday season and Christmas), always regular, or one theme all year.</li>
<li><strong>Backup and restore:</strong> see <a href="guide-backups.html">Backups and a new iPhone</a>.</li>
<li><strong>Help &amp; how-to</strong> (this guide), the <strong>Suggestion box</strong>, <strong>Rate DiaPetic</strong>, and <strong>Support DiaPetic</strong> (optional tips).</li>
<li><strong>About DiaPetic:</strong> privacy, the website, FAQ and the privacy policy.</li>
</ul>
"""),
("delete", "Deleting a pet", """
<p>At the bottom of the tab, <strong>Delete … and all records</strong> permanently removes every shot, reading and check-in for that pet. Make a backup first if you might want them later.</p>
"""),
("feedback", "Suggestions and support", """
<p>The <strong>Suggestion box</strong> sends a message from your own email: choose a suggestion, something that isn't working, a question or something you love, then talk or type. You can include app and iPhone details to help track down problems; your pet's health records are never included. Or email <a href="mailto:support@diapetic.com">support@diapetic.com</a>.</p>
"""),
], []),

# ------------------------------------------------------------------
("backups", "Backups and a new iPhone", "Back up, automatic copies, restore and moving phones.",
"""<p>Everything you enter is stored only on your iPhone. A backup is the only way to get it back if the phone is lost or the app is deleted.</p>""",
[
("now", "Back up now", f"""
<p>Open {P("your pet's tab › Backup and restore")} and tap <strong>Back up now</strong>. Save the file to <strong>iCloud Drive</strong> so it's safe even if your iPhone isn't. The backup has every pet, all logs, visits, bottles, syringe boxes, journal entries, reminders and settings.</p>
"""),
("auto", "Automatic weekly copy", """
<p>Once a week DiaPetic saves a copy by itself and keeps the last four. If those copies are only on the iPhone, they'd be lost with it, so use Back up now from time to time too.</p>
"""),
("restore", "Restoring and moving to a new iPhone", """
<ol>
<li>On the new iPhone, install DiaPetic and open <strong>Backup and restore</strong>.</li>
<li>Tap <strong>Restore from backup…</strong> and pick your backup file.</li>
<li>Check what's in it (pets and days of logs), then tap <strong>Restore</strong>.</li>
</ol>
<p>Restoring replaces what's currently in DiaPetic; a copy of the current data is saved first, just in case. If you have Pro, open the Pro screen and tap <strong>Restore purchase</strong>.</p>
"""),
], ["backup"]),
]
