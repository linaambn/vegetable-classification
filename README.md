# 🥦 Vegetable Classification using Deep Learning

<p align="center">
  <img src="assets/cover.jpg" width="700">
</p>

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
- [Visualisasi Akurasi Model](#visualisasi-akurasi-model)
- [Confusion Matrix](#confusion-matrix)
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
Dataset berupa citra sayuran dengan 15 kelas berbeda (carrot, broccoli, cabbage, tomato, dll).

📌 **Sumber Dataset**  
https://www.kaggle.com/datasets/username/vegetable-image-dataset

📌 **Jumlah Kelas**: 15  
📌 **Format**: JPG / PNG  
📌 **Pembagian Data**:
- Training
- Validation
- Testing

> ⚠️ Dataset tidak diunggah ke repository karena keterbatasan ukuran file GitHub.

---

## Preprocessing Data
Tahapan preprocessing:
- Resize citra (224 × 224)
- Normalisasi piksel (0–1)
- Data augmentation:
  - Rotation
  - Horizontal Flip
  - Zoom
- Pembagian data train, validation, dan test

---

## Model yang Digunakan

### 1️⃣ CNN Base
- CNN sederhana dari awal
- Digunakan sebagai baseline performa

### 2️⃣ MobileNetV2
- Transfer learning pretrained ImageNet
- Ringan dan efisien

### 3️⃣ EfficientNet
- CNN modern dengan compound scaling
- Memberikan performa terbaik

📌 **Model (.keras)** tersedia melalui Google Drive  
https://drive.google.com/your-model-link

---

## Hasil Evaluasi dan Analisis Perbandingan

### 📊 Tabel Perbandingan Performa Model

| Model | Accuracy | Precision | Recall | F1-Score |
|------|----------|----------|--------|----------|
| CNN Base | 85% | 0.84 | 0.83 | 0.83 |
| MobileNetV2 | 92% | 0.91 | 0.92 | 0.91 |
| EfficientNet | **95%** | **0.95** | **0.95** | **0.95** |

📌 **Analisis**:
- CNN Base memiliki performa terendah namun stabil
- MobileNetV2 unggul dari sisi efisiensi
- EfficientNet memberikan performa terbaik

---

## 📈 Visualisasi Akurasi Model

### CNN Base
<p align="center">
  <img src="assets/acc_cnn_base.png" width="600">
</p>

### MobileNetV2
<p align="center">
  <img src="assets/acc_mobilenetv2.png" width="600">
</p>

### EfficientNet
<p align="center">
  <img src="assets/acc_efficientnet.png" width="600">
</p>

---

## 📊 Confusion Matrix

### CNN Base
<p align="center">
  <img src="assets/Confusion Matrix-CNN Base.png" width="600">
</p>

### MobileNetV2
<p align="center">
  <img src="assets/Confusion Matrix-MobileNetV2.png" width="600">
</p>

### EfficientNet
<p align="center">
  <img src="assets/Confusion Matrix-Efficientnet.png" width="600">
</p>

---

## Implementasi Sistem Website
Aplikasi web dikembangkan menggunakan **Streamlit**, memungkinkan pengguna:
- Upload gambar sayuran
- Melihat hasil klasifikasi
- Menampilkan confidence score

---

## Panduan Menjalankan Sistem Secara Lokal

```bash
git clone https://github.com/linaambn/vegetable-classification.git
cd vegetable-classification
pip install -r requirements.txt
streamlit run app.py
