"""Independent storyboard timeline example; no media generation or network calls."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Scene:
    name: str
    seconds: int

def timeline(scenes: list[Scene]) -> list[dict]:
    result = []
    offset = 0
    for scene in scenes:
        if not isinstance(scene.name, str) or not scene.name.strip():
            raise ValueError("Scene name required")
        if type(scene.seconds) is not int or not 1 <= scene.seconds <= 120:
            raise ValueError("Duration must be an integer from 1 to 120")
        result.append({"scene": scene.name, "start": offset, "end": offset + scene.seconds})
        offset += scene.seconds
    return result

if __name__ == "__main__":
    import json
    print(json.dumps(timeline([Scene("Opening", 8), Scene("Resolution", 8)]), indent=2))
