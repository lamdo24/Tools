#Split a PDF file to n pages

import re, PyPDF2, os

path = input("\nInput the directory path that all the PDF files contained will be merged (e.g.,: C:\\Users\\Desktop\\Presentations): \n")

path.replace("\\","\\\\")

os.chdir(path)

wf = input("\nInput your file name, case insensitive, and no \".pdf\" needed, but it should be correct:\n")

#Do the file name
if not wf.endswith(".pdf"):
    wf = wf + ".pdf"

for file in os.listdir("."):
    if file.startswith("FINAL.pdf"):
        os.remove(file)

file_name = []

for file in os.listdir("."):
    if file.endswith(".pdf"):
        file_name.append(file)

for file in file_name.copy():
    if file.lower() != wf.lower():
        file_name.remove(file)

name = file_name[0]

inputFile = PyPDF2.PdfReader(open(name,"rb"))

count = int(input("\nInput the number of pages you would like your split your file to:\n"))

print("\nIn progress...")

for i in range(0,len(inputFile.pages),count):
    outputFile = PyPDF2.PdfWriter()
    outputFile.add_page(inputFile.pages[i])
    for j in range(1,count):
        if i+j <len(inputFile.pages):
            outputFile.add_page(inputFile.pages[i+j])
    with open("FINAL_%s-%s.pdf" %(i+1, i+count), "wb") as outputStream:
        outputFile.write(outputStream)

print("\nThe task is completed.\nThe final files are in your input directory, name \"FINAL-startpage-endpage.pdf\".\nPress Enter to close this tool.")

input("")  #To prevent closing this tool without announcement.
