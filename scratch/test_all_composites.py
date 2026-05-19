import os
import glob
from PIL import Image, ImageDraw

def test_composites():
    # Create a solid dummy graphic (e.g. red square with a cross)
    design = Image.new("RGBA", (800, 800), (255, 0, 0, 180))
    draw = ImageDraw.Draw(design)
    draw.rectangle([20, 20, 780, 780], outline=(255, 255, 255, 255), width=10)
    draw.line([0, 0, 800, 800], fill=(255, 255, 255, 255), width=8)
    draw.line([0, 800, 800, 0], fill=(255, 255, 255, 255), width=8)
    
    os.makedirs("static/output/test_fits", exist_ok=True)
    
    # Import agent_mockup_compositor logic
    from main import agent_mockup_compositor
    
    folders = ["tshirt_mockup", "sweatshirt_mockup"]
    for folder in folders:
        folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), folder)
        templates = sorted(glob.glob(os.path.join(folder_path, "*.png")))
        for t_path in templates:
            name = os.path.basename(t_path)
            try:
                # Composite using the normal function
                result = agent_mockup_compositor(design, niche="test", mockup_type=folder.split("_")[0], specific_template_path=t_path)
                out_path = f"static/output/test_fits/{folder}_{name}.jpg"
                result.save(out_path, quality=90)
                print(f"Generated test fit: {out_path}")
            except Exception as e:
                print(f"Error {name}: {e}")

if __name__ == "__main__":
    test_composites()
