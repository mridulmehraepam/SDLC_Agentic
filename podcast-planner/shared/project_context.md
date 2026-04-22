# Podcast Episode Planner & Script Assistant — Shared Agent Context

> This file is the shared knowledge baton passed between all 5 agents.
> Each agent reads all previous sections and appends their own.
> DO NOT delete or modify existing sections.

---
<!-- PIPELINE START -->

## Section 1: Requirements & Data Models

### 1.1 Functional Requirements

#### Episode Management
| Feature | Description |
|---------|-------------|
| Create Episode | Create a new episode with Title, Topic, Episode Number, and Planned Date |
| View Dashboard | Display all episodes showing title, topic, and status |
| Edit Episode | Modify any episode field |
| Delete Episode | Remove an episode from the system |
| Status Lifecycle | Episodes progress through: `Draft → Scripted → Published` |

#### Guest Management
| Feature | Description |
|---------|-------------|
| Add Guest | Create guest with Name, Bio, and Area of Expertise |
| Link to Episode | Associate a guest with an episode |
| Edit Guest | Modify guest information |
| Delete Guest | Remove a guest from the system |
| View Guests | List all guests with their details |

#### AI Features (Powered by EPAM AI DIAL)
| Feature | Input | Output |
|---------|-------|--------|
| Script Generator | Topic + Guest Bio | Full interview script |
| Question Bank | Topic + Guest Expertise | 10 interview questions |

### 1.2 Non-Functional Requirements
- **Performance**: Response time < 2 seconds for CRUD operations
- **AI Timeout**: Maximum 30 seconds for AI generation
- **Browser Support**: Chrome, Firefox, Safari, Edge (latest versions)
- **Responsiveness**: Mobile-friendly UI

### 1.3 TypeScript Data Models

```typescript
// Episode Status Enum
enum EpisodeStatus {
  Draft = "Draft",
  Scripted = "Scripted",
  Published = "Published"
}

// Episode Interface
interface Episode {
  id: string;              // Unique identifier (UUID) - Required
  title: string;           // Episode title - Required
  topic: string;           // Main topic/theme - Required
  episodeNumber: number;   // Sequential episode number - Required
  plannedDate: Date;       // Scheduled recording/publish date - Required
  guestId?: string;        // Reference to Guest (optional)
  status: EpisodeStatus;   // Current lifecycle status - Required, defaults to Draft
  aiScript?: string;       // AI-generated interview script (optional)
  aiQuestions?: string[];  // AI-generated questions (optional)
  createdAt: Date;         // Creation timestamp - Required
  updatedAt: Date;         // Last update timestamp - Required
}

// Guest Interface
interface Guest {
  id: string;              // Unique identifier (UUID) - Required
  name: string;            // Full name - Required
  bio: string;             // Biography/background - Required
  areaOfExpertise: string; // Primary expertise area - Required
  episodeIds: string[];    // Episodes this guest appears in - Required, defaults to []
  createdAt: Date;         // Creation timestamp - Required
  updatedAt: Date;         // Last update timestamp - Required
}
```

### 1.4 Field Documentation

#### Episode Fields
| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| `id` | string (UUID) | Yes | Unique identifier for database operations |
| `title` | string | Yes | Display name shown on dashboard |
| `topic` | string | Yes | Main subject for AI context |
| `episodeNumber` | number | Yes | Sequential ordering |
| `plannedDate` | Date | Yes | Scheduling and calendar display |
| `guestId` | string | No | Links to Guest for AI generation |
| `status` | EpisodeStatus | Yes | Tracks workflow progress |
| `aiScript` | string | No | Stores generated interview script |
| `aiQuestions` | string[] | No | Stores generated questions |
| `createdAt` | Date | Yes | Audit trail |
| `updatedAt` | Date | Yes | Audit trail |

#### Guest Fields
| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| `id` | string (UUID) | Yes | Unique identifier |
| `name` | string | Yes | Display and AI prompt input |
| `bio` | string | Yes | AI context for script generation |
| `areaOfExpertise` | string | Yes | AI context for question generation |
| `episodeIds` | string[] | Yes | Reverse lookup for guest appearances |
| `createdAt` | Date | Yes | Audit trail |
| `updatedAt` | Date | Yes | Audit trail |

