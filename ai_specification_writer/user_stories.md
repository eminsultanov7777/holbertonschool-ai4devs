[user_stories.md](https://github.com/user-attachments/files/34869624/user_stories.md)
# SOC Assistant -- User Stories

This document defines user stories and acceptance criteria for the SOC
Assistant platform. Priorities indicate the importance of each
capability for the initial product scope and later releases.

### User Story 1: View Security Alerts

As a **SOC Analyst**, I want to view security alerts in one centralized
dashboard so that I can understand current security activity without
switching between multiple tools.

**Acceptance Criteria:** - The dashboard displays each alert's title,
source, timestamp, severity, and status. - Alerts are presented in a
readable list or table. - The analyst can open an alert to view its
details.

**Priority**: MVP

### User Story 2: Filter and Prioritize Alerts

As a **SOC Analyst**, I want to filter and sort alerts by severity,
source, date, and status so that I can focus on events that need
attention first.

**Acceptance Criteria:** - The analyst can filter alerts by severity and
status. - The analyst can sort alerts by timestamp and severity. - The
dashboard displays only alerts matching the selected filters.

**Priority**: MVP

### User Story 3: Create an Incident

As a **SOC Analyst**, I want to create an incident from a security alert
so that related security events can be investigated and tracked in one
place.

**Acceptance Criteria:** - The analyst can create an incident from an
alert. - The incident stores a title, description, severity, creation
time, and linked alert. - The system assigns the incident a unique
identifier.

**Priority**: MVP

### User Story 4: Track Incident Status

As a **SOC Analyst**, I want to update an incident's status so that the
team can understand its investigation progress.

**Acceptance Criteria:** - The analyst can set a status to New,
Investigating, Escalated, Resolved, or Closed. - The current status is
visible in the incident list and details. - The system records when the
status was last updated.

**Priority**: MVP

### User Story 5: Add Investigation Notes and Evidence

As a **SOC Analyst**, I want to add investigation notes and evidence
references to an incident so that the investigation history and findings
are documented.

**Acceptance Criteria:** - The analyst can add timestamped notes to an
incident. - The analyst can attach or reference evidence, such as a file
name, URL, or log reference. - Notes and evidence references remain
visible in the incident record.

**Priority**: MVP

### User Story 6: Assign Incidents to Analysts

As a **SOC Team Lead**, I want to assign incidents to team members so
that investigation responsibilities are clear and work can be
distributed.

**Acceptance Criteria:** - The team lead can assign an incident to a
team member. - The assigned analyst is displayed in the incident
details. - The system records assignment changes.

**Priority**: High

### User Story 7: Collaborate on an Investigation

As a **SOC Analyst**, I want to add internal comments and hand over an
incident to another analyst so that team members can collaborate without
losing investigation context.

**Acceptance Criteria:** - Authorized team members can add comments to
an incident. - Comments display the author and creation time. - An
analyst can record a handoff note when transferring an incident.

**Priority**: High

### User Story 8: Use Incident Response Playbooks

As a **Junior SOC Analyst**, I want to follow step-by-step response
playbooks so that I can handle common incident types consistently.

**Acceptance Criteria:** - The system provides playbooks for common
incident types. - Each playbook displays ordered investigation or
response checklist steps. - The analyst can mark individual steps as
completed for an incident.

**Priority**: High

### User Story 9: Map Findings to MITRE ATT&CK

As a **SOC Analyst**, I want to associate investigation findings with
MITRE ATT&CK tactics and techniques so that I can describe observed
attacker behavior using a recognized framework.

**Acceptance Criteria:** - The analyst can search for and select a MITRE
ATT&CK tactic or technique. - Selected mappings are displayed in the
incident record. - The analyst can remove or update a mapping.

**Priority**: Medium

### User Story 10: Review Incident Metrics

As a **SOC Team Lead**, I want to view basic incident and workload
reports so that I can monitor team activity and identify operational
trends.

**Acceptance Criteria:** - The dashboard displays incident counts
grouped by status and severity. - Reports include basic response-time
information when the required timestamps are available. - The team lead
can select a date range for a report.

**Priority**: Medium

### User Story 11: Generate AI-Assisted Alert Summaries

As a **SOC Analyst**, I want AI to summarize alert information and
suggest investigation steps so that I can understand relevant context
more quickly.

**Acceptance Criteria:** - The analyst can request a summary for an
alert or incident. - The summary is based on available record
information and identifies missing context. - AI suggestions are clearly
labeled and require analyst review; no response action is performed
automatically.

**Priority**: Medium

### User Story 12: Manage Access to Incident Information

As a **SOC Team Lead**, I want access to incident information to be
limited to authorized team members so that security investigation data
is protected.

**Acceptance Criteria:** - Users must authenticate before accessing the
platform. - Users can access only features and records permitted by
their assigned role. - Unauthorized access attempts are denied.

**Priority**: MVP
