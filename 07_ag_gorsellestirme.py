# ============================================================
#  ADIM 7: Ağ (Network) Görselleştirme
# ============================================================
#  Akademisyenler arası iş birliği ağını görselleştiriyoruz.
#  "Kim kimle çalışıyor?" sorusuna görsel cevap!
#  WOW EFEKTİ: Gerçekçi sosyal ağ analizi
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np

np.random.seed(42)

# ============================================================
#  Akademik iş birliği ağı oluşturalım
# ============================================================

G = nx.Graph()

# Araştırmacılar ve bölümleri
arastirmacilar = {
    # Bilgisayar Bilimleri grubu
    "Prof. Yılmaz": "Bilgisayar", "Doç. Kaya": "Bilgisayar",
    "Dr. Çelik": "Bilgisayar", "Ar.Gör. Doğan": "Bilgisayar",
    # İstatistik grubu
    "Prof. Öztürk": "İstatistik", "Doç. Şahin": "İstatistik",
    "Dr. Arslan": "İstatistik",
    # Eğitim grubu
    "Prof. Demir": "Eğitim", "Doç. Aydın": "Eğitim",
    "Dr. Yıldız": "Eğitim", "Ar.Gör. Polat": "Eğitim",
    "Ar.Gör. Kurt": "Eğitim",
    # Psikoloji grubu
    "Prof. Şen": "Psikoloji", "Doç. Aksoy": "Psikoloji",
    "Dr. Erdoğan": "Psikoloji",
    # Tıp grubu
    "Prof. Korkmaz": "Tıp", "Doç. Özdemir": "Tıp",
    "Dr. Acar": "Tıp", "Ar.Gör. Kılıç": "Tıp",
    # Mühendislik
    "Prof. Taş": "Mühendislik", "Doç. Tekin": "Mühendislik",
    "Dr. Gül": "Mühendislik",
}

# Düğümleri ekle
for isim, bolum in arastirmacilar.items():
    G.add_node(isim, bolum=bolum)

# İş birlikleri (kenarlar) - ağırlıklı
is_birlikleri = [
    # Bölüm içi yoğun iş birliği
    ("Prof. Yılmaz", "Doç. Kaya", 5), ("Prof. Yılmaz", "Dr. Çelik", 4),
    ("Doç. Kaya", "Ar.Gör. Doğan", 3), ("Dr. Çelik", "Ar.Gör. Doğan", 2),
    ("Prof. Öztürk", "Doç. Şahin", 6), ("Doç. Şahin", "Dr. Arslan", 4),
    ("Prof. Demir", "Doç. Aydın", 5), ("Prof. Demir", "Dr. Yıldız", 3),
    ("Doç. Aydın", "Ar.Gör. Polat", 4), ("Ar.Gör. Polat", "Ar.Gör. Kurt", 3),
    ("Prof. Şen", "Doç. Aksoy", 5), ("Doç. Aksoy", "Dr. Erdoğan", 3),
    ("Prof. Korkmaz", "Doç. Özdemir", 4), ("Doç. Özdemir", "Dr. Acar", 3),
    ("Dr. Acar", "Ar.Gör. Kılıç", 2),
    ("Prof. Taş", "Doç. Tekin", 5), ("Doç. Tekin", "Dr. Gül", 4),
    # Disiplinler arası iş birlikleri (daha ince çizgiler)
    ("Prof. Yılmaz", "Prof. Öztürk", 3),   # Bilgisayar-İstatistik
    ("Doç. Kaya", "Dr. Arslan", 2),          # Bilgisayar-İstatistik
    ("Prof. Demir", "Prof. Şen", 2),         # Eğitim-Psikoloji
    ("Doç. Aydın", "Doç. Aksoy", 3),         # Eğitim-Psikoloji
    ("Dr. Yıldız", "Dr. Erdoğan", 2),        # Eğitim-Psikoloji
    ("Prof. Yılmaz", "Prof. Demir", 2),      # Bilgisayar-Eğitim
    ("Dr. Çelik", "Ar.Gör. Polat", 1),       # Bilgisayar-Eğitim
    ("Prof. Korkmaz", "Prof. Öztürk", 2),    # Tıp-İstatistik
    ("Prof. Taş", "Prof. Yılmaz", 3),        # Mühendislik-Bilgisayar
    ("Doç. Tekin", "Doç. Kaya", 2),           # Mühendislik-Bilgisayar
    ("Dr. Gül", "Dr. Acar", 1),              # Mühendislik-Tıp
    ("Ar.Gör. Kurt", "Ar.Gör. Kılıç", 1),   # Eğitim-Tıp
]

for u, v, w in is_birlikleri:
    G.add_edge(u, v, weight=w)

# ============================================================
#  Ağ görselini çizelim
# ============================================================

fig, ax = plt.subplots(figsize=(16, 12))

# Bölüm renkleri
bolum_renkleri = {
    "Bilgisayar": "#e74c3c",
    "İstatistik": "#3498db",
    "Eğitim": "#2ecc71",
    "Psikoloji": "#f39c12",
    "Tıp": "#9b59b6",
    "Mühendislik": "#1abc9c",
}

