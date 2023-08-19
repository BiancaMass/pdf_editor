""" This module houses functions for various PDF operations like splitting, merging, rotating,
adding annotations, extracting text, etc."""

import PyPDF2


class BasicPDFOperations:
    def __init__(self):
        pass

    @staticmethod
    def text_extractor(self, input_path, pages, output_path):
        try:
            # Call the read_pdf method to initialize self.pdf_reader
            # self.read_pdf(input_path)
            with open(input_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Initialize raw text variable
                raw_text = ""

                # Iterate through the specified pages
                for page_num in pages:
                    # Check if the page number is within the valid range
                    if 0 < page_num <= len(pdf_reader.pages):
                        # Get the specified page
                        page = pdf_reader.pages[page_num - 1]  # Adjust for 0-based indexing

                        # Extract text from the page
                        raw_text += page.extract_text()

                # Write the extracted raw text to the output file
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(raw_text)
        except Exception as e:
            raise Exception(f"An error occurred while extracting text: {str(e)}")



    # TODO: Extracting a single or multiple pages and saving to a new pdf

    # TODO: Pasting pages together




# TODO For the future
# rotating and cropping
# encrypting and decrypting
#
