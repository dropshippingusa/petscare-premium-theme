import os
from PIL import Image

def inspect_image(filepath):
    if not os.path.exists(filepath):
        print(f"{filepath} does not exist.")
        return
    img = Image.open(filepath)
    print(f"File: {os.path.basename(filepath)} | Size: {img.size} | Mode: {img.mode}")
    
    # Check some pixels at the top, bottom, and center to understand the background
    w, h = img.size
    top_pixel = img.getpixel((10, 10))
    bottom_pixel = img.getpixel((10, h - 10))
    center_pixel = img.getpixel((w // 2, h // 2))
    print(f"  Top pixel: {top_pixel}")
    print(f"  Bottom pixel: {bottom_pixel}")
    print(f"  Center pixel: {center_pixel}")

inspect_image("assets/banner-all.png")
inspect_image("assets/banner-top-picks.png")
inspect_image("assets/banner-beds.png")
