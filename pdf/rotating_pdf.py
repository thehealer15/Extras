import PyPDF2 as p 
# rotating pdf

location="file.pdf"
with open(location,'rb') as f:
    pdf=p.PdfFileReader(location)
    
    writer=p.PdfFileWriter()
    # why writer?
    # After rotating we need to save as pdf
    page=pdf.getPage(0)
    page.rotateClockwise(90)
    # counterClockwise also there angle must be standard angle i.e. multiple of 90 degree
    # if not passed no rotation
    writer.addPage(page)
    # we added page in writer, still this is RAM if we don't write it won't reflect in ROM - File heandling of Python
    # to export 
    with open("newFile.pdf",'wb') as f2:
        writer.write(f2)
        print("Rotated SuccessFully")