# ============================================================
#  ADIM 5: İnteraktif Grafikler - Plotly
# ============================================================
#  Plotly ile tarayıcıda açılan, zoom yapılabilen,
#  üstüne gelince bilgi gösteren interaktif grafikler!
#  WOW ANLARININ BAŞLANGICI!
# ============================================================

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

# ============================================================
#  ÖRNEK 1: İnteraktif Bubble Chart
# ============================================================
np.random.seed(42)

n = 100
universiteler = pd.DataFrame({
    "Üniversite": [f"Üni_{i+1}" for i in range(n)],
    "Öğrenci_Sayısı": np.random.randint(5000, 80000, n),
    "Yayın_Sayısı": np.random.poisson(500, n) + np.random.randint(50, 1000, n),
    "Atıf_Puanı": np.random.exponential(25, n) + 10,
    "Tür": np.random.choice(["Devlet", "Vakıf"], n, p=[0.65, 0.35]),
    "Bölge": np.random.choice(
        ["Marmara", "İç Anadolu", "Ege", "Akdeniz", "Karadeniz", "Doğu And.", "G.Doğu And."],
        n, p=[0.25, 0.2, 0.15, 0.12, 0.1, 0.1, 0.08]
    ),
})
universiteler["Atıf_Puanı"] = universiteler["Atıf_Puanı"].round(1)

fig1 = px.scatter(
    universiteler, x="Yayın_Sayısı", y="Atıf_Puanı",
    size="Öğrenci_Sayısı", color="Bölge",
    hover_name="Üniversite",
    hover_data={"Öğrenci_Sayısı": ":,", "Tür": True},
    title="Türkiye Üniversiteleri: Yayın vs Atıf Analizi<br><sub>Balon boyutu = Öğrenci sayısı | Renk = Bölge | Üstüne gelin!</sub>",
    labels={"Yayın_Sayısı": "Yayın Sayısı", "Atıf_Puanı": "Atıf Puanı"},
    color_discrete_sequence=px.colors.qualitative.Set2,
    size_max=50,
    template="plotly_white",
)

fig1.update_layout(
    font=dict(size=14),
    title_font_size=18,
    height=600,
)

fig1.write_html("05a_interaktif_bubble.html")
fig1.show()
print("05a_interaktif_bubble.html dosyası oluşturuldu - tarayıcıda açıyor!")

# ============================================================
#  ÖRNEK 2: Animasyonlu Çubuk Grafik Yarışı (Bar Chart Race)
# ============================================================

bolumler = ["Bilgisayar", "Tıp", "Hukuk", "Eğitim", "Mühendislik",
            "Fen", "Edebiyat", "Ekonomi"]
yillar = list(range(2015, 2026))

# Her bölüm için yıllık yayın verisi
np.random.seed(123)
rows = []
for yil in yillar:
    for bolum in bolumler:
        baz = {"Bilgisayar": 300, "Tıp": 450, "Hukuk": 120, "Eğitim": 200,
               "Mühendislik": 350, "Fen": 280, "Edebiyat": 90, "Ekonomi": 220}
        deger = int(baz[bolum] * (1 + 0.08 * (yil - 2015)) + np.random.normal(0, 30))
        rows.append({"Yıl": yil, "Bölüm": bolum, "Yayın": max(deger, 50)})

df_yaris = pd.DataFrame(rows)

fig2 = px.bar(
    df_yaris, x="Yayın", y="Bölüm", color="Bölüm",
    animation_frame="Yıl", orientation="h",
    range_x=[0, df_yaris["Yayın"].max() * 1.1],
    title="Bölümler Arası Yayın Yarışı (2015-2025)<br><sub>Play tuşuna basın ve izleyin!</sub>",
    color_discrete_sequence=px.colors.qualitative.Vivid,
    template="plotly_white",
)

fig2.update_layout(
    showlegend=False,
    height=500,
    font=dict(size=14),
    yaxis={"categoryorder": "total ascending"},
    title_font_size=18,
)

fig2.write_html("05b_bar_chart_race.html")
fig2.show()
print("05b_bar_chart_race.html dosyası oluşturuldu!")

# ============================================================
#  ÖRNEK 3: Sunburst (Güneş Patlaması) Grafiği
# ============================================================

