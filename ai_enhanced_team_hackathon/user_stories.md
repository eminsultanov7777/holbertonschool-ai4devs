# User Stories — PhishGuard AI

## Product Overview

**PhishGuard AI** is a web application that helps users understand whether an email may contain phishing indicators. A user pastes email text, requests an analysis, and receives a risk level, detected warning signs, an explanation, and recommended safe actions.

These user stories describe the planned MVP. They are written from the perspective of the people who will use or maintain the product.

## User Stories

### US-01 — Submit an email for analysis
**As a** user,  
**I want** to paste the text of a suspicious email into the application,  
**so that** I can request an assessment without opening links or attachments.

**Acceptance criteria:**
- The page provides a clearly labelled text input.
- The user can submit non-empty email text.
- Empty submissions are rejected with a clear validation message.
- The application does not require the user to open any link in the submitted email.

### US-02 — Receive an AI-generated assessment
**As a** user,  
**I want** the application to analyze the submitted email,  
**so that** I can understand whether it contains common phishing indicators.

**Acceptance criteria:**
- Submitting valid text starts an analysis request.
- The interface indicates that analysis is in progress.
- A successful response is displayed to the user.
- If the AI service is unavailable, the application displays a useful error message rather than an empty result.

### US-03 — See an understandable risk level
**As a** user,  
**I want** to see a simple risk level,  
**so that** I can quickly understand the overall assessment.

**Acceptance criteria:**
- The result displays one of three levels: Low, Medium, or High.
- The risk level is accompanied by a short explanation.
- The interface explains that the result is an estimate, not a guarantee that an email is safe or malicious.

### US-04 — Review detected warning signs
**As a** user,  
**I want** to see the warning signs found in the email,  
**so that** I know which parts of the message may be suspicious.

**Acceptance criteria:**
- The result lists the warning signs identified by the analysis.
- Each warning sign includes a brief explanation.
- If no clear warning signs are identified, the application says so without claiming that the email is definitely safe.

### US-05 — Get safe next-step recommendations
**As a** user,  
**I want** practical recommendations based on the assessment,  
**so that** I know how to handle the email safely.

**Acceptance criteria:**
- The result includes at least one relevant recommendation.
- Recommendations advise users not to open suspicious links or attachments.
- Where appropriate, the application advises verifying requests through an official channel.

### US-06 — Review previous results in the current session
**As a** user,  
**I want** to review analyses I have completed during my current session,  
**so that** I can compare results without submitting the same text again.

**Acceptance criteria:**
- Completed analyses appear in a session history area.
- Each history item shows its risk level and submission time.
- Selecting an item displays its result.
- Session history is temporary and is not presented as permanent account storage.

### US-07 — Understand input and service errors
**As a** user,  
**I want** clear messages when my input is invalid or a service fails,  
**so that** I can correct the issue or try again.

**Acceptance criteria:**
- Empty or whitespace-only input is rejected.
- Text exceeding the configured input limit is rejected with an explanation.
- API or AI-service failures produce a clear error state.
- The user can retry after a temporary failure.

### US-08 — Use the application on different screen sizes
**As a** user,  
**I want** the application to work on desktop and mobile screens,  
**so that** I can use it on the device available to me.

**Acceptance criteria:**
- The input, submit action, and results remain usable on narrow screens.
- Text is readable without horizontal scrolling.
- Interactive controls have clear labels and visible focus states.

### US-09 — Understand the limitations of AI analysis
**As a** user,  
**I want** to see a clear notice about the limitations of AI-generated assessments,  
**so that** I do not treat the result as a definitive security verdict.

**Acceptance criteria:**
- A disclaimer is visible near the result or analysis form.
- The disclaimer states that AI can make mistakes.
- The application advises users to verify suspicious messages independently.

### US-10 — Protect submitted email content
**As a** user,  
**I want** my submitted email text to be handled carefully,  
**so that** I do not expose sensitive information unnecessarily.

**Acceptance criteria:**
- The application does not ask for passwords or account credentials.
- The MVP does not store submitted email content in a permanent database by default.
- Secrets and API keys are kept on the server and are not exposed in frontend code.
- The application communicates if any third-party AI service processes submitted text.

## MVP Priority

| Priority | User stories | Reason |
|---|---|---|
| Must have | US-01, US-02, US-03, US-04, US-05, US-07 | These deliver the core analysis workflow. |
| Should have | US-06, US-09, US-10 | These improve usability, transparency, and privacy. |
| Could have | US-08 | Responsive behavior should be implemented where time allows and verified before the demo. |

## Definition of Done

A user story is considered complete when its acceptance criteria have been checked, the implementation has been reviewed by the team, and the relevant workflow has been tested. The MVP is ready for demonstration when a user can submit sample email text and receive a clearly explained assessment with safe recommendations.
