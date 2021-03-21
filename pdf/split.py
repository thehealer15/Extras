import PyPDF2 as p 
"""
logic:
    take 1 page at a time and extract them
    So to split a range deoends on for loop range
"""
location="merged.pdf"
pdf=p.PdfFileReader(location)

with open(location,'rb') as f:
    for page_number in range(pdf.getNumPages()):
        writer= p.PdfFileWriter()
        writer.addPage(pdf.getPage(page_number))

        output= f"page_{page_number+1}.pdf"
        with open(output,'wb') as out:
            writer.write(out)
    
print("Done")