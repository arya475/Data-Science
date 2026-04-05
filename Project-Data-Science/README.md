# Project-Data-Science

# Heart Disease Detector: AI-Based Heart Health Prediction

Deskripsi Proyek
Proyek ini adalah eksperimen Machine Learning sederhana untuk mendeteksi "Kesehatan Jantung" manusia berdasarkan data Heart.csv yang diberikan. Tujuan utama dari sistem ini adalah memberikan kesadaran kepada pengguna tentang dampak kolestrol, tekanan darah sistolik, gula darah puasa, dll terhadap kesehatan jantung mereka.
note: Proyek ini saat ini menggunakan Data Simulasi (Heart Disease Dataset) untuk keperluan demonstrasi algoritma dan edukasi dasar Data Science.

Fitur Utama

1. Prediksi Usia Jantung: Menghitung kesehatan jantung berdasarkan perbandingan dengan usia kronologis (asli).
2. Analisis : Mempertimbangkan variabel seperti umur, kolestrol, tekanan darah sistolik, tipe nyeri dada,dll untuk membuat anilisis kesehatan jantung
3. Visualisasi Data: Grafik feature importance (bobot yang menjadi perhitungan ai) #hanya dapat terlihat ketika menjaalankan code otak Ai dan tidak ditampilkan di web
   <img width="716" height="619" alt="Figure 1 (Ubuntu-22 04) 3_29_2026 3_24_57 PM" src="https://github.com/user-attachments/assets/df71b9e1-b97a-4ca6-8fa6-2ed1ad660022" />

4. Tampilan web : Berisi deteksi kesehatan jantung dengan memasukkan hasil pemeriksaan pasien(Dimana perhitungannya menggunakan model Ai yang sudah dilatih)
   <img width="1861" height="851" alt="Screenshot 2026-03-30 111222" src="https://github.com/user-attachments/assets/ece61762-f070-458c-8046-8f485492a68f" />

Teknologi yang Digunakan

1. Bahasa Pemrograman: Python 3
2. Analisis Data: Pandas & NumPy
3. Machine Learning: Scikit-Learn (Random Forest Classifier)
4. Visualisasi: Matplotlib, Streamlit

Cara Kerja Model
Model ini menggunakan algoritma Random Forest Classifier. Logika dasarnya adalah dibayangkan sebagai sebuah "Musyawarah Besar" yang dilakukan oleh sekumpulan Dokter Digital untuk melakukan voting penilaian.
Rumus Sederhana yang sebagai perbandingan:
Rumus untuk mencari score resiko: R = (Age x 0.05) + (Trestbps x 0.15) + (Chol x 0.1) + (CP_Factor).

AI Collaboration
Proyek ini dikembangkan dengan kolaborasi antara ide orisinal pengembang (Arya) dan bantuan asisten AI (Gemini). AI digunakan untuk membantu: 1. Arsitektur model Machine Learning. 2. Optimasi struktur kode Python dan dokumentasi.

Status Proyek: Tahap Awal (Early Stage)
Proyek ini masih berada dalam Tahap Pengembangan Awal (Prototipe).

1. Target Selanjutnya: Memberikan data tambahan untuk melatih model AI agar lebih pintar, membangun interface web yang mudah untuk dibaca.
2. Saya buatkan 10000 data simulasi buatan dengan data(heart.csv) yang sudah ada sebagai data reverensi, untuk saya ujikan model AI yang sudah saya buat kemudian hasil uji data itu saya gunakan lagi untuk melatih model AI, guna untuk melihat apa dampaknya jika model belajar kembali dari hasil prediksinya.
3. Memberikan data anomali/data tidak lengkap untuk melatih AI menangani data baru yang tidak sesuai dengan data yang sudah diberikan atau dilatihkan ke model AI tersebut.

Kelemahan model ini:
Karena masih tahap awal dan data yang diberikan masih relatif mudah maka akurasinya tinggi, belum diuji dengan data yang sulit atau banyak noise.

Yang ditemukan:

1. Semakin banyak data yang akan ditraining dan diujikan kemodel AI, semakin menurun juga score yang diberikan atau dihasilkan dari model AI (RandomForestClassifier). Namun solusi untuk meningkatkan score model AI tersebut maka kita tambah nilai max_depth pada model Random Forest Classifer. Pembagian training dan testing data masih sama yaitu 80% training 20% testing.
