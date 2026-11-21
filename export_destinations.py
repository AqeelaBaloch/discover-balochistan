
import json
from pathlib import Path

from data import DESTINATIONS

output_file = Path("static/data/destinations.json")

output_file.parent.mkdir(parents=True, exist_ok=True)

with output_file.open("w", encoding="utf-8") as file:
    json.dump(
        DESTINATIONS,
        file,
        ensure_ascii=False,
        indent=4
    )

print("Destination data exported successfully!")
print(f"Total destinations: {len(DESTINATIONS)}")
print(f"Saved to: {output_file}")