<!-- AGENT_1_COMPLETE -->

## Section 2: API Endpoints

### 2.1 Episode Endpoints

#### GET /api/episodes
**Description:** Retrieve all episodes

| Property | Value |
|----------|-------|
| Method | GET |
| URL | `/api/episodes` |
| Request Body | None |
| Success Response | `200 OK` |

```json
// Response
{
  "data": [
    {
      "id": "uuid-123",
      "title": "AI in Healthcare",
      "topic": "Machine Learning Applications",
      "episodeNumber": 1,
      "plannedDate": "2026-05-01",
      "guestId": "guest-456",
      "status": "Draft",
      "createdAt": "2026-04-22T10:00:00Z",
      "updatedAt": "2026-04-22T10:00:00Z"
    }
  ],
  "total": 1
}
```

| Error Code | Reason |
|------------|--------|
| 500 | Internal server error |

---

#### GET /api/episodes/:id
**Description:** Retrieve a single episode by ID

| Property | Value |
|----------|-------|
| Method | GET |
| URL | `/api/episodes/:id` |
| Request Body | None |
| Success Response | `200 OK` |

| Error Code | Reason |
|------------|--------|
| 404 | Episode not found |
| 500 | Internal server error |

---

#### POST /api/episodes
**Description:** Create a new episode

| Property | Value |
|----------|-------|
| Method | POST |
| URL | `/api/episodes` |
| Success Response | `201 Created` |

```typescript
// Request Body
interface CreateEpisodeRequest {
  title: string;        // Required
  topic: string;        // Required
  episodeNumber: number; // Required
  plannedDate: string;  // Required (ISO date)
  guestId?: string;     // Optional
}
```

| Error Code | Reason |
|------------|--------|
| 400 | Invalid request body / Missing required fields |
| 500 | Internal server error |

---

#### PUT /api/episodes/:id
**Description:** Update an existing episode

| Property | Value |
|----------|-------|
| Method | PUT |
| URL | `/api/episodes/:id` |
| Success Response | `200 OK` |

```typescript
// Request Body
interface UpdateEpisodeRequest {
  title?: string;
  topic?: string;
  episodeNumber?: number;
  plannedDate?: string;
  guestId?: string;
  aiScript?: string;
  aiQuestions?: string[];
}
```

| Error Code | Reason |
|------------|--------|
| 400 | Invalid request body |
| 404 | Episode not found |
| 500 | Internal server error |

---

#### DELETE /api/episodes/:id
**Description:** Delete an episode

| Property | Value |
|----------|-------|
| Method | DELETE |
| URL | `/api/episodes/:id` |
| Request Body | None |
| Success Response | `204 No Content` |

| Error Code | Reason |
|------------|--------|
| 404 | Episode not found |
| 500 | Internal server error |

---

#### PATCH /api/episodes/:id/status
**Description:** Transition episode status (Draft → Scripted → Published)

| Property | Value |
|----------|-------|
| Method | PATCH |
| URL | `/api/episodes/:id/status` |
| Success Response | `200 OK` |

```typescript
// Request Body
interface UpdateStatusRequest {
  status: "Draft" | "Scripted" | "Published";
}
```

| Error Code | Reason |
|------------|--------|
| 400 | Invalid status transition |
| 404 | Episode not found |
| 500 | Internal server error |

---

### 2.2 Guest Endpoints

#### GET /api/guests
**Description:** Retrieve all guests

| Property | Value |
|----------|-------|
| Method | GET |
| URL | `/api/guests` |
| Success Response | `200 OK` |

---

#### GET /api/guests/:id
**Description:** Retrieve a single guest by ID

| Property | Value |
|----------|-------|
| Method | GET |
| URL | `/api/guests/:id` |
| Success Response | `200 OK` |

| Error Code | Reason |
|------------|--------|
| 404 | Guest not found |

---

