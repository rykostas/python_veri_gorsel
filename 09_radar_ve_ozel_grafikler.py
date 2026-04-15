# ============================================================
#  ADIM 9: Radar, Waffle ve Özel Grafikler
# ============================================================
#  Klasik grafiklerin ötesine geçiyoruz!
#  Radar chart, Waffle chart, Waterfall gibi
#  farklı ve etkileyici görselleştirmeler.
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.style.use("seaborn-v0_8-whitegrid")

# ============================================================
#  GRAFİK 1: Radar (Örümcek Ağı) Grafiği
#  Üniversitelerin farklı boyutlarda karşılaştırılması
# ============================================================

kategoriler = ["Araştırma", "Eğitim\nKalitesi", "Uluslararası\nİş Birliği",
               "Sanayi\nBağlantısı", "Öğrenci\nMemnuniyeti", "Mezun\nİstihdam"]
n_kat = len(kategoriler)

# 3 üniversite profili (0-100 puan)
uni_A = [92, 78, 85, 70, 65, 72]  # Araştırma odaklı
uni_B = [65, 90, 60, 88, 92, 85]  # Eğitim odaklı
uni_C = [80, 82, 90, 75, 78, 68]  # Dengeli / uluslararası

# Radar için açıları hesapla
acilar = np.linspace(0, 2 * np.pi, n_kat, endpoint=False).tolist()
acilar += acilar[:1]  # Kapatmak için

for veri in [uni_A, uni_B, uni_C]:
    veri.append(veri[0])  # Kapatmak için

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Üniversiteleri çiz
profiller = [
    (uni_A, "#e74c3c", "Üniversite A (Araştırma Odaklı)"),
    (uni_B, "#3498db", "Üniversite B (Eğitim Odaklı)"),
    (uni_C, "#2ecc71", "Üniversite C (Uluslararası)"),
]

for veri, renk, isim in profiller:
    ax.plot(acilar, veri, "o-", linewidth=2.5, label=isim, color=renk, markersize=8)
    ax.fill(acilar, veri, alpha=0.1, color=renk)

ax.set_xticks(acilar[:-1])
ax.set_xticklabels(kategoriler, fontsize=12, fontweight="bold")
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=9, color="gray")
ax.set_title("Üniversite Karşılaştırma Radar Grafiği",
             fontsize=16, fontweight="bold", pad=30)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=11)

plt.tight_layout()
plt.savefig("09a_radar.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  GRAFİK 2: Waffle Chart - Yüzde gösterimi için harika
#  100 kutucuk ile oranları görselleştiriyoruz
# ============================================================

# Burs kaynakları dağılımı
kaynaklar = {
    "TÜBİTAK": 35,
    "YÖK": 25,
    "AB Projeleri": 15,
    "Özel Sektör": 12,
    "Üniversite": 8,
    "Diğer": 5,
}

renk_map = {
    "TÜBİTAK": "#e74c3c",
    "YÖK": "#3498db",
    "AB Projeleri": "#2ecc71",
    "Özel Sektör": "#f39c12",
    "Üniversite": "#9b59b6",
    "Diğer": "#95a5a6",
}

fig, ax = plt.subplots(figsize=(12, 8))

# 10x10 grid oluştur
kutucuk_no = 0
for kaynak, yuzde in kaynaklar.items():
    renk = renk_map[kaynak]
    for _ in range(yuzde):
        satir = kutucuk_no // 10
        sutun = kutucuk_no % 10
        kare = plt.Rectangle((sutun, 9 - satir), 0.9, 0.9,
                              facecolor=renk, edgecolor="white",
                              linewidth=2, alpha=0.85)
        ax.add_patch(kare)
        kutucuk_no += 1

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 10.5)
ax.set_aspect("equal")
ax.axis("off")

# Lejant
patches = [mpatches.Patch(color=renk_map[k], label=f"{k} (%{v})")
           for k, v in kaynaklar.items()]
ax.legend(handles=patches, loc="center left", bbox_to_anchor=(1.02, 0.5),
          fontsize=13, framealpha=0.9, title="Burs Kaynağı",
          title_fontsize=14)

