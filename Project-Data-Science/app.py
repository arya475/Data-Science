import os
import joblib
import streamlit as st
import pandas as pd


# 1. Load Model 
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'heart_model.pkl')
model_main = joblib.load(model_path)


st.title("💓 Heart Health Prediction")
st.write("Prediksi risiko jantung berdasarkan data medis Anda.")

st.sidebar.header("Input Data Pengguna")

data = {
    'age': st.sidebar.slider("Umur Anda", 10, 100, 45),
    'sex': st.sidebar.selectbox("Jenis Kelamin", [1, 0], format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan"),
    'cp': st.sidebar.selectbox("Tipe Nyeri Dada (0-3)", [0, 1, 2, 3], format_func=lambda x: "Nyeri Dada Berat" if x == 0 else ("Nyeri Dada Ringan" if x == 1 else ("Nyeri Dada Sedang" if x == 2 else "Tidak Nyeri Dada"))),
    'trestbps': st.sidebar.number_input("Tekanan Darah", 90, 200, 120),
    'chol': st.sidebar.number_input("Kolesterol", 100, 400, 200),
    'fbs': st.sidebar.selectbox("Gula Darah Puasa > 120 mg/dl", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak"),
    'restecg': st.sidebar.selectbox("Hasil Elektrokardiografi", [0, 1, 2], format_func=lambda x: "Normal" if x == 0 else ("ST-T Abnormal" if x == 1 else "Hypertrophy")),
    'thalach': st.sidebar.number_input("Detak Jantung Maksimum", 60, 220, 150),
    'exang': st.sidebar.selectbox("Angina Akibat Latihan", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak"),
    'oldpeak': st.sidebar.number_input("Oldpeak (depresi ST)", 0.0, 10.0, 1.0),
    'slope': st.sidebar.selectbox("Slope", [0, 1, 2], format_func=lambda x: "Naik" if x == 0 else ("Datar" if x == 1 else "Turun")),
    'ca': st.sidebar.selectbox("Jumlah Pembuluh Darah Utama", [0, 1, 2, 3], format_func=lambda x: "0" if x == 0 else ("1" if x == 1 else ("2" if x == 2 else "3"))),
    'thal': st.sidebar.selectbox("Thalassemia", [0, 1, 2, 3], format_func=lambda x: "Normal" if x == 0 else ("Fixed Defect" if x == 1 else ("Reversible Defect" if x == 2 else "Unknown")))
}


st.sidebar.markdown("""**Catatan:**
- Pastikan data yang dimasukkan akurat untuk hasil prediksi yang lebih baik.
- Hasil prediksi ini hanya sebagai indikasi awal, konsultasikan dengan dokter untuk diagnosis yang lebih akurat.""")

# Konversi ke DataFrame untuk prediksi
input_df = pd.DataFrame([data])

# Tombol Prediksi dan Menampilkan Hasil
if st.button("Cek Risiko Jantung"):
    prediksi = model_main.predict(input_df)    
    st.subheader("Hasil Analisis:")
    if prediksi[0] == 0:
        st.success("✅ Anda tidak berisiko mengalami penyakit jantung.")
    else:
        st.error("⚠️ Anda berisiko tinggi mengalami penyakit jantung. Segera konsultasi ke dokter.")
