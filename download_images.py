
import json
import urllib.request
from pathlib import Path

from data import DESTINATIONS

images_folder = Path("static/images")
json_file = Path("static/data/destinations.json")

images_folder.mkdir(parents=True, exist_ok=True)

image_names = {
    "Hingol National Park": "hingol.jpg",
    "Kund Malir Beach": "kund-malir.jpg",
    "Ziarat": "ziarat.jpg",
    "Hanna Lake": "hanna-lake.jpg",
    "Gwadar": "gwadar.jpg",
    "Moola Chotok": "moola-chotok.jpg"
}

successful = 0

for place in DESTINATIONS:
    name = place["name"]
    image_url = place["image"]
    filename = image_names[name]
    image_path = images_folder / filename

    try:
        request = urllib.request.Request(
            image_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=30) as response:
            image_path.write_bytes(response.read())

        place["image"] = f"/static/images/{filename}"

        successful += 1
        print(f"Downloaded: {name}")

    except Exception as error:
        print(f"Failed: {name} - {error}")

# Update the JSON only after successful downloads
if json_file.exists():
    with json_file.open("r", encoding="utf-8") as file:
        json_destinations = json.load(file)

    for place in json_destinations:
        name = place["name"]

        if name in image_names:
            local_image = images_folder / image_names[name]

            if local_image.exists():
                place["image"] = f"/static/images/{image_names[name]}"

    with json_file.open("w", encoding="utf-8") as file:
        json.dump(
            json_destinations,
            file,
            ensure_ascii=False,
            indent=4
        )

print("\nImage download process completed.")
print(f"Successfully downloaded: {successful}/6")
