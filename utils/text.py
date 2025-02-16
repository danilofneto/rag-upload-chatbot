import pandas as pd
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def process_files(files):
    text = ""

    for file in files:
        file_name = file.name
        if file_name.endswith('.pdf'):
            pdf = PdfReader(file)
            for page in pdf.pages:
                text += page.extract_text()
        elif file_name.endswith('.xlsx') or file_name.endswith('.xls'):
            excel_data = pd.read_excel(file)
            for column in excel_data.columns:
                text += excel_data[column].to_string(index=False)

    return text

def create_text_chunks(text):

    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    return chunks
