#!/usr/bin/env python3

import os

import requests

# external ip address for qwiklabs
external_tip = "34.70.247.156"
url = "http://{}/upload/".format(external_tip)

# depending on windows use below
images_dir = os.path.join("supplier-data", "images", "")

# depending on linux use below
# if PermissionError: [Errno 13] Permission denied: '/supplier-data' delete os.sep
# images_dir = os.path.join(os.sep, "supplier-data", "images", "")


# list name file in /data/feedbacks
image_list = [item for item in os.listdir(images_dir) if item.endswith(".jpeg")]


def prosess_image():
    """
    Performs HTTP protocol to post dict data requests to the url from the extracted file.txt
    """
    if len(image_list) != 0:
        for name_file in image_list:
            file_dir = os.path.join(images_dir, name_file)
            with open(file_dir, 'rb') as file:
                response = requests.post(url, files={'file': file})
            if response.ok and response.status_code == 201:
                print("Success")
            else:
                response.raise_for_status()
                raise Exception("GET failed with status code {}".format(response.status_code))


if __name__ == '__main__':
    prosess_image()
