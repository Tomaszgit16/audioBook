import PyPDF2
import pyttsx3

# Read as binary book rb
book = open('MySQL.pdf', 'rb')
# Read book
pdfReader = PyPDF2.PdfFileReader(book)

# Print number of pages - from 8 more text
pages = pdfReader.numPages
print(pages)

# 4 lines to start talk, change of voice
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
# In programming page 8 is 7 because it starts indexing from 0

# Beyond 1 page with for loop from 7 to pages - print(pages) - 111
for num in range(7, pages):
    page = pdfReader.getPage(num)
    # Extract text
    text = page.extractText()
    speaker.say(text)
    # speaker.say('Look Mama I can talk')
    speaker.runAndWait()
    # install pip isntall pyPDF2


