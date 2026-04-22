## AGENT 2 PROMPT — Backend API Design Agent

### Context
You are Agent 2 of 5 in a linear pipeline.
A previous agent has already written Section 1 into `shared/project_context.md`.

### Your Job
1. Open and read `shared/project_context.md` — pay close attention to Section 1 (data models).
2. Design a complete RESTful API for the Podcast Management System.

   Cover these resources:
   - Episodes: full CRUD
   - Guests: full CRUD
   - Status transitions: a dedicated PATCH endpoint to change episode status

3. For EVERY endpoint provide:
   - HTTP Method
   - Full URL path
   - Request Body (with TypeScript type or JSON example)
   - Success Response (with status code + JSON shape)
   - Error Responses (list possible codes and why)
   - A one-line description of what it does

### Output Instructions
- Open `shared/project_context.md`
- Append your output under this exact header:
  `## Section 2: API Endpoints`
- Use Markdown tables and JSON code blocks.
- At the very end of your section, add:
  `<!-- AGENT_2_COMPLETE -->`
