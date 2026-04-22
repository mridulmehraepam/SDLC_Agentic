# Agent 1: Requirements & Data Model

## Proposed File Structure

```
SDLC_Agentic/
│
├── backend/
│   ├── api/
│   │   ├── episodes.py
│   │   └── guests.py
│   ├── models/
│   │   ├── episode.py
│   │   └── guest.py
│   └── main.py
│
├── frontend/
│   ├── components/
│   │   ├── EpisodeDashboard.jsx
│   │   ├── EpisodeForm.jsx
│   │   ├── GuestForm.jsx
│   │   └── GuestList.jsx
│   └── App.jsx
│
├── agents/
│   ├── product-manager-agent.md
│   └── ...
│
├── README.md
└── requirements.txt / package.json
```

## Requirements Extracted

- **Episode Management:**
	- Create, view, edit, delete episodes
	- Episode fields: Title, Topic, Episode Number, Planned Date, Status (Draft, Scripted, Published)
- **Guest Management:**
	- Add guest (Name, Bio, Area of Expertise)
	- Link guest to episode
	- CRUD for guest

## Initial Data Models

### Episode
```python
class Episode:
		id: str
		title: str
		topic: str
		episode_number: int
		planned_date: str  # ISO format
		status: str  # Draft | Scripted | Published
		guests: list  # List of Guest IDs
```

### Guest
```python
class Guest:
		id: str
		name: str
		bio: str
		area_of_expertise: str
```

---

## Implementation Status: ✅ COMPLETED

### Completed Tasks:
1. ✅ File structure created as specified
2. ✅ Episode model implemented with:
   - Dataclass with validation
   - EpisodeStatus enum (Draft, Scripted, Published)
   - Auto-generated UUID
   - Serialization methods (to_dict, from_dict)
   - Guest management methods (add_guest, remove_guest)
3. ✅ Guest model implemented with:
   - Dataclass with validation
   - Auto-generated UUID
   - Serialization methods (to_dict, from_dict)
   - Update method for partial updates
4. ✅ requirements.txt created for Python dependencies
5. ✅ package.json created for frontend dependencies

### Files Created/Updated:
- `backend/models/episode.py` - Enhanced Episode model
- `backend/models/guest.py` - Enhanced Guest model
- `requirements.txt` - Python dependencies
- `frontend/package.json` - Frontend dependencies

// Agent 1 complete. Next: Agent 2 (Backend API Design)
