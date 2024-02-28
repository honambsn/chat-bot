import pdfplumber

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Provide the path to your PDF file
pdf_file_path = "E:\\KHTN\\Chuyên đề tốt nghiệp MMT\\Topic1_OpenAI.pdf"
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text)
