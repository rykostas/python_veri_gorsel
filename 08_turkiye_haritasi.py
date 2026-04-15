# ============================================================
#  ADIM 8: Türkiye Haritası Üzerinde Veri Görselleştirme
# ============================================================
#  Plotly ile interaktif Türkiye haritası!
#  İllere göre akademik veriyi harita üzerinde gösteriyoruz.
#  WOW EFEKTİ: Coğrafi veri görselleştirme
# ============================================================

import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

np.random.seed(42)

# ============================================================
#  Türkiye'nin büyük şehirlerinin koordinatları ve verileri
# ============================================================

sehirler = pd.DataFrame({
    "Şehir": ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya",
              "Adana", "Konya", "Gaziantep", "Kayseri", "Mersin",
              "Eskişehir", "Diyarbakır", "Samsun", "Trabzon", "Erzurum",
              "Malatya", "Van", "Denizli", "Elazığ", "Hatay",
              "Sakarya", "Manisa", "Muğla", "Çanakkale", "Isparta",
              "Edirne", "Bolu", "Kastamonu", "Rize", "Mardin"],
    "Enlem": [41.01, 39.93, 38.42, 40.19, 36.90,
              37.00, 37.87, 37.06, 38.73, 36.80,
              39.77, 37.91, 41.29, 41.00, 39.90,
              38.35, 38.49, 37.77, 38.67, 36.40,
              40.69, 38.61, 37.22, 40.15, 37.76,
              41.67, 40.73, 41.38, 41.02, 37.31],
    "Boylam": [28.98, 32.86, 27.14, 29.06, 30.69,
               35.32, 32.48, 37.38, 35.49, 34.63,
               30.52, 40.22, 36.33, 39.72, 41.27,
               38.31, 43.38, 29.09, 39.22, 36.17,
               30.40, 27.43, 28.36, 26.41, 30.55,
               26.56, 31.61, 33.78, 40.52, 40.74],
    "Üniversite_Sayısı": [60, 25, 12, 8, 6,
                          5, 4, 5, 4, 3,
                          3, 4, 3, 3, 2,
                          3, 2, 2, 2, 2,
                          3, 2, 3, 2, 2,
                          2, 2, 1, 2, 1],
    "Yayın_Sayısı": [15000, 12000, 5000, 3500, 2800,
                     2500, 2200, 2000, 1800, 1500,
                     2800, 1200, 1400, 1600, 1100,
                     1000, 700, 900, 800, 750,
                     1100, 800, 1200, 600, 700,
                     500, 400, 300, 500, 350],
    "Akademisyen_Sayısı": [8000, 6500, 3000, 2000, 1500,
                           1400, 1200, 1100, 1000, 800,
                           1500, 700, 800, 900, 600,
                           550, 400, 500, 450, 420,
                           600, 450, 650, 350, 400,
                           300, 250, 200, 300, 200],
})

sehirler["Kişi_Başı_Yayın"] = (sehirler["Yayın_Sayısı"] / sehirler["Akademisyen_Sayısı"]).round(2)

# ============================================================
#  HARİTA 1: Balon Haritası - Şehirlere göre yayın yoğunluğu
# ============================================================

fig1 = px.scatter_mapbox(
    sehirler,
    lat="Enlem", lon="Boylam",
    size="Yayın_Sayısı",
    color="Kişi_Başı_Yayın",
    hover_name="Şehir",
    hover_data={
        "Üniversite_Sayısı": True,
        "Yayın_Sayısı": ":,",
        "Akademisyen_Sayısı": ":,",
        "Kişi_Başı_Yayın": ":.2f",
        "Enlem": False, "Boylam": False,
    },
    color_continuous_scale="RdYlGn",
    size_max=45,
    zoom=5.2,
    center={"lat": 39.0, "lon": 35.5},
    mapbox_style="carto-positron",
    title="Türkiye Akademik Yayın Haritası<br><sub>Balon = Yayın sayısı | Renk = Kişi başı yayın | Üstüne gelin!</sub>",
)

fig1.update_layout(
    height=650,
    font=dict(size=13),
    title_font_size=18,
    coloraxis_colorbar_title="Kişi Başı<br>Yayın",
)

fig1.write_html("08a_turkiye_yayin_haritasi.html")
fig1.show()
print("08a_turkiye_yayin_haritasi.html oluşturuldu!")

# ============================================================
#  HARİTA 2: Bağlantı Haritası - Şehirler arası iş birliği
# ============================================================

