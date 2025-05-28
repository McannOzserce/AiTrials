veriler = [
    ([1], 2),
    ([2], 4),
    ([3], 6),
    ([4], 8),
]

agirlik = 0.5
ogrenme_orani = 0.1

for epoch in range(100):
    toplam_hata = 0
    for girdi, hedef in veriler:
        tahmin = girdi[0] * agirlik
        hata = hedef - tahmin
        agirlik += hata * ogrenme_orani
        toplam_hata += abs(hata)
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Toplam Hata: {toplam_hata:.4f}")

# Test et
print("\nSonuçlar:")
for girdi, hedef in veriler:
    tahmin = girdi[0] * agirlik
    print(f"Girdi: {girdi[0]}, Tahmin: {round(tahmin, 3)}, Hedef: {hedef}")