#### POST /api/guests
**Description:** Create a new guest

| Property | Value |
|----------|-------|
| Method | POST |
| URL | `/api/guests` |
| Success Response | `201 Created` |

```typescript
// Request Body
interface CreateGuestRequest {
  name: string;           // Required
  bio: string;            // Required
  areaOfExpertise: string; // Required
}
```

| Error Code | Reason |
|------------|--------|
| 400 | Missing required fields |
| 500 | Internal server error |

---

#### PUT /api/guests/:id
**Description:** Update an existing guest

| Property | Value |
|----------|-------|
| Method | PUT |
| URL | `/api/guests/:id` |
| Success Response | `200 OK` |

---

#### DELETE /api/guests/:id
**Description:** Delete a guest

| Property | Value |
|----------|-------|
| Method | DELETE |
| URL | `/api/guests/:id` |
| Success Response | `204 No Content` |

| Error Code | Reason |
|------------|--------|
| 404 | Guest not found |

---

#### POST /api/episodes/:id/guests/:guestId
**Description:** Link a guest to an episode

| Property | Value |
|----------|-------|
| Method | POST |
| URL | `/api/episodes/:id/guests/:guestId` |
| Request Body | None |
| Success Response | `200 OK` |

| Error Code | Reason |
|------------|--------|
| 404 | Episode or Guest not found |
| 409 | Guest already linked to episode |

<!-- AGENT_2_COMPLETE -->

## Section 3: AI Integration (EPAM AI DIAL)

### 3.1 DIAL API Configuration

```typescript
// Environment Variables
const DIAL_CONFIG = {
  baseUrl: process.env.DIAL_API_URL || "https://dial.epam.com/api/v1",
  apiKey: process.env.DIAL_API_KEY,
  model: "gpt-4",
  timeout: 30000, // 30 seconds
};

// DIAL API Client
async function callDialAPI(prompt: string): Promise<string> {
  const response = await fetch(`${DIAL_CONFIG.baseUrl}/chat/completions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${DIAL_CONFIG.apiKey}`,
    },
    body: JSON.stringify({
      model: DIAL_CONFIG.model,
      messages: [{ role: "user", content: prompt }],
      max_tokens: 2000,
      temperature: 0.7,
    }),
    signal: AbortSignal.timeout(DIAL_CONFIG.timeout),
  });
  
  if (!response.ok) {
    throw new Error(`DIAL API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}
```

### 3.2 Endpoint 1: Script Generator

#### POST /api/ai/generate-script
**Description:** Generate a full interview script using topic and guest bio

```typescript
// Request Interface
interface GenerateScriptRequest {
  topic: string;      // Episode topic
  guestBio: string;   // Guest biography
  guestName: string;  // Guest name for personalization
}

// Response Interface
interface GenerateScriptResponse {
  script: string;           // Generated interview script
  tokenCount: number;       // Tokens used
  generatedAt: string;      // ISO timestamp
}
```

#### Prompt Template
```
You are a professional podcast script writer. Create a comprehensive interview script for a podcast episode.

**Episode Topic:** {{topic}}

**Guest Information:**
- Name: {{guestName}}
- Bio: {{guestBio}}

Generate a structured interview script that includes:
1. Host introduction (30 seconds)
2. Guest welcome and brief intro
3. 5-7 main interview segments with transitions
4. Key talking points for each segment
5. Suggested follow-up questions
6. Closing remarks and call-to-action

Format the script with clear speaker labels (HOST: / GUEST:) and timing estimates.
```

#### Error Handling
| Error Scenario | HTTP Code | Response |
|----------------|-----------|----------|
| DIAL timeout (>30s) | 504 | `{ "error": "AI generation timed out. Please try again." }` |
| Invalid response | 502 | `{ "error": "AI returned invalid response format." }` |
| Rate limited | 429 | `{ "error": "Too many requests. Please wait before trying again.", "retryAfter": 60 }` |
| Missing fields | 400 | `{ "error": "Missing required fields: topic, guestBio" }` |

#### Token Estimates
- **Input**: ~200-400 tokens
- **Output**: ~1500-2000 tokens
- **Total per call**: ~2000-2400 tokens

---

### 3.3 Endpoint 2: Question Bank

#### POST /api/ai/generate-questions
**Description:** Generate 10 interview questions based on topic and guest expertise

```typescript
// Request Interface
interface GenerateQuestionsRequest {
  topic: string;           // Episode topic
  areaOfExpertise: string; // Guest's expertise area
  guestName: string;       // Guest name for context
}