# Hiyerarşik veri: Fakülte > Bölüm > Program
rows = []
fakulteler = {
    "Mühendislik Fak.": {
        "Bilgisayar Müh.": ["Lisans (250)", "Y.Lisans (80)", "Doktora (30)"],
        "Elektrik Müh.": ["Lisans (200)", "Y.Lisans (60)", "Doktora (20)"],
        "Makine Müh.": ["Lisans (180)", "Y.Lisans (50)", "Doktora (15)"],
    },
    "Fen-Edebiyat Fak.": {
        "Matematik": ["Lisans (120)", "Y.Lisans (40)", "Doktora (10)"],
        "Fizik": ["Lisans (80)", "Y.Lisans (30)", "Doktora (8)"],
        "Kimya": ["Lisans (100)", "Y.Lisans (35)", "Doktora (12)"],
        "Biyoloji": ["Lisans (90)", "Y.Lisans (25)", "Doktora (7)"],
    },
    "Tıp Fakültesi": {
        "Temel Tıp": ["Y.Lisans (45)", "Doktora (25)"],
        "Klinik Tıp": ["Uzmanlık (120)", "Yan Dal (30)"],
    },
    "Sosyal Bil. Fak.": {
        "Psikoloji": ["Lisans (150)", "Y.Lisans (50)"],
        "Sosyoloji": ["Lisans (100)", "Y.Lisans (30)"],
        "Tarih": ["Lisans (80)", "Y.Lisans (20)"],
    },
}

for fakulte, bolumler_dict in fakulteler.items():
    for bolum, programlar in bolumler_dict.items():
        for program in programlar:
            isim = program.split("(")[0].strip()
            sayi = int(program.split("(")[1].replace(")", ""))
            rows.append({
                "Fakülte": fakulte,
                "Bölüm": bolum,
                "Program": isim,
                "Öğrenci": sayi
            })

df_sun = pd.DataFrame(rows)

fig3 = px.sunburst(
    df_sun,
    path=["Fakülte", "Bölüm", "Program"],
    values="Öğrenci",
    color="Fakülte",
    color_discrete_sequence=["#e74c3c", "#3498db", "#2ecc71", "#f39c12"],
    title="Üniversite Öğrenci Dağılımı<br><sub>Dilimlere tıklayarak içine dalabilirsiniz!</sub>",
)

fig3.update_layout(
    font=dict(size=14),
    title_font_size=18,
    height=650,
)

fig3.update_traces(textinfo="label+percent parent")

fig3.write_html("05c_sunburst.html")
fig3.show()
print("05c_sunburst.html dosyası oluşturuldu!")

# ============================================================
#  ÖRNEK 4: 3D Scatter Plot
# ============================================================

np.random.seed(55)
n = 200
df_3d = pd.DataFrame({
    "Deneyim": np.random.uniform(1, 30, n),
    "Yayın": np.random.poisson(15, n) + np.random.randint(0, 20, n),
    "H_İndeks": np.random.poisson(5, n),
    "Unvan": np.random.choice(
        ["Ar.Gör.", "Dr.Öğr.Üyesi", "Doçent", "Profesör"], n,
        p=[0.3, 0.3, 0.25, 0.15]
    ),
})
df_3d["H_İndeks"] = (df_3d["Yayın"] * 0.3 + np.random.normal(0, 2, n)).clip(1).astype(int)

fig4 = px.scatter_3d(
    df_3d, x="Deneyim", y="Yayın", z="H_İndeks",
    color="Unvan", size="Yayın", opacity=0.7,
    title="3D Akademik Profil Haritası<br><sub>Mouse ile döndürün, zoom yapın!</sub>",
    labels={"Deneyim": "Deneyim (yıl)", "Yayın": "Yayın Sayısı", "H_İndeks": "H-İndeks"},
    color_discrete_sequence=["#e74c3c", "#3498db", "#2ecc71", "#f39c12"],
    template="plotly_white",
)

fig4.update_layout(
    font=dict(size=12),
    title_font_size=18,
    height=650,
)

fig4.write_html("05d_3d_scatter.html")
fig4.show()
print("05d_3d_scatter.html dosyası oluşturuldu!")

print("\n İnteraktif grafikler tamam!")
print("HTML dosyalarını herhangi bir tarayıcıda açabilirsiniz.")
print("Zoom, pan, hover, tıkla-filtrele... hepsi mevcut!")
