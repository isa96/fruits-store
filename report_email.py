#!/usr/bin/env python3

import datetime
import json
import os
import sys

import emails
import reports
from operator import itemgetter


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def process_data(data):
    summary_list = []
    new_data = sorted(data, key=itemgetter('name'))
    for item in new_data:
        summary = [
            "",
            "name: {}".format(item['name']),
            "weight: {} lbs".format(item['weight'])
        ]
        summary_list.append(summary)

    return summary_list


def generate_info(data):
    info = process_data(data)
    all_info = []
    for item in info:
        info_data = "<br/>".join(item)
        all_info.append(info_data)
    return "<br/>".join(all_info)


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("fruits.json")
    file = "processed.pdf"

    # depending on windows use below
    destination_dir = os.path.join(os.path.abspath("/"), os.getcwd(), "tmp")

    # depending on linux use below
    # destination_dir = os.path.join(os.path.abspath("/"), "tmp")
    # destination_dir = os.path.join(os.sep, "tmp")

    # Make /tmp/ directory
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    attachment = os.path.join(destination_dir, file)

    # Generate pdf by reports.py
    date = datetime.datetime.now().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(date)
    paragraph = generate_info(data)
    print(paragraph)

    reports.generate_report(attachment, title, paragraph)

    # Sending Email by emails.py
    sender = "automation@example.com"
    # fetch username on qwiklabs
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
