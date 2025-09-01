#!/usr/bin/env python3
"""
PDF Downloader and Text Extractor

This script downloads PDFs from URLs, extracts text content, and saves it to text files.
It's particularly useful for academic papers and research documents.

Requirements:
- requests: for downloading PDFs
- PyPDF2: for PDF text extraction
- urllib.parse: for URL parsing

Install dependencies:
pip install requests PyPDF2
"""

import requests
import PyPDF2
import os
import sys
from urllib.parse import urlparse, urljoin
from pathlib import Path
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PDFDownloader:
    def __init__(self, output_dir="extracted_texts"):
        """
        Initialize the PDF downloader.
        
        Args:
            output_dir (str): Directory to save extracted text files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Set up headers to mimic a real browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/pdf,application/octet-stream',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    
    def download_pdf(self, url, filename=None):
        """
        Download a PDF from a URL.
        
        Args:
            url (str): URL of the PDF to download
            filename (str, optional): Custom filename for the PDF
            
        Returns:
            str: Path to the downloaded PDF file
        """
        try:
            logger.info(f"Downloading PDF from: {url}")
            
            # Make the request with retry logic
            response = self._make_request_with_retry(url)
            
            if response.status_code == 200:
                # Generate filename if not provided
                if not filename:
                    filename = self._generate_filename(url, response)
                
                # Ensure unique PDF filename
                unique_filename = self._get_unique_filename(filename)
                pdf_path = self.output_dir / unique_filename
                
                # Save the PDF
                with open(pdf_path, 'wb') as f:
                    f.write(response.content)
                
                logger.info(f"PDF downloaded successfully: {pdf_path}")
                return str(pdf_path)
            else:
                logger.error(f"Failed to download PDF. Status code: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error downloading PDF: {str(e)}")
            return None
    
    def _make_request_with_retry(self, url, max_retries=3, delay=2):
        """
        Make HTTP request with retry logic for handling temporary failures.
        
        Args:
            url (str): URL to request
            max_retries (int): Maximum number of retry attempts
            delay (int): Delay between retries in seconds
            
        Returns:
            requests.Response: HTTP response object
        """
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                return response
            except requests.exceptions.RequestException as e:
                if attempt == max_retries - 1:
                    raise e
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
    
    def _generate_filename(self, url, response):
        """
        Generate a filename for the downloaded PDF.
        
        Args:
            url (str): Original URL
            response (requests.Response): HTTP response
            
        Returns:
            str: Generated filename
        """
        import re
        from urllib.parse import unquote
        
        # Try to get filename from Content-Disposition header
        content_disposition = response.headers.get('Content-Disposition', '')
        if 'filename=' in content_disposition:
            # Handle both quoted and unquoted filenames
            filename_match = re.search(r'filename\*?=(?:UTF-8\'\'|")?([^";\r\n]*)', content_disposition)
            if filename_match:
                filename = filename_match.group(1).strip()
                # URL decode the filename
                filename = unquote(filename)
                if filename and filename.endswith('.pdf'):
                    return self._sanitize_filename(filename)
        
        # Try to get filename from URL path
        parsed_url = urlparse(url)
        path = parsed_url.path
        
        # Remove query parameters and fragments from path
        clean_path = path.split('?')[0].split('#')[0]
        
        if clean_path.endswith('.pdf'):
            filename = os.path.basename(clean_path)
            return self._sanitize_filename(filename)
        
        # Try to extract meaningful name from URL path
        if clean_path and clean_path != '/':
            # Remove leading/trailing slashes and get the last meaningful part
            path_parts = [part for part in clean_path.split('/') if part]
            if path_parts:
                # Try to find a meaningful identifier (like article ID)
                for part in reversed(path_parts):
                    if part and len(part) > 3:  # Avoid very short parts
                        # Clean up the part and use it as filename
                        clean_part = re.sub(r'[^\w\-_.]', '_', part)
                        if clean_part:
                            return self._sanitize_filename(f"{clean_part}.pdf")
        
        # Generate filename from URL domain and timestamp
        domain = parsed_url.netloc.replace('www.', '').replace('.', '_')
        timestamp = int(time.time())
        return self._sanitize_filename(f"{domain}_{timestamp}.pdf")
    
    def _sanitize_filename(self, filename):
        """
        Sanitize filename by removing/replacing invalid characters.
        
        Args:
            filename (str): Original filename
            
        Returns:
            str: Sanitized filename
        """
        import re
        
        # Remove or replace invalid characters
        # Replace spaces with underscores
        filename = filename.replace(' ', '_')
        
        # Remove or replace other problematic characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        
        # Remove multiple consecutive underscores
        filename = re.sub(r'_+', '_', filename)
        
        # Remove leading/trailing underscores and dots
        filename = filename.strip('_.')
        
        # Ensure filename is not too long (max 200 characters)
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:200-len(ext)] + ext
        
        # Ensure filename is not empty
        if not filename:
            filename = f"downloaded_pdf_{int(time.time())}.pdf"
        
        return filename
    
    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text content from a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text content
        """
        try:
            logger.info(f"Extracting text from: {pdf_path}")
            
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                if not pdf_reader.pages:
                    logger.warning("PDF appears to be empty or corrupted")
                    return ""
                
                text_content = []
                total_pages = len(pdf_reader.pages)
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    try:
                        page_text = page.extract_text()
                        if page_text.strip():
                            text_content.append(f"--- Page {page_num} ---\n{page_text}\n")
                        else:
                            logger.warning(f"Page {page_num} appears to be empty or contains no extractable text")
                    except Exception as e:
                        logger.warning(f"Error extracting text from page {page_num}: {str(e)}")
                        text_content.append(f"--- Page {page_num} ---\n[Error extracting text: {str(e)}]\n")
                
                logger.info(f"Successfully extracted text from {total_pages} pages")
                return "\n".join(text_content)
                
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {str(e)}")
            return ""
    
    def save_text_to_file(self, text_content, output_filename):
        """
        Save extracted text to a file.
        
        Args:
            text_content (str): Text content to save
            output_filename (str): Name of the output file
            
        Returns:
            str: Path to the saved text file
        """
        try:
            output_path = self.output_dir / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text_content)
            
            logger.info(f"Text saved to: {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Error saving text to file: {str(e)}")
            return None
    
    def process_pdf_url(self, url, custom_filename=None):
        """
        Complete workflow: download PDF, extract text, and save to file.
        
        Args:
            url (str): URL of the PDF to process
            custom_filename (str, optional): Custom filename for the output
            
        Returns:
            tuple: (pdf_path, text_path) or (None, None) if failed
        """
        try:
            # Download the PDF
            pdf_path = self.download_pdf(url, custom_filename)
            if not pdf_path:
                return None, None
            
            # Extract text
            text_content = self.extract_text_from_pdf(pdf_path)
            if not text_content:
                logger.warning("No text content extracted from PDF")
                return pdf_path, None
            
            # Generate output filename
            if custom_filename:
                base_name = os.path.splitext(custom_filename)[0]
            else:
                base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            
            # Ensure unique text filename
            text_filename = self._get_unique_filename(f"{base_name}_extracted.txt")
            
            # Save text
            text_path = self.save_text_to_file(text_content, text_filename)
            
            return pdf_path, text_path
            
        except Exception as e:
            logger.error(f"Error in complete workflow: {str(e)}")
            return None, None
    
    def _get_unique_filename(self, filename):
        """
        Generate a unique filename by adding a counter if the file already exists.
        
        Args:
            filename (str): Base filename
            
        Returns:
            str: Unique filename
        """
        if not (self.output_dir / filename).exists():
            return filename
        
        # Split filename into name and extension
        name, ext = os.path.splitext(filename)
        counter = 1
        
        while True:
            new_filename = f"{name}_{counter}{ext}"
            if not (self.output_dir / new_filename).exists():
                return new_filename
            counter += 1

def main():
    """Main function to demonstrate usage."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_downloader.py <PDF_URL> [output_filename]")
        print("\nExample:")
        print("python pdf_downloader.py 'https://www.scielo.br/j/abc/a/FhdvV9qsmPbL4KFfMqwtNBv/?format=pdf&lang=pt'")
        print("python pdf_downloader.py 'https://example.com/paper.pdf' 'my_research_paper'")
        sys.exit(1)
    
    url = sys.argv[1]
    custom_filename = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Initialize downloader
    downloader = PDFDownloader()
    
    # Process the PDF
    pdf_path, text_path = downloader.process_pdf_url(url, custom_filename)
    
    if pdf_path and text_path:
        print(f"\n✅ Success!")
        print(f"📄 PDF downloaded to: {pdf_path}")
        print(f"📝 Text extracted to: {text_path}")
    else:
        print("\n❌ Failed to process PDF")
        if pdf_path:
            print(f"📄 PDF downloaded but text extraction failed: {pdf_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
