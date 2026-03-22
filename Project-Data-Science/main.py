import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

# Membuat data simulasi sederhana
data = {
    'usia_asli': [20, 25, 30, 45, 50, 22, 35, 40, 28, 60],
    'skor_stres': [2, 8, 5, 9, 3, 1, 7, 4, 6, 5], # Skala 1-10
    'olahraga_mingguan': [5, 1, 3, 0, 4, 6, 1, 2, 3, 2], # Frekuensi perminggu
    'pola_makan_sehat': [8, 4, 6, 3, 7, 9, 4, 5, 6, 6], # Skala 1-10
}

df = pd.DataFrame(data)

# Rumus logika sederhana untuk membuat "Target" (Usia Jantung)
# Aturan: Stres nambah umur, Olahraga ngurangin umur
df['usia_jantung'] = df['usia_asli'] + (df['skor_stres'] * .8) - (df['olahraga_mingguan'] * 1) - (df['pola_makan_sehat']*.5) 

print("Data Simulasi Project Jantung:")
#print(df.head())
print(df)