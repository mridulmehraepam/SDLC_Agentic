from enum import Enum
from typing import List, Optional
from dataclasses import dataclass, field, asdict
from datetime import datetime
import uuid


class EpisodeStatus(str, Enum):
    """Valid statuses for an episode"""
    DRAFT = "Draft"
    SCRIPTED = "Scripted"
    PUBLISHED = "Published"


@dataclass
class Episode:
    """
    Represents a podcast episode.
    
    Attributes:
        id: Unique identifier for the episode
        title: Episode title
        topic: Main topic of the episode
        episode_number: Sequential episode number
        planned_date: Planned release date (ISO format)
        status: Current status (Draft, Scripted, Published)
        guests: List of guest IDs associated with this episode
    """
    title: str
    topic: str
    episode_number: int
    planned_date: str
    status: EpisodeStatus = EpisodeStatus.DRAFT
    guests: List[str] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        """Validate fields after initialization"""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        if self.episode_number < 1:
            raise ValueError("Episode number must be positive")
        if isinstance(self.status, str):
            self.status = EpisodeStatus(self.status)
        # Validate date format
        try:
            datetime.fromisoformat(self.planned_date)
        except ValueError:
            raise ValueError("planned_date must be in ISO format (YYYY-MM-DD)")

    def to_dict(self) -> dict:
        """Convert episode to dictionary for serialization"""
        data = asdict(self)
        data['status'] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Episode":
        """Create an Episode instance from a dictionary"""
        return cls(**data)

    def add_guest(self, guest_id: str) -> None:
        """Add a guest to the episode"""
        if guest_id not in self.guests:
            self.guests.append(guest_id)

    def remove_guest(self, guest_id: str) -> bool:
        """Remove a guest from the episode. Returns True if removed."""
        if guest_id in self.guests:
            self.guests.remove(guest_id)
            return True
        return False
