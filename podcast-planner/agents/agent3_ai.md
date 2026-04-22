## AGENT 3 PROMPT — AI Integration Agent (EPAM AI DIAL)

### Context
You are Agent 3 of 5 in a linear pipeline.
Sections 1 and 2 are already written in `shared/project_context.md`.

### Pre-Validation Step
⚠️ Before starting, verify:
- [ ] `<!-- AGENT_1_COMPLETE -->` marker exists
- [ ] `<!-- AGENT_2_COMPLETE -->` marker exists
- [ ] Episode and Guest data models are defined
- [ ] API endpoints are documented

If ANY of these are missing, STOP and report: "Previous sections incomplete. Missing: [list items]"

### Your Job
1. Open and read `shared/project_context.md` — review Sections 1 and 2 carefully.
2. Design 2 AI-powered API endpoints using **EPAM AI DIAL**:

   **Endpoint 1: Script Generator**
   - `POST /api/ai/generate-script`
   - Input: Topic + Guest Bio
   - Output: Full interview script
   - DIAL API integration details

   **Endpoint 2: Question Bank**
   - `POST /api/ai/generate-questions`
   - Input: Topic + Guest Area of Expertise
   - Output: List of 10 interview questions
   - DIAL API integration details

3. For each endpoint define:
   - Full request/response contract (TypeScript interfaces)
   - The exact prompt template sent to DIAL (use `{{variable}}` placeholders)
   - DIAL API configuration (endpoint URL, headers, model selection)
   - Error handling:
     - DIAL API timeout (30 second limit)
     - Invalid response format
     - Rate limiting
     - Fallback behavior
   - Estimated token usage per call

4. Include DIAL API integration code snippet:
   ```typescript
   // DIAL API base URL and authentication pattern
   ```

### Output Validation Criteria
Before marking complete, verify your output contains:
- [ ] Script Generator endpoint fully documented
- [ ] Question Bank endpoint fully documented
- [ ] TypeScript interfaces for requests/responses
- [ ] Prompt templates with placeholders
- [ ] Error handling strategy defined
- [ ] DIAL API integration details

### Output Instructions
- Open `shared/project_context.md`
- Append your output under:
  `## Section 3: AI Integration (EPAM AI DIAL)`
- Use TypeScript code blocks for contracts and plain text for prompt templates.
- At the very end of your section, add:
  `<!-- AGENT_3_COMPLETE -->`
