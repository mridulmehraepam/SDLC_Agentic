"""
Podcast Management API - Agent 2 Implementation
FastAPI backend for managing podcast episodes and guests
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.episodes import router as episodes_router
from .api.guests import router as guests_router

app = FastAPI(
    title="Podcast Management API",
    description="API for managing podcast episodes and guests",
    version="1.0.0"
)

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(episodes_router, prefix="/api")
app.include_router(guests_router, prefix="/api")


@app.get("/")
def root():
    """API health check endpoint"""
    return {"status": "healthy", "service": "Podcast Management API"}


@app.get("/api")
def api_info():
    """API information endpoint"""
    return {
        "version": "1.0.0",
        "endpoints": {
            "episodes": "/api/episodes",
            "guests": "/api/guests"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
