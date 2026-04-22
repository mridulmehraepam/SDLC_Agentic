"""
Episode API endpoints - Agent 2 Implementation
CRUD operations for podcast episodes
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

from ..models.episode import Episode, EpisodeStatus

router = APIRouter(prefix="/episodes", tags=["Episodes"])

# In-memory storage (replace with database in production)
episodes_db: dict[str, Episode] = {}


# Pydantic schemas for request/response
class EpisodeCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Episode title")
    topic: str = Field(..., description="Main topic of the episode")
    episode_number: int = Field(..., gt=0, description="Episode number")
    planned_date: str = Field(..., description="Planned date in ISO format (YYYY-MM-DD)")
    status: str = Field(default="Draft", description="Episode status")
    guests: List[str] = Field(default=[], description="List of guest IDs")


class EpisodeUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    topic: Optional[str] = None
    episode_number: Optional[int] = Field(None, gt=0)
    planned_date: Optional[str] = None
    status: Optional[str] = None


class EpisodeResponse(BaseModel):
    id: str
    title: str
    topic: str
    episode_number: int
    planned_date: str
    status: str
    guests: List[str]


class GuestLink(BaseModel):
    guest_id: str = Field(..., description="Guest ID to link/unlink")


@router.post("/", response_model=EpisodeResponse, status_code=status.HTTP_201_CREATED)
def create_episode(episode_data: EpisodeCreate):
    """Create a new episode"""
    try:
        episode = Episode(
            title=episode_data.title,
            topic=episode_data.topic,
            episode_number=episode_data.episode_number,
            planned_date=episode_data.planned_date,
            status=EpisodeStatus(episode_data.status),
            guests=episode_data.guests
        )
        episodes_db[episode.id] = episode
        return episode.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[EpisodeResponse])
def list_episodes():
    """List all episodes"""
    return [ep.to_dict() for ep in episodes_db.values()]


@router.get("/{episode_id}", response_model=EpisodeResponse)
def get_episode(episode_id: str):
    """Get a specific episode by ID"""
    if episode_id not in episodes_db:
        raise HTTPException(status_code=404, detail="Episode not found")
    return episodes_db[episode_id].to_dict()


@router.put("/{episode_id}", response_model=EpisodeResponse)
def update_episode(episode_id: str, episode_data: EpisodeUpdate):
    """Update an existing episode"""
    if episode_id not in episodes_db:
        raise HTTPException(status_code=404, detail="Episode not found")
    
    episode = episodes_db[episode_id]
    
    try:
        if episode_data.title is not None:
            episode.title = episode_data.title
        if episode_data.topic is not None:
            episode.topic = episode_data.topic
        if episode_data.episode_number is not None:
            episode.episode_number = episode_data.episode_number
        if episode_data.planned_date is not None:
            episode.planned_date = episode_data.planned_date
        if episode_data.status is not None:
            episode.status = EpisodeStatus(episode_data.status)
        
        return episode.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{episode_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_episode(episode_id: str):
    """Delete an episode"""
    if episode_id not in episodes_db:
        raise HTTPException(status_code=404, detail="Episode not found")
    del episodes_db[episode_id]


@router.post("/{episode_id}/guests", response_model=EpisodeResponse)
def add_guest_to_episode(episode_id: str, guest_link: GuestLink):
    """Link a guest to an episode"""
    if episode_id not in episodes_db:
        raise HTTPException(status_code=404, detail="Episode not found")
    
    episode = episodes_db[episode_id]
    episode.add_guest(guest_link.guest_id)
    return episode.to_dict()


@router.delete("/{episode_id}/guests/{guest_id}", response_model=EpisodeResponse)
def remove_guest_from_episode(episode_id: str, guest_id: str):
    """Unlink a guest from an episode"""
    if episode_id not in episodes_db:
        raise HTTPException(status_code=404, detail="Episode not found")
    
    episode = episodes_db[episode_id]
    if not episode.remove_guest(guest_id):
        raise HTTPException(status_code=404, detail="Guest not linked to this episode")
    return episode.to_dict()
