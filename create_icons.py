
from PIL import Image, ImageDraw
from pathlib import Path

icons_folder = Path("static/icons")
icons_folder.mkdir(parents=True, exist_ok=True)


def create_icon(size, filename):
    image = Image.new("RGB", (size, size), "#123c35")
    draw = ImageDraw.Draw(image)

    # Sun
    draw.ellipse(
        (size * 0.65, size * 0.12, size * 0.82, size * 0.29),
        fill="#f5c66b"
    )

    # Mountains
    draw.polygon([
        (size * 0.12, size * 0.70),
        (size * 0.36, size * 0.34),
        (size * 0.55, size * 0.70)
    ], fill="#d6e8c5")

    draw.polygon([
        (size * 0.35, size * 0.70),
        (size * 0.62, size * 0.30),
        (size * 0.90, size * 0.70)
    ], fill="#d6e8c5")

    # Green landscape
    draw.rectangle(
        (0, size * 0.72, size, size),
        fill="#4f9b79"
    )

    image.save(icons_folder / filename)
    print(f"Created: {filename}")


create_icon(192, "icon-192.png")
create_icon(512, "icon-512.png")
create_icon(512, "icon-512-maskable.png")

print("All three PWA icons created successfully!")
