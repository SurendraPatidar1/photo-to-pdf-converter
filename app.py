
import streamlit as st
from PIL import Image
from io import BytesIO
import re, zipfile, io

st.set_page_config(page_title="DSA Notes PDF Generator", page_icon="📚", layout="wide")
st.title("📚 DSA Notes — Automatic PDF Generator")
st.caption("Upload your notes images. Numbered filenames are automatically sorted into the correct sequence.")

st.markdown("""
**Recommended filenames**

`001_Data_Structure.png`  
`002_Classification.png`  
`003_ADT.png`  
`004_DS_vs_Algorithm.png`  
`...`  
`059_Radix_Sort.png`  
`060_Complexity_Cheat_Sheet.png`

You can upload individual images or one ZIP containing all images.
""")

uploaded = st.file_uploader(
    "Upload PNG/JPG/JPEG images or a ZIP",
    type=["png", "jpg", "jpeg", "zip"],
    accept_multiple_files=True
)

def number_key(name):
    m = re.match(r"\s*(\d+)", name)
    return (int(m.group(1)) if m else 10**9, name.lower())

if uploaded:
    items = []

    for f in uploaded:
        if f.name.lower().endswith(".zip"):
            try:
                with zipfile.ZipFile(f) as z:
                    for info in z.infolist():
                        if not info.is_dir() and info.filename.lower().endswith((".png", ".jpg", ".jpeg")):
                            img = Image.open(io.BytesIO(z.read(info.filename))).convert("RGB")
                            items.append((Path(info.filename).name, img))
            except Exception as e:
                st.error(f"Could not read ZIP {f.name}: {e}")
        else:
            try:
                items.append((f.name, Image.open(f).convert("RGB")))
            except Exception:
                st.warning(f"Could not read: {f.name}")

    items.sort(key=lambda x: number_key(x[0]))

    if items:
        st.success(f"{len(items)} pages detected and sorted automatically.")

        st.subheader("PDF order")
        cols = st.columns(4)
        for i, (name, img) in enumerate(items):
            with cols[i % 4]:
                st.image(img, caption=f"{i+1}. {name}", use_container_width=True)

        st.divider()
        st.subheader("PDF settings")
        page_size = st.selectbox("Page size", ["A4 Portrait", "A4 Landscape"])
        margin = st.slider("White margin", 0, 36, 0)

        if st.button("🚀 Generate PDF", type="primary", use_container_width=True):
            W, H = (595, 842) if page_size == "A4 Portrait" else (842, 595)
            pages = []

            for _, img in items:
                canvas = Image.new("RGB", (W, H), "white")
                avail_w, avail_h = W - 2 * margin, H - 2 * margin
                scale = min(avail_w / img.width, avail_h / img.height)
                nw, nh = max(1, int(img.width * scale)), max(1, int(img.height * scale))
                resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
                canvas.paste(resized, ((W - nw)//2, (H - nh)//2))
                pages.append(canvas)

            output = BytesIO()
            pages[0].save(
                output, format="PDF", save_all=True,
                append_images=pages[1:], resolution=150.0
            )

            st.download_button(
                "⬇️ Download DSA Notes PDF",
                data=output.getvalue(),
                file_name="DSA_Notes_Complete.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.info("No readable images found.")
