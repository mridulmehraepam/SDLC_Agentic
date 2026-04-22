## AGENT 4 PROMPT — Frontend/UI Agent

### Context
You are Agent 4 of 5 in a linear pipeline.
Sections 1, 2, and 3 are already written in `shared/project_context.md`.

### Pre-Validation Step
⚠️ Before starting, verify:
- [ ] `<!-- AGENT_1_COMPLETE -->` marker exists
- [ ] `<!-- AGENT_2_COMPLETE -->` marker exists
- [ ] `<!-- AGENT_3_COMPLETE -->` marker exists
- [ ] Data models, API endpoints, and AI endpoints are all documented

If ANY of these are missing, STOP and report: "Previous sections incomplete. Missing: [list items]"

### Your Job
1. Open and read `shared/project_context.md` — review ALL sections carefully.
2. Design the complete React frontend component structure.

   **Core Components:**
   - `Dashboard` — main view showing all episodes with title, topic, and status
   - `EpisodeList` — table of episodes with status color badges, edit/delete/view actions
   - `EpisodeForm` — create/edit form with: Title, Topic, Episode Number, Planned Date, Guest dropdown
   - `GuestManager` — list of all guests with "Add Guest" modal (Name, Bio, Area of Expertise)
   - `GuestForm` — form for adding/editing guests
   - `AIPanel` — panel to trigger AI features:
     - "Generate Script" button → calls `/api/ai/generate-script`
     - "Generate Questions" button → calls `/api/ai/generate-questions`
   - `StatusBadge` — reusable badge for Draft (gray) / Scripted (blue) / Published (green)

3. For each component describe:
   - Props interface (TypeScript)
   - Internal state (useState/useReducer)
   - Which API endpoints it calls (reference Section 2)
   - Which AI endpoints it uses (reference Section 3)
   - User flow step by step
   - Loading states (spinner while AI generates)
   - Error states (toast notifications for failures)

4. Define these specific user flows:
   - **Create Episode Flow**: Dashboard → "New Episode" → EpisodeForm → Save → Dashboard
   - **Generate Script Flow**: EpisodeForm → AIPanel → "Generate Script" → Loading → Display result
   - **Link Guest Flow**: EpisodeForm → Guest dropdown → Select guest → Save

### Output Validation Criteria
Before marking complete, verify your output contains:
- [ ] All 7 components documented with props interfaces
- [ ] State management approach defined for each component
- [ ] API endpoint references match Section 2
- [ ] AI endpoint references match Section 3
- [ ] All 3 user flows documented step-by-step
- [ ] Loading and error states defined

### Output Instructions
- Open `shared/project_context.md`
- Append your output under this exact header:
  `## Section 4: UI Components & User Flows`
- Use TypeScript interfaces and numbered user flow steps.
- At the very end of your section, add this exact line:
  `<!-- AGENT_4_COMPLETE -->`
