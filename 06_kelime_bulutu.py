# ============================================================
#  ADIM 6: Kelime Bulutu - Metin Görselleştirme
# ============================================================
#  Akademik makalelerin anahtar kelimelerinden
#  göz alıcı kelime bulutları oluşturuyoruz.
#  Özellikle sosyal bilimciler bunu ÇOK sever!
# ============================================================

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

# ============================================================
#  ÖRNEK 1: Basit ama etkileyici kelime bulutu
# ============================================================

# Akademik anahtar kelimeler ve frekansları
akademik_kelimeler = {
    # Araştırma yöntemleri
    "nitel araştırma": 45, "nicel araştırma": 42, "karma yöntem": 38,
    "görüşme": 35, "anket": 50, "odak grup": 28,
    "içerik analizi": 40, "meta analiz": 33, "sistematik derleme": 30,
    "deneysel desen": 25, "boylamsal çalışma": 22, "kesitsel araştırma": 20,
    # İstatistik
    "regresyon": 35, "korelasyon": 30, "ANOVA": 28,
    "faktör analizi": 32, "yapısal eşitlik": 36, "güvenirlik": 18,
    "ki-kare": 15, "t-testi": 20, "normallik": 17,
    # Eğitim bilimleri
    "öğrenme": 55, "öğretim": 48, "müfredat": 35,
    "dijital öğrenme": 42, "uzaktan eğitim": 45, "yapay zeka": 60,
    "gamifikasyon": 30, "ters yüz sınıf": 28, "proje tabanlı": 25,
    # Genel akademik
    "sürdürülebilirlik": 40, "inovasyon": 38, "dijital dönüşüm": 50,
    "veri bilimi": 48, "büyük veri": 44, "makine öğrenmesi": 52,
    "derin öğrenme": 35, "etik": 30, "sosyal medya": 38,
    "pandemi": 33, "küreselleşme": 25, "iklim değişikliği": 28,
    "toplumsal cinsiyet": 22, "katılımcılık": 18, "interdisipliner": 35,
}

# Renk paleti: akademik ve şık
def akademik_renk(*args, **kwargs):
    renk_listesi = ["#2C3E50", "#E74C3C", "#3498DB", "#27AE60",
                    "#F39C12", "#8E44AD", "#16A085", "#D35400"]
    return np.random.choice(renk_listesi)

wc1 = WordCloud(
    width=1200, height=600,
    background_color="white",
    max_words=100,
    max_font_size=120,
    min_font_size=14,
    color_func=akademik_renk,
    prefer_horizontal=0.7,
    relative_scaling=0.5,
    margin=10,
    collocations=False,
).generate_from_frequencies(akademik_kelimeler)

fig, ax = plt.subplots(figsize=(16, 8))
ax.imshow(wc1, interpolation="bilinear")
ax.axis("off")
ax.set_title("Akademik Araştırma Trendleri - Kelime Bulutu",
             fontsize=20, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("06a_kelime_bulutu.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  ÖRNEK 2: Daire şeklinde kelime bulutu (özel maske!)
# ============================================================

# Daire maskesi oluştur
x, y = np.ogrid[:600, :600]
maske = ((x - 300) ** 2 + (y - 300) ** 2 > 280 ** 2).astype(np.uint8) * 255

wc2 = WordCloud(
    width=600, height=600,
    background_color="white",
    mask=maske,
    max_words=80,
    max_font_size=80,
    contour_width=3,
    contour_color="#2C3E50",
    colormap="viridis",
    collocations=False,
).generate_from_frequencies(akademik_kelimeler)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(wc2, interpolation="bilinear")
ax.axis("off")
ax.set_title("Akademik Trendler (Daire Format)",
             fontsize=18, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("06b_daire_kelime_bulutu.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  ÖRNEK 3: Karşılaştırmalı kelime bulutları
# ============================================================

fen_kelimeleri = {
    "deney": 50, "hipotez": 45, "ölçüm": 42, "laboratuvar": 40,
    "kontrol grubu": 38, "değişken": 35, "istatistik": 33,
    "veri analizi": 30, "gözlem": 28, "tekrarlanabilirlik": 25,
    "formül": 22, "model": 40, "simülasyon": 35, "algoritma": 45,
    "optimizasyon": 30, "hesaplama": 28, "tensör": 15,
    "diferansiyel": 18, "integral": 16, "matris": 20,
}

sosyal_kelimeleri = {
    "toplum": 50, "kültür": 45, "kimlik": 42, "söylev": 30,
    "ideoloji": 35, "görüşme": 48, "etnografi": 28,
    "fenomenoloji": 25, "hermeneutik": 20, "söylem analizi": 38,
    "katılımcı gözlem": 22, "ötekileştirme": 18, "hegemonya": 15,
    "habitus": 12, "modernite": 28, "postmodern": 22,
    "yapıbozum": 15, "epistemoloji": 20, "ontoloji": 18,
    "paradigma": 35,
}

fig, axes = plt.subplots(1, 2, figsize=(20, 8))

wc_fen = WordCloud(width=800, height=500, background_color="#1a1a2e",
                   colormap="cool", max_words=50, max_font_size=80,
                   collocations=False).generate_from_frequencies(fen_kelimeleri)

wc_sos = WordCloud(width=800, height=500, background_color="#1a1a2e",
                   colormap="autumn", max_words=50, max_font_size=80,
                   collocations=False).generate_from_frequencies(sosyal_kelimeleri)

axes[0].imshow(wc_fen, interpolation="bilinear")
axes[0].axis("off")
axes[0].set_title("Fen Bilimleri", fontsize=18, fontweight="bold",
                   color="#3498db", pad=15)

axes[1].imshow(wc_sos, interpolation="bilinear")
axes[1].axis("off")
axes[1].set_title("Sosyal Bilimler", fontsize=18, fontweight="bold",
                   color="#e74c3c", pad=15)

fig.suptitle("İki Dünya, İki Dil: Fen vs Sosyal Bilimler",
             fontsize=22, fontweight="bold", y=1.02)

plt.tight_layout()
plt.savefig("06c_karsilastirmali_bulut.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n Kelime bulutları hazır!")
print("Kendi metin verilerinizi kullanarak benzer görseller oluşturabilirsiniz.")
print("Örneğin: makale özetleri, öğrenci geri bildirimleri, tez başlıkları...")
