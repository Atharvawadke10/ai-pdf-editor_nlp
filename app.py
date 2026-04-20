import streamlit as st
from core.pdf_editor import extract_blocks, edit_pdf
from core.nlp_engine import summarize, paraphrase, correct

st.set_page_config(layout="wide")
st.title("🧠 AI PDF Editor ")

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
        edit_pdf(file_bytes, output_path, updated_blocks)

        with open(output_path, "rb") as f:
            st.download_button("Download Edited PDF", f, "edited.pdf")