import os

def rename_bat_frames(folder_path):
    # Get all PNG files in the folder and sort them
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.png')])

    # Rename each file to frame_0.png, frame_1.png, etc.
    for index, filename in enumerate(files):
        new_name = f"frame_{index}.png"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

# Replace this with your actual folder path
bat_folder = r"G:\My Drive\Python\Moonstone\assets\images\Enemies\Bat1\idle"
rename_bat_frames(bat_folder)
