from PIL import Image
import os

dataset_path = "dataset"
allowed_exts = ('.jpeg', '.png', '.webp', '.jfif', '.gif', '.jpe')

for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            name, ext = os.path.splitext(filename)

            # Normalize the extension to lowercase
            ext = ext.lower()

            if ext in allowed_exts:
                try:
                    img = Image.open(file_path).convert("RGB")

                    # Ensure no duplicate filenames
                    new_filename = name + ".jpg"
                    new_path = os.path.join(folder_path, new_filename)

                    # If the new file already exists, add a suffix to avoid overwrite
                    counter = 1
                    while os.path.exists(new_path):
                        new_filename = f"{name}_{counter}.jpg"
                        new_path = os.path.join(folder_path, new_filename)
                        counter += 1

                    img.save(new_path, "JPEG")
                    os.remove(file_path)
                    print(f"✅ Converted: {filename} ➜ {new_filename}")
                except Exception as e:
                    print(f"❌ Error converting {filename}: {e}")
