import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom
os.listdir('.')
document = zipfile.ZipFile('VINOTH.docx')

#name = ZipFile.read(document, pwd=None)

document.namelist()
