import pymupdf4llm

def main(file: str, format: str):
    # convert PDF -> markdown/text
    md = pymupdf4llm.to_markdown(file)
    
    output_path = f"./outputs/{format}/pymupdf_llm/j_0057.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)