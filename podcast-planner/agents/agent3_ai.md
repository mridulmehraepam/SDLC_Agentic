## AGENT 3 PROMPT — AI Integration Agent

### Context
You are Agent 3 of 5 in a linear pipeline.
Sections 1 and 2 are already written in `shared/project_context.md`.

### Your Job
1. Open and read `shared/project_context.md` — review Sections 1 and 2 carefully.
2. Design 3 AI-powered API endpoints that plug into the existing API design:

   - `POST /ai/generate-script`
     Input: episode title + guest bio
     Output: a full episode script

   - `POST /ai/generate-questions`
     Input: guest bio + episode topic
     Output: list of 10 interview questions

   - `POST /ai/generate-shownotes`
     Input: episode title + raw transcript or summary
     Output: formatted show notes with timestamps

3. For each endpoint define:
   - Full request/response contract (TypeScript interfaces)
   - The exact prompt template sent to the LLM (use `{{variable}}` placeholders)
   - Which LLM to use (OpenAI GPT-4 or Anthropic Claude)
   - Error handling (what if the LLM fails or returns bad output?)
   - Estimated token cost per call

### Output Instructions
- Open `shared/project_context.md`
- Append your output under:
  `## Section 3: AI Integration`
- Use TypeScript code blocks for contracts and plain text for prompt templates.
- At the very end of your section, add:
  `<!-- AGENT_3_COMPLETE -->`
