import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
# Load data
day_df = pd.read_csv("day_df.csv")
hour_df = pd.read_csv("hour_df.csv")

# Sidebar
st.sidebar.title('Proyek Analisis Data')
page = st.sidebar.selectbox("Pilih Halaman:", ["Analisis Jam", "Analisis Hari Libur"])

# Main content
st.title(page)

if page == "Analisis Jam":
    st.subheader("Pertanyaan: Bagaimana pengaruh waktu (hr) terhadap jumlah penggunaan sepeda casual pada rental bike?")
    
    # Analisis jam
    hour_per_casual = hour_df.groupby('hr')['casual'].mean()
    
    # Plot bar chart
    st.bar_chart(hour_per_casual)

elif page == "Analisis Hari Libur":
    st.subheader("Pertanyaan: Bagaimana pengaruh hari libur (holiday) terhadap jumlah penggunaan sepeda pada rental bike?")
    
    # Analisis hari libur
    usage_by_holiday = day_df.groupby('holiday')['cnt'].mean()
    
    # Plot bar chart
    st.bar_chart(usage_by_holiday)

# Menampilkan dataset jika diinginkan
if st.checkbox("Tampilkan Dataset Day"):
    st.write(day_df)

if st.checkbox("Tampilkan Dataset Hour"):
    st.write(hour_df)

st.subheader("Conclusion:")
st.write("- Pada Analisis Jam, kita dapat melihat bahwa banyak pengguna rental casual menggunakan sepedanya pada siang dan sore. Kita dapat menargetkan pengguna casual tersebut di jam tersebut untuk menjadi pengguna registered dengan menawarkan promo - promo spesial di jam tersebut. Selain pengguna registered yang akan bertambah banyak tentu pengguna casual lainnya akan bertambah lagi.")
st.write("- Pada Analisis Hari Libur, kita dapat melihat bahwa korelasi antara hari libur dengan jumlah penggunaan sepeda adalah negatif. Dari grafik juga terlihat bahwa penggunaan sepeda lebih tinggi pada hari bukan hari libur dibandingkan dengan hari libur. Kita bisa melihat enggagement pengguna lebih rendah saat hari libur.")
