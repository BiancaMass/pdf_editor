"""
This is your main script that acts as an entry point to your PDF editing tool.  It might contain
the user interface (CLI or GUI), configuration setup,  and calls to functions from the
pdf_operations module.
"""
from pdf_operations import BasicPDFOperations


pdf_path = "/Users/bmassacci/Downloads/978-981-19-6897-6.pdf"


pdf_operations = BasicPDFOperations()
try:
    pdf_operations.text_extractor(pdf_path, [1, 2, 3], "/Users/bmassacci/Desktop/deleteme.txt")
except Exception as e:
    print(f"Error: {str(e)}")
