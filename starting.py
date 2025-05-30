veriler = [
    ([1], 0),
    ([2], 1),
    ([3], 0),
    ([4], 1),
]
lastnum = 10
agirlik = 0.5
ogrenme_orani = 0.1
#learning process start
for epoch in range(100):
    toplam_hata = 0
    for girdi, hedef in veriler:
        tahmin = girdi[0] * agirlik
        hata = hedef - tahmin
        agirlik += hata * ogrenme_orani
        toplam_hata += abs(hata)
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Toplam Hata: {toplam_hata:.4f}")
#learning process end
# test
print("\nSonuçlar:")
tahmin = lastnum * agirlik
print(f"Girdi: {lastnum}, Tahmin: {round(tahmin, 3)}")
