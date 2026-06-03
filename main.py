import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import io
import zipfile

# Set page config
st.set_page_config(page_title="PDF Splitter & Merger", page_icon="📄", layout="centered")

# Title and description
st.title("PDF Splitter & Merger Web App")
st.markdown("""
This tool allows you to:
- **Merge multiple PDFs** into a single PDF file
- **Split a single PDF** into individual pages (downloadable as a ZIP file)
""")

# Create tabs for merge and split operations
tab1, tab2 = st.tabs(["Merge PDFs", "Split PDF"])

# Merge PDFs tab
with tab1:
    st.header("Merge Multiple PDFs")
    uploaded_files = st.file_uploader(
        "Choose PDF files to merge", 
        type="pdf", 
        accept_multiple_files=True,
        key="merge_uploader"
    )
    
    if uploaded_files:
        if st.button("Merge PDFs", key="merge_button"):
            try:
                merger = PdfMerger()
                
                for uploaded_file in uploaded_files:
                    # Read the PDF file
                    pdf_reader = PdfReader(uploaded_file)
                    merger.append(pdf_reader)
                
                # Write merged PDF to a bytes buffer
                merged_pdf_io = io.BytesIO()
                merger.write(merged_pdf_io)
                merged_pdf_io.seek(0)
                
                # Provide download button
                st.download_button(
                    label="Download Merged PDF",
                    data=merged_pdf_io,
                    file_name="merged.pdf",
                    mime="application/pdf",
                    key="download_merge"
                )
                st.success("PDFs merged successfully!")
                
            except Exception as e:
                st.error(f"Error merging PDFs: {str(e)}")

# Split PDF tab
with tab2:
    st.header("Split PDF into Pages")
    uploaded_file = st.file_uploader(
        "Choose a PDF file to split", 
        type="pdf", 
        accept_multiple_files=False,
        key="split_uploader"
    )
    
    if uploaded_file:
        if st.button("Split PDF", key="split_button"):
            try:
                pdf_reader = PdfReader(uploaded_file)
                num_pages = len(pdf_reader.pages)
                
                if num_pages == 0:
                    st.error("The PDF file appears to be empty or corrupted.")
                else:
                    # Create a zip file in memory to store all split pages
                    zip_buffer = io.BytesIO()
                    
                    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                        for page_num in range(num_pages):
                            # Create a PDF writer for this page
                            pdf_writer = PdfWriter()
                            pdf_writer.add_page(pdf_reader.pages[page_num])
                            
                            # Write page to bytes buffer
                            page_buffer = io.BytesIO()
                            pdf_writer.write(page_buffer)
                            page_buffer.seek(0)
                            
                            # Add page to zip file
                            zip_file.writestr(f"page_{page_num + 1}.pdf", page_buffer.getvalue())
                    
                    zip_buffer.seek(0)
                    
                    # Provide download button for the zip file
                    st.download_button(
                        label="Download Split Pages (ZIP)",
                        data=zip_buffer,
                        file_name="split_pages.zip",
                        mime="application/zip",
                        key="download_split"
                    )
                    st.success(f"PDF split into {num_pages} pages successfully!")
                    
            except Exception as e:
                st.error(f"Error splitting PDF: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit and PyPDF2")