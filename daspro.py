barang_jualan = ["susu", "roti", "minyak", "gula", "mie instan", "beras", "teh"]
barang_jualan[4] = "mentega"
jualan_set = set(barang_jualan)

print(f"Barang jualan sebelumnya = {jualan_set}")

barang_jualan_baru = {"kopi", "terigu"}
jualan_set.update(barang_jualan_baru)

print(f"barang jualan terkini = {jualan_set}")
print(len(jualan_set))