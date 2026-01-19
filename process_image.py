from PIL import Image
import os

try:
    img_path = '/Users/changeless/Desktop/Blog/Screenshot 2026-01-19 at 1.24.05 PM.png'
    if not os.path.exists(img_path):
        print(f'Error: File not found at {img_path}')
        exit(1)

    img = Image.open(img_path)
    width, height = img.size
    print(f'Original size: {width}x{height}')
    
    # Calculate crop box for a square crop
    # Strategy: Simple center square crop. 
    # Usually screenshots are already framed somewhat intentionally.
    
    min_dim = min(width, height)
    
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    
    # If the user wants it to be heads-only or specific, we can adjust 'top'.
    # But for a general "use this image", center crop is safest for a square avatar.

    print(f'Cropping box: {left}, {top}, {right}, {bottom}')
    img_cropped = img.crop((left, top, right, bottom))
    
    # Resize to standard avatar size, e.g., 512x512
    img_resized = img_cropped.resize((512, 512))
    
    output_path = '/Users/changeless/Desktop/Blog/images/profile.png'
    img_resized.save(output_path)
    print(f'Successfully saved cropped avatar to {output_path}')

except Exception as e:
    print(f'Error processing image: {e}')
