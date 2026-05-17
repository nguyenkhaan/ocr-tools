import subprocess

def main(file : str , format: str):  
    subprocess.run([
        "marker_single",
        file,
        "--output_format", format,
        "--output_dir", f"./outputs/{format}/marker_pdf",
    ])