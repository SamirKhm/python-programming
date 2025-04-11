from PyPDF2 import PdfReader, PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("How many pdfs do you want to merge? "))

for i in range(n):
    name=input(f"Enter the name of pdf {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()