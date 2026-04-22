# Requirements — Podcast Episode Planner & Script Assistant

## Project Overview

A web application that helps podcast producers plan episodes, manage guests, and generate AI-assisted content such as scripts, question banks, guest introductions, and episode hooks.

AI features are powered via **EPAM AI DIAL**. The backend acts as the orchestration layer. The frontend never calls AI directly.

---

## 1. Episode Management

- Create, view, edit, and delete episodes
- Episode fields:
  - `title` (string)
  - `topic` (string)
  - `episode_number` (integer)
  - `planned_date` (ISO date string)
  - `status` — one of: `Draft`, `Scripted`, `Published`
  - `guests` — list of Guest IDs linked to the episode

---

## 2. Guest Management

- Add, view, edit, and delete guests
- Guest fields:
  - `name` (string)
  - `bio` (string)
  - `area_of_expertise` (string)
- Link one or more guests to an episode

---

## 3. AI-Powered Features

All AI features are triggered by backend endpoints that call EPAM AI DIAL.

| Feature               | Trigger                          | Output                                  |
|-----------------------|----------------------------------|-----------------------------------------|
| Script generation     | Episode topic + guest profile    | Full draft interview script             |
| Question bank         | Topic + guest expertise          | 10–15 interview questions               |
| Guest introduction    | Guest bio + episode topic        | 2–3 sentence on-air introduction        |
| Episode hook creation | Episode title + topic            | 30-second opening hook paragraph        |

---

## 4. Non-Functional Requirements

- RESTful backend API (Python/FastAPI)
- React frontend
- PostgreSQL or SQLite for persistence
- EPAM AI DIAL API for all AI feature calls
- Stateless backend endpoints
- API responses in JSON

---

## 5. Episode Scope Example (Pilot)

- **Title:** AI in Healthcare: From Hype to Hospital Workflow
- **Topic:** AI adoption in clinical settings
- **Episode Number:** 1
- **Format:** Host + 1 expert guest
- **Target Duration:** 30 minutes
- **Guest Profile:** Clinician or healthcare AI product leader with hands-on deployment experience
- **Planned Segments:**
  - 0:00–3:00 Intro and guest introduction
  - 3:00–10:00 Current state of AI in healthcare
  - 10:00–20:00 Featured real-world use case
  - 20:00–26:00 Risks, ethics, and adoption barriers
  - 26:00–30:00 Future outlook and key takeaways

---

## 6. File Structure (Target)

```
SDLC_Agentic/
├── backend/
│   ├── api/
│   │   ├── episodes.py
│   │   ├── guests.py
│   │   └── ai_features.py
│   ├── models/
│   │   ├── episode.py
│   │   └── guest.py
│   ├── services/
│   │   └── dial_service.py
│   └── main.py
├── frontend/
│   ├── components/
│   │   ├── EpisodeDashboard.jsx
│   │   ├── EpisodeForm.jsx
│   │   ├── GuestForm.jsx
│   │   └── GuestList.jsx
│   └── App.jsx
├── agents/
├── requirements.md
├── project-context.md
├── README.md
└── requirements.txt
```

---

## 7. Out of Scope

- Deep model architecture walkthroughs
- Real-time collaboration
- Video or audio recording integration
- Full legal / compliance modules
- Multi-tenancy

---

## Gaps & Additions

- `[ASSUMED]` Database: SQLite for development, PostgreSQL for production
- `[ASSUMED]` Authentication: Not in scope for MVP — no login or user management required
- `[RECOMMENDED]` Add `requirements.txt` with FastAPI, SQLAlchemy, httpx (for DIAL calls), and uvicorn
- `[RECOMMENDED]` Add a `services/` layer in the backend to isolate EPAM AI DIAL calls from API route handlers
- `[MISSING]` EPAM AI DIAL base URL, model name, and auth token format — must be provided before AI feature implementation begins
