# ============================================================
#  ADIM 1: İlk Adım - Tek Satırda Güzel Grafikler
# ============================================================
#  "Python ile grafik çizmek bu kadar kolay mı?"
#  Matplotlib ve Seaborn ile ilk grafiklerimizi çiziyoruz.
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

# --- Matplotlib'in güzel tema ayarı ---
plt.style.use("seaborn-v0_8-whitegrid")

# ============================================================
#  ÖRNEK 1: En basit grafik - 3 satır kod!
# ============================================================

yillar = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
ogrenci_sayisi = [120, 145, 98, 210, 280, 350, 410, 475]

plt.figure(figsize=(10, 6))
plt.plot(yillar, ogrenci_sayisi, marker="o", linewidth=2.5, markersize=10,
         color="#2196F3", markerfacecolor="#FF5722", markeredgecolor="white",
         markeredgewidth=2)

# Bilgi etiketleri ekleyelim
for x, y in zip(yillar, ogrenci_sayisi):
    plt.annotate(f"{y}", (x, y), textcoords="offset points",
                 xytext=(0, 15), ha="center", fontsize=11, fontweight="bold")

plt.title("Programa Kayıtlı Öğrenci Sayısı", fontsize=18, fontweight="bold", pad=20)
plt.xlabel("Yıl", fontsize=14)
plt.ylabel("Öğrenci Sayısı", fontsize=14)
plt.tight_layout()
plt.savefig("01a_cizgi_grafik.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  ÖRNEK 2: Rengarenk çubuk grafik
# ============================================================

bolumler = ["Tarih", "Edebiyat", "Psikoloji", "Sosyoloji", "Felsefe", "Ekonomi"]
yayin_sayisi = [45, 62, 78, 53, 31, 89]

# Renkler - her çubuk farklı renk
renkler = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD"]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(bolumler, yayin_sayisi, color=renkler, edgecolor="white",
              linewidth=2, width=0.6)

# Her çubuğun üstüne değer yazalım
for bar, val in zip(bars, yayin_sayisi):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
            str(val), ha="center", va="bottom", fontsize=14, fontweight="bold")

ax.set_title("Bölümlere Göre Yıllık Yayın Sayısı", fontsize=18,
             fontweight="bold", pad=20)
ax.set_ylabel("Yayın Sayısı", fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("01b_cubuk_grafik.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  ÖRNEK 3: Pasta grafik - ama güzel bir pasta!
# ============================================================

kategoriler = ["Makale", "Kitap Bölümü", "Bildiri", "Rapor", "Tez Danışmanlığı"]
oranlar = [35, 15, 25, 10, 15]
patlat = (0.05, 0, 0.05, 0, 0)  # Bazı dilimleri hafif dışarı çıkar

fig, ax = plt.subplots(figsize=(9, 9))
renk_paleti = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

wedges, texts, autotexts = ax.pie(
    oranlar, explode=patlat, labels=kategoriler, autopct="%1.1f%%",
    colors=renk_paleti, shadow=True, startangle=140,
    textprops={"fontsize": 13}, pctdistance=0.75,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)

for t in autotexts:
    t.set_fontweight("bold")

ax.set_title("Akademik Çıktı Dağılımı", fontsize=18, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("01c_pasta_grafik.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n İlk 3 grafiğiniz hazır!")
print("Göreceğiniz gibi Python ile grafik çizmek çok kolay.")
