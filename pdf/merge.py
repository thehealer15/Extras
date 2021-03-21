import PyPDF2 as p 
#   merging pdf

# I took 2 pdf file and newFile
# Now I will merge them


location=["file.pdf","newFile.pdf"]

writer=p.PdfFileWriter()

for i in location:
    pdf=p.PdfFileReader(i,'rb') 

    # by this we will handle having multiple pages in files
    # page index starts from 0
    for page in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(page))

merged_pdf_name= "merged.pdf"

with open(merged_pdf_name,'wb') as f:
    writer.write(f)

print("done")
