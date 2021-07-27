import pyttsx3
from PyPDF2 import PdfFileReader
book = open('AddPath/PythonDefine.pdf', 'rb')
pdfReader = PdfFileReader(book)    # object of PdfFileReader class

print(pdfReader.numPages)

object = pyttsx3.init()        

page = pdfReader.getPage(2)          
text = page.extractText()
object.setProperty('rate',100)
object.save_to_file(text, 'AddPath/speech.mp3')
object.say(text)     
object.runAndWait()
