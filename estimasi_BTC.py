import pickle
import streamlit as st

model = pickle.load(open('estimasi_BTC.sav', 'rb'))

st.title('Estimasi Harga BTC')

Open = st.number_input('Input Harga awal')
High = st.number_input('Input Harga tertinggi')
Low = st.number_input('Input Harga Terendah')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[Open, High, Low]]
    )
    st.write ('Estimasi harga BTC dalam USD : ', predict)
    st.write ('Estimasi harga BTC dalam IDR (Juta) :', predict*15000)