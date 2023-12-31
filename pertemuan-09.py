import streamlit as st
st.title("Kuliah Praktikum Big Data")
st.write("Rizki")
st.write("# Heading 1")
st.write("## Heading 2")
st.write("### Heading 3")
st.write("#### Heading 4")
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)
st.metric("Harga Saham", 100, 20)

pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)

makanan = st.radio('Makanan Kesukaan', ['Bakso', 'Nasi Goreng', 'Mie Ayam'])

st.write(makanan)
minuman = st.selectbox('Pilih minuman yang akan dipesan', ['Es Teh Manis', 'Kopi', 'Jus'])

st.write(minuman)

bayar = st.multiselect('Bayar Pakai:',['Tunai', 'OVO', 'Gopay'])
st.write(bayar)
