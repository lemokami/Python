#having some fun with PDF using PyPdf2 library
import PyPDF2 as pypd2 #inporting PyPDF (Third-party library->should be installed before running the program)
import os #importing the os module

#changing the directory to Pdf folder in Files folder
os.chdir("Files\\Pdfs") #for windows users
#os.chdir("Files/Pdfs") # for linux users

pdf1 = open("20000Leagues.pdf","rb") #opening the PDF1 in binary mode since PDF are written in binary
pdf2 = open("aroundTheWorldIn80.pdf","rb")#opening the PDF2 in binary mode since PDF are written in binary

reader1 = pypd2.PdfFileReader(pdf1) # a reader object to read the pdf
reader2 = pypd2.PdfFileReader(pdf2) # a reader object to read the pdf

#Prints the total no of pages
print(f"No of pages in PDF 1:{reader1.numPages}")
print(f"No of pages in PDF 2:{reader2.numPages}\n")


#prints the first page of each PDFs
print(f"First Page of PDF 1:\n\n{reader1.getPage(0).extractText()}\n\n")
print(f"First Page of PDF 2:\n\n{reader2.getPage(0).extractText()}\n\n")

writer = pypd2.PdfFileWriter() #a writer object to write a pdf

#loop to run through each page in pdf1 and write using the writer
for i in range(reader1.numPages):
    page = reader1.getPage(i)
    writer.addPage(page)

#loop to run through each page in pdf2 and write using the writer
for i in range(reader2.numPages):
    page = reader2.getPage(i)
    writer.addPage(page)

#now the two pages are written in the writer which is in the volatile memory

mergf = open("CombinedPDF.pdf","wb") #opening/making a PDF file to store the merged PDFs

writer.write(mergf) #storing the Merged PDF

#closing the opened files
mergf.close()
pdf1.close()
pdf2.close()
