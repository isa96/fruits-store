#!/usr/bin/env python3
import os

from PIL import Image

# depending on windows use below
imagesDirectory = os.path.join("supplier-data", "images", "")


# depending on linux use below
# if PermissionError: [Errno 13] Permission denied: '/supplier-data' delete os.sep
# imagesDirectory = os.path.join(os.sep, "supplier-data", "images", "")


def create_destination():
    """Make directory for destination /opt/icons/"""
    # check if directory already created
    if not os.path.exists(imagesDirectory):
        os.makedirs(imagesDirectory)


def manipulate_image(infile):
    """Manipulate Image File
    - Rotate the image 90° clockwise
    - Resize the image from 192x192 to 128x128
    - Save the image to a new folder in .jpeg format"""

    # declares a location image and a new image location
    image_loc = os.path.join(imagesDirectory, infile)

    # make exception handle for manipulating image
    try:
        with Image.open(image_loc) as img:
            new_img = img.resize((600, 400)).convert("RGB")
            new_img.save(image_loc.replace(".tiff", ".jpeg"), "JPEG")
        print("Success convert {}".format(infile))
    except OSError:
        print("cannot convert", infile)


def prosessing_image():
    """Iterates over the file name in the directory"""
    # looping through on name file
    # os.listdir to list all file on directory
    for infile in os.listdir(imagesDirectory):
        # continue when .DS_Store file
        if not infile.endswith('.tiff'):
            continue
        manipulate_image(infile)


if __name__ == '__main__':
    create_destination()
    prosessing_image()
