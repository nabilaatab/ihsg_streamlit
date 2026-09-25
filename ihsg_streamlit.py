import streamlit as st
import pandas as pd

# Halaman penuh
st.set_page_config(page_title="IHSG Analytics", layout="wide")

# Header
st.title("📈 Dashboard Analisis Historis IHSG")
st.markdown("Visualisasi pergerakan Indeks Harga Saham Gabungan (IHSG) berdasarkan dataset historis harian untuk keperluan peninjauan tren pasar.")

# Panggil data
df = pd.read_csv("ihsg_daily.csv") 

# Tampilan grafik
st.subheader("Tren Harga Penutupan (Close Price)")
st.line_chart(df['Close']) 

# Tampilan tabel data
st.subheader("Tabel Data Historis")
st.dataframe(df, use_container_width=True)
