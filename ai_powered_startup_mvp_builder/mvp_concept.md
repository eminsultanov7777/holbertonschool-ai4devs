[mvp_concept.md](https://github.com/user-attachments/files/34922399/mvp_concept.md)
# MVP Concept - SOC Incident Tracker

## Problem Statement

Small IT and security teams often receive security alerts from different sources but lack a simple, centralized place to record, prioritize, and track incidents.

As a result, important alerts can be overlooked, incident status may be unclear, and team members may have difficulty coordinating their response.

SOC Incident Tracker is a lightweight web application that helps a small security team register security incidents, assign priorities, track their status, and keep basic investigation notes in one place.

## Target Users

- Junior SOC analysts who need a simple way to organize security incidents.
- Small IT and cybersecurity teams without a dedicated incident management platform.
- IT administrators who need to record and follow up on suspicious activity.

## Core Features

1. **Incident Submission**
   - Create an incident with a title, description, source, and date.
   - Select an incident category, such as phishing, malware, suspicious login, or network activity.

2. **Priority Classification**
   - Assign a priority level: Low, Medium, High, or Critical.
   - Display priority clearly so urgent incidents are easy to identify.

3. **Incident Status Tracking**
   - Track each incident as New, In Progress, Resolved, or Closed.
   - Allow users to update the status as an investigation progresses.

4. **Incident Dashboard**
   - Display all recorded incidents in a table or card list.
   - Show summary counts by priority and status.
   - Allow users to filter incidents by priority and status.

5. **Investigation Notes**
   - Add short notes to an incident to record findings and actions taken.
   - Display notes with their creation dates.

## Constraints

- The MVP is designed for a small team and a limited number of incidents.
- No authentication or role-based access control in the first version.
- No automatic integration with SIEM tools such as Wazuh or Splunk.
- Incidents are entered manually; automatic alert ingestion is out of scope.
- No email, SMS, or push notifications.
- No advanced analytics, reporting, or threat-intelligence enrichment.
- The first version focuses on the core workflow: create, prioritize, review, update, and resolve incidents.
