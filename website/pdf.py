import PyPDF2

pdf = open("1357.pdf",'rb')


inputpdf = PyPDF2.PdfFileReader(pdf)
pages_no = inputpdf.numPages
output = PyPDF2.PdfFileWriter()

for i in range(pages_no):
    inputpdf = PyPDF2.PdfFileReader(pdf)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt('joyconboyz179')

    with open("1357.pdf", "wb") as outputStream:
        output.write(outputStream)

pdf.close()