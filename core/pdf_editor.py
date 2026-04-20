import fitz  # PyMuPDF

# =========================
# EXTRACT TEXT BLOCKS
# =========================
def extract_blocks(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    blocks = []

    for page_num, page in enumerate(doc):
        data = page.get_text("dict")

        for b in data["blocks"]:
            if "lines" in b:
                text = ""

                for line in b["lines"]:
                    for span in line["spans"]:
                        text += span["text"] + " "

                blocks.append({
                    "page": page_num,
                    "bbox": b["bbox"],
                    "text": text.strip()
                })

    return blocks


# =========================
# EDIT PDF
# =========================
def edit_pdf(pdf_bytes, output_path, updated_blocks):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page_num, page in enumerate(doc):

        # Remove old content
        page.clean_contents()

        # Insert updated blocks
        for block in updated_blocks:
            if block["page"] == page_num:
                rect = fitz.Rect(block["bbox"])

                page.insert_textbox(
                    rect,
                    block["text"],
                    fontsize=11,
                    color=(0, 0, 0)
                )

    doc.save(output_path)
    doc.close()