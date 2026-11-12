
# Bench & Bolt — Repair Shop

IS218-003 — Review 1: Plan — Group Customer Studio

## Customer
Bench & Bolt, a repair shop.

## Project Goal
Create a simple web application that helps
staff record and track repair requests.

## Scope Comparison

### Option A: Walk-In Intake Queue
Staff enter repair requests and manage
their progress through a queue.

### Option B: Self-Service Inquiry
Customers submit inquiries online.
Staff review inquiries before accepting them.

## Proposed Decision
Option A: Walk-In Intake Queue

Reason: This option has a smaller workflow
and is easier to test for our first project.

Status: Awaiting customer-kit confirmation
and agreement with my teammate.

## Proposed User Stories
1. As staff, I want to create a repair request.
2. As staff, I want to see all open requests.
3. As a technician, I want to update a status.
4. As staff, I want to search for a request.
5. As staff, I want to close a completed request.

## Proposed Data
- Request ID
- Customer name
- Contact information
- Item needing repair
- Problem description
- Request status
- Date submitted

## Proposed Statuses
New -> In Progress -> Ready -> Closed

Status rules still need customer confirmation.

## Proposed Workflow
1. Customer arrives with an item.
2. Staff create a repair request.
3. Technician reviews the request.
4. Technician updates its status.
5. Staff close the completed request.

## Proposed Technology
- Python
- Flask
- SQLite
- HTML/CSS
- pytest

## Team Responsibilities

Member 1 (me):
- Initial scope comparison
- Draft user stories
- Draft data and workflow rules
- Create project repository

Member 2 (partner):
- Review and revise project scope
- Review user stories and workflow
- Contribute design, development,
  or QA planning

Both members:
- Cross-review each other's work
- Record feedback in GitHub issues
- Agree on the final plan

## Checks
- Initial plan drafted
- Customer-kit confirmation: Not done
- Partner review: Not done
- Application tests: Not run

## Next
Confirm requirements with the customer kit,
ask my partner to review the plan, and
record our final decisions.
