import os
from pathlib import Path
import PyPDF2

directories = [
    "txt_files",
    "pdf_files",
    "document_files",
]

def read_text_file(file_path):
    """Read content from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def read_pdf_file(file_path):
    """Read content from a PDF file."""
    try:
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def read_directories(dirs):
    """Read all text files from specified directories."""
    all_contents = {}
    
    for directory in dirs:
        if not os.path.exists(directory):
            print(f"Directory '{directory}' not found.")
            continue
        
        all_contents[directory] = {}
        
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if filename.endswith('.txt'):
                content = read_text_file(file_path)
            elif filename.endswith('.pdf'):
                content = read_pdf_file(file_path)
            else:
                continue
            
            if content:
                all_contents[directory][filename] = content
    
    return all_contents

if __name__ == "__main__":
    contents = read_directories(directories)
    
    for directory, files in contents.items():
        print(f"\n{directory}:")
        for filename, content in files.items():
            print(f"  - {filename}: {len(content)} characters")
            