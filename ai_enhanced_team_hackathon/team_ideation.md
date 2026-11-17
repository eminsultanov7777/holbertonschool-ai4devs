Team Ideation
1. Brainstormed Ideas
We considered the following ideas for a 24-hour AI-accelerated
hackathon:
1. AI Phishing Email Analyzer
   A web application that helps users assess suspicious emails by
   identifying warning signs, explaining potential risks, and providing
   safe next steps.
2. AI Study Planner
   A tool that turns a learner's goals, subjects, and available study
   time into a realistic weekly study plan.
3. AI Document Assistant
   A tool that summarizes uploaded or pasted documents, extracts key
   points, and answers questions about their content.
2. Chosen Idea
Project name: PhishGuard AI
Problem Statement
People often receive suspicious emails but may not know how to recognize
phishing attempts. These messages can imitate trusted organizations, use
urgent language, or contain suspicious links and requests for personal
information. Users need a simple way to understand the warning signs
before interacting with a potentially dangerous message.
Proposed Solution
PhishGuard AI is a lightweight web application that analyzes the text of
a suspicious email and gives the user an understandable risk assessment.
It highlights potentially suspicious language and indicators, explains
why they matter, and suggests safe actions.

The application is intended as an educational decision-support tool. It
does not guarantee that an email is safe or malicious, and users should
avoid opening suspicious links or attachments.
3. MVP Features
The minimum viable product will include these features:
1. Email text input
   Users can paste the content of a suspicious email into a text area.
2. AI-powered analysis
   The application sends the email text to an AI model with a
   structured prompt to identify common phishing indicators.
3. Risk assessment
   The result displays a simple risk level: Low, Medium, or High, with
   a short explanation.
4. Warning signs and recommendations
   The application lists detected warning signs, explains them in plain
   language, and provides safe next steps.
5. Analysis history for the current session
   Users can review the results generated during their current session.
4. Target Users
- People who want help evaluating unexpected or suspicious emails.
- Students learning about cybersecurity and phishing awareness.
- Small teams that need a simple educational tool for recognizing
  common email threats.
5. Proposed Technology and Architecture
The team will choose the final stack based on its existing experience
and the time available.
- Frontend: React or a simple HTML/CSS/JavaScript interface.
- Backend: Python with Flask or FastAPI, or Node.js.
- AI integration: An available LLM API with a carefully designed
  analysis prompt.
- Version control: Git and GitHub.
- Deployment: Vercel, Render, or another platform supported by the
  chosen stack.
High-Level Workflow
1. The user pastes an email into the application.
2. The frontend validates the input and sends it to the backend.
3. The backend submits the text to the AI service.
4. The AI returns a structured analysis.
5. The application displays the risk level, warning signs, explanation,
   and recommendations.
6. Team Roles
Replace the placeholders below with the actual names of the team members
before submission.
  Team Member             Role                    Main Responsibilities
  Member 1 --- \(Name\)   Project Lead & Product  Define priorities,
Coordinator             manage the 24-hour
timeline, coordinate
tasks, and keep the MVP
scope realistic.

  Member 2 --- \(Name\)   Frontend Developer      Build the user
interface, input form,
results view, and
responsive layout.

  Member 3 --- \(Name\)   Backend & AI            Implement the API,
Integration Developer   connect the AI model,
design the analysis
prompt, and handle
errors.
Member 4 --- \(Name\)   Testing, UX &           Test the main workflow,
Deployment Lead         improve usability,
document setup
instructions, and
coordinate deployment.
If the team has fewer than four members, responsibilities can be
combined. If it has more members, additional contributors can support
testing, design, documentation, or frontend/backend development.
7. Scope and 24-Hour Delivery Plan
  Phase                               Planned Work
  Hours 0--2                          Confirm requirements, agree on the
MVP, assign roles, and create the
repository.

  Hours 2--5                          Define the interface, API contract,
and AI response format.

  Hours 5--13                         Implement the frontend, backend,
and AI integration in parallel.

  Hours 13--17                        Integrate components and test the
complete user workflow.

  Hours 17--21                        Fix critical issues, improve the
interface, and prepare deployment.
Hours 21--24                        Deploy the demo, verify it, prepare
documentation, and rehearse the
presentation.
8. Success Criteria
The MVP will be considered successful if:
- A user can submit email text through the interface.
- The application returns an AI-generated analysis.
- The result includes a risk level, reasons, and practical
  recommendations.
- Invalid input and API errors are handled clearly.
- The application can be demonstrated through a live or locally
  running demo.
9. Risks and Limitations
- AI analysis may produce incorrect or incomplete assessments.
- External AI services may be unavailable or rate-limited.
- The team may need to simplify the interface to meet the deadline.
- The application must not present its assessment as a guarantee of
  email safety.
To reduce these risks, the team will keep the MVP focused, test with
sample emails, handle API failures, and clearly communicate that users
should verify suspicious messages independently.
10. Final Decision
The team selected PhishGuard AI because phishing is a practical
cybersecurity problem, the proposed solution has a clear target
audience, and its core workflow can be implemented and demonstrated
within a 24-hour hackathon. The project also provides a meaningful use
of AI through text analysis and explainable recommendations.
