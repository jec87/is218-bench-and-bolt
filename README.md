
# Bench & Bolt — Repair Shop

## IS218-003 — Group Customer Studio

### Customer
Bench & Bolt, a repair shop.

### Project Goal
Plan a simple web application to help
repair shop employees manage repair requests.

### Comparing Two Scopes

Option A: Walk-In Intake Queue
- Employees enter repair requests.
- Staff track the status of each repair.
- Staff can view active requests.

Option B: Self-Service Inquiry
- Customers submit inquiries online.
- Staff review the inquiries.
- Staff decide which requests to accept.

### Proposed Decision
Option A: Walk-In Intake Queue

We chose this as our starting proposal because
it has a smaller workflow and is easier to test.

Final decision pending partner review and
customer-kit confirmation.

### Five Proposed User Stories
1. As staff, I want to create repair requests.
2. As staff, I want to view pending repairs.
3. As a technician, I want to update statuses.
4. As staff, I want to search for requests.
5. As staff, I want to close finished requests.

### Proposed Data
- Repair ID
- Customer name
- Contact information
- Item description
- Repair problem
- Status
- Date submitted

### Proposed Status Rules
New -> In Progress -> Ready -> Closed

Exact status rules need customer confirmation.

### Proposed Workflow
1. Customer brings in an item.
2. Employee records the repair request.
3. Technician reviews the request.
4. Technician updates its status.
5. Employee closes the completed repair.

### Planned Technology
- Python and Flask
- SQLite
- HTML and CSS
- pytest

### Team Contributions

Member 1:
- Create GitHub repository
- Draft project scope
- Draft user stories and workflow

Member 2:
- Review the project plan
- Suggest improvements
- Help confirm final requirements

Both:
- Review each other's work
- Document feedback on GitHub

### Checks
- Initial plan: Drafted
- Customer-kit verification: Not completed
- Partner review: Not completed
- Application tests: Not run

### Next Steps
- Confirm customer requirements
- Review the plan with my partner
- Record feedback and final decisions
