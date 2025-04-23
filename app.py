import streamlit as st
import fitz  # PyMuPDF

def compress_pdf(input_path, output_path, quality):
    doc = fitz.open(input_path)
    doc.save(output_path, garbage=4, deflate=True, 
             compress_images=True, 
             compress_image_quality=quality)
    doc.close()

st.title("PDF Compression App")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    quality = st.slider("Compression Quality", 0, 100, 50)
    if st.button("Compress PDF"):
        with st.spinner("Compressing..."):
            compress_pdf(uploaded_file, "compressed.pdf", quality/100)
        st.success("Compression complete!")
        st.download_button("Download Compressed PDF", "compressed.pdf")