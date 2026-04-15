# ============================================================
#  ADIM 10: FİNAL - Maximum WOW Efekti!
# ============================================================
#  Workshop'un kapanışı için en etkileyici görseller:
#  1) Galaksi tarzı scatter plot
#  2) Müzik tarzı dalga formu
#  3) Matematik sanatı - Spirograph
#  4) Sankey diagram
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import plotly.graph_objects as go

# ============================================================
#  WOW 1: "Akademik Galaksi" - Bilim dallarının evreni
# ============================================================

np.random.seed(42)

fig, ax = plt.subplots(figsize=(14, 14), facecolor="#0a0a2e")
ax.set_facecolor("#0a0a2e")

# Galaksi kolu oluşturma fonksiyonu
def galaksi_kolu(n, aci_offset, yayilim, renk, isim):
    t = np.random.uniform(0, 4 * np.pi, n)
    r = t * 15 + np.random.normal(0, yayilim, n)
    x = r * np.cos(t + aci_offset) + np.random.normal(0, yayilim * 2, n)
    y = r * np.sin(t + aci_offset) + np.random.normal(0, yayilim * 2, n)
    boyut = np.random.exponential(3, n) * 5
    alpha = np.clip(0.3 + np.random.uniform(0, 0.5, n), 0, 0.8)
    return x, y, boyut, renk, alpha, isim

kollar = [
    galaksi_kolu(800, 0, 8, "#FF6B6B", "Fen Bilimleri"),
    galaksi_kolu(700, np.pi * 0.5, 8, "#4ECDC4", "Mühendislik"),
    galaksi_kolu(600, np.pi, 8, "#45B7D1", "Sağlık Bilimleri"),
    galaksi_kolu(750, np.pi * 1.5, 8, "#FFEAA7", "Sosyal Bilimler"),
]

for x, y, boyut, renk, alpha, isim in kollar:
    for i in range(len(x)):
        ax.scatter(x[i], y[i], s=boyut[i], c=renk, alpha=alpha[i],
                  edgecolors="none")

# Merkez - parlak çekirdek
for size, alpha in [(5000, 0.03), (2000, 0.05), (800, 0.1), (300, 0.2), (100, 0.4)]:
    ax.scatter(0, 0, s=size, c="white", alpha=alpha, edgecolors="none")

# Arka plan yıldızları
n_yildiz = 500
ax.scatter(np.random.uniform(-200, 200, n_yildiz),
           np.random.uniform(-200, 200, n_yildiz),
           s=np.random.uniform(0.1, 1, n_yildiz),
           c="white", alpha=0.3, edgecolors="none")

# Lejant
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#FF6B6B",
           markersize=12, label="Fen Bilimleri", linestyle="None"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#4ECDC4",
           markersize=12, label="Mühendislik", linestyle="None"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#45B7D1",
           markersize=12, label="Sağlık Bilimleri", linestyle="None"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#FFEAA7",
           markersize=12, label="Sosyal Bilimler", linestyle="None"),
]
ax.legend(handles=legend_elements, loc="upper right", fontsize=13,
          facecolor="#1a1a3e", edgecolor="#444", labelcolor="white",
          title="Bilim Dalları", title_fontsize=14)

ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.axis("off")
ax.set_title("Akademik Galaksi\nHer yıldız bir yayın, her kol bir bilim dalı",
             fontsize=20, fontweight="bold", color="white", pad=20)

plt.tight_layout()
plt.savefig("10a_akademik_galaksi.png", dpi=150, bbox_inches="tight",
            facecolor="#0a0a2e")
plt.show()

# ============================================================
#  WOW 2: Matematiksel Sanat - Spirograph Çizimleri
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 12), facecolor="#0a0a2e")

parametreler = [
    (5, 3, 5, "plasma"),
    (7, 4, 2, "viridis"),
    (8, 3, 4, "inferno"),
    (11, 7, 3, "magma"),
    (9, 5, 7, "coolwarm"),
    (13, 8, 5, "twilight"),
]

