import os
import random

# Path to dataset
dataset_path = "dataset"

# Go through each folder
for celeb_folder in os.listdir(dataset_path):
    celeb_path = os.path.join(dataset_path, celeb_folder)

    if os.path.isdir(celeb_path):
        images = [img for img in os.listdir(celeb_path) if img.lower().endswith(".jpg")]

        if len(images) > 30:
            # Randomly pick 30 to keep
            images_to_keep = set(random.sample(images, 30))

            for img in images:
                if img not in images_to_keep:
                    os.remove(os.path.join(celeb_path, img))
            print(f"{celeb_folder}: trimmed to 30 images.")
        else:
            print(f"{celeb_folder}: already has {len(images)} images or less.")
