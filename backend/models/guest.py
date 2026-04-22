from dataclasses import dataclass, field, asdict
from typing import Optional
import uuid


@dataclass
class Guest:
    """
    Represents a podcast guest.
    
    Attributes:
        id: Unique identifier for the guest
        name: Guest's full name
        bio: Short biography of the guest
        area_of_expertise: Guest's primary area of expertise
    """
    name: str
    bio: str
    area_of_expertise: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        """Validate fields after initialization"""
        if not self.name or not self.name.strip():
            raise ValueError("Name cannot be empty")
        if not self.area_of_expertise or not self.area_of_expertise.strip():
            raise ValueError("Area of expertise cannot be empty")

    def to_dict(self) -> dict:
        """Convert guest to dictionary for serialization"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Guest":
        """Create a Guest instance from a dictionary"""
        return cls(**data)

    def update(self, name: Optional[str] = None, bio: Optional[str] = None, 
               area_of_expertise: Optional[str] = None) -> None:
        """Update guest fields"""
        if name is not None:
            if not name.strip():
                raise ValueError("Name cannot be empty")
            self.name = name
        if bio is not None:
            self.bio = bio
        if area_of_expertise is not None:
            if not area_of_expertise.strip():
                raise ValueError("Area of expertise cannot be empty")
            self.area_of_expertise = area_of_expertise
