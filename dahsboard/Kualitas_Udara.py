# Import library yang diperlukan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Import dataset
all_df = pd.read_csv('all_data.csv')

datetime_columns = ["datetime"]
all_df.sort_values(by="datetime", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["datetime"].min()
max_date = all_df["datetime"].max()

with st.sidebar:
    # Menambahkan logo
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0K3SXsXbBQqYKwvVWb_nmk_YpIsxSdKrobg&s")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Date Filter',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.header('Kualitas Udara Kota Changping dan Kota Shunyi :sparkles:')

main_df = all_df[(all_df["datetime"] >= str(start_date)) &
                (all_df["datetime"] <= str(end_date))]


st.subheader("Peta Wilayah Kota Changping dan Kota Shunyi")
st.image('https://media.istockphoto.com/id/1264421903/id/vektor/peta-beijing-dengan-wilayah-distrik-administratif.jpg?s=612x612&w=is&k=20&c=vjV1mgxWC7Q_lyJAzLoK35rS71OeWu1XCAr57DhBN74=')

# Menampilkan PM2.5 di Kota Changping
st.subheader("Indeks Polusi PM2.5 di Kota Changping")
changping_data = all_df[all_df['station'] == 'Changping']
changping = changping_data.groupby(by='datetime').agg({"PM2.5":["mean"],})


fig = plt.figure(figsize=(10,6))
plt.plot(changping.index, changping["PM2.5"], label="PM2.5")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi (µg/m^3)")
plt.legend()
st.pyplot(fig)

# Menampilkan PM10 di Kota Changping
st.subheader("Indeks Polusi PM10 di Kota Changping")
changping_data = all_df[all_df['station'] == 'Changping']
changping = changping_data.groupby(by='datetime').agg({"PM10":["mean"],})

fig = plt.figure(figsize=(10,6))
plt.plot(changping.index, changping["PM10"], label="PM10")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi (µg/m^3)")
plt.legend()
st.pyplot(fig)

# Menampilkan SO2, NO2, CO, O3 di Kota Changping
st.subheader("Indeks Polusi SO2, NO2, CO, O3 di Kota Changping")
changping_data = all_df[all_df['station'] == 'Changping']
changping_ = changping_data.groupby(by='datetime').agg({"SO2":["mean"],"NO2":["mean"],"CO":["mean"],"O3":["mean"]})

fig = plt.figure(figsize=(10,6))
plt.plot(changping_.index, changping_["SO2"], label="SO2")
plt.plot(changping_.index, changping_["NO2"], label="NO2")
plt.plot(changping_.index, changping_["CO"], label="CO")
plt.plot(changping_.index, changping_["O3"], label="O3")
plt.xlabel("Tahun")
plt.ylabel("Kualitas Udara")
plt.legend()
st.pyplot(fig)

# Menampilkan PM2.5 di Kota Shunyi
st.subheader("Indeks Polusi PM2.5 di Kota Shunyi")
shunyi_data = all_df[all_df['station'] == 'Shunyi']
shunyi = shunyi_data.groupby(by='datetime').agg({"PM2.5":["mean"],})

fig = plt.figure(figsize=(10,6))
plt.plot(shunyi.index, shunyi["PM2.5"], label="PM2.5")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi (µg/m^3)")
plt.legend()
st.pyplot(fig)

# Menampilkan PM10 di Kota Shunyi
st.subheader("Indeks Polusi PM10 di Kota Shunyi")
shunyi_data = all_df[all_df['station'] == 'Shunyi']
shunyi = shunyi_data.groupby(by='datetime').agg({"PM10":["mean"],})

fig = plt.figure(figsize=(10,6))
plt.plot(shunyi.index, shunyi["PM10"], label="PM10")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi (µg/m^3)")
plt.legend()
st.pyplot(fig)

# Menampilkan SO2, NO2, CO, O3 di Kota Shunyi
st.subheader("Indeks Polusi SO2, NO2, CO, O3 di Kota Shunyi")
shunyi_data = all_df[all_df['station'] == 'Shunyi']
shunyi_ = shunyi_data.groupby(by='datetime').agg({"SO2":["mean"],"NO2":["mean"],"CO":["mean"],"O3":["mean"]})

fig = plt.figure(figsize=(10,6))
plt.plot(shunyi_.index, shunyi_["SO2"], label="SO2")
plt.plot(shunyi_.index, shunyi_["NO2"], label="NO2")
plt.plot(shunyi_.index, shunyi_["CO"], label="CO")
plt.plot(shunyi_.index, shunyi_["O3"], label="O3")
plt.xlabel("Tahun")
plt.ylabel("Kualitas Udara")
plt.legend()
st.pyplot(fig)
