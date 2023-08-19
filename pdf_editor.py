"""
This is your main script that acts as an entry point to your PDF editing tool.  It might contain
the user interface (CLI or GUI), configuration setup,  and calls to functions from the
pdf_operations module.
"""
from pdf_operations import BasicPDFOperations


pdf_path = "/Users/bmassacci/Downloads/978-981-19-6897-6.pdf"


pdf_operations = BasicPDFOperations()
# try:
#     pdf_operations.text_extractor(input_path=pdf_path,
#                                   pages=[1, 2, 3],
#                                   output_path="/Users/bmassacci/Desktop/deleteme.txt")
# except Exception as e:
#     print(f"Error: {str(e)}")


# Example usage
try:
    pdf_operations.extract_pages(pdf_path, [1, 3, 5], "/Users/bmassacci/Desktop/deleteme.pdf")
except Exception as e:
    print(f"Error: {str(e)}")