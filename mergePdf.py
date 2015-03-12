import sys
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

pathToPic='pic/front/'
pathToOut='pic/out/'
back = PdfFileReader(open("pic/back/Back.pdf", "rb"))
output = PdfFileWriter()

for filename in os.listdir('pic/front/'):
     if filename != ".DS_Store":
         input1 = PdfFileReader(open(pathToPic+filename, "rb"))
         output.addPage(back.getPage(0))
         output.addPage(input1.getPage(0))
         outputStreamSingle = file(pathToOut+"single_"+filename, "wb")
         output.write(outputStreamSingle)


outputStream = file(pathToOut+"total_"+filename, "wb")
output.write(outputStream)

print("Done.");
