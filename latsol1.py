
nama_buah = input("Masukkan nama buah (maksimum 20 karakter): ")
if len(nama_buah) > 20:
    print("Nama buah tidak boleh lebih dari 20 karakter.")
else:
    harga_jual = float(input("Masukkan harga jual per kilogram: "))
    kg_terjual = int(input("Masukkan jumlah kilogram yang terjual: "))
    total_keuntungan = harga_jual * kg_terjual
    print(f"Buah {nama_buah} menghasilkan keuntungan: {total_keuntungan:.2f}")