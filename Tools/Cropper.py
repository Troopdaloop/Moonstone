import os
from PIL import Image

# Constants
PLAYER_WIDTH = 800
PLAYER_HEIGHT = 800

# Input and output directories
input_folder = "G:/My Drive/Python/Moonstone/assets/images/Player/BlueKnight/Attack1/player_frames"
output_folder = "G:/My Drive/Python/Moonstone/assets/images/Player/BlueKnight/Attack1/unified_cropped_frames"
os.makedirs(output_folder, exist_ok=True)

# Load reference frames
frame_2_path = os.path.join(input_folder, "frame_2.png")
frame_3_path = os.path.join(input_folder, "frame_3.png")

frame_2 = Image.open(frame_2_path).convert("RGBA")
frame_3 = Image.open(frame_3_path).convert("RGBA")

bbox_2 = frame_2.getbbox()
bbox_3 = frame_3.getbbox()

# Combine bounding boxes to get unified box
left = min(bbox_2[0], bbox_3[0])
upper = min(bbox_2[1], bbox_3[1])
right = max(bbox_2[2], bbox_3[2])
lower = max(bbox_2[3], bbox_3[3])
unified_bbox = (left, upper, right, lower)

# Apply unified crop and resize to all frames
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".png"):
        path = os.path.join(input_folder, filename)
        img = Image.open(path).convert("RGBA")

        cropped = img.crop(unified_bbox)
        resized = cropped.resize((PLAYER_WIDTH, PLAYER_HEIGHT), Image.Resampling.LANCZOS)

        output_path = os.path.join(output_folder, filename)
        resized.save(output_path)

print(f"All frames cropped using unified bounding box and saved to '{output_folder}'.")