// Response Interface
interface GenerateQuestionsResponse {
  questions: Question[];    // Array of 10 questions
  tokenCount: number;       // Tokens used
  generatedAt: string;      // ISO timestamp
}

interface Question {
  id: number;              // Question number (1-10)
  question: string;        // The interview question
  category: string;        // Category: "Opening" | "Deep-Dive" | "Personal" | "Closing"
  followUp?: string;       // Optional follow-up question
}
```

#### Prompt Template
```
You are an expert podcast interviewer. Generate 10 engaging interview questions for a podcast episode.

**Episode Topic:** {{topic}}

**Guest Expertise:** {{areaOfExpertise}}
**Guest Name:** {{guestName}}

Create 10 questions distributed as follows:
- 2 Opening questions (warm-up, establish credibility)
- 5 Deep-dive questions (technical, insightful, specific to expertise)
- 2 Personal questions (journey, challenges, advice)
- 1 Closing question (future outlook, call-to-action)

For each question, provide:
1. The main question
2. Category label
3. A follow-up question for deeper exploration

Format as a numbered list with clear categories.
```

#### Error Handling
| Error Scenario | HTTP Code | Response |
|----------------|-----------|----------|
| DIAL timeout | 504 | `{ "error": "AI generation timed out." }` |
| Invalid response | 502 | `{ "error": "AI returned invalid response." }` |
| Rate limited | 429 | `{ "error": "Rate limited.", "retryAfter": 60 }` |
| Missing fields | 400 | `{ "error": "Missing required fields" }` |

#### Token Estimates
- **Input**: ~150-250 tokens
- **Output**: ~800-1200 tokens
- **Total per call**: ~1000-1500 tokens

### 3.4 Fallback Strategy

```typescript
// Fallback when DIAL fails
const FALLBACK_RESPONSES = {
  script: "Unable to generate script. Please try again or write manually.",
  questions: [
    "What inspired you to enter this field?",
    "Can you share your journey to becoming an expert in {{expertise}}?",
    "What are the biggest challenges you face in {{topic}}?",
    // ... 7 more generic questions
  ]
};
```

<!-- AGENT_3_COMPLETE -->

## Section 4: UI Components & User Flows

### 4.1 Component Architecture

```
App
├── Dashboard
│   ├── EpisodeList
│   │   ├── StatusBadge
│   │   └── EpisodeActions (Edit/Delete/View)
│   └── QuickStats
├── EpisodeForm
│   ├── GuestSelector
│   └── AIPanel
│       ├── ScriptGenerator
│       └── QuestionGenerator
├── GuestManager
│   ├── GuestList
│   └── GuestForm (Modal)
└── Common
    ├── StatusBadge
    ├── LoadingSpinner
    └── ToastNotification
```

### 4.2 Component Specifications

#### Dashboard Component
```typescript
interface DashboardProps {
  // No props - root component
}

interface DashboardState {
  episodes: Episode[];
  isLoading: boolean;
  error: string | null;
  filter: EpisodeStatus | "all";
}
```

**API Calls:** `GET /api/episodes`
**User Flow:**
1. Dashboard loads → calls `GET /api/episodes`
2. Displays loading spinner while fetching
3. Renders EpisodeList with data
4. User can filter by status (Draft/Scripted/Published/All)

---

#### EpisodeList Component
```typescript
interface EpisodeListProps {
  episodes: Episode[];
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
  onView: (id: string) => void;
}
```

**Rendered Elements:**
| Column | Content |
|--------|---------|
| Title | Episode title (clickable) |
| Topic | Topic text |
| Episode # | Number badge |
| Status | StatusBadge component |
| Date | Formatted planned date |
| Actions | Edit / Delete / View buttons |

---

#### EpisodeForm Component
```typescript
interface EpisodeFormProps {
  episodeId?: string;  // undefined for create, id for edit
  onSave: (episode: Episode) => void;
  onCancel: () => void;
}

