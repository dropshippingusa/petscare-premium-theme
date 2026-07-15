import os
from PIL import Image

def crop_banner_file(filepath):
    if not os.path.exists(filepath):
        return
    
    img = Image.open(filepath)
    w, h = img.size
    
    # If the image is not square (1024x1024), we might not need to crop it
    if w != 1024 or h != 1024:
        print(f"Skipping {filepath} (size is {w}x{h}, not 1024x1024)")
        return
        
    # Get the color of the top-left corner as the border color
    border_color = img.getpixel((5, 5))
    
    # Help functions to check if a row is mostly the border color
    def is_border_row(y, tolerance=10):
        # Sample 20 pixels across the row
        for x in range(0, w, w // 20):
            pixel = img.getpixel((x, y))
            # Calculate color distance
            dist = sum(abs(pixel[i] - border_color[i]) for i in range(3))
            if dist > tolerance:
                return False
        return True

    # Scan from top to find content start
    y_top = 0
    for y in range(h):
        if not is_border_row(y):
            y_top = y
            break
            
    # Scan from bottom to find content end
    y_bottom = h - 1
    for y in range(h - 1, -1, -1):
        if not is_border_row(y):
            y_bottom = y
            break
            
    # Add a tiny padding to prevent clipping the edge of products
    y_top = max(0, y_top - 5)
    y_bottom = min(h - 1, y_bottom + 5)
    
    crop_h = y_bottom - y_top
    print(f"File: {os.path.basename(filepath)} | Detected Content: y={y_top} to y={y_bottom} (Height: {crop_h}px)")
    
    # If the detected height is too small or too large, fall back to a standard center crop of 180px
    if crop_h < 100 or crop_h > 400:
        y_top = (h - 180) // 2
        y_bottom = y_top + 180
        print(f"  Fallback: Using standard center crop y={y_top} to y={y_bottom} (Height: 180px)")
        
    cropped_img = img.crop((0, y_top, w, y_bottom))
    cropped_img.save(filepath)
    print(f"  Saved cropped image to {filepath} | New Size: {cropped_img.size}")

# Process all banners
banners = [
    "assets/banner-all.png",
    "assets/banner-top-picks.png",
    "assets/banner-beds.png",
    "assets/banner-clothing.png",
    "assets/banner-grooming.png",
    "assets/banner-health.png",
    "assets/banner-toys.png",
    "assets/banner-smart.png",
    "assets/banner-training.png"
]

for banner in banners:
    crop_banner_file(banner)
