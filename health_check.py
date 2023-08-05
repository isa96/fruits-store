#!/usr/bin/env python3

import os
import shutil
import socket

import psutil

import emails

"""
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""

subject_list = ["Error - CPU usage is over 80%", "Error - Available disk space is less than 20%",
                "Error - Available memory is less than 500MB", "Error - localhost cannot be resolved to 127.0.0.1"]


def check_cpu_usage():
    """Verifies that there's enough unused CPU."""
    usage = psutil.cpu_percent(1)
    if usage > 80:
        specified_email(subject_list[0])
    else:
        print("CPU Usage OK")


def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    if free < 20:
        specified_email(subject_list[2])
    else:
        print("Disk Usage OK")


def check_memory_usage():
    """Verifies that there's available memory"""
    values = psutil.virtual_memory()
    total = values.available >> 20
    if total < 500:
        specified_email(subject_list[3])
    else:
        print("Memory Usage OK")


def check_localhost():
    """hostname 'localhost' can be resolved to '127.0.0.1'"""
    localhost = socket.gethostbyname('localhost')
    if localhost != "127.0.0.1":
        specified_email(subject_list[3])
    else:
        print("Hostname OK")


def specified_email(subject):
    # Sending Email by emails.py
    sender = "automation@example.com"
    # fetch username on qwiklabs
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)


def main():
    check_cpu_usage()
    check_cpu_usage()
    check_disk_usage("/")
    check_localhost()


if __name__ == '__main__':
    main()
