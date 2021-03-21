import PyPDF2 as p 

# depends on decoder so there is no assurence it will read the text

location="Testpdf.pdf"

with open(location,'rb') as f:
    pdf=p.PdfFileReader(f)
    page=pdf.getPage(0)
    print(page.extractText())

    # to read whole pdf and flush in text file

    no=pdf.numPages
    with open("text.txt",'a') as f2:
        for i in range(no):
            f2.write(pdf.getPage(i).extractText())


    