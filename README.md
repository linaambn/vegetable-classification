🥦 VEGETABLE CLASSIFICATION

Klasifikasi Sayuran Segar dan Busuk Menggunakan Deep Learning

📑 Daftar Isi

Deskripsi Proyek

Dataset

Preprocessing Data

Model yang Digunakan

Hasil Evaluasi dan Analisis Perbandingan

Implementasi Sistem Website (Streamlit)

Panduan Menjalankan Sistem Secara Lokal

Struktur Repository

Kesimpulan

💡 Semua judul di atas bisa diklik di GitHub

📌 Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem klasifikasi citra sayuran ke dalam dua kondisi utama, yaitu Fresh (Segar) dan Rotten (Busuk) menggunakan metode Deep Learning.

Penelitian ini membandingkan tiga model CNN, yaitu:

CNN Base (Non-Pretrained)

MobileNetV2 (Transfer Learning)

EfficientNet (Transfer Learning)

Model terbaik kemudian diimplementasikan ke dalam Sistem Website Sederhana berbasis Streamlit untuk mendemonstrasikan hasil prediksi secara interaktif.

📊 Dataset

Dataset terdiri dari 10 kelas citra sayuran:

FreshBellpepper

FreshCarrot

FreshCucumber

FreshPotato

FreshTomato

RottenBellpepper

RottenCarrot

RottenCucumber

RottenPotato

RottenTomato

📌 Catatan:
Dataset tidak disertakan langsung di repository karena ukuran file yang besar.
Dataset dapat diakses melalui tautan berikut:

🔗 Link Dataset:
https://drive.google.com/xxxxxxxx (isi dengan link Anda)

⚙️ Preprocessing Data

Tahapan preprocessing yang dilakukan meliputi:

Resize citra sesuai input model

Normalisasi nilai piksel

Data augmentation (rotasi, flipping, zoom)

Pembagian data ke train, validation, dan test set

🧠 Model yang Digunakan
1️⃣ CNN Base (Non-Pretrained)

Model CNN sederhana yang dilatih dari awal tanpa bobot pretrained.
Digunakan sebagai baseline untuk membandingkan efektivitas transfer learning.

2️⃣ MobileNetV2 (Transfer Learning)

Menggunakan bobot pretrained ImageNet sebagai feature extractor.
Model ini ringan, efisien, dan cocok untuk sistem dengan keterbatasan komputasi.

3️⃣ EfficientNet (Transfer Learning)

Menggunakan pendekatan compound scaling untuk menyeimbangkan kedalaman, lebar, dan resolusi input.
Model ini memberikan performa terbaik pada penelitian ini.

📈 Hasil Evaluasi dan Analisis Perbandingan
🔹 Tabel Perbandingan Model
Nama Model	Akurasi	Loss	Hasil Analisis
CNN Base	83.61%	0.5557	Performa cukup baik sebagai baseline, namun masih kesulitan mengenali kelas Rotten dengan konsisten.
MobileNetV2	93.84%	0.3618	Transfer learning meningkatkan performa secara signifikan dan stabil pada hampir semua kelas.
EfficientNet	95.27%	0.1501	Model terbaik dengan akurasi tertinggi dan loss terendah serta performa yang paling konsisten.

📌 Kesimpulan evaluasi:
Model EfficientNet dipilih sebagai model utama untuk implementasi sistem website.

🌐 Implementasi Sistem Website (Streamlit)

Sistem website sederhana dibangun menggunakan Streamlit dengan fitur:

Upload gambar oleh pengguna

Prediksi kelas sayuran (Fresh / Rotten)

Tampilan hasil prediksi model

📷 Contoh Tampilan Website

Tambahkan gambar di folder assets/ lalu gunakan format berikut:

![Tampilan Streamlit](assets/streamlit_app.png)


Contoh hasilnya di GitHub akan langsung tampil sebagai gambar.

▶️ Panduan Menjalankan Sistem Secara Lokal

Clone repository:

git clone https://github.com/linaambn/vegetable-classification.git


Masuk ke folder project:

cd vegetable-classification


Install dependency:

pip install -r requirements.txt


Jalankan Streamlit:

streamlit run app.py


Buka browser:

http://localhost:8501

📂 Struktur Repository
vegetable-classification/
│
├── app.py
├── requirements.txt
├── notebooks/
├── assets/
│   └── streamlit_app.png
├── README.md
└── .gitignore

📝 Model Artifacts

File model tidak disertakan langsung di repository karena ukuran file yang besar (>100MB).

Model dapat diunduh melalui Google Drive:

CNN Base: https://drive.google.com/xxxx

MobileNetV2: https://drive.google.com/xxxx

EfficientNet: https://drive.google.com/xxxx
