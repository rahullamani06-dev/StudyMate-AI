from modules.ppt_loader import PPTLoader

ppt_path = "data/uploads/sample.pptx"

loader = PPTLoader(ppt_path)

text = loader.extract_text()

print("=" * 60)
print("Extracted PPT Text")
print("=" * 60)
print(text)