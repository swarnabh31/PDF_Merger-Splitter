# Usage Guide

## Overview

This guide explains how to use the PDF Splitter & Merger Web App.

## Accessing the Application

1. Run the application locally:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to `http://localhost:8501`

## Merging PDFs

### Step-by-Step Instructions

1. **Navigate to the Merge Tab**
   - Click on the "Merge PDFs" tab at the top of the interface

2. **Upload PDF Files**
   - Click the "Choose PDF files to merge" button
   - Select multiple PDF files from your file explorer
   - Alternatively, you can drag and drop files directly onto the upload area

3. **Initiate Merge Process**
   - Once all files are selected, click the "Merge PDFs" button
   - The application will process the files and combine them in the order they were uploaded

4. **Download Result**
   - After processing completes, a "Download Merged PDF" button will appear
   - Click this button to download the merged PDF file
   - The file will be named "merged.pdf" by default

### Tips for Merging

- The order of files in the merged PDF corresponds to the order they appear in the file uploader
- To change the order, remove and re-add files in your desired sequence
- Large PDF files may take longer to process
- All standard PDF formats are supported

## Splitting PDF

### Step-by-Step Instructions

1. **Navigate to the Split Tab**
   - Click on the "Split PDF" tab at the top of the interface

2. **Upload a PDF File**
   - Click the "Choose a PDF file to split" button
   - Select a single PDF file from your file explorer
   - Alternatively, you can drag and drop the file directly onto the upload area

3. **Initiate Split Process**
   - Once a file is selected, click the "Split PDF" button
   - The application will process the file and extract each page as a separate PDF

4. **Download Result**
   - After processing completes, a "Download Split Pages (ZIP)" button will appear
   - Click this button to download a ZIP file containing all split pages
   - Each page is saved as "page_X.pdf" where X is the page number
   - The ZIP file will be named "split_pages.zip" by default

### Tips for Splitting

- The application extracts each page as an individual PDF file
- Page numbering starts at 1 (first page = page_1.pdf)
- The original PDF is not modified in any way
- Encrypted or password-protected PDFs may not be supported
- Very large PDFs with many pages will create larger ZIP files

## Troubleshooting

### Common Issues

1. **File Upload Problems**
   - Ensure you're uploading valid PDF files
   - Check that files are not corrupted
   - Verify file extensions are .pdf

2. **Processing Errors**
   - If you encounter an error, try refreshing the page and trying again
   - Large files may require more processing time
   - Some PDFs with unusual formatting may cause issues

3. **Download Problems**
   - Check your browser's download settings
   - Ensure you have sufficient disk space
   - Try a different browser if downloads fail

### Getting Help

If you continue to experience issues:
1. Check the console for error messages (right-click → Inspect → Console)
2. Ensure you're using the latest version of Streamlit and PyPDF2
3. Consider reporting the issue on the GitHub repository

## Best Practices

1. **File Management**
   - Keep original files safe before processing
   - Organize files in clearly named folders
   - Consider backing up important PDFs

2. **Performance**
   - Process files in reasonable batches
   - Close other applications when working with large PDFs
   - Use a stable internet connection if deploying online

3. **Security**
   - Only process PDFs from trusted sources
   - Be aware that files are processed locally (when running locally)
   - When deployed via Streamlit Community Cloud, processing happens on their servers

## Example Workflows

### Creating a Portfolio
1. Merge multiple project PDFs into one portfolio document
2. Add a cover page if needed
3. Distribute the single merged file

### Distributing Presentation Handouts
1. Split a long presentation PDF into individual slide PDFs
2. Distribute specific slides to team members
3. Archive slides separately for future reference

### Preparing Documents for Printing
1. Merge related documents into print-ready batches
2. Split combined documents for specific print jobs
3. Organize pages for booklet printing