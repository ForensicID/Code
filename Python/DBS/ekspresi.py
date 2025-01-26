dico = 750000

if dico > 500000:
    diskon = 0.1 * dico
    total_harga = dico - diskon
else:
    total_harga = dico
print("Total harga setelah diskon:", total_harga)