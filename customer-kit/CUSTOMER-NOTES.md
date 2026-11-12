
# Bench & Bolt — Customer Notes

## Customer
Maya Chen, fictional owner of Bench & Bolt, a neighborhood bike-repair shop.

## Customer Problem
Repair inquiries currently arrive through handwritten notes and messages. The shop needs one organized queue to track repair requests and their statuses.

## Scope Comparison

### Option A — Staff Intake
A coordinator enters walk-in repair inquiries, reviews the queue, and updates request statuses.

### Option B — Rider Intake
Riders submit repair inquiries online, and the coordinator reviews them.

### Selected Option: A — Staff Intake
Our team selected Option A because we prefer its simpler workflow and smaller interface.

Both team members agreed to the Bench & Bolt scenario. The fictional customer agreed to Option A during our simulated interview.

## Four Agreed User Stories

1. Intake: Staff can create a repair inquiry and receive a unique ID with the status Pending review.

2. Review: Staff can view saved inquiries and their information in one queue, including after restarting the application.

3. Decision: Staff can accept or decline pending requests and mark accepted repairs as Completed. Invalid status changes must be rejected.

4. Handoff: Staff can see the same saved status in the queue and request detail view. The confirmation must not promise an appointment.

## Required Data
- Generated inquiry ID
- Fictional rider label
- Bike type: city, road, or other
- Problem description: 1–240 nonblank characters
- Optional preferred day: maximum 40 characters
- Current status
- Creation order

## Status Rules
Pending review -> Accepted
Pending review -> Declined
Accepted -> Completed

Completed and Declined are final statuses.

A Pending review request cannot go directly to Completed.

## Validation Rules
- Reject blank problem descriptions.
- Reject unsupported bike types.
- Reject descriptions longer than 240 characters.
- Reject preferred-day text longer than 40 characters.
- Invalid requests must not be saved.

## Persistence
Repair inquiries must remain saved after the application closes and restarts.

The queue and detail view must show the same stored information.

## Project Boundaries
- No online booking
- No payments
- No real customer information
- No automated messages
- No customer portal

The first version is planned as a local application for trusted shop staff. A publicly accessible coordinator application would require server-side authentication and authorization.

## Proposed Technology
- Python
- Flask
- SQLite
- HTML/CSS
- pytest

## Planned Architecture
Staff -> Flask application -> SQLite database

Flask will handle validation and workflow rules. SQLite will store repair inquiries and their statuses.

## Design Experiment
Compare simple conditional status checks with centralized state-transition rules.

We will evaluate which approach is easier to understand, test, and maintain.

Status: Planned, not tested.

## Team Responsibilities

### Member 1
- Initial project setup
- Customer interview and planning
- Intake form and validation
- Intake tests
- Review Member 2's status and queue work

### Member 2
- Review and revise project plan
- Repair queue and status updates
- Persistence and status tests
- Review Member 1's intake work

Responsibilities are proposed and still need both teammates' confirmation.

## Customer Change Request
Not requested yet. The change request will be discussed after the first working application slice.

## Current Evidence
- Scenario selected: Bench & Bolt
- Scope selected: Option A
- Simulated customer agreement: Completed
- Partner agreement on scenario: Confirmed
- Detailed partner review: Pending
- Application implementation: Not started
- Automated tests: Not run
- Real peer testing: Not completed

## Next Steps
1. Confirm team responsibilities.
2. Review the project plan with the partner.
3. Begin the first working application slice.
4. Test valid and invalid repair requests.
5. Record real peer feedback in GitHub.

