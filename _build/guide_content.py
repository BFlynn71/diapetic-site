# Content for the DiaPetic guide (help.html hub + one page per area).
# Each chapter: slug, title, one-line summary, intro, list of (anchor, heading, html), and which illustrations to show.
# Keep in step with the app: when a screen or feature changes, update the matching chapter here.
# Voice: professional and plain. Complete sentences, button names exactly as they appear in the app.

P = lambda s: f'<span class="path">{s}</span>'   # an in-app location, e.g. P("Vet tab › Contacts")

CHAPTERS = [
# ------------------------------------------------------------------
("getting-started", "Getting started", "Installing DiaPetic and setting up your pet.",
"""<p>Setting up DiaPetic takes about ten minutes. Before you begin, have your veterinarian's instructions, the insulin bottle or box, and your pet's food packaging close at hand.</p>""",
[
("layout", "How the app is organized", """
<p>DiaPetic is organized into five tabs:</p>
<ul>
<li><strong>Tracker</strong> is the daily log, where you record shots, meals, the daily check-in and journal entries.</li>
<li><strong>Reports</strong> summarizes the last 7 days to 6 months, including glucose charts and PDF reports for your veterinarian.</li>
<li><strong>Vet</strong> holds appointments, questions for your veterinarian, clinic contacts and email.</li>
<li><strong>History</strong> lists every day you have logged, with the most recent first.</li>
<li>The last tab is named after your pet. It contains your pet's details, insulin, meal plan, medications, reminders, supplies and the app's settings.</li>
</ul>
<p>The <strong>pet menu</strong> at the top left of every screen switches between pets, and the red <strong>emergency button</strong> at the top right opens emergency help.</p>
"""),
("first-launch", "First launch", """
<p>When you open DiaPetic for the first time, a short note explains that DiaPetic is a record-keeping tool: it does not recommend doses and is not a substitute for veterinary care. Tap <strong>I understand</strong> to continue to the pet setup screen. Everything you enter there can be changed later.</p>
"""),
("pet", "Your pet's details", """
<p>Enter your pet's name and species, then choose a breed from the list or type one in. Select a coat color, or choose <em>Other…</em> to describe the color or markings. Add your pet's sex, whether your pet is spayed or neutered, and current weight.</p>
<p>The <strong>Microchip #</strong> field is optional. If you fill it in, the number appears on the pet information sheet you can share, which can help if your pet is ever lost.</p>
<div class="tip">Hormone cycles in unspayed females can affect how insulin works. Your veterinarian may recommend discussing spaying.</div>
"""),
("insulin", "Insulin", f"""
<ol>
<li>Select your pet's insulin and confirm that the strength, <strong>U-40</strong> or <strong>U-100</strong>, matches the bottle. Always use syringes made for that strength.</li>
<li>Enter the <strong>units</strong> and <strong>time</strong> for the morning and evening shots exactly as your veterinarian prescribed. If your pet receives only one shot a day, leave the other blank.</li>
<li>Leave <strong>Remind me at each shot time</strong> turned on unless you prefer not to receive reminders.</li>
</ol>
<div class="tip">DiaPetic records the dose your veterinarian prescribed; it never suggests or changes a dose. When your veterinarian adjusts the dose, update it in {P("your pet's tab")}. The change is recorded in your reports automatically.</div>
"""),
("meals", "Meals and treats", """
<ol>
<li>Choose a <strong>feeding style</strong>. Most pets on insulin eat set meals; free feeding is also available.</li>
<li>Tap <strong>Add meal food</strong> for each food your pet eats, and enter the type, brand, amount and the meal it is served with. Calories can be added now or later; the <a href="guide-food.html">Food and nutrition</a> chapter explains the options.</li>
<li>Add your pet's usual treats with <strong>Add treat</strong> so they are quick to log.</li>
<li>If your veterinarian has given you a <strong>daily calorie target</strong>, enter it.</li>
</ol>
"""),
("vet", "Your veterinarian and an emergency clinic", f"""
<p>Enter your veterinarian's clinic and phone number, along with an after-hours <strong>emergency clinic</strong>. These details power the call and directions buttons throughout the app, including on the emergency screen.</p>
<p>You can add the doctor's name, email address and clinic address later in {P("Vet tab › Contacts › Edit or find clinics")}, where you can also search for clinics nearby.</p>
"""),
("permissions", "Notifications and other permissions", """
<p>Tap <strong>Save</strong> to finish. When your iPhone asks whether DiaPetic may send notifications, tap <strong>Allow</strong>; reminders cannot appear without this permission. DiaPetic asks for other permissions, such as the calendar, camera, location or microphone, only when you first use a feature that needs them.</p>
"""),
("first-week", "A checklist for your first week", f"""
<ul class="checklist">
<li>Log every shot and meal on the <a href="guide-tracker.html">Tracker</a> for the first few days to establish the routine.</li>
<li>Confirm that reminders arrive at the right times, and adjust them in {P("your pet's tab › Reminders")} if needed.</li>
<li>Add any other medications or supplements in {P("your pet's tab › Other medications and supplements")}.</li>
<li>Record the insulin bottle in use and any spare bottles in {P("your pet's tab › Insulin bottles")}.</li>
<li>Add your next veterinary appointment in the {P("Vet tab")}.</li>
<li>Make your first backup in {P("your pet's tab › Backup and restore")}.</li>
</ul>
"""),
], ["setup"]),

# ------------------------------------------------------------------
("tracker", "The Daily Tracker", "Recording shots, meals, the check-in, weight, glucose and journal entries.",
"""<p>The Tracker is where you record each day's care. It always opens on today, and if you return to the app after more than five minutes, or on a new day, it returns to today automatically.</p>""",
[
("days", "Moving between days", """
<p>Swipe left or right, or use the <strong>‹ ›</strong> arrows beside the date, to move one day at a time. To go further back, tap the <strong>calendar</strong> button beside "Daily Tracker" and choose a date, or use one of the shortcuts for one week, two weeks or one month ago. Tap the date at any time to return to today.</p>
<p>When you change days, the page keeps your place, which makes it easy to compare the same section from one day to the next.</p>
"""),
("glance", "Summary and alerts", """
<p>The top of the page summarizes the day: calories eaten compared with the target, the most recent glucose reading, and the number of meals logged. Alerts appear above the summary when something needs attention:</p>
<ul>
<li><strong>Eating less than usual</strong> appears when recent meals have been smaller than normal.</li>
<li><strong>Low reading</strong> appears when a glucose reading falls below your low threshold, with buttons to call your veterinarian or emergency clinic.</li>
<li>An <strong>appointment reminder</strong> appears the day before and the day of a visit, along with what to bring.</li>
</ul>
"""),
("meals", "Recording a meal", """
<p>The morning and evening cards each begin with the meal. Tap <strong>All</strong>, <strong>Most</strong>, <strong>Some</strong> or <strong>None</strong> to record how much your pet ate. To clear the entry, tap the same button again.</p>
<p>For a precise record, tap the meal row to open the meal details and enter the amount offered and the amount left over, using the same unit for both. Grams are the most accurate. You can also add a note, such as "ate slowly" or "vomited afterward."</p>
<p>If your pet eats less than half of a meal, DiaPetic reminds you to follow your veterinarian's instructions before giving insulin.</p>
"""),
("shots", "Recording a shot", """
<ol>
<li>Tap <strong>Give</strong> on the Insulin row, which shows the prescribed dose, for example "Give 8 u."</li>
<li>Choose when the shot was given: <strong>Just now</strong>, <strong>At the scheduled time</strong>, or <strong>A different time…</strong> to enter the exact time.</li>
<li>The row then confirms the dose and time, for example "8 units given at 7:04 AM," so anyone checking later can see that it was given.</li>
</ol>
<p>To change the time or units, add a note, or record a <strong>skipped</strong> shot (for example, when your veterinarian has advised skipping a dose because your pet did not eat), tap the details button beside the shot. You can also delete an entry made by mistake.</p>
<div class="tip">If you are unsure whether a shot was given, <strong>do not give another one.</strong> Check the Tracker first. If the shot is not recorded and no one remembers giving it, call your veterinarian. The emergency screen includes a guide for this situation.</div>
"""),
("meds", "Medications, supplements and treats", """
<p>Medications scheduled for the morning or evening appear in the matching card. Tap a medication to check it off, or tap its time to change when it was given. Medications given as needed have their own section with a <strong>Give</strong> button, and supplements appear as a daily checkbox.</p>
<p>To record a treat from your list, tap <strong>Add a treat</strong> and enter how many were given. For anything outside the meal plan, such as table scraps or a snack your pet found, tap <strong>Something else</strong>. Extra food can raise blood sugar, so these entries are useful to your veterinarian.</p>
"""),
("weight", "Weight", """
<p>Tap the Weight section to record a weight. For a reliable trend, weigh your pet at about the same time of day on the same scale. If your veterinarian gives a <strong>body condition score</strong> at a checkup (on a scale of 1 to 9, where 4 to 5 is usually ideal), you can record it here as well.</p>
"""),
("checkin", "The daily check-in", """
<p>Water intake, urination, stool, energy and sleep are set to <strong>Normal</strong> by default and are saved that way, so you only need to change what was different. Turn on <strong>Vomited</strong> if your pet vomited that day, and enter a <strong>Water amount</strong> if you measure it. Drinking and urinating more than usual can indicate that blood sugar is running high.</p>
"""),
("journal", "The journal", """
<p>The journal, below the check-in, is for anything else worth noting: how the day went, a change in behavior, or a question for your veterinarian.</p>
<ol>
<li>Tap <strong>Write about today</strong>, or <strong>Add another entry</strong> if the day already has one.</li>
<li>Tap the microphone and speak. Your words are transcribed as you talk, with punctuation; tap again to stop. You can also type, or correct the text afterward.</li>
<li>Confirm the time and tap <strong>Save</strong>.</li>
</ol>
<p>A day can have several entries. Tap an entry to edit it, or swipe left to delete it. Journal entries appear in History, in Reports, in the PDF report and in the clinic summary on the emergency screen. In Reports, the journal is collapsed to keep the page short. Tap it to see the latest entries, or tap <strong>All entries</strong> to see every entry in the period.</p>
"""),
("glucose", "Glucose readings", """
<p>If you check your pet's glucose at home, record readings in the Blood glucose section. The <a href="guide-glucose.html">Glucose and lab results</a> chapter covers this in detail. If you do not check at home, the section remains minimized.</p>
"""),
("supplies", "Supplies", """
<p>The Insulin Supplies section at the bottom of today's page shows which item will run out next, along with the insulin bottle in use, syringes and food on hand. See <a href="guide-supplies.html">Insulin, syringes and food</a>.</p>
"""),
("history", "Correcting an earlier day", """
<p>To review or correct a previous day, move back with the calendar or a swipe, or open the <strong>History</strong> tab. History lists each logged day with its shots (a filled icon for given, an X for skipped and an empty circle for not logged), the glucose range and the first journal entry. Tap a day to open it and make changes, just as you would for today.</p>
"""),
], ["day", "journal"]),

# ------------------------------------------------------------------
("food", "Food and nutrition", "Meal plans, calories, the label scanner, food on hand and diet changes.",
f"""<p>Consistent meals help keep blood sugar stable. You can set up and adjust the meal plan in {P("your pet's tab › Meals and treats")}.</p>""",
[
("add", "Adding a food", """
<ol>
<li>Tap <strong>Add meal food</strong>, or <strong>Add treat</strong> for a treat.</li>
<li>Choose the type of food: dry kibble, wet or canned, fresh or cooked, raw, topper or mix-in, treat, or other.</li>
<li>Enter the brand and product, the unit of measure, the amount served and the meal it is <strong>fed at</strong>.</li>
<li>Enter the <strong>calories</strong>. To read them from the packaging, tap <strong>Scan the label</strong>, point the camera at the calorie statement and tap the number.</li>
</ol>
<div class="tip">Weighing food in grams on a kitchen scale is the most accurate method. Measuring cups can vary by 20 percent or more.</div>
"""),
("facts", "Nutrition facts", """
<p>If you enter the guaranteed analysis from the label (protein, fat, fiber, moisture and ash), DiaPetic converts the values to a <strong>dry-matter basis</strong> and estimates the carbohydrate content. This allows your veterinarian to compare foods with different moisture levels, such as dry and canned food. Carbohydrate and fiber are particularly relevant for diabetic pets. This section is optional.</p>
"""),
("onhand", "Food on hand", """
<p>To track how much food remains, turn on <strong>Track how much is left</strong> and enter how the food is sold, the size of each package and the number you have. DiaPetic deducts each logged meal, estimates when the food will run out and can remind you before it does.</p>
"""),
("target", "Calorie target and portions", """
<p>Enter the <strong>daily calorie target</strong> provided by your veterinarian. If you do not have one, DiaPetic shows the total for the meal plan, which you can adopt by tapping <strong>Use as target</strong>.</p>
<p><strong>Portion estimates</strong> determine how much "Most" and "Some" represent when you record a meal on the Tracker. Treats and other food count toward the day's total when calories are entered for them.</p>
"""),
("changes", "Diet changes", """
<p>DiaPetic records each change to the meal plan automatically. Reports mark diet changes on the charts and compare average glucose, calories and weight before and after, so your veterinarian can see how a new food has affected your pet.</p>
"""),
], []),

# ------------------------------------------------------------------
("medications", "Medications and supplements", "Adding medications and supplements, schedules and doses.",
f"""<p>Record everything your pet takes in addition to insulin in {P("your pet's tab › Other medications and supplements")}.</p>""",
[
("add", "Adding a medication or supplement", """
<ol>
<li>Tap <strong>Add medication or supplement</strong> and choose which one you are adding.</li>
<li>Enter the name, the <strong>dose as prescribed</strong> (for example, "60 mg capsule") and, if you wish, its purpose.</li>
<li>Choose a schedule: with the morning routine, with the evening routine, morning and evening, once a day, or as needed.</li>
<li>If a dose contains calories, as fish oil and chews often do, enter them so they are included in the day's total.</li>
<li>Enter the start date and any notes, such as "give with food."</li>
</ol>
"""),
("tracker", "On the Tracker", """
<p>Scheduled medications appear in the morning or evening card, ready to check off. Once-a-day supplements appear as a daily checkbox, and medications given as needed have a <strong>Give</strong> button. Reports show the percentage of scheduled doses that were recorded.</p>
"""),
("stop", "Stopping a medication", """
<p>When your pet stops taking a medication, turn on <strong>Stopped</strong> and enter the date rather than deleting it. This keeps its history in your reports. Deleting is best reserved for entries added by mistake.</p>
"""),
("reminders", "Medication reminders", f"""
<p>Morning and evening medications are listed in the shot reminder. Once-a-day medications can have a separate reminder, and DiaPetic can also remind you before a course of medication ends. These options are in {P("your pet's tab › Reminders › Medications and supplements")}.</p>
"""),
], []),

# ------------------------------------------------------------------
("glucose", "Glucose and lab results", "Home glucose readings, curves, time in range and laboratory results.",
f"""<p>Monitor glucose at home only if your veterinarian has asked you to. To turn on home monitoring, go to {P("your pet's tab › Home glucose monitoring")} and turn on <strong>I check glucose at home</strong>.</p>""",
[
("numbers", "Setting your thresholds", """
<p>Set <strong>Highlight readings below</strong> and <strong>Highlight readings above</strong> to the values your veterinarian recommends. These thresholds determine how readings are colored, when the low-reading alert appears and how time in range is calculated. You can choose mg/dL or mmol/L in the app settings.</p>
"""),
("add", "Recording a reading", """
<p>On the Tracker, tap <strong>Add reading</strong> in the Blood glucose section. Enter the value and time, and choose the source: <strong>glucose meter</strong>, <strong>CGM sensor</strong> or <strong>at the vet</strong>. You can add a note if anything was unusual. If a reading falls below your low threshold, DiaPetic displays a warning with buttons to call for help, and it can remind you to check on your pet again later.</p>
"""),
("curves", "Glucose curves", """
<p>A glucose curve is a series of readings taken over the course of a day. In <strong>Reports</strong>, switch to <strong>Glucose</strong> to view your readings as curves, along with weekly glucose, time in range, the relationship between eating and glucose, and any low readings.</p>
<p>Tap <strong>Compare curves</strong> to overlay up to three days. Veterinarians look closely at the lowest point of a curve and when it occurs to assess how well the insulin is working.</p>
"""),
("labs", "Lab results", f"""
<p>Record blood work, such as a fructosamine test, in {P("Reports › Lab results › Add lab result")} or when adding notes after a vet visit. Enter the test, the result, the unit and the date, along with any comments from your veterinarian. Lab results are included in your reports.</p>
"""),
], []),

# ------------------------------------------------------------------
("reminders", "Reminders", "Reminders for shots, meals, medications, supplies, checkups and more.",
f"""<p>All reminders are managed in {P("your pet's tab › Reminders")}. The <strong>Coming up</strong> list at the top of the screen shows what is scheduled, so you can confirm that reminders are set correctly.</p>""",
[
("insulin", "Insulin", """
<p><strong>At each shot time</strong> sends a reminder at the morning and evening shot times. <strong>Nudge if a shot isn't logged</strong> sends a follow-up if no shot has been recorded within a period you choose, from 15 minutes to 2 hours. This helps prevent both missed doses and double doses.</p>
"""),
("meals", "Meals", """
<p>A meal reminder can arrive with the shot reminder or 15, 30 or 45 minutes before it. The <strong>Fill the bowl</strong> option lists the planned portions in the reminder, which is helpful when someone else is feeding your pet.</p>
"""),
("care", "Medications, glucose and logging", """
<p>DiaPetic can remind you about morning, evening and once-a-day medications and supplements, and before a course of medication ends. It can also remind you to check glucose before each shot and to check on your pet after a low reading. A daily logging reminder and a weekly weigh-in reminder are also available.</p>
"""),
("supplies", "Supplies", """
<p>Supply reminders warn you before insulin, syringes or food run low; you choose how many days in advance. <strong>Time to open a new bottle</strong> reminds you when the insulin bottle in use reaches the end of its usable life. Unopened bottles and boxes you have recorded are taken into account, so you will not be prompted to reorder when spares are on hand.</p>
"""),
("checkups", "Checkups", """
<p><strong>Remind me to book a checkup</strong> prompts you every 3, 6 or 12 months, counting from your last completed visit, and only when no appointment is already scheduled. Reminders for scheduled appointments are set on each appointment in the Vet tab.</p>
"""),
("custom", "Custom reminders (Pro)", """
<p>Tap <strong>Add a reminder</strong> to create your own. Ready-made options include heartworm prevention, flea and tick prevention, insulin prescription refills, a fructosamine test or glucose curve, vaccines, nail trims, grooming, tooth brushing and cleaning the water bowl. You can also choose <strong>Something else…</strong>. Set the date of the first reminder and how often it repeats, from once to yearly.</p>
"""),
("snooze", "Snoozing and troubleshooting", """
<p>Each reminder can be snoozed for 15 minutes or an hour. Tapping a reminder opens the relevant pet and screen.</p>
<div class="tip">If reminders do not appear, go to iPhone <strong>Settings › Notifications › DiaPetic</strong> and make sure notifications are allowed, and check that a Focus mode such as Sleep is not silencing them. If notifications are turned off, the Reminders screen displays an <strong>Open Settings</strong> button.</div>
"""),
], ["reminders"]),

# ------------------------------------------------------------------
("supplies", "Insulin, syringes and food", "Insulin bottles, prescriptions, syringes and food supplies.",
"""<p>DiaPetic tracks your supplies based on the shots and meals you record, and alerts you before anything runs out.</p>""",
[
("bottles", "Insulin bottles", f"""
<p>Open {P("your pet's tab › Insulin bottles")}, or tap <strong>Manage</strong> in the Insulin Supplies section of the Tracker.</p>
<p><strong>Bottle in use.</strong> Turn on <strong>Bottle opened</strong> and enter the date it was opened, the number of units in the bottle and the expiration date on the label. Then set how many days an opened bottle remains usable, as stated on the insulin's label or by your veterinarian. For reference, a 10 mL bottle contains 400 units of U-40 insulin or 1,000 units of U-100 insulin.</p>
<p><strong>Spare bottles.</strong> Tap <strong>Got a new bottle</strong> to record unopened bottles with their expiration dates and lot numbers. DiaPetic suggests opening them in order of expiration and warns you if a bottle is likely to expire before it is needed.</p>
<p><strong>Starting a new bottle.</strong> Tap <strong>Open new bottle</strong>. The current bottle moves to the history and the next spare becomes the bottle in use. If you tap it by mistake, <strong>Undo</strong> is available for the rest of the day.</p>
"""),
("rx", "Prescription details", """
<p>On the same screen, you can record the date the prescription was filled, the number of <strong>refills left</strong>, the prescription number and the pharmacy. The prescription number can be copied when you call to reorder. When no refills remain, DiaPetic reminds you to request a new prescription from your veterinarian before the insulin runs out.</p>
"""),
("syringes", "Syringes", f"""
<p>Open {P("your pet's tab › Syringes")} and enter the date you started the current box and how many syringes it contains. DiaPetic counts one syringe for each shot. Record unopened boxes with <strong>Got new syringes</strong>.</p>
<p>When you open a new box, tap <strong>Start new box</strong>. If syringes remain in the previous box, indicate whether you are keeping them, in which case they are added to the new count, or have discarded them. This keeps the count accurate when boxes overlap.</p>
"""),
("food", "Food on hand", """
<p>Food supplies are tracked in each food's settings, as described in <a href="guide-food.html#onhand">Food on hand</a>. The Insulin Supplies section on the Tracker also shows when each food is expected to run out.</p>
"""),
], ["supplies"]),

# ------------------------------------------------------------------
("vet", "Your veterinarian", "Clinic contacts, appointments, visit notes, questions and email.",
"""<p>The Vet tab brings together everything related to your pet's veterinary care.</p>""",
[
("contacts", "Contacts and finding a clinic", f"""
<p>In {P("Vet tab › Contacts › Edit or find clinics")}, enter your veterinarian's clinic, the doctor's name, phone number, email address and clinic address. Add an emergency clinic as well, for after-hours problems such as very low blood sugar.</p>
<p>To search for a clinic, tap <strong>Find veterinarians near me</strong> or <strong>Find emergency clinics near me</strong> and search by your current location or by city or ZIP code. Then choose <strong>Use as my veterinarian</strong> or <strong>Use as my emergency clinic</strong>. Your location is used only for the search and is not stored.</p>
"""),
("appointments", "Scheduling an appointment", """
<ol>
<li>Tap <strong>Schedule an appointment</strong>.</li>
<li>Choose the type of visit: checkup, glucose curve, blood work or fructosamine, recheck, dental, vaccines, emergency visit, or other.</li>
<li>Enter the start and end times (or drop-off and pick-up times for a day stay), the location, and any instructions from the clinic.</li>
<li>List <strong>what to bring</strong>. This appears in reminders and on the Tracker the day before the visit.</li>
<li>Choose your reminders. To add the appointment to your iPhone calendar, tap <strong>Add to Calendar</strong>. If you later change or cancel the appointment in DiaPetic, the calendar event is updated or removed as well.</li>
</ol>
<div class="tip">Ask the clinic whether your pet should eat and receive insulin as usual on the morning of the visit, and record the answer in the instructions.</div>
"""),
("after", "After the visit", """
<p>After each appointment, DiaPetic asks how the visit went. Tap <strong>Add visit notes</strong> to record what your veterinarian said and any next steps, such as dose changes, rechecks or diet changes. From the same screen you can add a lab result or schedule a follow-up. If the appointment did not take place, tap <strong>It didn't happen</strong>.</p>
<p>If the insulin dose was changed, update it in your pet's tab so that the change appears in your reports.</p>
"""),
("questions", "Questions for your veterinarian", """
<p>Add questions under <strong>Questions for your veterinarian</strong> as they come up. Open questions are printed at the top of the PDF report and can be included when you email your veterinarian. Tap the circle beside a question once it has been answered, and add the answer if you wish.</p>
"""),
("email", "Emailing your veterinarian", """
<p>Tap <strong>Ask your vet</strong> to compose an email. Choose which questions to include, add a message and, if you like, a summary of the last 7 days, 2 weeks or 30 days. With DiaPetic Pro, you can also attach the PDF report. Tap <strong>Preview</strong> to review the email, then send it from your own email account, or choose <strong>Share another way</strong> to use another app, such as Gmail or Messages.</p>
"""),
], ["vet"]),

# ------------------------------------------------------------------
("reports", "Reports and sharing", "Progress and glucose reports, PDF and CSV files, and the pet information sheet.",
"""<p>The Reports tab shows how your pet is doing over time. Choose a period at the top of the screen: 7 days, 2 weeks or 30 days, or 90 or 180 days with DiaPetic Pro. Use the switch to move between <strong>Progress</strong> and <strong>Glucose</strong>.</p>""",
[
("progress", "Progress", """
<p>The Progress view begins with a summary of food eaten, calories, shots given and weight, each compared with the previous period. It then shows:</p>
<ul>
<li>The routine at a glance, with typical meal and shot times calculated from your records and a measure of how complete the log is.</li>
<li>The insulin dose history, with each change recorded automatically.</li>
<li>Daily grids of symptoms and shots, and a comparison of actual shot times with planned times. Giving shots about 12 hours apart at consistent times helps keep glucose stable.</li>
<li>Your most recent journal entries.</li>
<li>Nutrition, including daily calories, appetite, the timing of meals and insulin, calories and weight, treats, water intake and diet changes.</li>
<li>Medications, weight and lab results.</li>
</ul>
"""),
("pdf", "PDF report for your veterinarian (Pro)", """
<p>Tap <strong>Share a PDF report with your veterinarian</strong>, choose a period and tap <strong>Create PDF report</strong>. You can then send the report by email, Messages or AirDrop, save it to Files or print it.</p>
<p>The report opens with your open questions and a summary of the routine, followed by progress, glucose and curves, symptoms and shot consistency, nutrition and diet details, notable events (such as low readings, small meals, missed shots and medications), a day-by-day log, and your journal entries in full.</p>
<p>A <strong>CSV file</strong> containing every entry is also available for use in Numbers or Excel.</p>
"""),
("infosheet", "Pet information sheet", """
<p>In your pet's tab, tap <strong>Share</strong> beside your pet's name to create a one-page information sheet. It includes your pet's details and microchip number, insulin routine, other medications, meals, veterinary and emergency contacts, supplies, and the signs of low blood sugar. It is useful for pet sitters, boarding facilities, family members and emergency visits, and it is available to all users.</p>
"""),
], ["reports"]),

# ------------------------------------------------------------------
("emergency", "When something seems wrong", "Emergency help, guided questions, quick guides and the clinic summary.",
"""<p>The red <strong>emergency button</strong> at the top right of every screen opens <strong>Emergency help</strong>. If you are ever unsure, call your veterinarian or an emergency clinic.</p>""",
[
("now", "When to go to an emergency clinic immediately", """
<p>Go to an emergency clinic right away if your pet has collapsed or will not wake up, is having a seizure, is struggling to breathe, is bleeding heavily, or is very weak, unsteady or trembling. The emergency screen provides call and directions buttons for your emergency clinic, and <strong>Find nearby</strong> lists other clinics close to you.</p>
"""),
("decide", "Help me decide what to do", """
<p>This feature asks a short series of questions, for example whether your pet is weak or unsteady, may have eaten something harmful, is not eating or is vomiting, or whether there has been a problem with the insulin. Based on your answers, it recommends one of three courses of action: <strong>act now</strong>, <strong>call your veterinarian today</strong>, or <strong>call your veterinarian soon</strong>. In an emergency, do not wait to finish the questions.</p>
"""),
("guides", "Quick guides", """
<p>Step-by-step guides are available for the following situations:</p>
<ul class="columns">
<li>Going to an emergency clinic now</li>
<li>Possible low blood sugar</li>
<li>Possible poisoning</li>
<li>Needing to be seen today</li>
<li>Not eating while on insulin</li>
<li>Vomiting or diarrhea</li>
<li>Too much insulin</li>
<li>Uncertainty about whether a shot was given</li>
<li>A missed dose</li>
<li>Insulin that may be damaged</li>
<li>Increased drinking and urination</li>
<li>A high glucose reading</li>
<li>Serious and minor injuries</li>
<li>When something seems off</li>
</ul>
"""),
("summary", "Information for the clinic", """
<p>The emergency screen also prepares a summary from your records, including your pet's details and microchip number, insulin and dose, the last shot, meal and glucose reading, other medications, today's journal entries and your regular veterinarian. You can read it to the clinic over the phone, or tap <strong>Share</strong> or <strong>Copy</strong> to send it.</p>
"""),
("poison", "Poison control", """
<p>If your pet may have swallowed something harmful, you can call the <strong>ASPCA Animal Poison Control Center at (888) 426-4435</strong> or the <strong>Pet Poison Helpline at (855) 764-7661</strong> directly from the emergency screen. A consultation fee may apply.</p>
<div class="tip">Signs of low blood sugar include weakness, unsteadiness, trembling, twitching, confusion and seizures. Rub honey or corn syrup on your pet's gums and call your veterinarian or an emergency clinic immediately.</div>
"""),
], ["emergency"]),

# ------------------------------------------------------------------
("pet-tab", "Your pet's tab and settings", "Pet details, multiple pets, app settings and the app icon.",
"""<p>The last tab is named after your pet. It contains everything you entered during setup, along with the app's settings.</p>""",
[
("help", "Help and support", """
<p>Near the top of the tab, <strong>Help and support</strong> opens this guide (<strong>How to use DiaPetic</strong>), the <strong>FAQ &amp; support</strong> page and the <strong>Suggestion box</strong>. For your first two weeks, the Tracker also shows a short card with a link to the guide; tap <strong>Not now</strong> to hide it.</p>
"""),
("details", "Pet details", """
<p>Here you can update your pet's name, species, breed, color, sex and microchip number. The <strong>Weight</strong> section shows the weight trend, the body condition score, and the starting and target weights. Further down are the meal plan, insulin and shot times, other medications, reminders, supplies and home glucose settings.</p>
"""),
("pets", "Multiple pets", """
<p>Use the <strong>pet menu</strong> at the top left of any tab to switch between pets or to <strong>Add a pet</strong>. Your first pet is free; additional pets require DiaPetic Pro. Each pet has its own records, reminders, reports and supplies.</p>
"""),
("settings", "App settings", """
<ul>
<li><strong>Appearance</strong> follows your iPhone's setting by default, or can be set to light or dark.</li>
<li><strong>Glucose units</strong> can be mg/dL or mmol/L, and <strong>weight units</strong> can be lb or kg.</li>
<li><strong>App icon</strong> (Pro) lets you choose Obi the dog or Kitty. The icon can change with the seasons (fall, Halloween, Thanksgiving, the holiday season and Christmas), stay the same all year, or keep one seasonal theme.</li>
<li><strong>Backup and restore</strong> is described in <a href="guide-backups.html">Backups and a new iPhone</a>.</li>
<li><strong>Rate DiaPetic</strong> and <strong>Support DiaPetic</strong>, where you can leave an optional tip.</li>
<li><strong>About DiaPetic</strong> includes privacy information and links to this website and the privacy policy.</li>
</ul>
"""),
("delete", "Deleting a pet", """
<p>The option at the bottom of the tab permanently deletes the pet and all of its records. If you may want the records later, make a backup first.</p>
"""),
("feedback", "Suggestions and support", """
<p>The <strong>Suggestion box</strong>, in Help and support, sends a message from your own email account. Choose whether you are sending a suggestion, reporting a problem, asking a question or sharing something you like, then speak or type your message. You can include details about the app and your iPhone to help diagnose problems; your pet's health records are never included. You can also email <a href="mailto:support@diapetic.com">support@diapetic.com</a> directly.</p>
"""),
], []),

# ------------------------------------------------------------------
("backups", "Backups and a new iPhone", "Backing up, automatic copies, restoring and moving to a new iPhone.",
"""<p>Everything you enter in DiaPetic is stored only on your iPhone. A backup is the only way to recover your records if your phone is lost or the app is deleted.</p>""",
[
("now", "Making a backup", f"""
<p>Go to {P("your pet's tab › Backup and restore")} and tap <strong>Back up now</strong>. Save the file to <strong>iCloud Drive</strong> so it remains safe even if something happens to your iPhone. A backup includes every pet and all records, visits, insulin bottles, syringe boxes, journal entries, reminders and settings.</p>
"""),
("auto", "Automatic weekly copies", """
<p>DiaPetic also saves a copy automatically once a week and keeps the four most recent. Because these copies may be stored only on the iPhone, it is a good idea to use Back up now regularly as well.</p>
"""),
("restore", "Restoring or moving to a new iPhone", """
<ol>
<li>Install DiaPetic on the new iPhone and open <strong>Backup and restore</strong>.</li>
<li>Tap <strong>Restore from backup…</strong> and select your backup file.</li>
<li>Review the contents of the backup, including the pets and number of days recorded, and tap <strong>Restore</strong>.</li>
</ol>
<p>Restoring replaces the data currently in DiaPetic, and a copy of that data is saved first as a precaution. If you purchased DiaPetic Pro, open the Pro screen and tap <strong>Restore purchase</strong>.</p>
"""),
], ["backup"]),
]
