import qrcode
from PIL import Image  # For potential logo (install: pip install qrcode[pil

# Create customizable QR object
qr = qrcode.QRCode(
    version=None,  # Auto-fit to data length
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High tolerance (30% damage)
    box_size=15,  # Pixels per module: higher = larger/sharper (e.g., 10=small, 20=poster-sized)
    border=4,  # Quiet zone thickness in modules (min 4 for scanners)
)

qr.add_data("https://open.spotify.com/track/5R07oWK8UxfS6gxNuEXR0Q?si=a61985e4731a4d26")
qr.make(fit=True)

# Render with enhancements
img = qr.make_image(
    fill_color=(233, 30, 99),  # Foreground color (hex/RGB too)
    back_color=(13, 27, 42),    # Background
)

img.save("Love you Like A Love Song Baby III.jpg")
print("Enhanced QR saved! Test scan it.")

#  Use these clour palate for luxury and eye catching QR 
"""
Rose Quartz Navy
fill_color=(233, 30, 99),
back_color=(13, 27, 42)

Eternal Black Gold
fill_color=(181, 137, 0),
back_color=(0, 0, 0)

Neon Cyan Abyss
fill_color=(0, 212, 255),
back_color=(2, 0, 36)

"""