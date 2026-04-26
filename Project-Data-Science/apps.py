import streamlit as st

st.write("""
    # Selamat Datang di Aplikasi Cek Kesehatan Jantung!
    Aplikasi ini dirancang untuk membantu Anda memeriksa kesehatan jantung Anda dengan mudah dan cepat.
    Cukup masukkan data kesehatan Anda, dan aplikasi ini akan memberikan analisis serta rekomendasi yang sesuai untuk menjaga kesehatan jantung Anda.
    """)    
    
def sidebar():
    st.sidebar.title("Menu Navigasi")
    st.sidebar.markdown("Pilih halaman yang ingin Anda akses:")
    menu_options = ["Beranda", "Cek Kesehatan Jantung", "Informasi Kesehatan Jantung", "Tentang Kami"]
    selected_option = st.sidebar.selectbox("Pilih Menu", menu_options)
    return selected_option  

sidebar()