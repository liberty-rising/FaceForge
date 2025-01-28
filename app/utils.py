import os

def save_image(image_bytes, filename):
    """Save image bytes to the static/images directory"""
    os.makedirs("static/images", exist_ok=True)
    image_path = os.path.join("static/images", filename)
    
    with open(image_path, "wb") as f:
        f.write(image_bytes)
    
    return image_path