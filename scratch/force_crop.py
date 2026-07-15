import os
from PIL import Image

# Let's map original files to assets:
original_mappings = {
    "assets/banner-all.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_all_v2_1784123912460.png",
    "assets/banner-top-picks.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_top_picks_v2_1784123928550.png",
    "assets/banner-beds.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_beds_v2_1784123942826.png",
    "assets/banner-clothing.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_clothing_v2_1784123955842.png",
    "assets/banner-grooming.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_grooming_v2_1784123970422.png",
    "assets/banner-health.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_health_v2_1784123984906.png",
    "assets/banner-smart.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_smart_v2_1784124001017.png",
    "assets/banner-toys.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_toys_v2_1784124015298.png",
    "assets/banner-training.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_training_v2_1784124029002.png"
}

for dest, src in original_mappings.items():
    if os.path.exists(src):
        img = Image.open(src)
        w, h = img.size
        # Center crop to 1024x170 (exactly 6:1 ratio)
        target_h = 170
        y_top = (h - target_h) // 2
        y_bottom = y_top + target_h
        
        cropped_img = img.crop((0, y_top, w, y_bottom))
        cropped_img.save(dest)
        print(f"Cropped {src} -> {dest} | Size: {cropped_img.size}")
    else:
        print(f"Original source {src} not found.")
