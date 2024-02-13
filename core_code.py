from docx import Document
import os

#Defining directory for the generated file
subfolder_path = './generated_files'

if not os.path.exists(subfolder_path):
    os.makedirs(subfolder_path)

document_path = os.path.join(subfolder_path, 'instructions.docx')

# Create a new Document
doc = Document()
doc.save(document_path)

print("Empty Word document created successfully.")