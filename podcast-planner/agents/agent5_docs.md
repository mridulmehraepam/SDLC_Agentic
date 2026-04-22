## AGENT 5 PROMPT — Sequence Diagram & Documentation Agent

### Context
You are Agent 5 of 5 — the final agent in the pipeline.
All 4 previous sections are written in `shared/project_context.md`.

### Pre-Validation Step
⚠️ Before starting, verify ALL completion markers exist:
- [ ] `<!-- AGENT_1_COMPLETE -->`
- [ ] `<!-- AGENT_2_COMPLETE -->`
- [ ] `<!-- AGENT_3_COMPLETE -->`
- [ ] `<!-- AGENT_4_COMPLETE -->`

If ANY marker is missing, STOP and report: "Pipeline incomplete. Missing sections: [list]"

### Your Job
1. Open and read ALL of `shared/project_context.md` carefully from top to bottom.

2. Generate THREE Mermaid.js sequence diagrams:

   **Diagram A — "Create Episode Flow":**
   ```
   User → Dashboard → EpisodeForm → POST /api/episodes → Database → Response → Dashboard (updated)
   ```

   **Diagram B — "AI Script Generation Flow":**
   ```
   User → EpisodeForm → AIPanel → POST /api/ai/generate-script → EPAM AI DIAL → Response → AIPanel displays script
   ```

   **Diagram C — "Link Guest to Episode Flow":**
   ```
   User → EpisodeForm → Guest Dropdown → POST /api/episodes/:id/guests/:guestId → Database → Response → Form updated
   ```

3. Write a Final Project Summary with these exact sections:
   - **System Overview** (2–3 sentences describing the Podcast Episode Planner)
   - **Architecture Decisions** (why REST, why these data models, tech stack)
   - **AI Integration Approach** (EPAM AI DIAL, how prompts are structured)
   - **Frontend Architecture** (React component hierarchy from Section 4)
   - **How to Run the Project**:
     - Prerequisites (Node.js, npm)
     - Environment variables needed (DIAL_API_KEY, DIAL_API_URL)
     - Setup steps (npm install, npm run dev)
   - **Future Improvements** (at least 3 ideas beyond the 2 implemented AI features)

### Output Validation Criteria
Before marking complete, verify your output contains:
- [ ] All 3 Mermaid diagrams render correctly (valid syntax)
- [ ] System Overview accurately describes the application
- [ ] EPAM AI DIAL mentioned in AI Integration section
- [ ] Environment variables for DIAL documented
- [ ] At least 3 future improvement ideas listed

### Output Instructions
- Open `shared/project_context.md`
- Append your output under this exact header:
  `## Section 5: Sequence Diagrams & Final Documentation`
- Wrap ALL Mermaid diagrams in triple backtick mermaid code fences.
- At the very end of your section, add this exact line:
  `<!-- AGENT_5_COMPLETE -->`
- Then on the very last line of the entire file, add:
  `<!-- PIPELINE_COMPLETE -->`
