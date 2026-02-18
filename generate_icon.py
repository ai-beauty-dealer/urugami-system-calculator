from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # Settings
    size = (512, 512)
    bg_color = (39, 40, 71)     # #272847 Dark Navy
    text_color = (207, 168, 64) # #cfa840 Gold
    text = "US"
    
    # Create Image
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Font Selection
    font_paths = [
        "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
        "/System/Library/Fonts/Times.ttc",
        "/System/Library/Fonts/Palatino.ttc",
        "/Library/Fonts/Times New Roman.ttf",
        "/System/Library/Fonts/Optima.ttc"
    ]
    
    font = None
    for path in font_paths:
        try:
            font = ImageFont.truetype(path, 280)
            print(f"Using font: {path}")
            break
        except Exception:
            continue
            
    if not font:
        print("Warning: Could not load premium font. Using default.")
        font = ImageFont.load_default()

    # Center Text
    try:
        # Get bounding box for precise centering
        bbox = d.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size[0] - text_width) / 2
        y = (size[1] - text_height) / 2 - (text_height * 0.1) # Slightly adjust vertical center
        
        d.text((x, y), text, font=font, fill=text_color)
        
        # Add subtle gold border
        d.rectangle([0, 0, size[0]-1, size[1]-1], outline=text_color, width=10)
        
        # Save
        output_path = "apple-touch-icon.png"
        img.save(output_path)
        print(f"Icon saved to {output_path}")
        
    except Exception as e:
        print(f"Error drawing text: {e}")

if __name__ == "__main__":
    create_icon()
