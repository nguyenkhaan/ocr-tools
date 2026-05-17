import os
from docling.document_converter import DocumentConverter
# from docling.document_converter import Dock
def main(file: str, format: str):
    os.makedirs(f"./outputs/{format}/docling", exist_ok=True)

    converter = DocumentConverter()
    result = converter.convert(file)

    md = result.document.export_to_markdown()

    output_path = f"./outputs/{format}/docling/j_0057.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)