# PDF Splitter & Merger Web App

A browser-based tool built with Streamlit and PyPDF2 that allows users to:
- Merge multiple PDF files into a single PDF
- Split a single PDF into individual pages (downloadable as a ZIP file)

## Features

- **Merge PDFs**: Upload multiple PDF files and combine them into one PDF document
- **Split PDF**: Upload a single PDF and split it into individual pages, provided as a ZIP file
- **User-friendly Interface**: Simple and intuitive web interface
- **No Installation Required**: Runs directly in the browser (when deployed)
- **Privacy Focused**: All processing happens client-side in the browser (when deployed via Streamlit Community Cloud) or on your local machine

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-merger-splitter.git
   cd pdf-merger-splitter
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the application locally:

```bash
streamlit run main.py
```

Then open your web browser and go to `http://localhost:8501`.

## Usage

### Merging PDFs

1. Click on the "Merge PDFs" tab
2. Click "Choose PDF files to merge" or drag and drop your PDF files
3. Select multiple PDF files (you can select more than one)
4. Click the "Merge PDFs" button
5. Once processing is complete, click "Download Merged PDF" to save the combined file

### Splitting PDF

1. Click on the "Split PDF" tab
2. Click "Choose a PDF file to split" or drag and drop your PDF file
3. Select a single PDF file
4. Click the "Split PDF" button
5. Once processing is complete, click "Download Split Pages (ZIP)" to save the individual pages as a ZIP file

## Deployment

You can deploy this application for free using Streamlit Community Cloud:

1. Push your code to a GitHub repository
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your GitHub repository
4. Set the main file path to `main.py`
5. Click "Deploy!"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web application framework
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF manipulation capabilities