interface EpisodeFormState {
  formData: Partial<Episode>;
  guests: Guest[];
  isSubmitting: boolean;
  errors: Record<string, string>;
  aiScript: string | null;
  aiQuestions: string[] | null;
}
```

**API Calls:**
- Create: `POST /api/episodes`
- Update: `PUT /api/episodes/:id`
- Load guests: `GET /api/guests`
- Link guest: `POST /api/episodes/:id/guests/:guestId`

---

#### GuestManager Component
```typescript
interface GuestManagerProps {
  onGuestSelect?: (guest: Guest) => void;
  selectionMode?: boolean;
}

interface GuestManagerState {
  guests: Guest[];
  isLoading: boolean;
  showAddModal: boolean;
  editingGuest: Guest | null;
}
```

**API Calls:**
- `GET /api/guests`
- `POST /api/guests`
- `PUT /api/guests/:id`
- `DELETE /api/guests/:id`

---

#### GuestForm Component (Modal)
```typescript
interface GuestFormProps {
  guest?: Guest;       // undefined for create
  onSave: (guest: Guest) => void;
  onClose: () => void;
}

interface GuestFormState {
  name: string;
  bio: string;
  areaOfExpertise: string;
  isSubmitting: boolean;
  errors: Record<string, string>;
}
```

---

#### AIPanel Component
```typescript
interface AIPanelProps {
  episode: Episode;
  guest: Guest | null;
  onScriptGenerated: (script: string) => void;
  onQuestionsGenerated: (questions: string[]) => void;
}

interface AIPanelState {
  isGeneratingScript: boolean;
  isGeneratingQuestions: boolean;
  scriptResult: string | null;
  questionsResult: string[] | null;
  error: string | null;
}
```

**API Calls:**
- `POST /api/ai/generate-script`
- `POST /api/ai/generate-questions`

---

#### StatusBadge Component
```typescript
interface StatusBadgeProps {
  status: EpisodeStatus;
  size?: "sm" | "md" | "lg";
}

const STATUS_COLORS = {
  Draft: "bg-gray-200 text-gray-800",
  Scripted: "bg-blue-200 text-blue-800",
  Published: "bg-green-200 text-green-800",
};
```

### 4.3 User Flows

#### Flow 1: Create Episode
```
1. User clicks "New Episode" button on Dashboard
2. EpisodeForm opens in create mode
3. User fills in: Title, Topic, Episode Number, Planned Date
4. User optionally selects a Guest from dropdown
5. User clicks "Save"
6. Form validates all required fields
7. If valid → POST /api/episodes
8. If guest selected → POST /api/episodes/:id/guests/:guestId
9. Success toast appears: "Episode created successfully"
10. User redirected to Dashboard
11. New episode appears in list with "Draft" status
```

#### Flow 2: Generate Script (AI)
```
1. User opens an episode in EpisodeForm
2. User ensures a Guest is linked to the episode
3. User clicks "Generate Script" in AIPanel
4. Loading spinner appears: "Generating script..."
5. POST /api/ai/generate-script with topic + guestBio
6. Wait for response (max 30 seconds)
7. On success:
   - Script appears in textarea
   - "Copy to Clipboard" button enabled
   - Token count displayed
8. On error:
   - Error toast: "Failed to generate script. Please try again."
   - Retry button appears
