from pathlib import Path 
from tools.marker_pdf import main as marker_pdf 
from tools.docling import main as docling_pdf 
from tools.pymupdf_llm import main as pymupdf_pdf
from tools.mineru import main as mineru_pdf 
TRAINING_FILES = [
    'j_0057.pdf'  # Testing with 1 document first 
] 
FILE_PATHS = [
    Path(f'./lava-challenge-2026/train_pdfs/train_pdfs/{file}').resolve() 
    for file in TRAINING_FILES 
]
import time 
def handle_parse_pdf(callback , file , format): 
    start = time.perf_counter() 
    callback(file , format) 
    end = time.perf_counter() 
    return (end - start) 
    

if __name__ == '__main__': 
    # markdown 
    # marker - pdf  
    # t1 = handle_parse_pdf(marker_pdf , FILE_PATHS[0] , 'markdown') 532.6957
    # t2 = handle_parse_pdf(docling_pdf , FILE_PATHS[0] , 'markdown') 81.2590
    # t3 = handle_parse_pdf(pymupdf_pdf , FILE_PATHS[0] , 'markdown')  5.5660
    t4 = handle_parse_pdf(mineru_pdf , FILE_PATHS[0] , 'markdown')  
    # print(f'Marker pdf run in {t1:.4f} seconds')
    # print(f'Docling pdf run in {t2:.4f} seconds')
    print(f'Mineru run in {t4:.4f} seconds')
    