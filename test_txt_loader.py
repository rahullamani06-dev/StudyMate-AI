from modules.txt_loader import TXTLoader

txt_path = "data/uploads/sample.txt"

loader = TXTLoader(txt_path)

text = loader.extract_text()

print("=" * 60)
print("Extracted TXT Text")
print("=" * 60)
print(text)