import os
from pathlib import Path

import pandas as pd
import streamlit as st


FILE_NAME = "data/shared_file.csv"

st.text("Task 6")
st.text(f"instance_id = {os.getenv('INSTANCE_ID')}")

uploaded_file = st.file_uploader(
    label="Upload", 
    key="uploader_key",
    type=["csv"],
    max_upload_size=10,
    accept_multiple_files=False,
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.to_csv(FILE_NAME, index=False, encoding="utf-8")

file_path = Path(FILE_NAME)
if file_path.is_file():
    df = pd.read_csv(file_path)
    st.dataframe(df, height=200)
else:
    st.info("No file to show.")