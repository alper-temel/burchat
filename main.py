import streamlit as st
import pywhatkit
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

st.markdown("# :violet[BURCHAT] :clap: :muscle: :nazar_amulet:")

st.radio("Tür Seçiniz", ["Hem Metin Hem Görsel", "Sadece Metin", "Sadece Görsel"], label_visibility = "visible")

uploaded_excel = st.file_uploader(label = "**Gönderilecek Excel Dosyasını Seçin**", type = "csv")
if uploaded_excel is not None:
    st.dataframe(pd.read_csv(uploaded_excel))
else:
    st.caption("Lütfen Excel Dosyasını Kontrol Edin")

uploaded_image = st.file_uploader(label = "**Gönderilecek Görseli Seçin**", type = ["jpg", "jpeg", "png"])
if uploaded_image is not None:
    st.image(uploaded_image)
else:
    st.caption("Lütfen Görseli Kontrol Edin")

def sendMessage():
    if uploaded_excel is not None:
        uploaded_excel.seek(0)
        data = pd.read_csv(uploaded_excel)
        counter = 0
        for gsm, text in zip(data[data.columns[1]], data[data.columns[2]]):
            phone_number = "+90" + str(gsm)
            pywhatkit.sendwhatmsg_instantly(phone_number, text, wait_time = 10, tab_close=True)
            time.sleep(3)
            counter += 1
            print(counter)
            if counter >= 3:
                uploaded_excel.seek(0)
                st.stop()
                

st.button("WhatsApp Mesajlaşmasını Başlat :rocket:", on_click = sendMessage)  

st.text("Burchat v2.0 ~ Hepiyi 2023")
