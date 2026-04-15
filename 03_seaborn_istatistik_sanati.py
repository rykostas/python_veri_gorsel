# ============================================================
#  ADIM 3: Seaborn - İstatistiğin Sanatı
# ============================================================
#  Seaborn, istatistiksel grafikleri çok güzel çiziyor.
#  Akademisyenler için özellikle anlamlı grafikler!
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# --- Güzel tema ---
sns.set_theme(style="whitegrid", palette="husl", font_scale=1.1)

# ============================================================
#  Gerçekçi bir anket/araştırma verisi oluşturalım
# ============================================================
np.random.seed(2024)
n = 300

veri = pd.DataFrame({
    "Yaş": np.random.normal(35, 8, n).astype(int).clip(24, 65),
    "Deneyim_Yıl": np.random.exponential(8, n).astype(int).clip(1, 35),
    "Yayın_Sayısı": np.random.poisson(12, n),
    "Atıf_Sayısı": np.random.exponential(50, n).astype(int),
    "H_İndeks": np.random.poisson(6, n),
    "Bölüm": np.random.choice(
        ["Fen", "Mühendislik", "Tıp", "Sosyal Bil.", "Eğitim", "Hukuk"],
        n, p=[0.2, 0.25, 0.15, 0.2, 0.1, 0.1]
    ),
    "Unvan": np.random.choice(
        ["Ar.Gör.", "Dr.Öğr.Üyesi", "Doçent", "Profesör"],
        n, p=[0.3, 0.3, 0.25, 0.15]
    ),
    "Cinsiyet": np.random.choice(["Kadın", "Erkek"], n, p=[0.45, 0.55]),
})

# Atıf sayısını yayın sayısıyla ilişkilendirelim (gerçekçi olsun)
veri["Atıf_Sayısı"] = (veri["Yayın_Sayısı"] * np.random.uniform(2, 8, n)).astype(int)
veri["H_İndeks"] = (np.sqrt(veri["Atıf_Sayısı"]) * np.random.uniform(0.3, 0.7, n)).astype(int)

print("Örnek Veri (ilk 5 satır):")
print(veri.head())
print(f"\nToplam {len(veri)} akademisyen verisi")

# ============================================================
#  GRAFİK 1: Violin Plot - Dağılımı görmek için harika
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.violinplot(data=veri, x="Unvan", y="Yayın_Sayısı", hue="Cinsiyet",
               split=True, inner="quart", palette=["#FF6B6B", "#4ECDC4"],
               ax=axes[0],
               order=["Ar.Gör.", "Dr.Öğr.Üyesi", "Doçent", "Profesör"])
axes[0].set_title("Unvana Göre Yayın Dağılımı (Cinsiyet Karşılaştırması)",
                   fontsize=13, fontweight="bold")

sns.boxenplot(data=veri, x="Bölüm", y="Atıf_Sayısı",
              palette="Spectral", ax=axes[1])
axes[1].set_title("Bölüm Bazlı Atıf Dağılımı (Boxen Plot)",
                   fontsize=13, fontweight="bold")
axes[1].tick_params(axis="x", rotation=20)

plt.tight_layout()
plt.savefig("03a_violin_boxen.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  GRAFİK 2: Pair Plot - Tüm ilişkileri tek grafikte!
# ============================================================

print("\nPair Plot hazırlanıyor (biraz süre alabilir)...")

secilen = veri[["Deneyim_Yıl", "Yayın_Sayısı", "Atıf_Sayısı", "H_İndeks", "Unvan"]]

g = sns.pairplot(secilen, hue="Unvan", palette="husl",
                 diag_kind="kde", corner=True,
                 plot_kws={"alpha": 0.6, "s": 30},
                 hue_order=["Ar.Gör.", "Dr.Öğr.Üyesi", "Doçent", "Profesör"])
g.figure.suptitle("Akademik Göstergeler Arası İlişkiler", y=1.02,
                   fontsize=16, fontweight="bold")

plt.savefig("03b_pair_plot.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  GRAFİK 3: Korelasyon Haritası - Değişkenlerin dansı
# ============================================================

fig, ax = plt.subplots(figsize=(8, 6))

sayisal_kolonlar = ["Yaş", "Deneyim_Yıl", "Yayın_Sayısı", "Atıf_Sayısı", "H_İndeks"]
korelasyon = veri[sayisal_kolonlar].corr()

mask = np.triu(np.ones_like(korelasyon, dtype=bool))
sns.heatmap(korelasyon, mask=mask, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, square=True, linewidths=2,
            cbar_kws={"shrink": 0.8, "label": "Korelasyon Katsayısı"},
            annot_kws={"fontsize": 14, "fontweight": "bold"})

ax.set_title("Akademik Değişkenler Arası Korelasyon",
             fontsize=16, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("03c_korelasyon.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  GRAFİK 4: Joint Plot - İki değişkenin detaylı ilişkisi
# ============================================================

g = sns.jointplot(data=veri, x="Yayın_Sayısı", y="Atıf_Sayısı",
                  hue="Bölüm", kind="scatter", palette="bright",
                  height=8, alpha=0.6, marginal_kws={"common_norm": False})

g.figure.suptitle("Yayın vs Atıf: Bölüm Bazlı Dağılım",
                   fontsize=14, fontweight="bold", y=1.02)

plt.savefig("03d_joint_plot.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n Seaborn ile istatistiksel görselleştirme tamamlandı!")
print("Pair Plot ve Korelasyon Haritası, verinizdeki ilişkileri anında ortaya koyuyor.")
