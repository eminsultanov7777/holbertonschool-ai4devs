# User Stories - SOC Incident Tracker

## Overview

These user stories describe the first version of SOC Incident Tracker. The MVP is intended for small IT and security teams and focuses on manually recording, prioritizing, reviewing, and resolving security incidents.

## User Story 1 - Create an Incident

As a SOC analyst, I want to submit a new incident with a title, description, source, and date so that a security event can be recorded in one place.

**Acceptance criteria:**
- The incident form includes title, description, source, and date fields.
- Required fields are validated before submission.
- A successfully submitted incident appears in the incident list.

## User Story 2 - Categorize an Incident

As a SOC analyst, I want to select an incident category so that incidents can be classified consistently.

**Acceptance criteria:**
- The category can be selected from phishing, malware, suspicious login, or network activity.
- The selected category is saved with the incident.
- The category is visible in the incident details and list.

## User Story 3 - Set Incident Priority

As a SOC analyst, I want to assign a priority of Low, Medium, High, or Critical so that urgent incidents are easy to identify.

**Acceptance criteria:**
- The priority field offers Low, Medium, High, and Critical.
- Each incident has one priority value.
- The priority is visible in the incident list.

## User Story 4 - View All Incidents

As a team member, I want to see all recorded incidents in a dashboard so that I can review the team's current workload.

**Acceptance criteria:**
- The dashboard displays recorded incidents in a table or card list.
- Each item shows its title, category, priority, date, and status.
- An empty-state message is shown when no incidents have been recorded.

## User Story 5 - Filter Incidents

As a team member, I want to filter incidents by priority and status so that I can focus on the incidents that need attention.

**Acceptance criteria:**
- A priority filter is available.
- A status filter is available.
- The list updates to show incidents matching the selected filters.
- The user can clear filters and return to the full list.

## User Story 6 - Update Incident Status

As a SOC analyst, I want to change an incident's status so that the team can track investigation progress.

**Acceptance criteria:**
- The available statuses are New, In Progress, Resolved, and Closed.
- A user can update the status of an existing incident.
- The updated status is shown in the dashboard.

## User Story 7 - Add Investigation Notes

As a SOC analyst, I want to add notes to an incident so that investigation findings and actions are documented.

**Acceptance criteria:**
- A user can add a text note to an existing incident.
- Each note is associated with its incident.
- Each note displays its creation date and time.

## User Story 8 - View Incident Summary

As a team member, I want to see summary counts by priority and status so that I can quickly understand the current incident situation.

**Acceptance criteria:**
- The dashboard displays incident counts grouped by priority.
- The dashboard displays incident counts grouped by status.
- Counts update when incidents are created or their priority/status changes.

## User Story 9 - Validate Incident Input

As a user, I want clear validation and error messages when I submit incomplete or invalid incident information so that I can correct the information before saving.

**Acceptance criteria:**
- Required fields are checked before saving.
- Invalid submissions are not saved.
- Clear messages identify fields that need correction.

## User Story 10 - Review an Incident's Details

As a team member, I want to open an incident and view its full details and investigation notes so that I can understand what happened and what actions have been taken.

**Acceptance criteria:**
- The detail view shows the incident description, source, date, category, priority, and status.
- All notes associated with the incident are displayed.
- The user can return to the incident dashboard.

## MVP Scope Notes

- The first version does not include user authentication or role-based access control.
- Incidents are entered manually; automated SIEM ingestion is not included.
- Email, SMS, and push notifications are outside the MVP scope.
