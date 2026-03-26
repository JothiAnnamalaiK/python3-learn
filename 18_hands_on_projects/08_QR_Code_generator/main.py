"""
python library: qrcode
pip install qrcode

documentation: https://pypi.org/project/qrcode/
"""

import qrcode
import os

url = input("Enter your url: ")

filepath = os.path.join(os.path.dirname(__file__), "qr-gen")

filename = input("Enter the filename to save the QR code (without extension): ")

if filename.strip() == "":
    filename = "qr_code"

file_full_path = os.path.join(filepath, f"{filename}.png")

img = qrcode.make(url)

# img.save(f"{filname}.png")
img.save(file_full_path)


# https://dariusforoux.com/8-online-business-ideas/
