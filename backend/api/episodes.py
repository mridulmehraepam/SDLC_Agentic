from typing import Any
from uuid import uuid4

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/episodes", tags=["episodes"])

_episodes: list[dict[str, Any]] = []


@router.get("")
def list_episodes() -> list[dict[str, Any]]:
	return _episodes


@router.post("")
def create_episode(payload: dict[str, Any]) -> dict[str, Any]:
	episode = {
		"id": str(uuid4()),
		"title": payload.get("title", "Untitled Episode"),
		"topic": payload.get("topic", "General"),
		"episode_number": payload.get("episode_number", len(_episodes) + 1),
		"planned_date": payload.get("planned_date", ""),
		"status": payload.get("status", "Draft"),
		"guests": payload.get("guests", []),
	}
	_episodes.append(episode)
	return episode


@router.get("/{episode_id}")
def get_episode(episode_id: str) -> dict[str, Any]:
	for episode in _episodes:
		if episode["id"] == episode_id:
			return episode
	raise HTTPException(status_code=404, detail="Episode not found")


@router.put("/{episode_id}")
def update_episode(episode_id: str, payload: dict[str, Any]) -> dict[str, Any]:
	for episode in _episodes:
		if episode["id"] == episode_id:
			episode.update(payload)
			return episode
	raise HTTPException(status_code=404, detail="Episode not found")


@router.delete("/{episode_id}")
def delete_episode(episode_id: str) -> dict[str, str]:
	for index, episode in enumerate(_episodes):
		if episode["id"] == episode_id:
			_episodes.pop(index)
			return {"message": "Episode deleted"}
	raise HTTPException(status_code=404, detail="Episode not found")
