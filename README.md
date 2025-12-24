# 🥦 Vegetable Classification using Deep Learning

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

## 📑 Daftar Isi
- [Deskripsi Proyek](#deskripsi-proyek)
- [Dataset](#dataset)
- [Preprocessing Data](#preprocessing-data)
- [Model yang Digunakan](#model-yang-digunakan)
- [Hasil Evaluasi dan Analisis Perbandingan](#hasil-evaluasi-dan-analisis-perbandingan)
- [Implementasi Sistem Website](#implementasi-sistem-website)
- [Panduan Menjalankan Sistem Secara Lokal](#panduan-menjalankan-sistem-secara-lokal)
- [Struktur Repository](#struktur-repository)
- [Kesimpulan](#kesimpulan)

---

## Deskripsi Proyek
Proyek **Vegetable Classification** bertujuan untuk mengklasifikasikan jenis sayuran berdasarkan citra digital menggunakan pendekatan **Deep Learning berbasis Convolutional Neural Network (CNN)**.  

Sistem ini membandingkan performa beberapa model CNN dan diimplementasikan dalam bentuk **aplikasi website interaktif menggunakan Streamlit**.

---

## Dataset
Dataset yang digunakan merupakan dataset citra sayuran dengan beberapa kelas (misalnya: carrot, broccoli, cabbage, tomato, dll).

📌 **Sumber Dataset**:  
👉 Kaggle: https://www.kaggle.com/datasets/username/vegetable-image-dataset  

📌 **Jumlah Kelas**: 15 kelas  
📌 **Format Data**: JPG / PNG  
📌 **Pembagian Data**:
- Training set
- Validation set
- Testing set

> ⚠️ Dataset tidak diunggah langsung ke repository karena ukuran file yang besar.

---

## Preprocessing Data
Tahapan preprocessing yang dilakukan meliputi:
- Resize citra ke ukuran input model (224 × 224)
- Normalisasi nilai piksel (0–1)
- Data augmentation:
  - Rotation
  - Horizontal flip
  - Zoom
- Pembagian data train, validation, dan test

---

## Model yang Digunakan
Tiga model Deep Learning digunakan dalam penelitian ini:

### 1️⃣ CNN Base
- Model CNN sederhana yang dibangun dari awal
- Digunakan sebagai baseline performa

### 2️⃣ MobileNetV2
- Transfer learning dari model pretrained ImageNet
- Ringan dan efisien secara komputasi

### 3️⃣ EfficientNet
- Model CNN modern dengan scaling teroptimasi
- Memberikan performa terbaik dalam eksperimen

📌 **Model artifacts (file .keras)** dapat diunduh melalui Google Drive:  
👉 https://drive.google.com/your-model-link

---

## Hasil Evaluasi dan Analisis Perbandingan

### 📊 Tabel Perbandingan Performa Model

| Model          | Accuracy | Precision | Recall | F1-Score |
|---------------|----------|-----------|--------|----------|
| CNN Base       | 85%      | 0.84      | 0.83   | 0.83     |
| MobileNetV2   | 92%      | 0.91      | 0.92   | 0.91     |
| EfficientNet  | **95%**  | **0.95**  | **0.95** | **0.95** |

📌 **Analisis**:
- CNN Base memiliki performa terendah namun stabil
- MobileNetV2 unggul dalam efisiensi dan akurasi
- EfficientNet memberikan hasil terbaik secara keseluruhan

---

## Implementasi Sistem Website
Sistem diimplementasikan dalam bentuk **aplikasi web menggunakan Streamlit** yang memungkinkan pengguna:
- Mengunggah gambar sayuran
- Melihat hasil klasifikasi secara real-time
- Menampilkan confidence score prediksi

📷 **Tampilan Aplikasi**:
![Tampilan Streamlit](assets/streamlit_app.png)

---

## Panduan Menjalankan Sistem Secara Lokal

### 1️⃣ Clone Repository
```bash
git clone https://github.com/linaambn/vegetable-classification.git
cd vegetable-classification

