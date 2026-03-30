# Project-Data-Science

# Heart Disease Detector: AI-Based Heart Health Prediction

Deskripsi Proyek
Proyek ini adalah eksperimen Machine Learning sederhana untuk mendeteksi "Kesehatan Jantung" manusia berdasarkan data Heart.csv yang diberikan. Tujuan utama dari sistem ini adalah memberikan kesadaran kepada pengguna tentang dampak kolestrol, tekanan darah sistolik, gula darah puasa, dll terhadap kesehatan jantung mereka.
note: Proyek ini saat ini menggunakan Data Simulasi (Heart Disease Dataset) untuk keperluan demonstrasi algoritma dan edukasi dasar Data Science.

Fitur Utama

1. Prediksi Usia Jantung: Menghitung kesehatan jantung berdasarkan perbandingan dengan usia kronologis (asli).
2. Analisis : Mempertimbangkan variabel seperti umur, kolestrol, tekanan darah sistolik, tipe nyeri dada,dll untuk membuat anilisis kesehatan jantung
3. Visualisasi Data: Grafik feature importance (bobot yang menjadi perhitungan ai) #hanya dapat terlihat ketika menjaalankan code otak Ai dan tidak ditampilkan di web
4. Tampilan web : Berisi deteksi kesehatan jantung dengan memasukkan hasil pemeriksaan pasien(Dimana perhitungannya menggunakan model Ai yang sudah dilatih)
   <img width="1861" height="851" alt="Screenshot 2026-03-30 111222" src="https://github.com/user-attachments/assets/ece61762-f070-458c-8046-8f485492a68f" />


Teknologi yang Digunakan

1. Bahasa Pemrograman: Python 3
2. Analisis Data: Pandas & NumPy
3. Machine Learning: Scikit-Learn (Random Forest Classifier)
4. Visualisasi: Matplotlib, Streamlit

Cara Kerja Model
Model ini menggunakan algoritma Random Forest Classifier. Logika dasarnya adalah dibayangkan sebagai sebuah "Musyawarah Besar" yang dilakukan oleh sekumpulan Dokter Digital untuk melakukan voting penilaian.
Rumus Sederhana yang Dipelajari AI:
Rumus untuk mencari score resiko: R = (Age x 0.05) + (Trestbps x 0.15) + (Chol x 0.1) + (CP_Factor).

AI Collaboration
Proyek ini dikembangkan dengan kolaborasi antara ide orisinal pengembang (Arya) dan bantuan asisten AI (Gemini). AI digunakan untuk membantu: 1. Arsitektur model Machine Learning. 2. Optimasi struktur kode Python dan dokumentasi.

Status Proyek: Tahap Awal (Early Stage)
Proyek ini masih berada dalam Tahap Pengembangan Awal (Prototipe). 1. Target Selanjutnya: Memberikan data tambahan untuk melatih model AI agar lebih pintar, membangun interface web yang mudah untuk dibaca

Kelemahan model ini:
Karena masih tahap awal dan data yang diberikan masih relatif mudah maka akurasinya tinggi, belum diuji dengan data yang sulit atau banyak noise.
