import os
from PIL import Image
input_folder = "images_input"   
output_folder = "images_output" 
new_size = (800, 600)           
output_format = "JPEG"        
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if not os.path.isfile(file_path):
        continue
    try:
        with Image.open(file_path) as img:
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            base_name, _ = os.path.splitext(filename)
            output_file = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img_resized.save(output_file, output_format)
            print(f" Resized & saved: {output_file}")
    except Exception as e:
        print(f" Error processing {filename}: {e}")
print(" Batch image resizing completed!")