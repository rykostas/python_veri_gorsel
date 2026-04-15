# ============================================================
#  ADIM 4: Animasyonlu Grafik - Veri Canlanıyor!
# ============================================================
#  Hans Rosling'in ünlü "Gapminder" tarzında
#  ülkelerin zaman içindeki değişimini animasyonla gösteriyoruz.
#  WOW efekti garantili!
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd

# ============================================================
#  Türkiye ve komşu ülkelerin simülasyon verisi
# ============================================================
np.random.seed(42)

ulkeler = {
    "Türkiye":    {"renk": "#e74c3c", "baslangic_gsyh": 8000,  "baslangic_yas": 68, "pop": 70},
    "Almanya":    {"renk": "#3498db", "baslangic_gsyh": 35000, "baslangic_yas": 78, "pop": 82},
    "İran":       {"renk": "#2ecc71", "baslangic_gsyh": 5000,  "baslangic_yas": 65, "pop": 68},
    "Yunanistan": {"renk": "#f39c12", "baslangic_gsyh": 22000, "baslangic_yas": 77, "pop": 11},
    "Mısır":      {"renk": "#9b59b6", "baslangic_gsyh": 3000,  "baslangic_yas": 63, "pop": 75},
    "Polonya":    {"renk": "#1abc9c", "baslangic_gsyh": 12000, "baslangic_yas": 73, "pop": 38},
}

yillar = list(range(2000, 2026))
n_yil = len(yillar)

# Her ülke için zaman serisi oluştur
veri = {}
for ulke, info in ulkeler.items():
    gsyh = [info["baslangic_gsyh"]]
    yas = [info["baslangic_yas"]]
    for i in range(1, n_yil):
        gsyh.append(gsyh[-1] * (1 + np.random.uniform(0.01, 0.06)))
        yas.append(yas[-1] + np.random.uniform(0.05, 0.25))
    veri[ulke] = {
        "gsyh": gsyh,
        "yasam": yas,
        "nufus": info["pop"] * (1 + np.random.uniform(0, 0.01, n_yil)).cumprod(),
        "renk": info["renk"]
    }

# ============================================================
#  Animasyonu hazırlayalım
# ============================================================

fig, ax = plt.subplots(figsize=(12, 8))

def animate(frame):
    ax.clear()

    for ulke, d in veri.items():
        # Önceki pozisyonları hafif göster (iz bırakma efekti)
        if frame > 2:
            ax.scatter(d["gsyh"][max(0,frame-3):frame],
                      d["yasam"][max(0,frame-3):frame],
                      s=20, color=d["renk"], alpha=0.15)

        # Mevcut pozisyon
        boyut = d["nufus"][frame] * 5  # Nüfusa orantılı balon
        ax.scatter(d["gsyh"][frame], d["yasam"][frame],
                  s=boyut, color=d["renk"], alpha=0.7,
                  edgecolors="white", linewidth=2, zorder=5)

        # Ülke ismi
        ax.annotate(ulke, (d["gsyh"][frame], d["yasam"][frame]),
                   fontsize=10, fontweight="bold", ha="center",
                   xytext=(0, np.sqrt(boyut)/2 + 8),
                   textcoords="offset points")

    ax.set_xlim(1500, 70000)
    ax.set_ylim(60, 85)
    ax.set_xscale("log")
    ax.set_xlabel("Kişi Başı GSYH ($, log ölçek)", fontsize=14)
    ax.set_ylabel("Ortalama Yaşam Süresi (yıl)", fontsize=14)
    ax.set_title(f"Ülkelerin Gelişimi - {yillar[frame]}",
                fontsize=18, fontweight="bold")

    # Yıl bilgisi - büyük ve soluk
    ax.text(0.95, 0.15, str(yillar[frame]),
            transform=ax.transAxes, fontsize=60, color="gray",
            alpha=0.3, ha="right", va="center", fontweight="bold")

    ax.grid(True, alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Açıklama notu
    ax.text(0.02, 0.02, "Balon boyutu = Nüfus",
            transform=ax.transAxes, fontsize=10, color="gray",
            style="italic")

print("Animasyon hazırlanıyor...")
print("(Bu işlem 10-20 saniye sürebilir)\n")

anim = animation.FuncAnimation(fig, animate, frames=n_yil,
                                interval=400, repeat=True)

# GIF olarak kaydet
try:
    anim.save("04_animasyon.gif", writer="pillow", fps=3, dpi=120)
    print("Animasyon '04_animasyon.gif' olarak kaydedildi!")
except Exception as e:
    print(f"GIF kaydı sırasında hata: {e}")
    print("Animasyonu ekranda gösteriyoruz...")

plt.show()

# ============================================================
#  BONUS: Statik versiyon - son kare
# ============================================================
fig2, ax2 = plt.subplots(figsize=(12, 8))

for ulke, d in veri.items():
    # Tüm yılların izini çiz
    ax2.plot(d["gsyh"], d["yasam"], color=d["renk"], alpha=0.3,
             linewidth=1.5, zorder=1)
    # Son pozisyon
    boyut = d["nufus"][-1] * 5
    ax2.scatter(d["gsyh"][-1], d["yasam"][-1],
               s=boyut, color=d["renk"], alpha=0.7,
               edgecolors="white", linewidth=2, zorder=5)
    ax2.annotate(ulke, (d["gsyh"][-1], d["yasam"][-1]),
                fontsize=11, fontweight="bold", ha="center",
                xytext=(0, np.sqrt(boyut)/2 + 8),
                textcoords="offset points")
    # Başlangıç noktası
    ax2.scatter(d["gsyh"][0], d["yasam"][0],
               s=40, color=d["renk"], alpha=0.5, marker="x", zorder=4)

ax2.set_xscale("log")
ax2.set_xlabel("Kişi Başı GSYH ($, log ölçek)", fontsize=14)
ax2.set_ylabel("Ortalama Yaşam Süresi (yıl)", fontsize=14)
ax2.set_title("Ülkelerin 25 Yıllık Gelişim Yolculuğu (2000-2025)",
              fontsize=16, fontweight="bold")
ax2.text(0.02, 0.02, "x = 2000 başlangıç | Balon = 2025 (boyut = nüfus)",
         transform=ax2.transAxes, fontsize=10, color="gray", style="italic")
ax2.grid(True, alpha=0.3)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("04_gelisim_yolculugu.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n Gapminder tarzı animasyon tamamlandı!")
print("Her balonun hareketi, bir ülkenin hikayesini anlatıyor.")