# En çok iş birliği yapılan şehir çiftlerini oluştur
is_birlikleri = [
    ("İstanbul", "Ankara", 500), ("İstanbul", "İzmir", 300),
    ("Ankara", "İzmir", 200), ("İstanbul", "Bursa", 180),
    ("Ankara", "Eskişehir", 150), ("İzmir", "Denizli", 80),
    ("Ankara", "Konya", 120), ("İstanbul", "Antalya", 150),
    ("Trabzon", "Erzurum", 90), ("Diyarbakır", "Mardin", 60),
    ("Gaziantep", "Hatay", 70), ("Adana", "Mersin", 130),
    ("İstanbul", "Trabzon", 100), ("Ankara", "Kayseri", 110),
    ("İstanbul", "Gaziantep", 90), ("Ankara", "Malatya", 70),
    ("İzmir", "Muğla", 60), ("İstanbul", "Samsun", 80),
    ("Ankara", "Samsun", 75), ("İstanbul", "Çanakkale", 50),
]

fig2 = go.Figure()

# Bağlantı çizgilerini ekle
for s1, s2, agirlik in is_birlikleri:
    r1 = sehirler[sehirler["Şehir"] == s1].iloc[0]
    r2 = sehirler[sehirler["Şehir"] == s2].iloc[0]
    opaklik = min(agirlik / 500, 0.8)

    fig2.add_trace(go.Scattermapbox(
        lat=[r1["Enlem"], r2["Enlem"]],
        lon=[r1["Boylam"], r2["Boylam"]],
        mode="lines",
        line=dict(width=max(agirlik / 100, 0.5), color=f"rgba(231,76,60,{opaklik})"),
        hoverinfo="text",
        text=f"{s1} ↔ {s2}: {agirlik} ortak yayın",
        showlegend=False,
    ))

# Şehir noktalarını ekle
fig2.add_trace(go.Scattermapbox(
    lat=sehirler["Enlem"],
    lon=sehirler["Boylam"],
    mode="markers+text",
    marker=dict(
        size=sehirler["Üniversite_Sayısı"] * 1.5 + 5,
        color=sehirler["Yayın_Sayısı"],
        colorscale="Blues",
        showscale=True,
        colorbar=dict(title="Yayın Sayısı"),
    ),
    text=sehirler["Şehir"],
    textposition="top center",
    textfont=dict(size=10, color="#2c3e50"),
    hovertext=[f"<b>{r.Şehir}</b><br>Üniversite: {r.Üniversite_Sayısı}<br>Yayın: {r.Yayın_Sayısı:,}"
               for _, r in sehirler.iterrows()],
    hoverinfo="text",
    showlegend=False,
))

fig2.update_layout(
    mapbox=dict(
        style="carto-positron",
        zoom=5.2,
        center=dict(lat=39.0, lon=35.5),
    ),
    title="Şehirler Arası Akademik İş Birliği Ağı<br><sub>Çizgi kalınlığı = Ortak yayın sayısı</sub>",
    height=650,
    font=dict(size=13),
    title_font_size=18,
)

fig2.write_html("08b_isbirligi_haritasi.html")
fig2.show()
print("08b_isbirligi_haritasi.html oluşturuldu!")

# ============================================================
#  HARİTA 3: Isı Haritası (Density Map)
# ============================================================

# Tüm akademisyenleri koordinatlarla dağıtın
tum_noktalar = []
for _, row in sehirler.iterrows():
    for _ in range(row["Akademisyen_Sayısı"] // 10):
        tum_noktalar.append({
            "lat": row["Enlem"] + np.random.normal(0, 0.2),
            "lon": row["Boylam"] + np.random.normal(0, 0.2),
        })

df_noktalar = pd.DataFrame(tum_noktalar)

fig3 = px.density_mapbox(
    df_noktalar, lat="lat", lon="lon",
    radius=15, zoom=5.2,
    center={"lat": 39.0, "lon": 35.5},
    mapbox_style="carto-darkmatter",
    title="Akademisyen Yoğunluk Haritası<br><sub>Sıcak bölgeler = Yüksek akademisyen yoğunluğu</sub>",
    color_continuous_scale="Hot",
)

fig3.update_layout(
    height=650,
    font=dict(size=13, color="white"),
    title_font_size=18,
    paper_bgcolor="#1a1a2e",
)

fig3.write_html("08c_yogunluk_haritasi.html")
fig3.show()
print("08c_yogunluk_haritasi.html oluşturuldu!")

print("\n Harita görselleştirmeleri tamamlandı!")
print("Türkiye'nin akademik haritası karşınızda.")
print("3 farklı harita türünü interaktif olarak inceleyebilirsiniz.")
