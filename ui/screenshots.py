import streamlit as st
from datetime import datetime
from pathlib import Path


def upload_screenshots():
    st.markdown("### 📷 Upload Trade Screenshots")

    uploaded_files = st.file_uploader(
        "Upload one or more trade screenshots (HTF, LTF, etc.)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    screenshot_paths = []

    if uploaded_files:
        screenshots_dir = Path("data/screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        for uploaded_file in uploaded_files:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{uploaded_file.name}"
            save_path = screenshots_dir / filename

            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.image(uploaded_file, caption=f"Uploaded: {filename}", width=300)
            screenshot_paths.append(str(save_path))

    return screenshot_paths