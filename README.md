# colab-pdf-viewer

A simple utility to display PDFs as scrollable images inside a fixed-size box in Google Colab or Jupyter Notebook.

## Install

```python
!apt-get -y install poppler-utils
!pip install colab-pdf-viewer
```

## Usage (inside Colab)

```python
from pdf_viewer import display_scrollable_pdf_from_url

display_scrollable_pdf_from_url(
    "https://raw.githubusercontent.com/your_username/your_repo/main/example.pdf",
    width=800,
    height=450
)
```
