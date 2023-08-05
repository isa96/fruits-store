#!/usr/bin/env python3

import json
import os

import requests

# external ip address for qwiklabs
external_ip = "34.70.247.156"
url = "http://{}/fruits/".format(external_ip)

# depending on windows use below
images_dir = os.path.join("supplier-data", "images", "")
desc_dir = os.path.join("supplier-data", "descriptions", "")

# depending on linux use below
# images_dir = os.path.join(os.sep, "supplier-data", "images", "")
# desc_dir = os.path.join(os.sep, "supplier-data", "images", "")

# list name file in /data/feedback
images_list = [item for item in os.listdir(images_dir) if item.endswith(".jpeg")]
desc_list = os.listdir(desc_dir)


def prosess_text():
    """
    Used to perform the process of changing from file.txt to a list dictionary
    :rtype: list
    :return: list of dict text
    """
    list_dict = []
    key = ['name', 'weight', 'description', 'image_name']
    for file_index, name_file in enumerate(desc_list):
        file_dir = os.path.join(desc_dir, name_file)
        with open(file_dir) as file:
            text_list = [n.strip() for n in file]
            text_dict = {}
            for index, value in enumerate(text_list):
                if key[index] == 'weight':
                    value = value.replace(" lbs", "")
                    text_dict[key[index]] = int(value)
                else:
                    text_dict[key[index]] = value
            text_dict[key[3]] = images_list[file_index]
            list_dict.append(text_dict)
    return list_dict


def post_request():
    """
    Performs HTTP protocol to post dict data requests to the url from the extracted file.txt
    """
    p = prosess_text()
    for data in p:
        response = requests.post(url, json=data)
        if response.ok and response.status_code == 201:
            print("Success")
        else:
            response.raise_for_status()
            raise Exception("GET failed with status code {}".format(response.status_code))


def make_json():
    with open('fruits.json', 'w') as fruits_json:
        json.dump(prosess_text(), fruits_json, indent=2)


if __name__ == '__main__':
    make_json()
    post_request()
