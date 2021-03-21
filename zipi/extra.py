from zipfile import ZipFile

path="MyZip.zip"

# extracting all files
f=ZipFile(path,'r')
f.extractall()
print("All Files Extracted")

# f.namelist() => lists names of all files
for i in f.namelist():
    print(i)

# TO extract a specific folder use if - else and name of folder 