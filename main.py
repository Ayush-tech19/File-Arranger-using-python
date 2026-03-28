import streamlit as st
import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]

    if not os.path.exists("images"):
        os.mkdir("images")

    for i, file in enumerate(files_with_ext):
        os.rename(file, f"images/photo-{i+1}{ext}")

    return files_with_ext


st.title("📁 File Arranger App")

uploaded_files = st.file_uploader(
    "Upload your images",
    accept_multiple_files=True,
    type=["jpg"]
)

if uploaded_files:
    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

    st.success("Files uploaded successfully!")

    if st.button("Arrange Files"):
        files = os.listdir()
        arranged = arrange_files(files, ".jpg")

        st.write("### Arranged Files:")
        st.write(arranged)

        st.success("Files moved to 'images' folder ")