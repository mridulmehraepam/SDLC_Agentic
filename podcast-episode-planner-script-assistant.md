# Podcast Episode Planner + Script Assistant (Frontend/UI Spec)

## Assumptions

- Existing backend APIs support episode and guest CRUD operations.
- AI capabilities exist for summary generation and script generation.
- Auth/session handling is already available in the app shell.
- This spec targets a modern React-based frontend, but is framework-agnostic at the UX level.

---

## 1) User Flows

### Flow A: Plan a New Episode
1. User opens **Episode Planner Dashboard**.
2. User clicks **Create Episode**.
3. User fills metadata: title, topic, objective, target duration, tone, publish date.
4. User selects or adds guests.
5. User clicks **Save Draft**.
6. UI calls episode create API and shows success toast.
7. User is redirected to **Episode Detail Workspace**.

### Flow B: Generate Episode Outline with AI
1. From Episode Detail Workspace, user opens **AI Assistant Panel**.
2. User enters prompt/context (audience, key points, constraints).
3. User clicks **Generate Outline**.
4. UI shows generating state with progress indicator.
5. AI returns structured outline.
6. User can **Accept**, **Edit**, or **Regenerate**.
7. Accepted outline is saved to episode draft via update API.

### Flow C: Generate Full Script
1. User clicks **Generate Script** using selected outline.
2. UI sends episode context + outline + style controls to AI API.
3. UI displays streaming or async status.
4. Script output appears in editable rich text editor.
5. User can **Regenerate section**, **Undo**, **Save Version**.
6. Final script is saved as current script version.

### Flow D: Collaborate and Finalize
1. User reviews script sections (intro, transitions, interview, outro).
2. User marks sections complete and resolves feedback notes.
3. User clicks **Mark Ready for Recording**.
4. Episode status updates from `Draft` to `Scripted`.

### Flow E: Failure/Recovery (AI + API)
1. API/AI request fails.
2. UI shows inline error with reason and `Retry` action.
3. User retries with same prompt or edits prompt and regenerates.
4. If retries exceed threshold, UI suggests fallback manual editing.

---

## 2) Component Hierarchy

### App-Level
- `AppShell`
  - `TopNav`
  - `SidebarNav`
  - `NotificationToastHost`
  - `RouteOutlet`

### Episode Planner Module
- `EpisodePlannerPage`
  - `EpisodeFiltersBar`
  - `EpisodeList`
    - `EpisodeCard`
  - `CreateEpisodeButton`
  - `EpisodePagination`

### Episode Detail Workspace
- `EpisodeWorkspacePage`
  - `EpisodeHeader`
  - `EpisodeMetaForm`
  - `GuestSelector`
  - `OutlinePanel`
  - `ScriptEditorPanel`
  - `AiAssistantPanel`
    - `AiPromptInput`
    - `AiActionButtons` (Generate Outline, Generate Script, Regenerate)
    - `AiResultPreview`
    - `AiRunHistory`
  - `VersionHistoryDrawer`
  - `StatusActionsBar`

### Shared UI System
- `Button`, `Input`, `Textarea`, `Select`, `DatePicker`
- `Modal`, `Drawer`, `Tabs`, `Accordion`
- `Skeleton`, `Spinner`, `EmptyState`, `ErrorState`
- `ConfirmDialog`, `Badge`, `Tooltip`

---

## 3) Wireframes (Text-Based)

### A) Episode Planner Dashboard

```text
+--------------------------------------------------------------------------------+
| TopNav: Logo | Search | New Episode | User Menu                                |
+----------------------+---------------------------------------------------------+
| Sidebar              | Episode Planner                                          |
| - Dashboard          | [Filters: Status | Date | Guest | Search ]              |
| - Episodes           |                                                         |
| - Guests             | [ + Create Episode ]                                     |
| - AI Tools           |                                                         |
|                      | ------------------------------------------------------- |
|                      | | Episode Card: Title, Date, Guests, Status, Actions | |
|                      | | Episode Card: ...                                   | |
|                      | ------------------------------------------------------- |
|                      | [Pagination]                                             |
+--------------------------------------------------------------------------------+
```

### B) Episode Workspace (Planner + AI Script Assistant)

```text
+--------------------------------------------------------------------------------+
| Episode Header: "Ep 024 - Future of AI in Podcasting" [Draft Badge]            |
+-------------------------------------+------------------------------------------+
| Left/Main                           | Right/Ai Assistant                        |
|                                     |                                          |
| Episode Meta Form                   | Prompt Input                             |
| - Title, Topic, Duration, Date      | [Describe audience/goals/style...]       |
| - Tone, Objective                   |                                          |
|                                     | [Generate Outline] [Generate Script]     |
| Guest Selector                      | [Regenerate]                             |
| - Search/Add Guest                  |                                          |
| - Guest Cards                       | AI Output Preview                        |
|                                     | - Outline / Script tabs                  |
| Outline Panel                       | - Accept / Edit / Retry                  |
| - Editable sections                 |                                          |
|                                     | Run History                              |
| Script Editor Panel                 | - timestamp, prompt, status              |
| - Rich text script                  |                                          |
| - Section regenerate                |                                          |
+-------------------------------------+------------------------------------------+
| Bottom Actions: [Save Draft] [Save Version] [Mark Ready for Recording]         |
+--------------------------------------------------------------------------------+
```

