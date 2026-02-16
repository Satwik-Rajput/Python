import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
import os

# Use CURRENT directory (where your script is running)
current_dir = os.getcwd()
print(f"Working in: {current_dir}")
print(f"Files here: {os.listdir('.')[:5]}")  # Show first 5 files

# QR with HIGH error correction
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data("https://open.spotify.com/track/5R07oWK8UxfS6gxNuEXR0Q?si=a61985e4731a4d26")
qr.make(fit=True)

# Create styled QR (NO logo needed)
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    color_mask=RadialGradiantColorMask(
      back_color=(240, 233, 223),
center_color=(173, 166, 150),
edge_color=(86, 44, 44)
    )
)

# Save in current directory
output_path = os.path.join(current_dir, "QR_Code_III.jpg")  # It give the location of your current directory path
img.save(output_path)
print(f"✅ QR saved to: {output_path}")

"""If you don't want to give your directory path you can comment out all your Os fuction and simply
   save your OR image just by using .save("file_name.jpg")"""
# img.save("music.jpg")

#  Use these gradient clour palate for luxury and eye catching QR 
"""Midnight Gold
back_color=(26, 26, 46),
center_color=(22, 33, 62),
edge_color=(239, 192, 123)

Platinum Elegance
back_color=(44, 62, 80),
center_color=(52, 73, 94),
edge_color=(236, 240, 241)

Wine Taupe
back_color=(240, 233, 223),
center_color=(173, 166, 150),
edge_color=(86, 44, 44)

Black Gold Fusion
back_color=(27, 27, 27),
center_color=(66, 52, 22),
edge_color=(221, 153, 0)


"""
