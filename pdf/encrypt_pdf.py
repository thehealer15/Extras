import PyPDF2 as p 

"""
Encrypt a pdf
There are 2 types of passwords
    1. Owner Passwords
    2. User Passwords

PyPDF2 supports only pdf passwords
provides 2 types of encryption 
    1. 40 bit
    2. 128 bit

AES method is used => Advance Encryption System
"""

# we will create a pdf with same content which will have passwords
# we will not encrypt original pdf
pdf=p.PdfFileReader("file.pdf")
writer=p.PdfFileWriter()

for i in range(pdf.getNumPages()):
    writer.addPage(pdf.getPage(i))
    
#encrypt(user_pwd, owner_pwd=None, use_128bit=True)
writer.encrypt(user_pwd="PassWord",owner_pwd= None,use_128bit=True)
with open("Encrypted.pdf",'wb') as output:
    writer.write(output)