9. User can edit the generated script
10. User clicks "Save" to store script with episode
```

#### Flow 3: Link Guest to Episode
```
1. User opens EpisodeForm for existing episode
2. User clicks Guest dropdown
3. Dropdown shows list of all guests (from GET /api/guests)
4. User selects a guest
5. POST /api/episodes/:id/guests/:guestId
6. Guest info appears in form
7. AIPanel becomes active (Generate buttons enabled)
8. Success toast: "Guest linked to episode"
```

### 4.4 Loading & Error States

| Component | Loading State | Error State |
|-----------|---------------|-------------|
| Dashboard | Skeleton table rows | "Failed to load episodes" + Retry button |
| EpisodeForm | Submit button disabled + spinner | Field-level error messages |
| GuestManager | Skeleton cards | "Failed to load guests" + Retry button |
| AIPanel | "Generating..." + spinner + progress | Error toast + Retry button |
| GuestForm | Submit button disabled | Inline validation errors |

### 4.5 Toast Notifications
```typescript
type ToastType = "success" | "error" | "warning" | "info";

interface Toast {
  id: string;
  type: ToastType;
  message: string;
  duration: number; // ms, default 5000
}

// Example toasts
const TOASTS = {
  episodeCreated: { type: "success", message: "Episode created successfully" },
  episodeDeleted: { type: "success", message: "Episode deleted" },
  guestLinked: { type: "success", message: "Guest linked to episode" },
  aiTimeout: { type: "error", message: "AI generation timed out. Please try again." },
  networkError: { type: "error", message: "Network error. Check your connection." },
};
```

<!-- AGENT_4_COMPLETE -->

## Section 5: Sequence Diagrams & Final Documentation

### 5.1 Sequence Diagrams

#### Diagram A: Create Episode Flow

```mermaid
sequenceDiagram
    actor User
    participant Dashboard
    participant EpisodeForm
    participant API as REST API
    participant DB as Database

    User->>Dashboard: Click "New Episode"
    Dashboard->>EpisodeForm: Open form (create mode)
    User->>EpisodeForm: Fill in Title, Topic, Episode #, Date
    User->>EpisodeForm: Select Guest (optional)
    User->>EpisodeForm: Click "Save"
    EpisodeForm->>EpisodeForm: Validate fields
    EpisodeForm->>API: POST /api/episodes
    API->>DB: INSERT episode
    DB-->>API: Return new episode
    API-->>EpisodeForm: 201 Created + episode data
    EpisodeForm->>Dashboard: Navigate back
    Dashboard->>API: GET /api/episodes
    API->>DB: SELECT episodes
    DB-->>API: Return episodes
    API-->>Dashboard: 200 OK + episodes list
    Dashboard->>User: Display updated list with new episode
```

#### Diagram B: AI Script Generation Flow

```mermaid
sequenceDiagram
    actor User
    participant EpisodeForm
    participant AIPanel
    participant API as REST API
    participant DIAL as EPAM AI DIAL

    User->>EpisodeForm: Open episode with linked guest
    User->>AIPanel: Click "Generate Script"
    AIPanel->>AIPanel: Show loading spinner
    AIPanel->>API: POST /api/ai/generate-script
    Note over API: {topic, guestBio, guestName}
    API->>DIAL: POST /chat/completions
    Note over DIAL: Process prompt template
    DIAL-->>API: Generated script text
    API-->>AIPanel: 200 OK + script response
    AIPanel->>AIPanel: Hide spinner
    AIPanel->>User: Display script in textarea
    User->>EpisodeForm: Edit script (optional)
    User->>EpisodeForm: Click "Save"
    EpisodeForm->>API: PUT /api/episodes/:id
    Note over API: {aiScript: "..."}
    API-->>EpisodeForm: 200 OK
    EpisodeForm->>User: Show success toast
```

#### Diagram C: Link Guest to Episode Flow

```mermaid
sequenceDiagram
    actor User
    participant EpisodeForm
    participant GuestDropdown
    participant API as REST API
    participant DB as Database

    User->>EpisodeForm: Open existing episode
    EpisodeForm->>API: GET /api/guests
    API->>DB: SELECT guests
    DB-->>API: Return guests list
    API-->>GuestDropdown: Populate dropdown
    User->>GuestDropdown: Select a guest
    GuestDropdown->>API: POST /api/episodes/:id/guests/:guestId
    API->>DB: UPDATE episode SET guestId
    API->>DB: UPDATE guest ADD episodeId
    DB-->>API: Success
    API-->>EpisodeForm: 200 OK
    EpisodeForm->>EpisodeForm: Display guest info
    EpisodeForm->>AIPanel: Enable AI generation buttons
    EpisodeForm->>User: Show "Guest linked" toast
