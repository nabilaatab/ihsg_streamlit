import streamlit as st
import pandas as pd

# Configure page layout and properties
st.set_page_config(page_title="IHSG Analytics", layout="wide")

st.title("Dashboard Analisis Historis IHSG")
st.markdown("Visualisasi pergerakan Indeks Harga Saham Gabungan (IHSG).")

# Data loading and preprocessing
df = pd.read_csv("ihsg_daily.csv") # Note: Update filename accordingly
df['Date'] = pd.to_datetime(df['Date'])

# Define dynamic date range for filtering
tahun_awal = int(df['Date'].dt.year.min())
tahun_akhir = int(df['Date'].dt.year.max())
pilihan_tahun = st.slider(
    "Pilih Rentang Tahun:", 
    min_value=tahun_awal, 
    max_value=tahun_akhir, 
    value=(2020, tahun_akhir)
)

# Apply filter based on user selection
df_filter = df[(df['Date'].dt.year >= pilihan_tahun[0]) & (df['Date'].dt.year <= pilihan_tahun[1])]

# Render Key Performance Indicators (KPI)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Harga Terakhir", value=f"Rp {df_filter['Close'].iloc[-1]:,.0f}")
with col2:
    st.metric(label="Harga Tertinggi", value=f"Rp {df_filter['Close'].max():,.0f}")
with col3:
    st.metric(label="Harga Terendah", value=f"Rp {df_filter['Close'].min():,.0f}")

st.divider()

# Initialize UI navigation tabs
tab1, tab2, tab3 = st.tabs(["Grafik Tren", "Data Mentah", "Tanya AI"])

# Render primary line chart
with tab1:
    st.line_chart(df_filter.set_index('Date')['Close']) 

# Render raw dataframe table
with tab2:
    st.dataframe(df_filter, use_container_width=True)

# Render AI Assistant interface simulation
with tab3:
    st.markdown("**Simulasi AI Financial Assistant**")
    
    # Initialize system greeting
    with st.chat_message("assistant"):
        st.write("Halo. Saya asisten data Anda. Ada yang ingin dianalisis dari tren IHSG ini?")
        
    prompt = st.chat_input("Ketik pertanyaan Anda di sini...")
    
    if prompt:
        # Render user prompt
        with st.chat_message("user"):
            st.write(prompt)
            
        # Render simulated AI response
        with st.chat_message("assistant"):
            st.write(f"*(Simulasi respons sistem)* Anda bertanya: '{prompt}'. Endpoint API LLM dapat diintegrasikan pada blok fungsi ini.")