ax.set_title("Akademik Burs Kaynakları Dağılımı\nHer kutucuk = %1",
             fontsize=18, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("09b_waffle.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  GRAFİK 3: Şelale (Waterfall) Grafiği
#  Bütçe değişimlerini adım adım gösterme
# ============================================================

kalemler = ["Başlangıç\nBütçe", "TÜBİTAK\nHibe", "AB\nProjesi",
            "Patent\nGeliri", "Lab\nHarcaması", "Personel\nGideri",
            "Seyahat", "Ekipman\nAlımı", "Yıl Sonu\nBakiye"]
degerler = [500, 200, 150, 50, -120, -180, -45, -80, None]

# Yıl sonu bakiye hesapla
toplam = sum(d for d in degerler if d is not None)
degerler[-1] = toplam

# Kümülatif hesapla
kumulatif = [0]
for i, d in enumerate(degerler[:-1]):
    kumulatif.append(kumulatif[-1] + d)

fig, ax = plt.subplots(figsize=(14, 7))

for i, (kalem, deger) in enumerate(zip(kalemler, degerler)):
    if i == 0 or i == len(kalemler) - 1:
        # Başlangıç ve bitiş çubuğu
        ax.bar(i, deger, color="#3498db", edgecolor="white", linewidth=1.5, width=0.6)
        ax.text(i, deger + 8, f"{deger}K TL", ha="center", fontsize=11,
                fontweight="bold", color="#3498db")
    elif deger > 0:
        # Pozitif değişim (yeşil)
        ax.bar(i, deger, bottom=kumulatif[i], color="#2ecc71",
               edgecolor="white", linewidth=1.5, width=0.6)
        ax.text(i, kumulatif[i] + deger + 8, f"+{deger}K",
                ha="center", fontsize=10, fontweight="bold", color="#2ecc71")
    else:
        # Negatif değişim (kırmızı)
        ax.bar(i, deger, bottom=kumulatif[i], color="#e74c3c",
               edgecolor="white", linewidth=1.5, width=0.6)
        ax.text(i, kumulatif[i] + deger - 15, f"{deger}K",
                ha="center", fontsize=10, fontweight="bold", color="#e74c3c")

    # Bağlantı çizgileri
    if 0 < i < len(kalemler) - 1:
        ust = kumulatif[i] + max(deger, 0)
        ax.plot([i - 0.3, i + 0.7], [kumulatif[i + 1], kumulatif[i + 1]],
                color="gray", linewidth=0.8, linestyle="--", alpha=0.5)

ax.set_xticks(range(len(kalemler)))
ax.set_xticklabels(kalemler, fontsize=10, fontweight="bold")
ax.set_ylabel("Bin TL", fontsize=13)
ax.set_title("Araştırma Grubu Yıllık Bütçe Akışı (Şelale Grafiği)",
             fontsize=16, fontweight="bold", pad=20)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.axhline(y=0, color="gray", linewidth=0.5)

plt.tight_layout()
plt.savefig("09c_waterfall.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  GRAFİK 4: Lollipop (Lolipop) Grafiği
#  Çubuk grafiğe modern bir alternatif
# ============================================================

dergiler = ["Nature", "Science", "Cell", "Lancet", "NEJM",
            "IEEE Trans.", "PNAS", "PLoS ONE", "Elsevier\nToplu",
            "Springer\nToplu", "Wiley\nToplu", "Taylor &\nFrancis"]
etki_faktor = [64.8, 56.9, 66.6, 168.9, 176.1, 12.3,
               12.8, 3.7, 4.2, 5.1, 3.8, 2.9]

# Sırala
sira = np.argsort(etki_faktor)
dergiler = [dergiler[i] for i in sira]
etki_faktor = [etki_faktor[i] for i in sira]

fig, ax = plt.subplots(figsize=(12, 8))

renkler = plt.cm.RdYlGn(np.linspace(0.2, 0.9, len(dergiler)))

for i, (dergi, ef, renk) in enumerate(zip(dergiler, etki_faktor, renkler)):
    ax.hlines(y=i, xmin=0, xmax=ef, color=renk, linewidth=2.5, alpha=0.8)
    ax.scatter(ef, i, color=renk, s=150, zorder=5, edgecolors="white", linewidth=2)
    ax.text(ef + 3, i, f"{ef}", va="center", fontsize=11, fontweight="bold")

ax.set_yticks(range(len(dergiler)))
ax.set_yticklabels(dergiler, fontsize=11)
ax.set_xlabel("Etki Faktörü (Impact Factor)", fontsize=13)
ax.set_title("Önemli Akademik Dergilerin Etki Faktörleri",
             fontsize=16, fontweight="bold", pad=20)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlim(0, max(etki_faktor) * 1.15)

plt.tight_layout()
plt.savefig("09d_lollipop.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n 4 özel grafik türü tamamlandı!")
print("Radar, Waffle, Waterfall ve Lollipop - bunları sunumlarınızda kullanabilirsiniz.")
