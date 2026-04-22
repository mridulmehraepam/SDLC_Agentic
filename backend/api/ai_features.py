from typing import Any

from fastapi import APIRouter

router = APIRouter(prefix="/ai", tags=["ai"])


def _mock_ai_response(feature: str, payload: dict[str, Any]) -> dict[str, Any]:
	topic = payload.get("topic", "the selected topic")
	guest = payload.get("guest_name", "your guest")
	return {
		"feature": feature,
		"source": "mock-dial",
		"content": f"Draft {feature} output for {topic} with {guest}.",
	}


@router.post("/script")
def generate_script(payload: dict[str, Any]) -> dict[str, Any]:
	return _mock_ai_response("script", payload)


@router.post("/questions")
def generate_questions(payload: dict[str, Any]) -> dict[str, Any]:
	return _mock_ai_response("questions", payload)


@router.post("/guest-intro")
def generate_guest_intro(payload: dict[str, Any]) -> dict[str, Any]:
	return _mock_ai_response("guest-intro", payload)


@router.post("/hook")
def generate_hook(payload: dict[str, Any]) -> dict[str, Any]:
	return _mock_ai_response("hook", payload)
