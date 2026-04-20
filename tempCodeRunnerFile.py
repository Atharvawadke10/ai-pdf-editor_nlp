import streamlit as st
from core.pdf_editor import extract_blocks, edit_pdf
from core.nlp_engine import summarize, paraphrase, correct
from app.diff_viewer import show_diff

st.set_page_config(layout="wide")
st.title("🧠 AI PDF Editor (Full Document Mode)")

# Load models once
@st.cache_resource
def load_models():
    from core.nlp_engine import load_models
    load_models()

load_models()

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    file_bytes = uploaded_file.read()

    # Extract blocks
    blocks = extract_blocks(file_bytes)

    if not blocks:
        st.error("No text extracted from PDF")
        st.stop()

    # Merge blocks into one text
    full_text = "\n\n".join([b["text"] for b in blocks])

    # Store in session state
    if "edited_text" not in st.session_state:
        st.session_state.edited_text = full_text

    st.subheader("📄 Edit Full Document")

    edited_text = st.text_area(
        "Edit Text",
        value=st.session_state.edited_text,
        height=400
    )

    # NLP buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Summarize"):
            st.session_state.edited_text = summarize(edited_text)

    with col2:
        if st.button("Paraphrase"):
            st.session_state.edited_text = paraphrase(edited_text)

    with col3:
        if st.button("Correct"):
            st.session_state.edited_text = correct(edited_text)

    # Always reflect latest state
    edited_text = st.session_state.edited_text

    # Map back to blocks
    def map_text_to_blocks(blocks, edited_text):
        edited_parts = edited_text.split("\n\n")

        for i, block in enumerate(blocks):
            if i < len(edited_parts):
                block["text"] = edited_parts[i]

        return blocks

    # Save PDF
    if st.button("💾 Save PDF"):
        updated_blocks = map_text_to_blocks(blocks, edited_text)
        output_path = "edited.pdf"
        
        edit_pdf(
        file_bytes,
        output_path,
        updated_blocks,
        add_text=add_text_data,
        add_shapes=add_shape_data,
        add_images=add_image_data
    )

    with open(output_path, "rb") as f:
        st.download_button("Download Edited PDF", f, "edited.pdf")


# =========================
# ADD OBJECT CONTROLS
# =========================

st.subheader("➕ Add Content")

new_text = st.text_input("Text to Add")
x = st.number_input("X Position", 0, 1000, 50)
y = st.number_input("Y Position", 0, 1000, 50)

add_text_data = []
if st.button("Add Text to PDF"):
    add_text_data.append({
        "page": 0,
        "x": x,
        "y": y,
        "text": new_text
    })

# Shape
add_shape_data = []
if st.button("Draw Rectangle"):
    add_shape_data.append({
        "page": 0,
        "x1": 50, "y1": 50,
        "x2": 200, "y2": 150
    })

# Image
uploaded_img = st.file_uploader("Upload Image", type=["png", "jpg"])
add_image_data = []

if uploaded_img:
    with open("temp_img.png", "wb") as f:
        f.write(uploaded_img.read())

    add_image_data.append({
        "page": 0,
        "x1": 100, "y1": 100,
        "x2": 300, "y2": 300,
        "path": "temp_img.png"
    })