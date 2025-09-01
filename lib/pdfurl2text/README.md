# PDF URL to Text

A simple internal Python library that downloads PDFs from URLs and extracts their text content. Perfect for processing academic papers, research documents, and any PDF accessible via URL.

## Features

- **Direct PDF Download**: Downloads PDFs from any accessible URL
- **Text Extraction**: Extracts text content from PDF files using PyPDF2
- **Smart Filenames**: Automatically generates meaningful filenames
- **Error Handling**: Robust retry logic and comprehensive error handling
- **Batch Processing**: Process multiple PDFs efficiently
- **Logging**: Detailed logging for debugging and monitoring

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup with Virtual Environment (Recommended)

```bash
# Clone or navigate to the library directory
cd lib/pdfurl2text

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Alternative: Direct Installation

```bash
pip install requests PyPDF2
```

## Quick Start

### Basic Usage

```python
from main import PDFDownloader

# Initialize downloader
downloader = PDFDownloader()

# Process a PDF URL
pdf_path, text_path = downloader.process_pdf_url(
    "https://example.com/document.pdf"
)

print(f"PDF: {pdf_path}")
print(f"Text: {text_path}")
```

### Command Line Usage

```bash
# Basic usage
python main.py "https://example.com/document.pdf"

# With custom filename
python main.py "https://example.com/document.pdf" "my_research_paper"
```

## API Reference

### PDFDownloader Class

#### Constructor
```python
PDFDownloader(output_dir="extracted_texts")
```
- `output_dir`: Directory to save extracted files (default: "extracted_texts")

#### Methods

##### `download_pdf(url, filename=None)`
Downloads a PDF from a URL.
- `url`: PDF URL to download
- `filename`: Optional custom filename
- Returns: Path to downloaded PDF or None if failed

##### `extract_text_from_pdf(pdf_path)`
Extracts text content from a PDF file.
- `pdf_path`: Path to the PDF file
- Returns: Extracted text content as string

##### `process_pdf_url(url, custom_filename=None)`
Complete workflow: download PDF, extract text, and save to file.
- `url`: PDF URL to process
- `custom_filename`: Optional custom filename for output
- Returns: Tuple of (pdf_path, text_path) or (None, None) if failed

## Examples

### Process Multiple PDFs

```python
from main import PDFDownloader

urls = [
    "https://example.com/paper1.pdf",
    "https://example.com/paper2.pdf",
    "https://example.com/paper3.pdf"
]

downloader = PDFDownloader()

for url in urls:
    pdf_path, text_path = downloader.process_pdf_url(url)
    if pdf_path and text_path:
        print(f"✅ Processed: {url}")
    else:
        print(f"❌ Failed: {url}")
```

### Custom Output Directory

```python
from main import PDFDownloader

# Set custom output directory
downloader = PDFDownloader(output_dir="my_papers")

# Process PDF
pdf_path, text_path = downloader.process_pdf_url(
    "https://example.com/paper.pdf"
)
```

## Output Structure

The library creates the following structure:
```
output_dir/
├── document.pdf                    # Downloaded PDF
├── document_extracted.txt          # Extracted text
├── another_paper.pdf              # Another PDF
└── another_paper_extracted.txt    # Another extracted text
```

## Error Handling

The library handles common issues:
- Network timeouts and retries
- Invalid URLs
- Corrupted PDFs
- Permission errors
- Disk space issues

All errors are logged with detailed information for debugging.

## Dependencies

- **requests**: HTTP library for downloading PDFs
- **PyPDF2**: PDF text extraction library

## License

This project is licensed under the same license as the parent repository.

## Contributing

See the main project's CONTRIBUTING.md for guidelines.

## Troubleshooting

### Common Issues

1. **PDF Download Fails**
   - Check if URL is accessible
   - Verify PDF exists at URL
   - Check network connectivity

2. **Text Extraction Fails**
   - Ensure PDF is not corrupted
   - Check if PDF contains extractable text
   - Verify PyPDF2 installation

3. **Permission Errors**
   - Check write permissions for output directory
   - Ensure sufficient disk space

### Debug Mode

Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Performance Notes

- Large PDFs may take time to process
- Text extraction speed depends on PDF complexity
- Network speed affects download performance
- Consider batch processing for multiple PDFs
