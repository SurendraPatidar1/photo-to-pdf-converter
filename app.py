import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PhotoToPDF Studio",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

.main-title {
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 4px;
}

.subtitle {
    color: #6b7280;
    font-size: 16px;
    margin-bottom: 25px;
}

.small-text {
    color: #6b7280;
    font-size: 14px;
}

.upload-box {
    padding: 35px;
    border: 2px dashed #cbd5e1;
    border-radius: 18px;
    text-align: center;
    background: #ffffff;
    margin-bottom: 20px;
}

.upload-title {
    font-size: 22px;
    font-weight: 700;
}

.feature-title {
    font-size: 16px;
    font-weight: 700;
}

.feature-text {
    color: #6b7280;
    font-size: 13px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("📄 PhotoToPDF")

    st.caption("Professional PDF Studio")

    st.divider()

    st.subheader("Workspace")

    st.button("🏠 Dashboard", use_container_width=True)

    st.button("📄 My Documents", use_container_width=True)

    st.button("⭐ Templates", use_container_width=True)

    st.divider()

    st.subheader("Tools")

    st.button("🖼️ Images → PDF", use_container_width=True)

    st.button("✂️ Image Editor", use_container_width=True)

    st.button("🗜️ Compress PDF", use_container_width=True)

    st.button("🔍 OCR Scanner", use_container_width=True)

    st.divider()

    st.subheader("Settings")

    st.button("⚙️ Preferences", use_container_width=True)

    st.divider()

    st.caption("PhotoToPDF Studio")
    st.caption("Version 1.0")


# =========================================================
# HEADER
# =========================================================

header_left, header_right = st.columns([5, 1])

with header_left:

    st.markdown(
        '<div class="main-title">Photo to PDF Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Turn your images into professional, high-quality PDF documents.'
        '</div>',
        unsafe_allow_html=True
    )

with header_right:

    st.success("● Ready")


# =========================================================
# UPLOAD AREA
# =========================================================

st.markdown("### ☁️ Upload your images")

st.info(
    "Upload multiple photos or a ZIP file containing your images."
)

uploaded_files = st.file_uploader(
    "Choose images",
    type=["png", "jpg", "jpeg", "zip"],
    accept_multiple_files=True
)


# =========================================================
# WHEN NO FILES
# =========================================================

if not uploaded_files:

    st.divider()

    st.markdown("## 📄 Your PDF workspace is empty")

    st.markdown(
        '<div class="small-text">'
        'Upload images above to start creating your document.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("## ✨ Everything you need")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("### 🖼️")

        st.markdown(
            '<div class="feature-title">Multiple Images</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">'
            'Upload multiple images or complete ZIP folders.'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown("### ↕️")

        st.markdown(
            '<div class="feature-title">Easy Reordering</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">'
            'Arrange pages exactly how you want.'
            '</div>',
            unsafe_allow_html=True
        )

    with col3:

        st.markdown("### 🎨")

        st.markdown(
            '<div class="feature-title">Image Editing</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">'
            'Crop, rotate and enhance your pages.'
            '</div>',
            unsafe_allow_html=True
        )

    with col4:

        st.markdown("### 📄")

        st.markdown(
            '<div class="feature-title">High Quality PDF</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-text">'
            'Generate clean and professional PDF documents.'
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# WHEN FILES ARE UPLOADED
# =========================================================

else:

    st.divider()

    st.markdown("## 📑 Page Manager")

    st.caption(
        f"{len(uploaded_files)} file(s) uploaded."
    )

    # -----------------------------------------
    # ACTIONS
    # -----------------------------------------

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "➕ Add Images",
            use_container_width=True
        )

    with col2:
        st.button(
            "↕️ Sort Pages",
            use_container_width=True
        )

    with col3:
        st.button(
            "↶ Rotate",
            use_container_width=True
        )

    with col4:
        st.button(
            "✂️ Crop",
            use_container_width=True
        )

    with col5:
        st.button(
            "🗑️ Remove",
            use_container_width=True
        )

    st.divider()

    # -----------------------------------------
    # IMAGE PREVIEW
    # -----------------------------------------

    image_columns = st.columns(4)

    for index, file in enumerate(uploaded_files):

        with image_columns[index % 4]:

            st.caption(
                f"PAGE {index + 1} — {file.name}"
            )

            st.image(
                file,
                use_container_width=True
            )

            c1, c2 = st.columns(2)

            with c1:

                st.button(
                    "↶ Rotate",
                    key=f"rotate_{index}",
                    use_container_width=True
                )

            with c2:

                st.button(
                    "🗑️ Delete",
                    key=f"delete_{index}",
                    use_container_width=True
                )


    # =====================================================
    # PDF SETTINGS
    # =====================================================

    st.divider()

    st.markdown("## ⚙️ PDF Settings")

    col1, col2, col3 = st.columns(3)

    with col1:

        page_size = st.selectbox(
            "📐 Page Size",
            [
                "A4 Portrait",
                "A4 Landscape",
                "Letter Portrait",
                "Letter Landscape",
                "Legal Portrait",
                "Legal Landscape"
            ]
        )

    with col2:

        image_fit = st.selectbox(
            "🖼️ Image Fit",
            [
                "Contain",
                "Cover",
                "Original Size"
            ]
        )

    with col3:

        quality = st.select_slider(
            "🎯 PDF Quality",
            options=[
                "Low",
                "Medium",
                "High",
                "Maximum"
            ],
            value="High"
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        margin = st.slider(
            "White Margin",
            0,
            50,
            10
        )

    with col2:

        add_page_numbers = st.checkbox(
            "🔢 Add Page Numbers"
        )

    with col3:

        add_watermark = st.checkbox(
            "💧 Add Watermark"
        )


    # =====================================================
    # OUTPUT
    # =====================================================

    st.divider()

    st.markdown("## 📄 Output")

    pdf_name = st.text_input(
        "PDF File Name",
        value="My_Document.pdf"
    )

    st.caption(
        f"{len(uploaded_files)} pages ready."
    )

    st.button(
        "🚀 Generate PDF",
        type="primary",
        use_container_width=True
    )