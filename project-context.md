# Project Context

## Project Name
Podcast Episode Planner & Script Assistant

## Purpose
Plan podcast episodes, manage guests, and support AI-assisted script/question/hook/intro generation via EPAM AI DIAL.

## Tech Stack
- Backend: Python + FastAPI
- Frontend: React (JSX)
- Database: SQLite (dev) / PostgreSQL (prod)
- AI Integration: EPAM AI DIAL (via backend)

## Current Agent Status
- Product manager: requirements captured in requirements.md
- Project scaffolding: initial structure created
- Backend/API/AI/frontend implementation: pending

## Data Models
- Episode: title, topic, episode_number, planned_date, status, guests
- Guest: name, bio, area_of_expertise

## API Endpoints (Known)
- Episodes CRUD: /episodes
- Guests CRUD: /guests
- AI features: /ai/script, /ai/questions, /ai/guest-intro, /ai/hook

## AI Features (Scope)
- Script generation
- Question bank generation
- Guest introduction
- Episode hook creation

## File Structure (Current)
- backend/main.py
- backend/api/episodes.py
- backend/api/guests.py
- backend/api/ai_features.py
- backend/models/episode.py
- backend/models/guest.py
- backend/services/dial_service.py
- frontend/App.jsx
- frontend/components/EpisodeDashboard.jsx
- frontend/components/EpisodeForm.jsx
- frontend/components/GuestForm.jsx
- frontend/components/GuestList.jsx
- requirements.md
- requirements.txt

## Open Items
- EPAM AI DIAL base URL
- EPAM AI DIAL model name
- EPAM AI DIAL auth token format

## Last Updated
April 22, 2026
