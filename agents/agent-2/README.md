# Agent 2: Backend API Design

## Implementation Status: ✅ COMPLETED

## API Architecture

### Technology Stack
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Validation**: Pydantic

### API Endpoints

#### Episodes API (`/api/episodes`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/episodes/` | Create a new episode |
| GET | `/api/episodes/` | List all episodes |
| GET | `/api/episodes/{id}` | Get episode by ID |
| PUT | `/api/episodes/{id}` | Update an episode |
| DELETE | `/api/episodes/{id}` | Delete an episode |
| POST | `/api/episodes/{id}/guests` | Link guest to episode |
| DELETE | `/api/episodes/{id}/guests/{guest_id}` | Unlink guest from episode |

#### Guests API (`/api/guests`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/guests/` | Create a new guest |
| GET | `/api/guests/` | List all guests |
| GET | `/api/guests/{id}` | Get guest by ID |
| PUT | `/api/guests/{id}` | Update a guest |
| DELETE | `/api/guests/{id}` | Delete a guest |

### Request/Response Schemas

#### Episode
```json
{
  "id": "uuid",
  "title": "string",
  "topic": "string",
  "episode_number": "integer",
  "planned_date": "YYYY-MM-DD",
  "status": "Draft | Scripted | Published",
  "guests": ["guest_id_1", "guest_id_2"]
}
```

#### Guest
```json
{
  "id": "uuid",
  "name": "string",
  "bio": "string",
  "area_of_expertise": "string"
}
```

### Running the API

```bash
cd SDLC_Agentic
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

API will be available at `http://localhost:8000`

### Interactive Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Files Implemented
- `backend/main.py` - FastAPI app entry point with CORS
- `backend/api/episodes.py` - Episode CRUD endpoints
- `backend/api/guests.py` - Guest CRUD endpoints
- `backend/api/__init__.py` - API module exports
- `backend/__init__.py` - Backend package init

---

// Agent 2 complete. Next: Agent 3 (Frontend Implementation)
