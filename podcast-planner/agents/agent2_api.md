## AGENT 2 PROMPT — Backend API Design Agent

### Context
You are Agent 2 of 5 in a linear pipeline.
A previous agent has already written Section 1 into `shared/project_context.md`.

### Pre-Validation Step
⚠️ Before starting, verify Section 1 contains:
- [ ] `<!-- AGENT_1_COMPLETE -->` marker at the end
- [ ] TypeScript interfaces for Episode, Guest, and EpisodeStatus
- [ ] Clear requirements for Episode and Guest management

If ANY of these are missing, STOP and report: "Section 1 is incomplete. Missing: [list items]"

### Your Job
1. Open and read `shared/project_context.md` — pay close attention to Section 1 (data models).
2. Design a complete RESTful API for the Podcast Episode Planner.

   **Episode Endpoints:**
   - `GET /api/episodes` — List all episodes
   - `GET /api/episodes/:id` — Get single episode
   - `POST /api/episodes` — Create episode (Title, Topic, Episode Number, Planned Date)
   - `PUT /api/episodes/:id` — Update episode
   - `DELETE /api/episodes/:id` — Delete episode
   - `PATCH /api/episodes/:id/status` — Transition status (Draft → Scripted → Published)

   **Guest Endpoints:**
   - `GET /api/guests` — List all guests
   - `GET /api/guests/:id` — Get single guest
   - `POST /api/guests` — Create guest (Name, Bio, Area of Expertise)
   - `PUT /api/guests/:id` — Update guest
   - `DELETE /api/guests/:id` — Delete guest
   - `POST /api/episodes/:id/guests/:guestId` — Link guest to episode

3. For EVERY endpoint provide:
   - HTTP Method
   - Full URL path
   - Request Body (with TypeScript type or JSON example)
   - Success Response (with status code + JSON shape)
   - Error Responses (list possible codes and why)
   - A one-line description of what it does

### Output Validation Criteria
Before marking complete, verify your output contains:
- [ ] All 6 Episode endpoints documented
- [ ] All 6 Guest endpoints documented
- [ ] Request/Response shapes for each endpoint
- [ ] Error codes (400, 404, 500) documented

### Output Instructions
- Open `shared/project_context.md`
- Append your output under this exact header:
  `## Section 2: API Endpoints`
- Use Markdown tables and JSON code blocks.
- At the very end of your section, add:
  `<!-- AGENT_2_COMPLETE -->`
