from modules.docx_loader import DOCXLoader

docx_path = "data/uploads/sample.docx"

loader = DOCXLoader(docx_path)

text = loader.extract_text()

print("=" * 60)
print("Extracted DOCX Text")
print("=" * 60)
print(text)
