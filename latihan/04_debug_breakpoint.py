
def hitung_total(harga, jumlah):
    subtotal = harga * jumlah
    pajak = subtotal * 0.1
    total = subtotal + pajak
    return total


hasil = hitung_total(10000, 2)
print("Total pembayaran:", hasil)
