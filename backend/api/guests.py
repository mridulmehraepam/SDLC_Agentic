"""
Guest API endpoints - Agent 2 Implementation
CRUD operations for podcast guests
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

from ..models.guest import Guest

router = APIRouter(prefix="/guests", tags=["Guests"])

# In-memory storage (replace with database in production)
guests_db: dict[str, Guest] = {}


# Pydantic schemas for request/response
class GuestCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Guest's full name")
    bio: str = Field(default="", description="Short biography")
    area_of_expertise: str = Field(..., min_length=1, description="Primary area of expertise")


class GuestUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    bio: Optional[str] = None
    area_of_expertise: Optional[str] = Field(None, min_length=1)


class GuestResponse(BaseModel):
    id: str
    name: str
    bio: str
    area_of_expertise: str


@router.post("/", response_model=GuestResponse, status_code=status.HTTP_201_CREATED)
def create_guest(guest_data: GuestCreate):
    """Create a new guest"""
    try:
        guest = Guest(
            name=guest_data.name,
            bio=guest_data.bio,
            area_of_expertise=guest_data.area_of_expertise
        )
        guests_db[guest.id] = guest
        return guest.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[GuestResponse])
def list_guests():
    """List all guests"""
    return [guest.to_dict() for guest in guests_db.values()]


@router.get("/{guest_id}", response_model=GuestResponse)
def get_guest(guest_id: str):
    """Get a specific guest by ID"""
    if guest_id not in guests_db:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guests_db[guest_id].to_dict()


@router.put("/{guest_id}", response_model=GuestResponse)
def update_guest(guest_id: str, guest_data: GuestUpdate):
    """Update an existing guest"""
    if guest_id not in guests_db:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    guest = guests_db[guest_id]
    
    try:
        guest.update(
            name=guest_data.name,
            bio=guest_data.bio,
            area_of_expertise=guest_data.area_of_expertise
        )
        return guest.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{guest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_guest(guest_id: str):
    """Delete a guest"""
    if guest_id not in guests_db:
        raise HTTPException(status_code=404, detail="Guest not found")
    del guests_db[guest_id]
