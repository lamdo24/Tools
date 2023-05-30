#Create a new file with selected pages
import re, PyPDF2, os

path = input("\nInput the directory path that all the PDF files contained will be merged (e.g.,: C:\\Users\\Desktop\\Presentations): \n")

path.replace("\\","\\\\")

os.chdir(path)

wf = input("\nInput your file name, case insensitive, and no \".pdf\" needed, but it should be correct:\n")

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

n = input("\nInput the page numbers. E.g.:10,15-20,45\n")

n_split = re.split("\s|,|,+\s",n)

list = []

for i in n_split:
    list.append(i)
    if i == "":
        list.remove(i)

list_1 = []

for i in list:
    if re.match("[0-9]+-[0-9]+",i):
        list_1.append(i)

list_2 = []
for i in list_1:
    for j in range(int(i.split("-")[0]),int(i.split("-")[1])+1):
        list_2.append(j)


del list_1

list_1 = []

for i in list:
    if not re.match("[0-9]+-[0-9]+",i):
        list_1.append(i)

for i in list_2:
    list_1.append(int(i))

list_file = []

for i in list_1:
    list_file.append(int(i))

del list_1, list_2

list_file.sort()

writer = PyPDF2.PdfWriter()

newFile = PyPDF2.PdfReader(open(name,"rb"))

for number in list_file:
    writer.add_page(newFile.pages[number-1])

writer.write(open("FINAL.pdf","wb"))

writer.close()

print("\nThe task is completed.\nThe final files are in your input directory, name \"FINAL.pdf\".\nPress Enter to close this tool.")

input("")  #To prevent closing this tool without announcement.