# Düğüm renkleri
node_colors = [bolum_renkleri[arastirmacilar[n]] for n in G.nodes()]

# Düğüm boyutları - merkezilik ölçüsüne göre (önemli kişiler büyük)
merkezilik = nx.betweenness_centrality(G)
node_sizes = [2000 + merkezilik[n] * 15000 for n in G.nodes()]

# Kenar kalınlıkları
edge_weights = [G[u][v]["weight"] for u, v in G.edges()]

# Yay düzeni (spring layout)
pos = nx.spring_layout(G, k=2.5, iterations=100, seed=42)

# Kenarları çiz
nx.draw_networkx_edges(G, pos, ax=ax, width=edge_weights,
                        alpha=0.3, edge_color="#7f8c8d",
                        style="solid")

# Düğümleri çiz
nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                        node_size=node_sizes, alpha=0.85,
                        edgecolors="white", linewidths=2)

# Etiketler
for node, (x, y) in pos.items():
    kisa_isim = node.split(". ")[-1]  # Sadece soyisim
    unvan = node.split(".")[0] + "."
    ax.annotate(f"{unvan}\n{kisa_isim}",
                xy=(x, y), ha="center", va="center",
                fontsize=8, fontweight="bold",
                color="white" if merkezilik[node] > 0.05 else "#2c3e50")

# Lejant
patches = [mpatches.Patch(color=renk, label=bolum)
           for bolum, renk in bolum_renkleri.items()]
ax.legend(handles=patches, loc="upper left", fontsize=11, framealpha=0.9,
          title="Bölümler", title_fontsize=13)

ax.set_title("Akademik İş Birliği Ağı\nDüğüm boyutu = Aracılık Merkeziliği (ne kadar köprülük rolü var)",
             fontsize=16, fontweight="bold", pad=20)
ax.axis("off")

plt.tight_layout()
plt.savefig("07a_akademik_ag.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
#  Ağ istatistikleri
# ============================================================

print("\n" + "=" * 50)
print("  AĞ İSTATİSTİKLERİ")
print("=" * 50)
print(f"  Toplam araştırmacı  : {G.number_of_nodes()}")
print(f"  Toplam iş birliği   : {G.number_of_edges()}")
print(f"  Ağ yoğunluğu        : {nx.density(G):.3f}")
print(f"  Ort. bağlantı sayısı: {sum(dict(G.degree()).values())/G.number_of_nodes():.1f}")

print("\n  En merkezi araştırmacılar (köprülük rolü):")
for isim, deger in sorted(merkezilik.items(), key=lambda x: -x[1])[:5]:
    print(f"    {isim}: {deger:.3f}")

# ============================================================
#  BONUS: Topluluk Tespiti (Community Detection)
# ============================================================

from networkx.algorithms.community import greedy_modularity_communities

topluluklar = list(greedy_modularity_communities(G))

fig2, ax2 = plt.subplots(figsize=(16, 12))

# Her topluluğa farklı renk
topluluk_renkleri = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]
node_renk_topluluk = []
for node in G.nodes():
    for i, topluluk in enumerate(topluluklar):
        if node in topluluk:
            node_renk_topluluk.append(topluluk_renkleri[i % len(topluluk_renkleri)])
            break

# Topluluk alanları çiz
for i, topluluk in enumerate(topluluklar):
    members_pos = np.array([pos[n] for n in topluluk])
    center = members_pos.mean(axis=0)
    radius = np.max(np.linalg.norm(members_pos - center, axis=1)) + 0.15
    circle = plt.Circle(center, radius, alpha=0.08,
                        color=topluluk_renkleri[i % len(topluluk_renkleri)])
    ax2.add_patch(circle)

nx.draw_networkx_edges(G, pos, ax=ax2, width=edge_weights,
                        alpha=0.2, edge_color="#95a5a6")

nx.draw_networkx_nodes(G, pos, ax=ax2, node_color=node_renk_topluluk,
                        node_size=node_sizes, alpha=0.85,
                        edgecolors="white", linewidths=2)

for node, (x, y) in pos.items():
    kisa = node.split(". ")[-1]
    ax2.annotate(kisa, xy=(x, y), ha="center", va="center",
                fontsize=9, fontweight="bold")

ax2.set_title("Topluluk Tespiti (Community Detection)\nAlgoritma otomatik olarak araştırma kümelerini buluyor!",
              fontsize=16, fontweight="bold", pad=20)
ax2.axis("off")

plt.tight_layout()
plt.savefig("07b_topluluk_tespiti.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"\n  Tespit edilen topluluk sayısı: {len(topluluklar)}")
for i, topluluk in enumerate(topluluklar):
    uyeler = ", ".join([n.split('. ')[-1] for n in sorted(topluluk)])
    print(f"  Topluluk {i+1}: {uyeler}")

print("\n Ağ görselleştirmesi tamamlandı!")
print("İş birliği örüntüleri ve topluluklar tek bakışta görülüyor.")
