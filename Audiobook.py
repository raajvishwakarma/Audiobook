import pyttsx3
from PyPDF2 import PdfFileReader
book = open('Path/PythonDefine.pdf', 'rb')
pdfReader = PdfFileReader(book)    # object of PdfFileReader class

print(pdfReader.numPages)

object = pyttsx3.init()        

page = pdfReader.getPage(2)          
text = page.extractText()
object.setProperty('rate',100)
object.save_to_file(text, 'Path/speech.mp3')
object.say(text)     
object.runAndWait()

















"""
object = p.init()                    #object is object of pyttsx3
object.say("Hey, I am you partner in programming")
object.runAndWait()

speakingrate = object.getProperty('rate')      #rate of speaking
print(speakingrate)
object.setProperty('rate',100)
object.say("Hey, I am you partner in programming for tonight")
object.runAndWait()

voice = object.getProperty('voices')
print(voice)
object.setProperty('voice',voice[1].id)   # voice[0] for male and voice[1] for female  and id is an attribute

object.say("Hey, I am you partner in programming for tonight")
object.runAndWait()
"""
"""
object = p.init()                    #object is object of pyttsx3
object.setProperty('rate',150)
object.say("Hey, I am you partner in programming for tonight")
object.runAndWait()
object.stop()
# To save the audio in a file
object.save_to_file("Hey, I am you partner in programming for tonight", 'Audiobook.mp3')
object.runAndWait()
"""