```

### 5.2 Final Project Summary

#### System Overview
The **Podcast Episode Planner & Script Assistant** is a web application designed for podcast creators to manage their episodes and guests efficiently. It integrates with EPAM AI DIAL to automatically generate interview scripts and questions, streamlining the pre-production workflow from planning to publishing.

#### Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| **REST API** | Industry standard, stateless, easy to test, excellent tooling support |
| **TypeScript** | Type safety across frontend and backend, better IDE support, fewer runtime errors |
| **Episode/Guest Models** | Normalized data structure allowing many-to-many relationships, optimized for common queries |
| **Status Enum** | Explicit lifecycle states enable workflow automation and filtering |
| **Separate AI Endpoints** | Decoupled AI features allow independent scaling and easier error handling |

**Tech Stack:**
- **Frontend**: React 18 + TypeScript + TailwindCSS
- **Backend**: Node.js + Express + TypeScript
- **Database**: PostgreSQL with Prisma ORM
- **AI**: EPAM AI DIAL API

#### AI Integration Approach

**EPAM AI DIAL Integration:**
- All AI features use the DIAL `/chat/completions` endpoint
- Model: GPT-4 for high-quality content generation
- Prompt templates use `{{variable}}` placeholders for dynamic content
- Structured prompts with clear sections (context, instructions, format)
- 30-second timeout with graceful fallback responses
- Token estimation for cost monitoring (~2000 tokens/script, ~1200 tokens/questions)

**Prompt Engineering Principles:**
1. Clear role definition ("You are a professional podcast script writer")
2. Structured input sections (topic, guest info)
3. Explicit output format requirements
4. Category-based question distribution

#### Frontend Architecture

```
React Component Hierarchy:
─────────────────────────
App (Router)
├── Dashboard (main view)
│   ├── QuickStats (episode counts by status)
│   └── EpisodeList (table with actions)
│       └── StatusBadge (color-coded status)
├── EpisodeForm (create/edit)
│   ├── GuestSelector (dropdown)
│   └── AIPanel (AI generation UI)
├── GuestManager (CRUD for guests)
│   └── GuestForm (modal)
└── Shared Components
    ├── LoadingSpinner
    └── ToastNotification
```

**State Management:** React hooks (useState, useReducer) for local state; React Query for server state caching.

#### How to Run the Project

**Prerequisites:**
- Node.js 18+ 
- npm 9+
- PostgreSQL 14+
- EPAM AI DIAL API access

**Environment Variables:**
```bash
# .env file
DATABASE_URL=postgresql://user:password@localhost:5432/podcast_planner
DIAL_API_URL=https://dial.epam.com/api/v1
DIAL_API_KEY=your-dial-api-key
PORT=3000
```

**Setup Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/your-repo/podcast-planner.git
cd podcast-planner

# 2. Install dependencies
npm install

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your values

# 4. Run database migrations
npx prisma migrate dev

# 5. Seed sample data (optional)
npm run seed

# 6. Start development server
npm run dev

# 7. Open in browser
# http://localhost:3000
```

#### Future Improvements

1. **Guest Introduction Generator** — AI feature to generate host introductions for guests based on their bio

2. **Episode Hook Generator** — AI feature to create compelling 30-second opening hooks for episodes

3. **Transcript Integration** — Upload episode recordings and auto-generate transcripts for show notes

4. **Calendar Sync** — Integrate with Google Calendar/Outlook for scheduling episodes and reminders

5. **Analytics Dashboard** — Track episode performance, AI usage metrics, and content generation patterns

6. **Multi-user Collaboration** — Add team roles (Host, Producer, Editor) with permission-based access

7. **Template Library** — Save and reuse successful script templates and question sets

<!-- AGENT_5_COMPLETE -->
<!-- PIPELINE_COMPLETE -->
