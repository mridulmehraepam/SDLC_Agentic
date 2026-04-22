## AGENT 1 PROMPT — Requirements & Data Model Agent

### Context
You are Agent 1 of 5 in a linear pipeline. This is the first run — there is no prior context.
You are building a **Podcast Management System**.

### Your Job
1. Define clear functional and non-functional requirements for the system.
   - The system manages podcast episodes and guests.
   - It supports AI-generated scripts, interview questions, and show notes.
   - It tracks episode status through a lifecycle.

2. Define the following TypeScript data models:
   - `Episode`: id, title, description, guestIds (string[]), status (enum), publishDate, aiScript (optional)
   - `Guest`: id, name, bio, socialLinks (object), episodeIds (string[])
   - `Status`: enum with values Draft | Scheduled | Published | Archived

3. For each model, explain every field: its type, purpose, and whether it is required.

### Output Instructions
- Open the file `shared/project_context.md`
- Append ALL your output under this exact header:
  `## Section 1: Requirements & Data Models`
- Use sub-headers, bullet points, and TypeScript code blocks.
- At the very end of your section, add this exact line:
  `<!-- AGENT_1_COMPLETE -->`
