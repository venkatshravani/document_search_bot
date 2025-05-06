# utils/file_utils.py
import os
from PyPDF2 import PdfReader
from django.core.files.storage import default_storage

# Utility functions
def save_file(file, storage=default_storage):
    # Saving logic
    file_name = os.path.join('uploads', file.name)
    path = storage.save(file_name, file)
    return storage.url(path)

def extract_text_from_pdf(file_path):
    # PDF text extraction logic
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def chunk_text(text, chunk_size=2000):
    # Chunking text into smaller pieces
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks
