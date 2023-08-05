#!/usr/bin/env python3
import os
from PIL import Image

# depending on windows use below
imagesDirectory = os.path.join("supplier-data", "images", "")
# depending on linux use below
# if PermissionError: [Errno 13] Permission denied: '/supplier-data' delete os.sep
# imagesDirectory = os.path.join(os.sep, "supplier-data", "images", "")

for infile in os.listdir(imagesDirectory):
    image = os.path.join(imagesDirectory, infile)
    try:
        with Image.open(image) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        pass

"""
Task :

~/supplier-data/images directory to the following specifications:
1. Size: Change image resolution from 3000x2000 to 600x400 pixel
2. Format: Change image format from .TIFF to .JPEG
"""