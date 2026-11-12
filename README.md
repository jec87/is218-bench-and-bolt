
# Bench & Bolt — Repair Inquiry Queue

## IS218-003 — Group Customer Studio
Review 1: Plan

## Customer
Bench & Bolt is a fictional neighborhood
bicycle repair shop owned by Maya Chen.

The shop needs one place to organize
repair inquiries and track their statuses.

## Scope Comparison

### Option A — Staff Intake
A coordinator enters walk-in repair
inquiries and manages them in one queue.

### Option B — Rider Intake
Riders submit inquiries online.
A coordinator reviews them in the queue.

### Selected Scope: Option A
Our team chose staff intake because
we prefer the simpler workflow.

The simulated customer approved this scope.

## Four Agreed User Stories

1. Intake:
Staff can submit a valid repair inquiry.
The system generates an ID and starts
the request as Pending review.

2. Review:
Staff can view saved repair inquiries
in a queue, including their details
and current statuses.

3. Decision:
Staff can accept or decline pending
inquiries and complete accepted ones.
Invalid status changes are rejected.

4. Confirmation:
Staff can see the request ID and
Pending review status after submission.
Queue and detail views stay consistent.

## Data Rules
- Generated inquiry ID
- Synthetic rider label
- Bike type: city, road, other
- Problem description: 1-240 characters
- Optional preferred day: max 40 characters
- Status
- Creation order

## Status Workflow

Pending review -> Accepted -> Completed

Pending review -> Declined

Completed and Declined are final statuses.

A request cannot go directly from
Pending review to Completed.

## Validation Rules
- Reject blank problem descriptions
- Reject unsupported bike types
- Reject descriptions over 240 characters
- Reject preferred-day text over 40 characters
- Invalid requests must not be saved

## Persistence
All records must remain saved after
the application closes and restarts.

Queue and detail views must display
the same stored information.

## Proposed Architecture

Browser (HTML/CSS)
       |
       v
Flask Application
       |
       v
SQLite Database

The application will run locally for
trusted repair shop staff.

If deployed publicly, coordinator actions
must be protected by server-side
authentication and authorization.

## Proposed Technology
- Python
- Flask
- SQLite
- HTML/CSS
- pytest

## Planned Tests
1. Valid inquiry creates a saved record.
2. Blank problem creates no record.
3. Unsupported bike type is rejected.
4. Overlong input is rejected.
5. Pending review can become Accepted.
6. Pending review can become Declined.
7. Accepted can become Completed.
8. Pending review cannot become Completed.
9. Completed and Declined cannot change.
10. Records survive application restart.
11. Queue and detail views agree on status.

Tests have not been run.

## Design Experiment
Compare two ways to implement
status transitions:

A: Simple conditional checks

B: Centralized state-transition rules

We will compare clarity, invalid-transition
handling, and testability.

Experiment status: Planned.

## Team Responsibilities

Member 1:
- Initial repository and project plan
- Customer interview and scope notes
- Proposed intake form and validation
- Planned intake tests
- Review partner's queue/status work

Member 2:
- Review and revise the project plan
- Proposed queue and status management
- Planned persistence/status tests
- Review Member 1's intake work

Both:
- Agree on final responsibilities
- Cross-review each other's work
- Document real feedback in GitHub
- Integrate and test the full workflow

Assignments remain proposed until
both teammates confirm them.

## Customer Agreement
See [CUSTOMER-NOTES.md](customer-kit/CUSTOMER-NOTES.md).

Customer agreement: Confirmed in simulation.
Partner review of detailed plan: Pending.

## Current Checks
- Scope selected: Yes
- Customer interview: Completed in simulation
- Customer notes: Saved locally
- Partner cross-review: Pending
- Application implementation: Not started
- Automated tests: Not run

## Next
- Confirm team responsibilities
- Commit the customer notes and README
- Record real partner feedback
- Begin the first working application slice
