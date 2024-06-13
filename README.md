# PDF-OCR Toolkit

## Description
This toolkit is designed to perform Optical Character Recognition (OCR) on PDF documents. It provides utilities to extract specific pages from a PDF file and apply OCR to generate searchable text within those pages. The project utilizes Python libraries including PyMuPDF (Fitz), PIL (Python Imaging Library), and Tesseract-OCR.

## Features
- **Page Extraction**: Extract specific pages from a PDF file.
- **OCR Processing**: Convert images or non-searchable PDF pages into searchable text format.

## Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- PyMuPDF (Fitz)
- PIL (Python Imaging Library)
- Tesseract-OCR
- Ghostscript (for PDF processing)
- OCRmyPDF (for advanced OCR processing)

### Setting up the Environment
1. **Clone the Repository**: Clone this repository to your local machine.
   git clone [repository-url]
### Install Dependencies
Install the required Python libraries.
pip install -r requirements.txt
## Usage

### Extracting Pages from PDF
To extract pages from a PDF, use the `extract_pages` function. For example, to extract pages 1 to 18:
input_pdf = "path_to_your_pdf.pdf"
output_pdf = "extracted_pages.pdf"
extract_pages(input_pdf, output_pdf, 1, 18)

### Applying OCR
To apply OCR to the extracted PDF pages:
```python
ocr_pdf(output_pdf, "output_with_ocr.pdf")
