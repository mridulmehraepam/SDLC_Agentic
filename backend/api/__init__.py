"""API module - Episode and Guest routes"""
from .episodes import router as episodes_router
from .guests import router as guests_router

__all__ = ["episodes_router", "guests_router"]
