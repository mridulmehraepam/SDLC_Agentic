# Project Context

> **All agents must read this file before starting work.**
> Update the relevant section when your agent completes a task.

---

## Project Name

Podcast Episode Planner & Script Assistant

---

## Purpose

A web application for podcast producers to plan episodes, manage guests, and generate AI-assisted content (scripts, question banks, guest introductions, episode hooks) using EPAM AI DIAL as the AI backend.

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python, FastAPI                   |
| Frontend   | React (JSX)                       |
| Database   | SQLite (dev) / PostgreSQL (prod)  |
| AI Service | EPAM AI DIAL API                  |
| ORM        | SQLAlchemy                        |
| HTTP Client| httpx (for DIAL calls)            |
| Server     | uvicorn                           |

---

## Current Agent Status

| Agent                        | Status      | Output File(s)                              |
|------------------------------|-------------|---------------------------------------------|
| product-manager-agent        | Complete    | requirements.md                             |
| project-scaffolding-agent    | Pending     | project structure, project-context.md       |
| backend-architecture         | Pending     | backend/                                    |
| backend-api-design           | Pending     | API spec in requirements.md or separate doc |
| ai-integration-agent         | Pending     | AI endpoint design in Markdown              |
| workflow-diagram-agent       | Pending     | Mermaid sequence diagrams                   |

---

## Data Models

### Episode
```
id              : str        (UUID)
title           : str
topic           : str
episode_number  : int
planned_date    : str        (ISO 8601)
status          : str        ("Draft" | "Scripted" | "Published")
guests          : list[str]  (list of Guest IDs)
```

### Guest
```
id                  : str   (UUID)
name                : str
bio                 : str
area_of_expertise   : str
```

---

## API Endpoints (Known)

### Episodes
| Method | Path                  | Description              |
|--------|-----------------------|--------------------------|
| GET    | /episodes             | List all episodes        |
| POST   | /episodes             | Create a new episode     |
| GET    | /episodes/{id}        | Get a single episode     |
| PUT    | /episodes/{id}        | Update an episode        |
| DELETE | /episodes/{id}        | Delete an episode        |

### Guests
| Method | Path              | Description          |
|--------|-------------------|----------------------|
| GET    | /guests           | List all guests      |
| POST   | /guests           | Create a guest       |
| GET    | /guests/{id}      | Get a single guest   |
| PUT    | /guests/{id}      | Update a guest       |
| DELETE | /guests/{id}      | Delete a guest       |

### AI Features (Backend → EPAM AI DIAL)
| Method | Path                             | AI Feature                |
|--------|----------------------------------|---------------------------|
| POST   | /ai/script                       | Script generation         |
| POST   | /ai/questions                    | Question bank generation  |
| POST   | /ai/guest-intro                  | Guest introduction        |
| POST   | /ai/hook                         | Episode hook creation     |

---

## AI Features (Scope)

| Feature               | Input                             | Output                               |
|-----------------------|-----------------------------------|--------------------------------------|
| Script generation     | episode topic + guest profile     | Full draft interview script          |
| Question bank         | topic + guest expertise           | 10–15 interview questions            |
| Guest introduction    | guest bio + episode topic         | 2–3 sentence on-air introduction     |
| Episode hook creation | episode title + topic             | 30-second opening hook paragraph     |

**Constraint:** Frontend never calls AI directly. All AI calls go through the backend.

---

## File Structure (Current)

```
SDLC_Agentic/
├── backend/                  ← TO BE SCAFFOLDED
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
├── frontend/                 ← TO BE SCAFFOLDED
│   ├── components/
│   │   ├── EpisodeDashboard.jsx
│   │   ├── EpisodeForm.jsx
│   │   ├── GuestForm.jsx
│   │   └── GuestList.jsx
│   └── App.jsx
├── agents/
│   ├── product-manager-agent.md
│   ├── backend-architecture.md
│   ├── backend-api-design.agent.md
│   ├── ai-integration-agent.agent.md
│   ├── workflow-diagram-agent.agent.md
│   └── project-scaffolding-agent.agent.md
├── requirements.md           ← Populated
├── project-context.md        ← This file
├── README.md
└── requirements.txt          ← TO BE CREATED
```

---

## Open Items

- `[MISSING]` EPAM AI DIAL base URL, model name, and auth token format — required before AI features can be built
- `[MISSING]` Frontend state management choice (plain React state vs Redux vs Zustand)
- `[ASSUMED]` No authentication / user management in MVP
- `[ASSUMED]` SQLite for local development; PostgreSQL for production
- `[RECOMMENDED]` Add a `config.py` or `.env` file pattern for DIAL credentials

---

## Last Updated

April 22, 2026 — Initial context created by project-scaffolding-agent setup. Populated from requirements.md and conversation scope.

---

> **For agents:** When you complete a task, update the `Current Agent Status` table and the `File Structure` section to reflect what was actually created or changed.
