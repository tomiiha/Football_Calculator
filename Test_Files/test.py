# Get file listing
import glob, os
file_list = []
os.chdir(r"C:\Users\tihalainen\Desktop\Data Stuff\Data")
for file in glob.glob("*.xlsx"):
    file = file[5:14]
    file_list.append(file)
print(file_list)
