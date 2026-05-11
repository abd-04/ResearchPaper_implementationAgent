import streamlit as st
import os
import requests


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="PaperToCode",
    page_icon="📄",
    layout="wide"
)


# ---------------- LOAD CSS ---------------- #

css_path = os.path.join(
    os.path.dirname(__file__),
    "styles.css"
)

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# ---------------- HEADER ---------------- #

st.title("PaperToCode")

st.markdown("""
AI Research Paper Implementation Agent

Upload a research paper PDF to:
- analyze architecture
- retrieve related GitHub repositories
- generate PyTorch implementation
- generate explanations and summaries
""")


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("Pipeline")

    st.markdown("""
    1. PDF Extraction  
    2. Planning Agent  
    3. GitHub Retrieval  
    4. Code Generation  
    5. Explanation Generation  
    6. Packaging  
    """)

    st.divider()

    st.caption("Built with LangGraph, Groq, FastAPI, and Streamlit")


# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)


# ---------------- MAIN WORKFLOW ---------------- #

if uploaded_file is not None:

    st.success("PDF uploaded successfully")

    if st.button("Generate Implementation", use_container_width=True):

        with st.spinner("Running PaperToCode pipeline..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                "http://backend:8000/analyze",
                files=files
            )

            result = response.json()

            summary = result["summary"]

            implementation = result["implementation"]

            explanation = result["explanation"]

            references = result["references"]

        st.success("Pipeline completed successfully")


        # ---------------- TABS ---------------- #

        tab1, tab2, tab3, tab4 = st.tabs([
            "Summary",
            "Implementation",
            "Explanation",
            "References"
        ])


        # ---------------- SUMMARY ---------------- #

        with tab1:

            st.markdown(summary)


        # ---------------- IMPLEMENTATION ---------------- #

        with tab2:

            st.code(implementation, language="python")

            st.download_button(
                label="Download implementation.py",
                data=implementation,
                file_name="implementation.py",
                mime="text/plain"
            )


        # ---------------- EXPLANATION ---------------- #

        with tab3:

            st.markdown(explanation)


        # ---------------- REFERENCES ---------------- #

        with tab4:

            st.markdown(references)