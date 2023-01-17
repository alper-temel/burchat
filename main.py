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

sending_type = st.radio("**Gönderim Türü**", options = ["Sadece Metin", "Hem Metin Hem Görsel", "Sadece Görsel"])
print(sending_type)

uploaded_excel = st.file_uploader(label = "**Gönderilecek Excel Dosyasını Seçin**", type = ["csv", "xlsx"])
if uploaded_excel is not None:
    st.dataframe(pd.read_csv(uploaded_excel))
else:
    st.caption("Lütfen Excel Dosyasını Kontrol Edin")

uploaded_image = st.file_uploader(label = "**Gönderilecek Görseli Seçin**", type = ["jpg", "jpeg", "png"])
if uploaded_image is not None:
    st.image(uploaded_image)
    img = str(uploaded_image).split(",")[1].split("'")[1].replace("'", "")
else:
    st.caption("Lütfen Görseli Kontrol Edin")



@st.cache
def sendMessage():
    if sending_type == "Sadece Metin":
        if uploaded_excel is not None:
            uploaded_excel.seek(0)
            data = pd.read_csv(uploaded_excel)
            counter = 0
            for gsm, text in zip(data[data.columns[1]], data[data.columns[2]]):
                phone_number = "+90" + str(gsm)
                pywhatkit.sendwhatmsg_instantly(phone_number, text, wait_time = 10, tab_close=True)
                time.sleep(3)
                counter += 1
                if counter >= len(data):
                    st.stop()
    if sending_type == "Sadece Görsel":
        if uploaded_image is not None:
            uploaded_image.seek(0)
            uploaded_excel.seek(0)
            data = pd.read_csv(uploaded_excel)
            counter = 0
            for gsm, text in zip(data[data.columns[1]], data[data.columns[2]]):
                phone_number = "+90" + str(gsm)
                pywhatkit.sendwhats_image(phone_number, img, " ", 12, True)
                time.sleep(3)
                counter += 1
                if counter >= len(data):
                    st.stop()
    if sending_type == "Hem Metin Hem Görsel":
        if uploaded_image is not None and uploaded_excel is not None:
            uploaded_image.seek(0)
            uploaded_excel.seek(0)
            data = pd.read_csv(uploaded_excel)
            counter = 0
            for gsm, text in zip(data[data.columns[1]], data[data.columns[2]]):
                phone_number = "+90" + str(gsm)
                pywhatkit.sendwhats_image(phone_number, img, text, 12, True)
                time.sleep(3)
                counter += 1
                if counter >= len(data):
                    st.stop()
    else:
        st.markdown("# Hata! Girdileri kontrol ediniz veya programı yeniden başlatınız.")                      

st.button("WhatsApp Mesajlaşmasını Başlat :rocket:", on_click = sendMessage)  

st.markdown("Burchat v2.0 ~ Hepiyi :robot_face: 2023")
