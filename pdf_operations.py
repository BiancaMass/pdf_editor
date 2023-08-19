from pypdf import PdfReader
# from pathlib import Path

pdf_path = "/Users/bmassacci/Downloads/978-981-19-6897-6.pdf"

print(pdf_path)

pdf_reader = PdfReader(pdf_path)
print(pdf_reader.metadata)

# Extracting text from a page
def text_extractor():
    