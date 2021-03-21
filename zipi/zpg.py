from zipfile import ZipFile
file="railway.jpg"

f= ZipFile("newFile.zip",'w')
f.write(file)
f.write("extra.py")

