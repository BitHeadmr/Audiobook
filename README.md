Installation:
Python has an ocean of libraries that serve various purposes. In this article, we will require two libraries (pyttsx3, PyPDF2) to develop an audiobook.

You can install the libraries from PyPl,

pip install PyPDF2

pip install pyttsx3

1) Read the PDF file:
Python has library PyPDF2 which is built as a PDF toolkit. It allows pdf manipulation in memory. This library is capable of:

extracting document information, such as title, author, etc

splitting documents by page

merging documents by page

cropping pages

merging multiple pages into a single page

encrypting and decrypting PDF files

and more!

We are using this library to split the pdf file page by page, read the text on each page, and send the text to the next layer/step.

2) Initialize Speaker:

Python has a library pyttsx3, that is capable to convert text-to-speech offline. Text that we are reading from a pdf file using the pypdf2 library is fed as an input to the text-to-speech engine.

3) Play the Audiobook:

Extract the text from the pdf file page by page using the PyPDF2 implementation. Loop through each page, by reading the text and feeding it to the pyttsx3 speaker engine. It will read out loud the text from the pdf page.

Loop the process for every page in the pdf file and stop the pyttsx3 speaker engine as last.

Changing Voice, Rate, and Volume of pyttsx3 speaker:

You can tune the speed and volume of speech, and change the voice-over from male to female and vice-versa, depending on your requirements.

Rate of speed:
Initialize the pyttsx3 library, and use getProperty(‘rate’) to get the current speaking rate. Change the rate of speaking using setProperty(‘rate’, x), where x=100 being normal speed (1x).

Voice:

Initialize the pyttsx3 library, and use getProperty(‘voice’) to get the current gender of the speaker. Change the speaker's gender using setProperty(‘voice’, voice[x].id), where x=0 for male and x=1 for female.
