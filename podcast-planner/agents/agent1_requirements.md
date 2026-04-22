## AGENT 1 PROMPT — Requirements & Data Model Agent

### Context
You are Agent 1 of 5 in a linear pipeline. This is the first run — there is no prior context.
You are building a **Podcast Episode Planner & Script Assistant** — a web application that helps podcast creators plan their episodes, manage guests, and use AI to generate scripts, questions, and episode content.

### Your Job

#### 1. Define Functional Requirements

**Episode Management:**
- Create a new episode with: Title, Topic, Episode Number, and Planned Date
- View all episodes on a dashboard showing title, topic, and status
- Edit or delete an episode
- Episode status lifecycle: `Draft → Scripted → Published`

**Guest Management:**
- Add a guest with: Name, Bio, and Area of Expertise
- Link a guest to an episode
- Full CRUD operations for guests

**AI Features (Powered by EPAM AI DIAL):**
Implement these 2 AI features using DIAL API:
1. **Script Generator**: Topic + Guest Bio → DIAL generates a full interview script
2. **Question Bank**: Topic + Guest Expertise → DIAL generates 10 interview questions

#### 2. Define TypeScript Data Models

- `Episode`: id, title, topic, episodeNumber, plannedDate, guestId (string, optional), status (enum), aiScript (optional), aiQuestions (optional)
- `Guest`: id, name, bio, areaOfExpertise, episodeIds (string[])
- `EpisodeStatus`: enum with values `Draft | Scripted | Published`

#### 3. Define Non-Functional Requirements
- Response time < 2 seconds for CRUD operations
- AI generation timeout: 30 seconds max
- Support for modern browsers (Chrome, Firefox, Safari, Edge)

#### 4. For each model, explain every field: its type, purpose, and whether it is required.

### Output Validation Criteria
Before marking complete, verify your output contains:
- [ ] All Episode Management requirements listed
- [ ] All Guest Management requirements listed
- [ ] Both AI features clearly defined with inputs/outputs
- [ ] Complete TypeScript interfaces for Episode, Guest, and EpisodeStatus
- [ ] Field-by-field documentation for each model

### Output Instructions
- Open the file `shared/project_context.md`
- Append ALL your output under this exact header:
  `## Section 1: Requirements & Data Models`
- Use sub-headers, bullet points, and TypeScript code blocks.
- At the very end of your section, add this exact line:
  `<!-- AGENT_1_COMPLETE -->`
