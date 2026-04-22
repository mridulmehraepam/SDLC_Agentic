## AGENT 5 PROMPT — Sequence Diagram & Documentation Agent

### Context
You are Agent 5 of 5 — the final agent in the pipeline.
All 4 previous sections are written in `shared/project_context.md`.

### Your Job
1. Open and read ALL of `shared/project_context.md` carefully from top to bottom.
2. Generate TWO Mermaid.js sequence diagrams:

   Diagram A — "Create Episode Flow":
   Actor: User → EpisodeForm → POST /episodes API → Database → Response back to UI

   Diagram B — "AI Script Generation Flow":
   Actor: User → AIPanel → POST /ai/generate-script → LLM API → Response → AIPanel displays result

3. Write a Final Project Summary with these exact sections:
   - System Overview (2–3 sentences)
   - Architecture Decisions (why REST, why these data models)
   - AI Integration Approach (how prompts are structured, which LLM)
   - Frontend Architecture (component hierarchy)
   - How to Run the Project (setup steps, env vars needed)
   - Future Improvements (at least 3 ideas)

### Output Instructions
- Open `shared/project_context.md`
- Append your output under this exact header:
  `## Section 5: Sequence Diagrams & Final Documentation`
- Wrap ALL Mermaid diagrams in triple backtick mermaid code fences.
- At the very end of your section, add this exact line:
  `<!-- AGENT_5_COMPLETE -->`
- Then on the very last line of the entire file, add:
  `<!-- PIPELINE_COMPLETE -->`
