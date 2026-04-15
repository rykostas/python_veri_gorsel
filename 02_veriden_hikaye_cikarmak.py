# ============================================================
#  ADIM 2: Veriden Hikaye Çıkarmak
# ============================================================
#  Gerçekçi bir akademik veri seti oluşturup,
#  birden fazla grafiği bir arada göstereceğiz.
#  "Dashboard" mantığı ile tek bakışta bütün resmi görelim.
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

# --- Gerçekçi bir akademik veri seti oluşturalım ---
np.random.seed(42)

bolumler = ["Bilgisayar", "Elektrik", "Makine", "İnşaat", "Kimya", "Biyoloji"]
yillar = list(range(2015, 2026))

# Her bölüm için yıllık yayın verisi
veri = {}
baz_yayin = [30, 25, 20, 22, 18, 28]
for i, bolum in enumerate(bolumler):
    veri[bolum] = [int(baz_yayin[i] * (1 + 0.08 * y + np.random.normal(0, 0.1)))
                   for y in range(len(yillar))]

df = pd.DataFrame(veri, index=yillar)
print("Veri Setimiz:")
print(df)
print()

# ============================================================
#  4'lü Dashboard - Tek bakışta her şey!
# ============================================================

fig = plt.figure(figsize=(16, 12))
fig.suptitle("Fakülte Akademik Performans Raporu (2015-2025)",
             fontsize=20, fontweight="bold", y=0.98)

gs = gridspec.GridSpec(2, 2, hspace=0.35, wspace=0.3)

# --- Grafik 1: Çizgi grafik - Trend analizi ---
ax1 = fig.add_subplot(gs[0, 0])
renkler = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c"]
for i, bolum in enumerate(bolumler):
    ax1.plot(yillar, df[bolum], marker="o", label=bolum, linewidth=2,
             markersize=5, color=renkler[i])

ax1.set_title("Yıllara Göre Yayın Trendi", fontsize=14, fontweight="bold")
ax1.set_xlabel("Yıl")
ax1.set_ylabel("Yayın Sayısı")
ax1.legend(fontsize=8, loc="upper left")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# --- Grafik 2: Yığın çubuk grafik ---
ax2 = fig.add_subplot(gs[0, 1])
x = np.arange(len(yillar))
alt = np.zeros(len(yillar))
for i, bolum in enumerate(bolumler):
    ax2.bar(x, df[bolum], bottom=alt, label=bolum, color=renkler[i],
            edgecolor="white", linewidth=0.5)
    alt += df[bolum].values

ax2.set_title("Toplam Yayın Kompozisyonu", fontsize=14, fontweight="bold")
ax2.set_xticks(x[::2])
ax2.set_xticklabels([str(y) for y in yillar[::2]])
ax2.set_ylabel("Toplam Yayın")
ax2.legend(fontsize=8, loc="upper left")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# --- Grafik 3: Kutu grafik (Box Plot) ---
ax3 = fig.add_subplot(gs[1, 0])
bp = ax3.boxplot([df[b] for b in bolumler], labels=bolumler, patch_artist=True,
                 medianprops={"color": "black", "linewidth": 2})
for patch, renk in zip(bp["boxes"], renkler):
    patch.set_facecolor(renk)
    patch.set_alpha(0.7)

ax3.set_title("Bölüm Bazlı Yayın Dağılımı", fontsize=14, fontweight="bold")
ax3.set_ylabel("Yayın Sayısı")
ax3.tick_params(axis="x", rotation=30)
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# --- Grafik 4: Isı haritası (Heatmap) ---
ax4 = fig.add_subplot(gs[1, 1])
im = ax4.imshow(df.T.values, cmap="YlOrRd", aspect="auto")

ax4.set_xticks(range(len(yillar)))
ax4.set_xticklabels([str(y)[2:] for y in yillar], fontsize=9)
ax4.set_yticks(range(len(bolumler)))
ax4.set_yticklabels(bolumler, fontsize=10)
ax4.set_title("Isı Haritası - Yayın Yoğunluğu", fontsize=14, fontweight="bold")

# Hücrelere değer yazalım
for i in range(len(bolumler)):
    for j in range(len(yillar)):
        val = df.T.values[i, j]
        renk = "white" if val > df.T.values.mean() + 5 else "black"
        ax4.text(j, i, str(val), ha="center", va="center", fontsize=8,
                 fontweight="bold", color=renk)

fig.colorbar(im, ax=ax4, shrink=0.8)

plt.savefig("02_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n 4 farklı bakış açısıyla aynı veriyi anlattık!")
print("Isı haritası ile hangi bölümün hangi yıl parlak olduğunu görebiliyoruz.")
