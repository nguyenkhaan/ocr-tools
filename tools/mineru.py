import subprocess 

def main(file : str, format : str): 
    subprocess.run([
        "mineru", "-p", file, 
        "-o" , f"./outputs/{format}/mineru", 
        "--output_format", format
    ] , check=True)
    