from modules.pdf_loader import PDFLoader

pdf_path = "data/uploads/sample.pdf"

loader = PDFLoader(pdf_path)

text = loader.extract_text()

print("=" * 60)
print("Extracted Text")
print("=" * 60)
print(text[:1000])  # Print first 1000 characters