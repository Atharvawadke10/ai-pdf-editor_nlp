import streamlit as st
import fitz
from PIL import Image

# =========================
# PDF PREVIEW
# =========================
def show_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")

    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        st.image(img, caption=f"Page {i+1}", use_column_width=True)