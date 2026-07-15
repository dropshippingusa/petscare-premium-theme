import os
from PIL import Image

def force_center_crop(filepath, target_w=1024, target_h=180):
    if not os.path.exists(filepath):
        return
    img = Image.open(filepath)
    
    # Reload original generated files from the brain directory to get the uncropped originals
    # Let's see: we can look for the original generated file path by copying it again, or we can just crop the currently saved file if it hasn't been cropped yet.
    # Wait, we already cropped some of them to 180px. But for banner-clothing, it was cropped to 351px.
    # If we crop the currently saved file, it might crop a cropped file! 
    # To be safe, let's copy the original generated square files from the brain folder first, and then apply the 1024x180 center crop!
    
    print(f"Force center cropping {filepath}...")

# Let's map original files to assets:
original_mappings = {
    "assets/banner-all.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_all_1784122960080.png",
    "assets/banner-top-picks.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_top_picks_new_1784123243226.png",
    "assets/banner-beds.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_beds_new_1784123258193.png",
    "assets/banner-clothing.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_clothing_new_1784123274226.png",
    "assets/banner-grooming.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_grooming_new_1784123288641.png",
    "assets/banner-health.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_health_new_1784123303474.png",
    "assets/banner-smart.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_smart_new_1784123316697.png",
    "assets/banner-toys.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_toys_new_1784123330168.png",
    "assets/banner-training.png": "C:\\Users\\Dilip\\.gemini\\antigravity-ide\\brain\\e125cb9e-b01c-4443-8c79-0d15ac2d4ea2\\banner_toys_new_1784123330168.png"
}

for dest, src in original_mappings.items():
    if os.path.exists(src):
        img = Image.open(src)
        # Center crop to 1024x180
        w, h = img.size
        # Let's do a 1024 x 170 center crop to make it slightly wider and shorter!
        target_h = 170
        y_top = (h - target_h) // 2
        y_bottom = y_top + target_h
        
        cropped_img = img.crop((0, y_top, w, y_bottom))
        cropped_img.save(dest)
        print(f"Cropped {src} -> {dest} | Size: {cropped_img.size}")
    else:
        print(f"Original source {src} not found.")