### C) Mobile Layout

```text
- Top nav condensed with menu drawer
- Episode workspace uses stacked sections:
  1) Metadata
  2) Guests
  3) Outline
  4) Script Editor
  5) AI Assistant
- Sticky bottom action bar: Save / Generate / Ready
```

---

## 4) API → UI Mapping

| Backend Capability | Endpoint (Example) | UI Components | UX Notes |
|---|---|---|---|
| List episodes | `GET /api/episodes` | `EpisodePlannerPage`, `EpisodeList`, `EpisodeCard` | Use pagination + filter query params; show skeletons on load |
| Create episode | `POST /api/episodes` | `CreateEpisodeModal`, `EpisodeMetaForm` | Optimistic close + success toast |
| Update episode | `PATCH /api/episodes/:id` | `EpisodeMetaForm`, `StatusActionsBar` | Auto-save (debounced) and manual Save |
| Manage guests | `GET/POST /api/guests` | `GuestSelector`, `GuestModal` | Search with debounce; empty states for no guests |
| Link guest to episode | `POST /api/episodes/:id/guests` | `GuestSelector` | Reflect linked guests instantly in UI |
| Generate outline (AI) | `POST /api/ai/outline` | `AiAssistantPanel`, `AiPromptInput`, `AiResultPreview` | Show in-progress state and retry actions |
| Generate script (AI) | `POST /api/ai/script` | `AiAssistantPanel`, `ScriptEditorPanel` | Handle long-running request with progress + cancellation |
| Save script version | `POST /api/episodes/:id/script-versions` | `VersionHistoryDrawer`, `StatusActionsBar` | Add version comment input and timestamp |

---

## 5) AI Interaction Design

### Input UX
- Prompt box with helper chips:
  - `Audience`
  - `Tone`
  - `Length`
  - `Must-include points`
- Preset templates:
  - `Interview Episode`
  - `Solo Thought Leadership`
  - `News Roundup`

### Output UX
- Two AI output modes:
  1. **Draft Mode**: full generated content for quick start.
  2. **Assist Mode**: section-level suggestions only.
- Every AI result includes:
  - generation timestamp
  - model/action label
  - prompt reference
  - confidence/disclaimer note

### Feedback Loop
- Actions per response: `Accept`, `Edit`, `Regenerate`, `Copy`, `Discard`.
- Section-level regenerate in script editor for targeted rewrites.
- Error handling:
  - transient error => quick retry
  - validation error => explain what to adjust in prompt
  - timeout => keep draft and allow resume

### Transparency + Trust
- Show “AI generated” badge on inserted content.
- Keep version history with diff-friendly metadata.
- Never overwrite manual edits silently; ask for confirmation.

---

## 6) Frontend Architecture Recommendations

## Suggested Stack
- **Framework:** React + TypeScript
- **Routing:** React Router
- **Server State:** TanStack Query
- **Client State:** Zustand (or Context for small scope)
- **Forms:** React Hook Form + Zod
- **Editor:** TipTap or Lexical for script editing
- **UI Kit:** Existing design system (or shadcn/ui style primitives)

## Folder Structure (Feature-Based)

```text
frontend/
  src/
    app/
      router/
      providers/
    features/
      episodes/
        api/
        components/
        hooks/
        pages/
        types/
      guests/
        api/
        components/
        hooks/
      ai-assistant/
        api/
        components/
        hooks/
        utils/
      script-editor/
        components/
        hooks/
        utils/
    shared/
      components/
      ui/
      lib/
      types/
```

## State Strategy
- Server/cache state in TanStack Query.
- Local UI state (panels, selections) in feature-local hooks or Zustand store.
- Form state isolated per form; autosave with debounced mutation.

## Performance and Reliability
- Debounce search and autosave updates.
- Use request cancellation for AI regenerate spam.
- Virtualize long episode lists.
- Prefetch episode detail on card hover (desktop).

---

## 7) UX States Checklist

- Loading: skeletons for list/cards/panels.
- Empty: no episodes, no guests, no AI history.
- Error: inline component-level + global fallback.
- Success: toast + non-blocking confirmations.
- Offline/slow: network banners and retry queue hints.

---

## 8) MVP Scope (Recommended)

1. Episode dashboard with create/edit/list/filter.
2. Guest selector with link/unlink.
3. AI outline generation with accept/regenerate.
4. AI full script generation with editable output.
5. Save versions + mark episode as `Scripted`.

This sequence provides a fast path from planning to record-ready scripts while keeping architecture modular for future collaboration and publishing features.
