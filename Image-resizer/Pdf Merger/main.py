import PyPDF2

merger= PyPDF2.PdfMerger
pdffiles = ["1.pdf","2.pdf"]
for filename in pdffiles:
    pdffile = open(filename,'rb')
    pdfreader = PyPDF2.PdfReader(pdffile)
    merger.append(filename)

merger.write("merged.pdf")