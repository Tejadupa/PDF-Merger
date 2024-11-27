from PyPDF2 import PdfMerger
import os
from os.path import curdir

merger=PdfMerger()

list_of_files=os.listdir(curdir)

for file_item in list_of_files:
    if '.pdf' in file_item:
        print(file_item)
        merger.append(file_item)

merger.write("Resultant.pdf")
merger.close()