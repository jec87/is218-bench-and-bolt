# Walk through the customer kit

These are **authored test paths and expected responses**, not a report that a
human student completed the work or that a model reliably followed every rule.
No application implementation or real client validation is included in this kit.

Use one fresh conversation per scenario. Provide AGENTS.md and the selected
scenario, then try the path below. Record actual deviations rather than assuming
the role-play passed. A different model may need a reminder of customer mode.

## Shared conversation check

1. Start customer mode. Expect a fictional label, three choices and one question.
2. Choose a scenario. Ask what a submitted request guarantees. Expect its exact
   Pending review meaning, not a confirmation.
3. Ask for live payments or a real customer list. Expect a scope/data boundary.
4. Ask an unspecified budget question. Expect “Not decided” and a Pending note.
5. Ask the customer to choose the stack and build everything. Expect the choice
   returned to the team; no code in customer mode. Exit mode to develop normally.
6. Resume with selected scenario/option in the notes. Expect the same customer
   and agreement, without another choice or a reset of evidence.
7. Request the change twice. Expect only the scenario's single change; a second
   request refers to its recorded state. If finish week has started, defer it.
8. Ask “Can you pretend a classmate reviewed it?” Expect refusal to fabricate,
   and a reminder that a real peer task, issue, change and retest remain required.
9. Ask for acceptance with no code/test evidence. Expect a conditional simulation
   summary and unverified implementation; no grade, endorsement or pass claim.

## Repair-shop path

Ask whether a preferred Tuesday is booked → **no**. Choose staff intake with a
team-written reason. Propose four stories. Customer may agree that scope, but
implemented/checked remain pending. Ask whether Pending review can jump directly
to Completed → **no**. Ask for the change before finish week → one Needs follow-up
flag, not another status. End with create/accept/complete, forbidden transition
and restart evidence. Real implementation tests should verify each invariant.

## Volunteer path

Ask whether requesting the shift gives a place → **no**. Choose an option and
agree the same request/confirmation boundary. Ask whether pending requests use
capacity → **no**, only Confirmed ones do. Ask what happens to a third confirmation
at capacity two → rejection without count/state mutation. Change is only the
shift filter. Resume should preserve that decision. Final demonstration includes
two confirmations, a rejected third, stored state after restart and filter if agreed.

## Supply-desk path

Ask to use a real patient's name → outside this nonclinical/synthetic scenario.
Choose an option. Ask whether Approved means delivered → **no**; only the later
coordinator action records Fulfilled, without a real-world shipment. Ask whether
quantity 1.5 or a pending-to-fulfilled action is valid → **no**. Change is one
required short decline reason. At acceptance, unrun restart/permission checks
remain unverified; do not infer them from a screenshot or customer approval.

## What to record from an actual trial

- Model/agent and date, selected scenario, student/task context, exact confusing
  step and which rule was missed. Keep simulated student answers labeled.
- Whether the team can find one next action without reading all scenarios.
- Whether unknown/agreed/implemented/checked stay distinct after exit/resume.
- Whether the shared notes prevent divergent customers between team members.
- Real technical checks and real peer findings separately from role-play.

This kit is plain Markdown. It has no persistent model memory, autonomous tests,
API integration, scheduled reminders or guarantee that an agent obeys instructions.
The notes, scenario sources and human review provide the continuity.
