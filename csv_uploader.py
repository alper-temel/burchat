import streamlit as st
import pandas as pd
import time

st.markdown("""
                <style>
                    .css-h5rgaw.egzxvld1
                {
                    visibility: hidden;
                }
                </style>
            """, 
            unsafe_allow_html = True)

st.markdown("# BURCHAT :clap: :muscle: :nazar_amulet:")

uploaded_excel = st.file_uploader(label = "**Gönderilecek Excel Dosyasını Seçin**", type = "csv")
if uploaded_excel is not None:
    st.dataframe(pd.read_csv(uploaded_excel))
else:
    pass

uploaded_image = st.file_uploader("**Gönderilecek Fotoğrafı Seçin**", type = ["png", "jpg", "jpeg"])
if uploaded_image is not None:
    st.image(uploaded_image)
else:
    pass

def send_message():
    if uploaded_excel is not None:
        time_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            time_bar.progress(i + 1)
             
    else:
        return st.caption("Lütfen Excel Dosyasını Kontrol Edin")
    
    return time_bar

send_button = st.button("WhatsApp Mesajlaşmasını Başlat :rocket:", on_click = send_message)



st.text("Burchat v2.0 ~ Hepiyi 2023")