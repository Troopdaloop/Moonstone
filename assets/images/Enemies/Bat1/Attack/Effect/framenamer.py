import os

def rename_png_files_in_current_dir():
    # Get all PNG files in the current directory and sort them
    files = sorted([f for f in os.listdir('.') if f.lower().endswith('.png')])

    # Rename each file to frame_0.png, frame_1.png, etc.
    for index, filename in enumerate(files):
        new_name = f"frame_{index}.png"
        os.rename(filename, new_name)
        print(f"Renamed: {filename} -> {new_name}")

# Run the function
rename_png_files_in_current_dir()
