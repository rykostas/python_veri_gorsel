# ============================================================
#  WORKSHOP: Python ile Veri Görselleştirme
#  Dosya 00 - Kurulum ve Ortam Hazırlığı
# ============================================================
#  Bu dosyayı çalıştırarak gerekli kütüphaneleri yükleyin.
# ============================================================

import subprocess
import sys

paketler = [
    "matplotlib",
    "numpy",
    "pandas",
    "seaborn",
    "plotly",
    "wordcloud",
    "scikit-learn",
    "Pillow",
    "networkx",
]

print("=" * 50)
print("  Gerekli paketler yükleniyor...")
print("=" * 50)

for paket in paketler:
    print(f"\n>>> {paket} yükleniyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", paket, "-q"])

print("\n" + "=" * 50)
print("  Tüm paketler başarıyla yüklendi!")
print("  Workshop'a hazırsınız!")
print("=" * 50)
