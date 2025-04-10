import os
import requests
from pdf2image import convert_from_path
from IPython.display import display, HTML
from urllib.parse import urlparse
import tempfile

def convert_to_raw_github_url(url):
    if "github.com" in url and "/blob/" in url:
        return url.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")
    return url

def is_url_accessible(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except Exception:
        return False

def display_scrollable_pdf_from_url(url: str, width: int = 800, height: int = 450):
    url = convert_to_raw_github_url(url)
    if not is_url_accessible(url):
        raise ValueError(f"Invalid or unreachable PDF URL: {url}")

    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to download PDF. HTTP status code: {response.status_code}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    images = convert_from_path(tmp_file_path)
    os.unlink(tmp_file_path)

    img_tags = "".join([
        f'<img src="data:image/png;base64,{img_to_base64(img)}" style="display:block; margin-bottom:10px; width:{width}px;"/>'
        for img in images
    ])

    html = f'''
    <div style="overflow-y:scroll; height:{height}px; border:1px solid #ccc; padding:10px;">
        {img_tags}
    </div>
    '''
    display(HTML(html))

def img_to_base64(img):
    import io
    import base64
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception as e:
        display(HTML(f"<div style='color:red;'>Error loading PDF: {e}</div>"))
