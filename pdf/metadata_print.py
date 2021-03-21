import PyPDF2 as p 

# Extracting Meta data from pdf i.e. info like name of author, number of pages, title day of release
# I kept 1 pdf from same folder if same folder give name of in other folder, give path


# we need pdfFileReader class in PyPDF2 we can read pdf with help of class 

location_of_file="file.pdf" # You can give as /foldername/filename as well


# why open in binary ?
# as txt supports plain text only iy can be opened in any file format
# that means we should open images, pdf , zip , .. and any other files in binary formats
with open(location_of_file,'rb') as f: 
    pdf = p.PdfFileReader(f) # file we want to read

    # Now we can use this variable 
    info = pdf.getDocumentInfo() # return dict
    print(info.author) # If you are in windows, while saving on docx there is option to maintain author
    print(info.title) 
    print(info.creator)
    print(info.getText)

    # number of pgaes
    no=pdf.numPages
    print(no,type(no))
    
