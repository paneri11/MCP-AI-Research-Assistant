import json
import os

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")

# Ensure file exists
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as f:
        json.dump([], f)


def summarize_text(text: str) -> str:
    """
    Basic summarization logic.
    (LLM can also refine it.)
    """
    return text[:500] + "..." if len(text) > 500 else text


def extract_key_points(text: str) -> list:
    """
    Extract first few important sentences.
    """
    sentences = text.split(".")
    key_points = [s.strip() for s in sentences if s.strip()]
    return key_points[:5]


def save_note(note: str) -> str:
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    notes.append(note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

    return "Note saved successfully."


def get_notes() -> list:
    with open(NOTES_FILE, "r") as f:
        return json.load(f)
