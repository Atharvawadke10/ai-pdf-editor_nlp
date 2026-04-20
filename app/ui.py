import streamlit as st
from core.nlp_engine import summarize, paraphrase, correct
from app.diff_viewer import show_diff

def render_block_editor(blocks):
    edited_blocks = []

    for i, block in enumerate(blocks):
        st.markdown(f"### Block {i+1} (Page {block['page']})")

        # ✅ Initialize session state
        if f"text_{i}" not in st.session_state:
            st.session_state[f"text_{i}"] = block["text"]

        # ✅ Use session state as source of truth
        edited_text = st.text_area(
            "Edit Text",
            key=f"text_{i}",
            height=100
        )

        col1, col2, col3 = st.columns(3)

        # ✅ Update session state instead of local variable
        with col1:
            if st.button("Summarize", key=f"s{i}"):
                st.session_state[f"text_{i}"] = summarize(st.session_state[f"text_{i}"])

        with col2:
            if st.button("Paraphrase", key=f"p{i}"):
                st.session_state[f"text_{i}"] = paraphrase(st.session_state[f"text_{i}"])

        with col3:
            if st.button("Correct", key=f"c{i}"):
                st.session_state[f"text_{i}"] = correct(st.session_state[f"text_{i}"])

        # ✅ Always read latest value
        updated_text = st.session_state[f"text_{i}"]

        st.markdown("#### Diff Viewer")
        show_diff(block["text"], updated_text)

        edited_blocks.append({
            "page": block["page"],
            "bbox": block["bbox"],
            "text": updated_text
        })

    return edited_blocks