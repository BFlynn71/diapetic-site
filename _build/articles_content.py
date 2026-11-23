# Guides for owners: longer articles for people searching for help with a diabetic pet,
# whether or not they use DiaPetic yet. Separate from the app how-to chapters (guide_content.py).
# Rules: record-keeping and vet preparation only. Never suggest a dose or a change to treatment;
# send every health decision to the vet. Website voice: no contractions, "vet" in everyday copy,
# "veterinarian" in safety lines. Lines with general health information were checked by the developer
# (or his vet) before publishing; keep them general and point to the vet.
# Each article: (slug, title tag, meta description, h1, intro html, [(anchor, h2, html)], published, modified)

ARTICLES = [
# ------------------------------------------------------------------
("glucose-curve-at-home",
"How to Track Your Pet's Glucose Curve at Home",
"Your vet asked for a glucose curve. Learn what to record, how to keep each reading in order, and how to share a clear curve with your dog or cat's vet.",
"How to track a dog or cat's glucose curve at home",
"""<p>A glucose curve is a set of blood sugar readings taken across one day. Your vet uses it to see how your pet's insulin is working: when blood sugar is lowest, how long the insulin lasts, and whether readings stay in the range your vet wants.</p>
<p>Many vets now ask owners to do curves at home. A pet at home is calmer and eats as usual, which can give a truer picture than a day at the clinic. This matters most for cats, whose blood sugar can rise from the stress of a clinic visit.</p>
<p>This guide is about keeping good records. Your vet decides the schedule, the target range and any change to insulin.</p>""",
[
("before", "Before the curve day", """
<ul>
<li>Ask your vet when to start, how often to test and which reading means you should call. Veterinary guidelines describe a reading before the meal and shot, then about every two hours for 10 to 12 hours, with checks more often when readings are low.</li>
<li>Use the meter your vet recommends. Veterinary guidelines favor meters calibrated for dogs and cats, because meters made for people can show different numbers for the same drop of blood. Tell your vet which one you use.</li>
<li>Plan an ordinary day, with the usual food, meal times and walks.</li>
<li>Set out test strips, lancets, cotton balls and a small reward for afterward.</li>
</ul>
"""),
("record", "What to write down", """
<p>A number on its own does not tell your vet much. Record what happened around it:</p>
<ul class="checklist">
<li>The time of each reading and the result</li>
<li>The time of the morning shot and the amount given, as prescribed</li>
<li>The time of each meal and how much was eaten</li>
<li>Walks, play, treats and anything unusual, such as vomiting, shaking or tiredness</li>
<li>Readings that had to be repeated, and why</li>
</ul>
<p>Write each reading down when you take it. Times written in later are easy to get wrong.</p>
"""),
("diapetic", "Keeping it in order with DiaPetic", """
<p>DiaPetic saves each glucose reading with its time and draws that day's curve, with shots, meals and walks shown on the same chart. You can also enter the low and high alerts your vet gives you. See <a href="guide-glucose.html">Glucose, ketones and lab results</a> in the DiaPetic guide.</p>
"""),
("share", "Sharing the curve with your vet", """
<p>Send the curve on the same day, while your vet can still ask questions about it. In DiaPetic you can share a day's curve as a picture by text or email, or send a report covering the past weeks. See <a href="guide-reports.html">Reports and sharing</a>.</p>
"""),
("call", "When to stop and call", """
<p>If a reading is below the low number your vet gave you, or your pet seems weak, wobbly, shaky or confused, or has a seizure, call your veterinarian or an emergency clinic now. DiaPetic has an emergency button on every screen with a low blood sugar guide. See <a href="guide-emergency.html">When something seems wrong</a>.</p>
"""),
], "2026-11-18", "2026-11-18"),

# ------------------------------------------------------------------
("insulin-and-meal-schedule",
"Twice-Daily Pet Insulin and Meal Schedule Tips",
"How to keep twice-daily insulin shots and meals on time for a diabetic dog or cat, share care at home, and help prevent missed or double doses.",
"Managing twice-daily pet insulin shots and meal schedules",
"""<p>Many diabetic dogs and cats get insulin twice a day, about 12 hours apart, with meals to match. The routine soon becomes part of the day, but busy mornings, shared care and changes in plans make it easy to lose track. This guide covers ways to keep the schedule steady and the record clear.</p>""",
[
("vet", "Set the routine with your vet", """
<p>Ask your vet these questions now, before you need the answers:</p>
<ul class="checklist">
<li>What times should shots be given, and how far apart?</li>
<li>Should the shot come before or after the meal?</li>
<li>What should I do if my pet does not eat?</li>
<li>What should I do if a shot is missed?</li>
<li>What should I do if I am not sure whether a shot was given?</li>
</ul>
<p>Write the answers down where everyone who helps can see them.</p>
"""),
("double", "How double doses happen", """
<p>Double doses are rarely about carelessness. Two people share the care, the morning is rushed, and each thinks the other has not given the shot yet. A clear record that everyone checks before giving a shot is the best protection.</p>
"""),
("log", "Keep one record and log right away", """
<ul>
<li>Log each shot as soon as it is given, with the real time.</li>
<li>Check the record before every shot, every time.</li>
<li>Keep the record in one place rather than on scraps of paper.</li>
</ul>
<p>In DiaPetic, you log a shot with one tap. DiaPetic asks before logging a shot within 10 hours of another, and sends a nudge when a shot has not been logged. You can mark a shot as given from the reminder, on your iPhone or Apple Watch. Each iPhone keeps its own records, so if two people give shots, agree on one iPhone to log them. See <a href="guide-tracker.html">The Daily Tracker</a> and <a href="guide-reminders.html">Reminders</a>.</p>
"""),
("unsure", "If you are not sure a shot was given", """
<p>Do not give another shot to be safe. Call your veterinarian and follow their advice.</p>
"""),
("meals", "Meals", """
<p>Do not give insulin to a pet that has not eaten unless your vet has told you what to do. Call your vet instead. Record how much of each meal was eaten. A pet that eats less than usual for more than one meal is worth a call to your vet. DiaPetic records each meal as All, Most, Some or None. See <a href="guide-food.html">Food and nutrition</a>.</p>
"""),
("away", "Weekends, travel and sitters", """
<p>Keep shot times steady on weekends and while traveling. When someone else is caring for your pet, give them your vet's written instructions and a contact number. DiaPetic can share a one-page pet information sheet with insulin and vet details. See <a href="guide-reports.html#infosheet">Pet information sheet</a>.</p>
"""),
], "2026-11-18", "2026-11-18"),

# ------------------------------------------------------------------
("diabetic-pet-vet-visit-checklist",
"Diabetic Pet Vet Visit Checklist: What to Bring",
"A checklist for diabetic dog and cat vet visits: the records, supplies and questions to bring, and how to share a 30- to 180-day summary with your vet.",
"What to bring to a diabetic pet vet appointment",
"""<p>Rechecks are where your vet decides what comes next. They go better when you arrive with clear records instead of trying to remember the past month on the spot.</p>""",
[
("week", "The week before", """
<ul>
<li>Ask whether your pet should eat and get insulin as usual on the morning of the visit. Vets have different instructions.</li>
<li>Ask whether to bring a urine sample or do a glucose curve at home first.</li>
<li>Start a list of questions as they come to you.</li>
</ul>
"""),
("checklist", "Checklist", """
<ul class="checklist">
<li>A summary of care since the last visit: shots, meals, glucose readings, weight and anything unusual</li>
<li>Your pet's insulin bottle and a syringe, so your vet can check the type and how you give the shot</li>
<li>The name of the food and how much is fed at each meal</li>
<li>A list of treats, supplements and other medications</li>
<li>Recent glucose readings or a home glucose curve</li>
<li>Home ketone test results, if you test for ketones</li>
<li>Notes on changes in water drinking, urination, appetite or energy</li>
<li>Your questions</li>
<li>Supplies you need refilled</li>
</ul>
"""),
("summary", "Why a summary helps", """
<p>A summary turns weeks of days into something your vet can read in a minute. Patterns stand out that are easy to miss day to day, such as appetite slowly dropping or readings drifting higher.</p>
<p>DiaPetic summarizes 7, 14, 30, 90 or 180 days, with shots, appetite, symptoms, weight, glucose curves, ketone tests, dose history, lab results and journal notes. The last 30 days are free. PDF reports and 90- and 180-day trends come with DiaPetic Gold, $9.99, one time, no subscription. See <a href="guide-reports.html">Reports and sharing</a>.</p>
"""),
("after", "After the visit", """
<ul>
<li>Write down any new instructions exactly as your vet gives them.</li>
<li>Record lab results, such as a fructosamine test, so they appear in the next report.</li>
<li>Add the next appointment to your calendar.</li>
</ul>
<p>DiaPetic's Vet tab keeps appointments, what to bring, questions for your vet and clinic contacts together. See <a href="guide-vet.html">Your vet</a>.</p>
"""),
], "2026-11-18", "2026-11-22"),

# ------------------------------------------------------------------
("pet-insulin-supplies",
"How to Track Pet Insulin, Syringes and Food Supplies",
"Keep track of your diabetic pet's insulin bottles, syringes and prescription food: open dates, matching syringes, refills and spares, so nothing runs out.",
"How to track pet insulin bottles, syringes and prescription food supplies",
"""<p>Running out of insulin on a weekend is stressful. A few simple habits keep supplies ahead of need.</p>""",
[
("bottles", "Insulin bottles", """
<ul>
<li>Write the date on each bottle when you open it.</li>
<li>How long a bottle can be used after opening depends on the product. Check the label, or ask your vet or pharmacist.</li>
<li>Store and handle insulin the way the label says.</li>
<li>Ask your vet whether to keep a spare bottle on hand.</li>
</ul>
"""),
("syringes", "Syringes must match the insulin", """
<p>Pet insulins come in different strengths, and syringes are marked to match: U-40 syringes for U-40 insulin and U-100 syringes for U-100 insulin. Using the wrong syringe gives the wrong amount. Check the box each time you pick up a refill.</p>
<p>DiaPetic shows a warning when your syringes do not match your insulin. Set U-40 or U-100 in Syringes to turn it on.</p>
"""),
("food", "Prescription food", """
<p>Keep track of how much food is left and when to reorder. Changing food can change blood sugar, so talk to your vet before switching brands or amounts.</p>
"""),
("refills", "Refills and deliveries", """
<ul>
<li>Note how many refills are left on each prescription.</li>
<li>Reorder about a week before you run out, to allow for delays.</li>
<li>If your pharmacy refills on a schedule, note the next delivery date.</li>
</ul>
<p>DiaPetic shows how long each insulin bottle and box of syringes will last and when to order more. It counts spare bottles and boxes on hand, tells you when a prescription has no refills left, and with Auto refill on, reminds you on delivery day. See <a href="guide-supplies.html">Insulin, syringes and food</a>.</p>
"""),
("list", "Supply checklist", """
<ul class="checklist">
<li>Insulin, with the open date written on the bottle</li>
<li>Syringes that match the insulin strength</li>
<li>Prescription food, with the reorder date noted</li>
<li>Glucose test strips and lancets, if you test at home</li>
<li>A sharps container for used syringes</li>
<li>Your vet's and the emergency clinic's phone numbers</li>
</ul>
"""),
], "2026-11-18", "2026-11-18"),

# ------------------------------------------------------------------
("ketones-dka-diabetic-pets",
"Ketones and DKA in Dogs and Cats: What to Record",
"What ketones mean for a diabetic dog or cat, how home ketone tests work, what to write down, and the DKA warning signs that mean you should call your vet now.",
"Ketones and DKA in diabetic dogs and cats: what to record and when to call your vet",
"""<p>When a diabetic pet's body cannot use sugar for energy, often because there is not enough insulin working, it starts breaking down fat instead. That makes ketones. A build-up of ketones can lead to diabetic ketoacidosis (DKA), a serious emergency that needs a veterinarian.</p>
<p>Some vets ask owners to test for ketones at home, especially in the first weeks after a diagnosis or when a pet is unwell. This guide covers how home tests work and what to record. Your vet decides when to test, what the results mean and what to do next.</p>""",
[
("signs", "Signs that mean call your vet now", """
<p>Call your veterinarian or an emergency clinic right away if your diabetic pet:</p>
<ul class="checklist">
<li>Will not eat, or eats much less than usual</li>
<li>Is vomiting</li>
<li>Seems weak, very tired or unlike themselves</li>
<li>Is drinking or urinating much more than usual</li>
<li>Has breath that smells sweet or like nail polish remover</li>
<li>Is breathing fast or deeply</li>
</ul>
<p>Do not wait for a ketone test if your pet shows these signs. A negative test does not rule out a problem.</p>
"""),
("when", "When vets ask for a ketone test", """
<p>Ask your vet whether they want you to test for ketones at home, and when. Many ask for a test when a pet is not eating, is vomiting or seems unwell, or when glucose readings are higher than usual. If your cat takes an oral diabetes medicine instead of insulin, your vet may ask you to check ketones regularly, because ketones can build up even when glucose readings look normal. Write down their answer so everyone who helps with care can find it.</p>
"""),
("tests", "Urine strips and blood meters", """
<ul>
<li><strong>Urine strips</strong> change color when ketones are in the urine. Dip the strip in fresh urine, wait the time printed on the bottle, then compare it with the color chart. Results are words such as Negative, Trace, Small, Moderate or Large.</li>
<li><strong>Blood ketone meters</strong> measure ketones in a drop of blood and show a number in mmol/L. Ask your vet which meter to use and which number they want to hear about.</li>
</ul>
<p>Urine strips do not detect the main ketone the body makes, so they can read lower than a blood meter, especially early on. Veterinary guidelines note that blood meters pick up the early stages of DKA more accurately. Tell your vet which test you used.</p>
"""),
("record", "What to write down", """
<ul class="checklist">
<li>The time of the test, which test you used and the result</li>
<li>A glucose reading taken at the same time, if you check glucose at home</li>
<li>Whether your pet ate, and how much</li>
<li>When the last insulin shot was given</li>
<li>Vomiting, weakness, drinking or anything else unusual</li>
<li>What your vet said to do</li>
</ul>
<p>Do not change or skip an insulin dose because of a ketone result. Call your veterinarian and follow their instructions.</p>
"""),
("diapetic", "Recording ketone tests in DiaPetic", """
<p>In DiaPetic, open the <strong>Glucose &amp; ketones</strong> tile on the Tracker and tap <strong>Add ketone test</strong>. Choose a blood meter or a urine strip and enter the result. Any urine result above Negative, and any blood result at or above the level you set with your vet, opens a screen that asks you to call your veterinarian, with buttons to call your vet or an emergency clinic.</p>
<p>Ketone tests appear on the Tracker, in History, on that day's glucose curve, in reports and in the clinic summary on the emergency screen. They are part of the free app. See <a href="guide-glucose.html#ketones">Ketone tests</a> in the DiaPetic guide and <a href="guide-emergency.html">When something seems wrong</a>.</p>
"""),
], "2026-11-23", "2026-11-23"),
]

