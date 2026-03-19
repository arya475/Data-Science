import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt # Library standar untuk visualisasi

# --- (Bagian 1-3: Data, Revisi, & Filter - Sama seperti kode sebelumnya) ---
data_penjualan = np.array([
    [10, 15, 8], [12, 20, 10], [5, 30, 15], [15, 25, 20]
])
harga_produk = np.array([15000000, 8000000, 5000000])

df = pd.DataFrame(data_penjualan, 
                  columns=['Laptop', 'Smartphone', 'Tablet'],
                  index=['Senin', 'Selasa', 'Rabu', 'Kamis'])

# Revisi & Hitung Omzet (Logika Dot Product)
df.loc['Rabu', 'Tablet'] = 25
df['Omzet'] = df.values @ harga_produk

# --- TAHAP 5: VISUALISASI DATA ---
print("\n--- Menampilkan Grafik Omzet... ---")

# 1. Membuat Figure (kanvas) dan Axis (subplot)
# figsize=(8, 5) menentukan ukuran gambar (lebar, tinggi) dalam inci
fig, ax = plt.subplots(figsize=(8, 5))

# 2. Membuat Grafik Batang (Bar Chart)
# Sumbu X = index (Hari), Sumbu Y = kolom Omzet
ax.plot(df.index, df['Omzet'], color='royalblue', edgecolor='black')

# 3. Menghias Grafik (Penting untuk Kejelasan)
ax.set_title('Total Omzet Penjualan Harian', fontsize=14, fontweight='bold')
ax.set_ylabel('Omzet (dalam Puluhan Juta Rp)', fontsize=12)
ax.set_xlabel('Hari Penjualan', fontsize=12)

# 4. Merapikan Format Sumbu Y (Menghilangkan notasi ilmiah/scientific notation)
# Kita bagi angkanya dengan 1 juta agar labelnya lebih bersih (misal: 150)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{x/1e6:,.0f}jt"))

# 5. Menampilkan Grid (Garis bantu) agar mudah membaca nilai
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 6. Menampilkan Grafik
plt.tight_layout() # Memastikan tidak ada label yang terpotong
plt.show() # Perintah wajib untuk memunculkan jendela grafik