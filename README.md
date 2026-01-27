<h1>🧴 Cilt Ürün İçerik Analiz Uygulaması</h1>

Bu proje, kullanıcıların bir cilt  ürünün içerik listesini girerek cilt tipine ve hassasiyet durumuna göre riskli içerikleri hızlıca analiz edebilmesini sağlar.

Uygulama Streamlit ile geliştirilmiştir ve tarayıcı üzerinden (bilgisayar & telefon) çalışır.

<h2>🎯 Projenin Amacı</h2>

   Kozmetik ürün içeriklerini tek tek manuel araştırma zahmetini azaltmak

   Cilt ürünü alırken alışverişte kolaylık sağlamak

   Farklı cilt tipleri (yağlı, kuru, karma) için potansiyel riskleri göstermek

   Hassas ciltler için ekstra uyarılar sunmak

   Basit, anlaşılır ve kullanıcı dostu bir arayüz sağlamak

<h2> Nasıl Çalışır?</h2>

Kullanıcı cilt tipini seçer.

Hassas cilt durumu belirtilir.

Ürünün içerik listesi (virgülle ayrılmış şekilde) yapıştırılır.

Uygulama, önceden tanımlı riskli içerik veritabanı ile eşleştirme yapar.

Cilt tipine ve hassasiyete uygun zararlı olabilecek içerikler ekranda listelenir.

Girdi büyük/küçük harf fark etmeksizin analiz edilir.

<h2>Kullanılan Ugulamalar</h2>

**Python**

Streamlit

<h2>Proje Dosya Yapısı</h2>

cilt_içerik_analiz_projesi/
│
├─ uygulama_streamlit.py      # Streamlit arayüzü

├─ riskli_içerik.py           # Riskli içerik sözlüğü

├─ requirements.txt           # Gerekli kütüphaneler

└─ README.md                  # Proje açıklaması

<h2>Uygulamayı Çalıştırma</h2>

Yerel Ortamda

  pip install -r requirements.txt
  streamlit run uygulama_streamlit.py

<h2>Önemli Not</h2>

Bu uygulama bilgilendirme amaçlıdır. Tıbbi veya dermatolojik teşhis yerine geçmez. Cilt problemleri için bir uzmana danışılması önerilir.


<h2>Geliştirici Notu</h2>

Bu proje öğrenmek ve kişisel kullanım amacıyla geliştirdim.