# Further reading shown at the end of each guide (general sources checked Nov 23, 2026)
SOURCES = {
"glucose-curve-at-home": ['<a href="https://www.aaha.org/diabetes-management/">AAHA Diabetes Management Guidelines</a>', '<a href="https://www.redcross.org/take-a-class/resources/learn-pet-first-aid/dog/hypoglycemia-blood-sugar-emergencies">American Red Cross Pet First Aid: Low blood sugar</a>'],
"insulin-and-meal-schedule": ['<a href="https://www.aaha.org/diabetes-management/">AAHA Diabetes Management Guidelines</a>', '<a href="https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/health-info/diabetes">Cornell Riney Canine Health Center: Diabetes</a>'],
"diabetic-pet-vet-visit-checklist": ['<a href="https://www.aaha.org/diabetes-management/">AAHA Diabetes Management Guidelines</a>'],
"pet-insulin-supplies": ['<a href="https://www.aaha.org/diabetes-management/">AAHA Diabetes Management Guidelines</a>', '<a href="https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/health-info/diabetes">Cornell Riney Canine Health Center: Diabetes</a>'],
"ketones-dka-diabetic-pets": ['<a href="https://www.aaha.org/diabetes-management/">AAHA Diabetes Management Guidelines</a>', '<a href="https://vet.cornell.edu/animal-health-diagnostic-center/about/news/discontinuation-acetest-confirmation-urinary-ketones">Cornell Animal Health Diagnostic Center: urine ketone testing</a>', '<a href="https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/health-info/diabetes">Cornell Riney Canine Health Center: Diabetes</a>'],
}
