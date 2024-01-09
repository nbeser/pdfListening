import pyttsx3, PyPDF2

speaker = pyttsx3.init()
pdfReader = PyPDF2.PdfReader("sample.pdf", "rb")

for pageNum in range(len(pdfReader.pages)):
    text = pdfReader.pages[pageNum].extract_text()
    rawText = text.strip().replace("\n", " ")

speaker.save_to_file(rawText, "sample.mp3")

speaker.runAndWait()
speaker.stop()
