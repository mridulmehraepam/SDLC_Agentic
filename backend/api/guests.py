from typing import Any
from uuid import uuid4

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/guests", tags=["guests"])

_guests: list[dict[str, Any]] = []


@router.get("")
def list_guests() -> list[dict[str, Any]]:
	return _guests


@router.post("")
def create_guest(payload: dict[str, Any]) -> dict[str, Any]:
	guest = {
		"id": str(uuid4()),
		"name": payload.get("name", "Unnamed Guest"),
		"bio": payload.get("bio", ""),
		"area_of_expertise": payload.get("area_of_expertise", ""),
	}
	_guests.append(guest)
	return guest


@router.get("/{guest_id}")
def get_guest(guest_id: str) -> dict[str, Any]:
	for guest in _guests:
		if guest["id"] == guest_id:
			return guest
	raise HTTPException(status_code=404, detail="Guest not found")


@router.put("/{guest_id}")
def update_guest(guest_id: str, payload: dict[str, Any]) -> dict[str, Any]:
	for guest in _guests:
		if guest["id"] == guest_id:
			guest.update(payload)
			return guest
	raise HTTPException(status_code=404, detail="Guest not found")


@router.delete("/{guest_id}")
def delete_guest(guest_id: str) -> dict[str, str]:
	for index, guest in enumerate(_guests):
		if guest["id"] == guest_id:
			_guests.pop(index)
			return {"message": "Guest deleted"}
	raise HTTPException(status_code=404, detail="Guest not found")
