import os
import glob
from PIL import Image

def check_folder(folder):
    print(f"\n--- Checking {folder} ---")
    folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), folder)
    templates = sorted(glob.glob(os.path.join(folder_path, "*.png")))
    for t_path in templates:
        name = os.path.basename(t_path)
        try:
            img = Image.open(t_path)
            w, h = img.size
            top_left = img.getpixel((20, 20))
            
            # Check transparency
            has_alpha = img.mode == 'RGBA'
            is_transparent = False
            if has_alpha and len(top_left) == 4 and top_left[3] == 0:
                is_transparent = True
                
            r, g, b = top_left[0], top_left[1], top_left[2]
            is_flat_lay_color = (r > 235 and g > 235 and b > 235)
            
            print(f"File: {name} | Size: {w}x{h} | Mode: {img.mode} | TopLeft: {top_left} | IsTransparent: {is_transparent} | ColorWhite: {is_flat_lay_color}")
        except Exception as e:
            print(f"Error {name}: {e}")

check_folder("tshirt_mockup")
check_folder("sweatshirt_mockup")
