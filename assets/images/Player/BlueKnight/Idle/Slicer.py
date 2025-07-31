from PIL import Image
import os

# Update the number of frames num_frames to match

# Load the sprite sheet
sprite_sheet = Image.open("BlueKnightSpriteSheet.png")  # Replace with your actual file name

# Get dimensions
sheet_width, sheet_height = sprite_sheet.size
num_frames = 11
frame_width = sheet_width // num_frames
frame_height = sheet_height

# Create output directory
output_dir = "player_frames"
os.makedirs(output_dir, exist_ok=True)

# Slice and save each frame
for i in range(num_frames):
    left = i * frame_width
    upper = 0
    right = left + frame_width
    lower = frame_height
    frame = sprite_sheet.crop((left, upper, right, lower))
    frame.save(os.path.join(output_dir, f"frame_{i}.png"))

print(f"Sliced {num_frames} frames and saved to '{output_dir}' directory.")
