from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.ai_features import router as ai_router
from backend.api.episodes import router as episodes_router
from backend.api.guests import router as guests_router

app = FastAPI(title="Podcast Episode Planner API", version="0.1.0")

# Allow local frontend development clients.
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
	return {"status": "ok"}


app.include_router(episodes_router)
app.include_router(guests_router)
app.include_router(ai_router)
