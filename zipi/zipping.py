"""
Many ==> One
Deflate Algo is used to compress 
Why .zip ?
- reduced size
- encapsulate data in single file

"""

# printing contents  of python file
from zipfile import ZipFile # Note Capital  
# builting file

file_name="MyZip.zip"

f=ZipFile(file_name,'r')
f.printdir()
f.close()