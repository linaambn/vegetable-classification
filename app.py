import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os
import pandas as pd

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as mob_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as eff_preprocess

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Vegetable Image Classification",
    page_icon="🥦",
    layout="wide"
)
st.markdown("""
<style>

/* Sidebar outer */
section[data-testid="stSidebar"] {
    background-color: #66BB6A !important;
}

/* Sidebar inner */
section[data-testid="stSidebar"] > div {
    background-color: #66BB6A !important;
}

/* Sidebar content */
section[data-testid="stSidebar"] div[data-testid="stSidebarContent"] {
    background-color: #66BB6A !important;
}

/* Sidebar text */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {
    color: #1B5E20;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# PATH KONFIGURASI
# =====================================================
ARTIFACT_DIR = "model_artifacts"

# =====================================================
# LOAD CLASS LABELS
# =====================================================
with open(f"{ARTIFACT_DIR}/class_indices.json") as f:
    class_idx = json.load(f)

labels = {v: k for k, v in class_idx.items()}

# =====================================================
# MODEL LOADER (CACHE)
# =====================================================
@st.cache_resource
def load_model(choice):
    if choice == "CNN Base":
        return tf.keras.models.load_model(f"{ARTIFACT_DIR}/cnn_base.keras")
    elif choice == "MobileNetV2":
        return tf.keras.models.load_model(f"{ARTIFACT_DIR}/mobilenet.keras")
    else:
        return tf.keras.models.load_model(f"{ARTIFACT_DIR}/efficientnet.keras")

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.markdown(
    """
    <h2 style="color:#ffffff;">⚙️ Pengaturan Model</h2>
    """,
    unsafe_allow_html=True
)

model_choice = st.sidebar.selectbox(
    "🔽 Pilih Arsitektur Model",
    ["CNN Base", "MobileNetV2", "EfficientNet"]
)

st.sidebar.markdown("---")

model_info = {
    "CNN Base": "CNN sederhana tanpa pretrained (dibangun dari awal).",
    "MobileNetV2": "Model ringan pretrained ImageNet (efisien & cepat).",
    "EfficientNet": "Model pretrained dengan scaling optimal (akurasi tinggi)."
}

st.sidebar.markdown(
    f"""
    <div style="
        background-color:#66BB6A;
        padding:15px;
        border-radius:12px;
        color:#ffffff;
        font-size:14px;
    ">
        🧠 <b>Deskripsi Model</b><br><br>
        {model_info[model_choice]}
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    📌 <b>Framework</b><br>
    TensorFlow + Streamlit<br><br>

    📌 <b>Task</b><br>
    Image Classification<br><br>

    📌 <b>Dataset</b><br>
    Vegetable Image Dataset
    """,
    unsafe_allow_html=True
)

# LOAD MODEL
model = load_model(model_choice)

# =====================================================
# HEADER
# =====================================================
st.markdown(
    """
    <div style="
        background-color:#66BB6A;
        padding:30px;
        border-radius:15px;
        text-align:center;
        box-shadow:0 4px 10px rgba(0,0,0,0.08);
        margin-bottom:20px;
    ">
        <h1 style="color:#ffffff; margin-bottom:10px;">
            🥕 Vegetable Image Classification Dashboard
        </h1>
        <p style="font-size:18px; color:#ffffff;">
            Sistem klasifikasi citra sayuran menggunakan CNN Base dan Transfer Learning
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================================
# MAIN LAYOUT
# =====================================================
col1, col2 = st.columns([1.1, 1])

# =====================================================
# IMAGE UPLOAD
# =====================================================
with col1:
    st.subheader("📤 Upload Gambar Sayuran")

    file = st.file_uploader(
        "Unggah gambar (JPG / PNG)",
        type=["jpg", "png", "jpeg"]
    )

    if file:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Gambar Input", width=350)



# =====================================================
# PREDICTION
# =====================================================
with col2:
    st.subheader("📊 Hasil Prediksi")

    if file:
        img_resized = img.resize((224, 224))
        img_array = np.array(img_resized)
        img_array = np.expand_dims(img_array, axis=0)

        # PREPROCESSING SESUAI MODEL
        if model_choice == "CNN Base":
            img_array = img_array / 255.0
        elif model_choice == "MobileNetV2":
            img_array = mob_preprocess(img_array)
        else:
            img_array = eff_preprocess(img_array)

        pred = model.predict(img_array, verbose=0)
        pred_class = int(np.argmax(pred))
        confidence = float(np.max(pred) * 100)

        st.success(f"✅ **Prediksi:** {labels[pred_class]}")
        st.metric("Confidence (%)", f"{confidence:.2f}")

        st.progress(int(confidence))

        # ===========================
        # PROBABILITY BAR CHART
        # ===========================
        st.markdown("### 📈 Probabilitas Semua Kelas")

        prob_df = pd.DataFrame({
            "Kelas": [labels[i] for i in range(len(pred[0]))],
            "Probabilitas (%)": pred[0] * 100
        }).sort_values("Probabilitas (%)", ascending=False)

        st.bar_chart(prob_df.set_index("Kelas"))

        # ===========================
        # INSIGHT
        # ===========================
        with st.expander("🧠 Insight Model"):
            st.write(
                f"""
                - Model **{model_choice}** memprediksi gambar ini sebagai **{labels[pred_class]}**
                - Tingkat keyakinan model sebesar **{confidence:.2f}%**
                - Probabilitas kelas lain ditampilkan pada grafik di atas
                """
            )

    else:
        st.warning("Silakan upload gambar terlebih dahulu.")

# =====================================================
# TRAINING HISTORY
# =====================================================
st.markdown("---")
st.subheader("📉 Grafik Training Model")

history_map = {
    "CNN Base": "CNN_Base_history.png",
    "MobileNetV2": "MobileNetV2_history.png",
    "EfficientNet": "EfficientNet_history.png"
}

history_path = f"{ARTIFACT_DIR}/{history_map[model_choice]}"

if os.path.exists(history_path):
    st.image(
        history_path,
        caption=f"Training History - {model_choice}",
        width=900
    )
else:
    st.info("Grafik training belum tersedia.")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.markdown(
    "<center style='color:gray;'>📌 Praktikum UAP Pembelajaran Mesin | Streamlit Dashboard</center>",
    unsafe_allow_html=True
)