for ax, (R, r, d, cmap) in zip(axes.flat, parametreler):
    ax.set_facecolor("#0a0a2e")
    t = np.linspace(0, 2 * np.pi * r / np.gcd(R, r), 10000)
    x = (R - r) * np.cos(t) + d * np.cos((R - r) / r * t)
    y = (R - r) * np.sin(t) + d * np.sin((R - r) / r * t)

    # Renk değişimini zamana göre yap
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    colors = plt.cm.get_cmap(cmap)(np.linspace(0, 1, len(x)))

    for i in range(0, len(x) - 1, 5):
        ax.plot(x[i:i+6], y[i:i+6], color=colors[i], linewidth=0.5, alpha=0.8)

    ax.set_xlim(min(x) * 1.1, max(x) * 1.1)
    ax.set_ylim(min(y) * 1.1, max(y) * 1.1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"R={R}, r={r}, d={d}", color="white", fontsize=12)

fig.suptitle("Spirograph: Matematiksel Sanat\nSadece sinüs ve kosinüs fonksiyonları ile",
             fontsize=20, fontweight="bold", color="white", y=0.98)

plt.tight_layout()
plt.savefig("10b_spirograph.png", dpi=150, bbox_inches="tight",
            facecolor="#0a0a2e")
plt.show()

# ============================================================
#  WOW 3: Fibonacci Spirali - Doğanın Matematiği
# ============================================================

fig, ax = plt.subplots(figsize=(12, 12), facecolor="#fefae0")
ax.set_facecolor("#fefae0")

# Altın oran spirali
phi = (1 + np.sqrt(5)) / 2
t = np.linspace(0, 6 * np.pi, 2000)
r = phi ** (t / (2 * np.pi))
x = r * np.cos(t)
y = r * np.sin(t)

# Renk gradyanı
colors = plt.cm.YlOrRd(np.linspace(0.2, 0.9, len(t)))

for i in range(len(t) - 1):
    ax.plot(x[i:i+2], y[i:i+2], color=colors[i], linewidth=2)

# Fibonacci sayıları ile kareler
fib = [1, 1, 2, 3, 5, 8, 13, 21]
pozisyon_x, pozisyon_y = 0, 0
yon = 0  # 0: sağ, 1: yukarı, 2: sol, 3: aşağı

for i, f in enumerate(fib):
    renk = plt.cm.YlOrRd(i / len(fib) * 0.7 + 0.2)
    rect = plt.Rectangle((pozisyon_x, pozisyon_y), f, f,
                          fill=False, edgecolor=renk, linewidth=2, alpha=0.5)
    ax.add_patch(rect)
    ax.text(pozisyon_x + f/2, pozisyon_y + f/2, str(f),
            ha="center", va="center", fontsize=min(f * 3, 20),
            fontweight="bold", color=renk, alpha=0.7)

    if yon == 0:
        pozisyon_x += f
    elif yon == 1:
        pozisyon_y += f
    elif yon == 2:
        pozisyon_x -= fib[i+1] if i+1 < len(fib) else f
    elif yon == 3:
        pozisyon_y -= fib[i+1] if i+1 < len(fib) else f

    yon = (yon + 1) % 4

ax.set_xlim(-5, 40)
ax.set_ylim(-15, 30)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Fibonacci Spirali - Doğanın Matematiği\n"
             "Altın Oran (φ = 1.618...) her yerde: çiçeklerde, kabuklarda, galaksilerde...",
             fontsize=16, fontweight="bold", pad=20, color="#5a3e2b")

plt.tight_layout()
plt.savefig("10c_fibonacci.png", dpi=150, bbox_inches="tight",
            facecolor="#fefae0")
plt.show()

# ============================================================
#  WOW 4: Sankey Diagram - Öğrenci Akışı
# ============================================================

fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20,
        thickness=25,
        line=dict(color="white", width=1),
        label=[
            # Kaynak (0-4)
            "Fen Lisesi", "Anadolu Lisesi", "Meslek Lisesi",
            "Özel Lise", "Diğer",
            # Fakülte (5-10)
            "Mühendislik", "Tıp", "Hukuk",
            "Fen-Edebiyat", "Eğitim", "Sosyal Bil.",
            # Çıktı (11-15)
            "Özel Sektör", "Kamu", "Akademi",
            "Girişimci", "Yurt Dışı"
        ],
        color=[
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7",
            "#e74c3c", "#3498db", "#f39c12", "#2ecc71", "#9b59b6", "#1abc9c",
            "#2c3e50", "#7f8c8d", "#8e44ad", "#d35400", "#16a085"
        ],
    ),
    link=dict(
        source=[
            # Lise -> Fakülte
            0,0,0,0, 1,1,1,1,1, 2,2,2, 3,3,3,3, 4,4,
            # Fakülte -> Kariyer
            5,5,5,5, 6,6,6, 7,7,7, 8,8,8, 9,9, 10,10,10
        ],
        target=[
            # Lise -> Fakülte
            5,6,8,10, 5,6,7,8,9, 5,9,10, 5,6,7,8, 9,10,
            # Fakülte -> Kariyer
            11,12,13,14, 11,12,14, 11,12,13, 12,13,14, 12,13, 11,12,14
        ],
        value=[
            # Lise -> Fakülte
            40,30,15,5, 25,15,20,20,15, 30,20,10, 15,10,10,8, 10,5,
            # Fakülte -> Kariyer
            50,20,15,10, 25,15,10, 20,15,5, 10,25,8, 20,15, 15,12,5
        ],
        color=[
            "rgba(255,107,107,0.3)", "rgba(255,107,107,0.3)",
            "rgba(255,107,107,0.3)", "rgba(255,107,107,0.3)",
            "rgba(78,205,196,0.3)", "rgba(78,205,196,0.3)",
            "rgba(78,205,196,0.3)", "rgba(78,205,196,0.3)",
            "rgba(78,205,196,0.3)",
            "rgba(69,183,209,0.3)", "rgba(69,183,209,0.3)",
            "rgba(69,183,209,0.3)",
            "rgba(150,206,180,0.3)", "rgba(150,206,180,0.3)",
            "rgba(150,206,180,0.3)", "rgba(150,206,180,0.3)",
            "rgba(255,234,167,0.3)", "rgba(255,234,167,0.3)",
            "rgba(231,76,60,0.3)", "rgba(231,76,60,0.3)",
            "rgba(231,76,60,0.3)", "rgba(231,76,60,0.3)",
            "rgba(52,152,219,0.3)", "rgba(52,152,219,0.3)",
            "rgba(52,152,219,0.3)",
            "rgba(243,156,18,0.3)", "rgba(243,156,18,0.3)",
            "rgba(243,156,18,0.3)",
            "rgba(46,204,113,0.3)", "rgba(46,204,113,0.3)",
            "rgba(46,204,113,0.3)",
            "rgba(155,89,182,0.3)", "rgba(155,89,182,0.3)",
            "rgba(26,188,156,0.3)", "rgba(26,188,156,0.3)",
            "rgba(26,188,156,0.3)",
        ],
    )
)])

fig_sankey.update_layout(
    title_text="Öğrenci Yolculuğu: Lise → Üniversite → Kariyer<br>"
               "<sub>Akışların kalınlığı öğrenci sayısını temsil eder</sub>",
    font_size=14,
    title_font_size=20,
    height=650,
    paper_bgcolor="white",
)

fig_sankey.write_html("10d_sankey_ogrenci_akisi.html")
fig_sankey.show()
print("10d_sankey_ogrenci_akisi.html oluşturuldu!")

# ============================================================
#  KAPANIŞ MESAJI
# ============================================================

print("\n" + "=" * 60)
print("   WORKSHOP TAMAMLANDI!")
print("=" * 60)
print("""
   Bu workshop'ta öğrendiklerimiz:

   01 - Temel grafikler (çizgi, çubuk, pasta)
   02 - Dashboard mantığı (4'lü görsel)
   03 - Seaborn ile istatistiksel grafikler
   04 - Animasyonlu Gapminder grafiği
   05 - Plotly interaktif grafikler (3D, Sunburst)
   06 - Kelime bulutu
   07 - Ağ (Network) görselleştirme
   08 - Türkiye haritası üzerinde veri
   09 - Radar, Waffle, Waterfall, Lollipop
   10 - Galaksi, Spirograph, Fibonacci, Sankey

   Şimdi sıra sizde!
   Kendi verilerinizle denemeler yapın.
""")
print("=" * 60)
