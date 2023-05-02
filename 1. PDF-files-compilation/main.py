import PyPDF2, os, re

print("\nChương trình này ghép các file PDF trong folder mà bạn nhập thành 1 file PDF duy nhất.")
print("\nNếu bạn muốn sắp xếp các file theo thứ tự bạn chọn, hãy đặt tên file theo định dạng \"STT.ten file\" (VD: 1.abc.pdf).")
print("Nếu không, các file sẽ được sắp xếp theo thứ tự tăng dần.\n")

path = input("Nhập đường dẫn của folder chứa các file PDF bạn muốn ghép (VD: C:\\Users\\Desktop\\Presentations): \n")

print("\nĐang thực hiện...")

# Thay đổi \ thành \\ để bất kỳ đường dẫn nào cũng chạy được
path.replace("\\","\\\\")

os.chdir(path)

Name = []

# Xoá file kết quả (nếu có), mục đích là để có thể chạy nhiều lần
for files in os.listdir("."):
    if files.startswith("COMPILATION.pdf"):
        os.remove(files)

#Chọn các file PDF để ghép
for files in os.listdir("."):
    if files.endswith(".pdf"):
        Name.append(files)

#Đếm số lượng file bắt đầu bằng số để chọn cách sắp xếp cho phù hợp. Ý tưởng là nếu tất cả các file đều bắt đầu bằng số
#thì mới sắp xếp theo số, không thì sắp xếp theo thứ tự tăng dần
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

print("\nĐã ghép xong các file.\nFile đã ghép nằm tại folder bạn đã nhập và tên là \"COMPILATION.pdf\".\nNhấn Enter để thoát chương trình.")

input("")

