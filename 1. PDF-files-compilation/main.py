import PyPDF2, os, re

print("\nThis tool merges all the PDF files in your input directory to a single PDF file.")
print("\nIf you would like to sort your files in order, please rename your file names as \"No.file_name\" (e.g., 1.abc.pdf).")
print("If not, files will be sorted in the programming default order.\n")

path = input("Input the directory path that all the PDF files contained will be merged (e.g.,: C:\\Users\\Desktop\\Presentations): \n")

print("\nOn progress...")

# Change \ to \\ so any Windows path is worked
path.replace("\\","\\\\")

os.chdir(path)

Name = []

# Delete the Final file (if applicable) to run multiple times
for files in os.listdir("."):
    if files.startswith("COMPILATION.pdf"):
        os.remove(files)

#Store all the PDF file names to a list
for files in os.listdir("."):
    if files.endswith(".pdf"):
        Name.append(files)

#Count the number of files that start with a number to arrange a proper sort. The idea is that if all the file names begin with numbers, these numbers are used to 
#sort the files. Otherwise, the programming default order is applied.
count = 0

for i in Name:
    if re.match("^\d+",i):
        count+=1

if count == len(Name):
    fileName = sorted(Name, key=lambda x: int(re.split("\W+",x)[0]))
else:
    fileName = sorted(Name)

writer = PyPDF2.PdfWriter()

for file in fileName:
    newFile = PyPDF2.PdfReader(open(file,"rb"))
    for pageNum in range(0, len(newFile.pages)):
        page0 = newFile.pages[pageNum]
        writer.add_page(page0)

writer.write(open("COMPILATION.pdf", "wb"))
writer.close()

print("\nThe task is completed.\nThe final file is in your input directory, and is \"COMPILATION.pdf\".\nPress Enter to close this tool.")

input("")  #To prevent closing this tool without announcement.
