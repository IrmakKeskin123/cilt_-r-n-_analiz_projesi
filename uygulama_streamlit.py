import streamlit as st
from riskli_içerik import riskler

st.title("Cilt İçerik Analiz Uygulaması")

cilt_tipi = st.radio("Cilt tipiniz nedir?", ("Yağlı", "Kuru", "Karma"))
hassas = st.radio("Hassas cilt misiniz?", ("Evet", "Hayır"))
icerikler = st.text_area("İçerikleri buraya yapıştırın (virgülle ayırabilirsiniz):")

if st.button("Analiz Et"):
    if not icerikler.strip():
        st.warning("Lütfen içerikleri girin.")
    else:
        icerik_listesi = [i.strip().lower() for i in icerikler.split(",")]
        st.subheader("⚠️ Riskli İçerikler")

        found = False
        cilt_key = cilt_tipi.lower()

        for girilen in icerik_listesi:
            for riskli in riskler:
                if riskli in girilen:
                    madde_risk = []

                    if cilt_key in riskler[riskli]:
                        madde_risk.append(f"{cilt_tipi}: {riskler[riskli][cilt_key]}")

                    if hassas == "Evet" and "hassas" in riskler[riskli]:
                        madde_risk.append(f"Hassas: {riskler[riskli]['hassas']}")

                    if madde_risk:
                        found = True
                        st.write(f"{riskli.title()} ({'; '.join(madde_risk)})")

        if not found:
            st.success("Girdiğiniz içeriklerde seçilen duruma uygun risk bulunamadı.")
