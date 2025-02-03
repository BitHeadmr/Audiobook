import pyttsx3
import PyPDF2
book=open("robot-programming.pdf",'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)

speaker=pyttsx3.init()
for num in range(2, pages):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    #rare is the speech speed
    engine.setProperty("rate", 200)
    #female voice change by the video id
    engine.setProperty("voice",voices[0].id)
    page=pdfreader.getPage(2)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()