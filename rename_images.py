import os

dataset_dir = "dataset"

for celeb_folder in os.listdir(dataset_dir):
    celeb_path = os.path.join(dataset_dir, celeb_folder)

    if os.path.isdir(celeb_path):
        images = [img for img in os.listdir(celeb_path) if img.lower().endswith(".jpg")]
        images.sort()  # Ensures consistent order

        # Step 1: Temporarily rename all to avoid conflicts
        for i, img in enumerate(images):
            temp_name = f"temp_{i}.jpg"
            os.rename(os.path.join(celeb_path, img), os.path.join(celeb_path, temp_name))

        # Step 2: Rename to final name
        temp_images = [img for img in os.listdir(celeb_path) if img.startswith("temp_")]
        temp_images.sort()

        for i, img in enumerate(temp_images, start=1):
            new_name = f"{celeb_folder}_{i}.jpg"
            os.rename(os.path.join(celeb_path, img), os.path.join(celeb_path, new_name))

        print(f"✅ Renamed in: {celeb_folder}")
