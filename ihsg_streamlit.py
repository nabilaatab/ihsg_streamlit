import streamlit as st
import pandas as pd

st.set_page_config(page_title="IHSG Analytics", layout="wide")

st.title("Dashboard Analisis Historis IHSG")
st.markdown("Visualisasi pergerakan Indeks Harga Saham Gabungan (IHSG). Gunakan slider di bawah untuk menyesuaikan rentang waktu analisis.")

# Panggil Data
df = pd.read_csv("ihsg_daily.csv") 

# Ubah kolom tanggal jadi tipe Datetime biar bisa difilter
df['Date'] = pd.to_datetime(df['Date'])

# Fitur slider
tahun_awal = int(df['Date'].dt.year.min())
tahun_akhir = int(df['Date'].dt.year.max())

# Set dari tahun 2020
pilihan_tahun = st.slider("Pilih Rentang Tahun Analisis:", 
                          min_value=tahun_awal, 
                          max_value=tahun_akhir, 
                          value=(2020, tahun_akhir))

# Filter data berdasarkan tahun yang dipilih di slider
df_filter = df[(df['Date'].dt.year >= pilihan_tahun[0]) & (df['Date'].dt.year <= pilihan_tahun[1])]

# Tampilan grafik
st.subheader(f"Tren Harga Penutupan ({pilihan_tahun[0]} - {pilihan_tahun[1]})")
st.line_chart(df_filter.set_index('Date')['Close']) 

# Tampilan tabel
st.subheader("Tabel Data Historis Terfilter")
st.dataframe(df_filter, use_container_width=True)
