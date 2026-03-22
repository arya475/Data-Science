# Project-Data-Science

# Heart Age Detector: AI-Based Biological Age Prediction

Deskripsi Proyek
Proyek ini adalah eksperimen Machine Learning sederhana untuk mendeteksi "Usia Biologis" jantung manusia berdasarkan data gaya hidup dan kondisi fisik. Tujuan utama dari sistem ini adalah memberikan kesadaran kepada pengguna tentang dampak stres, pola makan, dan olahraga terhadap kesehatan jantung mereka.
note: Proyek ini saat ini menggunakan Data Simulasi (Synthetic Data) untuk keperluan demonstrasi algoritma dan edukasi dasar Data Science.

Fitur Utama

1. Prediksi Usia Jantung: Menghitung estimasi umur jantung berdasarkan perbandingan dengan usia kronologis (asli).
2. Analisis Gaya Hidup: Mempertimbangkan variabel seperti Skor Stres, Frekuensi Olahraga, dan Kualitas Pola Makan.
3. Visualisasi Data: Grafik perbandingan antara usia asli vs usia jantung untuk memudahkan pemahaman pengguna.

Teknologi yang Digunakan

1. Bahasa Pemrograman: Python 3
2. Analisis Data: Pandas & NumPy
3. Machine Learning: Scikit-Learn (Linear Regression)
4. Visualisasi: Matplotlib & Seaborn

Cara Kerja Model
Model ini menggunakan algoritma Linear Regression. Logika dasarnya adalah mencari korelasi linear antara variabel input (fitur) dengan target usia jantung.
Rumus Sederhana yang Dipelajari AI:
Usia Jantung = Usia Asli + (Stres \times 1.5) - (Olahraga \times 1) - (Nutrisi \times 0.5)

Hasil Visualisasi
Proyek ini menghasilkan visualisasi tren kesehatan jantung. Salah satu temuan utamanya adalah tingginya korelasi antara Skor Stres terhadap peningkatan usia biologis jantung secara signifikan.

AI Collaboration
Proyek ini dikembangkan dengan kolaborasi antara ide orisinal pengembang (Arya) dan bantuan asisten AI (Gemini). AI digunakan untuk membantu: 1. Arsitektur model Machine Learning. 2. Pembuatan data simulasi (Synthetic Data). 3. Optimasi struktur kode Python dan dokumentasi.

Status Proyek: Tahap Awal (Early Stage)
Proyek ini masih berada dalam Tahap Pengembangan Awal (Prototipe). 1. Target Selanjutnya: Menggunakan dataset medis asli (seperti dataset dari UCI Machine Learning Repository). 2. Pengembangan Algoritma: Mencoba algoritma yang lebih kompleks seperti Random Forest atau Neural Network untuk akurasi yang lebih tinggi. 3. Integrasi UI: Membangun antarmuka web sederhana menggunakan Streamlit agar pengguna bisa memasukkan data mereka sendiri secara langsung.
