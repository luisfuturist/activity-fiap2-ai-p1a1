#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.pdfurl2text.main import PDFDownloader

def main():
    urls = [
        "https://www.scielo.br/j/abc/a/FhdvV9qsmPbL4KFfMqwtNBv/?format=pdf&lang=pt",
        "https://www.scielo.br/j/abc/a/K9Ns38vDyW3qXDkJSQj56Jk/?format=pdf&lang=pt",
    ]
    
    # Initialize the downloader
    downloader = PDFDownloader(output_dir="extracted_texts")
    
    print("🚀 Starting PDF download and text extraction...\n")
    
    for i, url in enumerate(urls, 1):
        print(f"📋 Processing URL {i}/{len(urls)}")
        print(f"🔗 URL: {url}")
        
        # Process the PDF (download, extract text, save)
        pdf_path, text_path = downloader.process_pdf_url(url)
        
        if pdf_path and text_path:
            print(f"✅ Success! PDF: {pdf_path}, Text: {text_path}")
        else:
            print(f"❌ Failed to process this URL")
        
        print("-" * 80)
    
    print("\n🎉 All URLs processed!")

if __name__ == "__main__":
    main()
