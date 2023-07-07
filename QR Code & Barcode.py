# pip install qrcode
# pip install python-barcode
# pip install "python-barcode[images]"

# pip install pyzbar
# pip install pyzbar[scripts]

import os
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter

from pyzbar.pyzbar import decode
from PIL import Image


def QrCodeGenerator():
    ''' Generate's QR Code '''
    img = qrcode.make(input("Enter data : "))
    filename = input("Enter file name : ")
    type(img)
    img.save(filename)
    print("Your QR Code is saved at", os.path.abspath(filename))

def QrCodeReader():
    ''' Read's QR Code '''
    img = Image.open(input("Enter path : "))
    cont = decode(img)
    print(cont[0].data.decode())

def BarcodeGenerator():
    ''' Generate's Barcode '''
    data = input("Enter data : ")
    filename = input("Enter file name : ")
    with open(filename, "wb") as f:
        EAN13((data), writer=ImageWriter()).write(f)
    print("Your Barcode is saved at", os.path.abspath(filename))

def BarcodeReader():
    ''' Read's Barcode '''
    img = Image.open(input("Enter path : "))
    cont = decode(img)
    print(cont[0].data.decode())

askUser = int(input("Press 1 for QR Code Generator\nPress 2 for QR Code Reader\nPress 3 for Barcode Generator\nPress 4 for Barcode Reader\n"))

if (askUser == 1):
    QrCodeGenerator()

elif (askUser == 2):
    QrCodeReader()

elif (askUser == 3):
    BarcodeGenerator()

elif (askUser == 4):
    BarcodeReader()

else:
    raise ValueError("Enter proper value")
