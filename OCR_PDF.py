import subprocess
import fitz  # PyMuPDF for PDF manipulation
import pytesseract
from PIL import Image
import io
#! (tf) C:\Users\admin\Desktop\lstm paper>          set PATH=C:\Users\admin\miniconda3\envs\tf\Scripts;%PATH%
#! set path teseract
#! set path ghostscript
import subprocess
import fitz  # PyMuPDF for PDF manipulation
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io
def extract_pages(input_pdf, output_pdf, start_page, end_page):
    # Open the source PDF.
    with fitz.open(input_pdf) as pdf:
        # Create a new PDF to store the extracted pages.
        writer = fitz.open()
        for page_num in range(start_page - 1, end_page):  # PyMuPDF is 0-indexed
            writer.insert_pdf(pdf, from_page=page_num, to_page=page_num)
        # Write the extracted pages to the output PDF.
        writer.save(output_pdf)
        writer.close()

def ocr_pdf(input_pdf, output_pdf):
    try:
        result = subprocess.run(["ocrmypdf", "--force-ocr", input_pdf, output_pdf], check=True, text=True, capture_output=True)
        print(f"OCR complete. Output saved to: {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"Standard Error Output: {e.stderr}")
        print(f"An error occurred during OCR: {e}")
    except FileNotFoundError:
        print("ocrmypdf is not installed or not found in PATH.")

# Example usage
input_pdf = "WT-web technology akash.pdf"
pages_pdf = "WT-web technology akash.pdf_pages_0_5825.pdf"  # Temporary PDF with extracted pages
output_pdf = "WT-web technology akash.pdf_full2.pdf"

# Extract pages 95-105
extract_pages(input_pdf, pages_pdf, 0, 18)

# Apply OCR to the extracted pages PDF
ocr_pdf(pages_pdf, output_pdf)
