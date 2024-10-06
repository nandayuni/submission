import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load datasets
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')
# 1. Segmentasi Pengguna Sepeda Berdasarkan Waktu (Jam)
st.subheader('Segmentasi Pengguna Sepeda Berdasarkan Waktu (Jam)')
# Mengelompokkan data berdasarkan jam
hourly_data = hour_data[['hr', 'cnt']].groupby('hr').sum().reset_index()
# Membuat plot segmentasi pengguna berdasarkan jam
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hourly_data)
plt.title('Segmentasi Pengguna Sepeda Berdasarkan Waktu (Jam)')
plt.xlabel('Jam Penggunaan')
plt.ylabel('Total Pengguna Sepeda (per Jam)')
st.pyplot(plt)
# 2. Pengaruh Suhu terhadap Total Pengguna Sepeda
st.subheader('Pengaruh Suhu terhadap Total Pengguna Sepeda')
# Membuat plot suhu vs pengguna sepeda
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_data)
plt.title('Pengaruh Suhu terhadap Total Pengguna Sepeda')
plt.xlabel('Suhu (Normalisasi)')
plt.ylabel('Total Pengguna Sepeda (per Hari)')
st.pyplot(plt)
