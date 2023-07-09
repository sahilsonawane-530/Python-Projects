# pip install PyPDF2

from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import glob

def Merge():
    '''Merge's a pdf file'''
    
    pdfPath = input("Enter PDF path : ")
    files = glob.glob(f"{pdfPath}*.pdf")

    merger = PdfMerger()
    
    for file in files:
        merger.append(file)
    merger.write(f"{pdfPath}Merged.pdf")
    merger.close()
    print("\nMerged Pdf has been saved successfully.")

def Split():
    '''Split's a pdf file'''

    pdf = input("Enter PDF path : ")
    splitPDF = input("Files to be saved at : ")

    with open(pdf, "rb") as file:
        reader = PdfReader(file)

        for index, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)

            with open(f"{splitPDF}{index+1}.pdf", "wb") as s:
                writer.write(s)
    print("\nSplit Pdf's have been saved successfully.")

def Compress():
    '''Compress's a pdf file'''

    pdfPath = input("Enter PDF path : ")
    
    reader = PdfReader(pdfPath)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    compressPDF = input("File to be saved at : ")

    with open(compressPDF, "wb") as c:
        writer.write(c)
    print("\nCompressed Pdf has been saved successfully.")

def Encrypt():
    '''Encrypt's a pdf file'''

    pdfPath = input("Enter PDF path : ")

    reader = PdfReader(pdfPath)
    writer = PdfWriter()

    password = input("Enter password : ")
    writer.encrypt(user_password=password, use_128bit=True)

    for page in reader.pages:
        writer.add_page(page)

    encryptPDF = input("File to be saved at : ")
    with open(encryptPDF, "wb") as e:
        writer.write(e)
    print("\nEncrypted Pdf has been saved successfully.")

def Decrypt():
    '''Decrypt's a pdf file'''
    
    pdfPath = input("Enter PDF path : ")

    reader = PdfReader(pdfPath)
    writer = PdfWriter()

    if reader.is_encrypted:
        password = input("Enter password : ")
        reader.decrypt(password)
    else:
        print("The file isn't encrypted!")
        exit()

    for page in reader.pages:
        writer.add_page(page)

    decryptPDF = input("File to be saved at : ")
    with open(decryptPDF, "wb") as d:
        writer.write(d)
    print("\nDecrypted Pdf has been saved successfully.")

userInput = int(input("Press 1 for Merge\nPress 2 for Split\nPress 3 for Compress\nPress 4 for Encryption\nPress 5 for Decryption\n"))

if (userInput == 1):
    Merge()

elif (userInput == 2):
    Split()

elif (userInput == 3):
    Compress()

elif (userInput == 4):
    Encrypt()

elif (userInput == 5):
    Decrypt()

else:
    raise ValueError("Enter valid value")