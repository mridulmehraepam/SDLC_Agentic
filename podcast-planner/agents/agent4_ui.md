## AGENT 4 PROMPT — Frontend/UI Agent

### Context
You are Agent 4 of 5 in a linear pipeline.
Sections 1, 2, and 3 are already written in `shared/project_context.md`.

### Your Job
1. Open and read `shared/project_context.md` — review ALL sections carefully.
2. Design the complete React frontend component structure.

   Build a component plan for:
   - `EpisodeList` — shows all episodes in a table with status color badges, edit/delete/view actions
   - `EpisodeForm` — create and edit form with all Episode fields; status dropdown
   - `GuestManager` — list of all guests with an "Add Guest" modal
   - `AIPanel` — a right-side panel to trigger each AI endpoint and display results
   - `StatusBadge` — reusable badge component for Draft/Scheduled/Published/Archived

3. For each component describe:
   - Props interface (TypeScript)
   - Internal state (useState/useReducer)
   - Which API endpoints it calls (reference Section 2)
   - Which AI endpoints it uses (reference Section 3)
   - User flow step by step (e.g. "User clicks Generate Script → AIPanel calls POST /ai/generate-script → displays result in textarea")
   - Any important edge cases or loading/error states

### Output Instructions
- Open `shared/project_context.md`
- Append your output under this exact header:
  `## Section 4: UI Components & User Flows`
- Use TypeScript interfaces and numbered user flow steps.
- At the very end of your section, add this exact line:
  `<!-- AGENT_4_COMPLETE -->`
