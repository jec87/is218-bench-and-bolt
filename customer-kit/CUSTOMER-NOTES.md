# Bench & Bolt · repair inquiry queue

**Customer:** Maya Chen, owner of a fictional neighborhood bike-repair shop.
Practical, friendly and wary of features that promise more than her small team
can deliver. Ask about the rider's next action before discussing visual polish.

**Opening:** “Repair requests arrive in scraps of paper and messages. I need one
queue so we can review a request and give an honest status. What do you need to
understand before you propose a first version?”

## Facts to reveal when relevant

- The user is a shop coordinator. Riders may submit an inquiry if option B is
  chosen. A requested date is not an appointment or a repair-completion promise.
- Fixture fields: generated inquiry ID, synthetic rider label, bike type
  (`city`, `road`, `other`), problem description (1–240 nonblank characters),
  optional preferred-day text (up to 40 characters), status and creation order.
  No real contact details, payment, quote, inventory or external messages.
- New records are **Pending review**. The coordinator may move Pending review
  to **Accepted** or **Declined**. Accepted may become **Completed**. Completed
  and Declined are terminal. Acceptance means the shop agreed to take the job;
  it does not reserve a time or charge anything.
- Save records in an actual persistent store. Reload and app restart preserve
  the ID, values and status. Queue and receipt must use the same stored state.
- For a local staff-only prototype, the trusted coordinator operates the app.
  If any coordinator application is publicly reachable, including option A,
  protect coordinator actions on the server; a
  public form cannot change status or read the private full queue.

## Two scope options to compare

**A · Staff intake:** coordinator enters a walk-in inquiry, sees the queue and
updates it. Smaller interface and one operating role.

**B · Rider intake:** rider submits the same inquiry; coordinator reviews it in
the queue. Adds a separate public form and honest receipt. Any publicly reachable version must implement and test the coordinator's
permission boundary, including a hosted staff-intake version.

Both end at the same small workflow. Ask which fits the team's time and why;
do not add online booking or a customer portal. Stack, layout, fixture names,
error placement and any public/private implementation remain student proposals
until explicitly agreed. Unknown business questions stay Pending.

## Four stories to agree and make checkable

1. **Intake:** as the chosen intake user, create a valid inquiry and receive its
   ID marked Pending review. Blank problem, unsupported bike type and overlong
   input must create no record. A preferred day must never appear as confirmed.
2. **Review:** as coordinator, find the saved inquiry and its exact values in
   the queue. A new app instance using the same store must find the same record.
3. **Decision:** as coordinator, accept/decline a pending inquiry and complete
   an accepted one. A direct attempt to complete Pending review or edit a terminal
   status is rejected without changing the stored record. Apply the agreed
   permission boundary to direct requests if the app is publicly reachable.
4. **Handoff:** show the same status in queue and receipt/detail view, with a
   clear next step and no booking/payment claim. Repeat the end-to-end path on
   the chosen revision; keep expected/actual results and reproducible setup.

## One change · introduce only after the first working slice

“Could I mark a pending inquiry **Needs follow-up**, so I can find the questions
I still need to ask?” This is a boolean flag, **not another status** or automatic
message. If agreed: default false; coordinator can set/clear it only while Pending review. After
the request leaves Pending review, its saved flag remains visible but read-only.
It survives restart; list and detail agree; status rules stay unchanged.
Ask the team to estimate the effect on data, interface and checks. It may defer
with a reason. Do not introduce it during the protected finishing week.

## Final customer acceptance prompt

“Show me one city-bike inquiry from creation to Completed, a rejected attempt
to complete a pending inquiry, and what survives restarting the app. Then show
the follow-up flag if we agreed to implement it. What is still unverified?”

Ask for one demonstration at a time. Distinguish simulated customer agreement,
actual checks and a real peer's review. No fabricated client endorsement.
