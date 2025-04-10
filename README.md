# colab-pdf-viewer

A simple utility to display PDFs as scrollable images in a fixed-size box inside Google Colab or Jupyter Notebook.

## 📦 Installation

```bash
!apt-get -y install poppler-utils
!pip install colab-pdf-viewer
```

## 🧪 Example (Google Colab)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marc86316/colab_pdf_viewer/blob/main/example_colab.ipynb)

```python
# Install dependencies (in Colab)
!apt-get -y install poppler-utils
!pip install colab-pdf-viewer

# Use the viewer
from pdf_viewer import display_scrollable_pdf_from_url

display_scrollable_pdf_from_url(
    "https://www.africau.edu/images/default/sample.pdf",
    width=800,
    height=450
)
```

## 📂 Project Structure
- `pdf_viewer/` – Python package
- `example_colab.ipynb` – Colab demo notebook
- `setup.py`, `MANIFEST.in` – Packaging files

## 📌 Links
- PyPI: https://pypi.org/project/colab-pdf-viewer/
- GitHub: https://github.com/Marc86316/colab_pdf_viewer

---

Built by [Marc86316](https://github.com/Marc86316).

