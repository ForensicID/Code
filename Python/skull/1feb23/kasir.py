import json
import ramdom
import datetime

menu = {}
file_path = "\RANZ\SAAS\1 Februari\menu.json"

try :
    with open(file_path, 'r') as file:
    # Parse string JSON ke dictionary
        menu = json.load(file)

except Exception as e :
    print (f"Terjadi kesalahan: {e}")

# Menampilkan menu makanan dan minuman
print()
print('|=================================|')
print('|           DAFTAR MENU           |')
print('|=================================|')
print(f"|{' Kode':7} | {' Menu':15} | {' Harga ':8}")
print('|=================================|')
for item, info in menu.items():
    print(f"| {info[ 'kode']:4} | { item:14} | Rp{info['harga']:8}    |")
print('|=================================|')

# Fungsi untuk mengambil pesanan dari pelanggan
def take_order(menu):
    name = input("Nama Pelanggan: ")
    orders = []
    total_harga = 0
    print("Masukkan kode menu dan porsi (Contoh: 3, 2)")
    print('(Pilih nomor 0 untuk selesai)')
    while True:
        try:
            order = input("Pesanan: ")
            if order.lower() == '0':
                break
            kode_pesanan, porsi = order.split(", ")
            if kode_pesanan in [info['kode'] for info in menu.values()]:
                item_terpilih = next(item for item, info in menu.items() if info['kode'] == kode_pesanan)
                harga_terpilih = menu[item_terpilih]['harga']
                print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
                if item in menu:
                    harga = harga_terpilih * int(porsi)
                    total_harga += harga
                    orders.append({'item': item_terpilih, 'porsi': int(porsi), 'harga': harga})
                else:
                    print(f"Item {item} tidak tersedia di menu.")
            else:
                print("Kode menu tidak valid.")
        except:
            print('Format input salah')

    print(f"Total Harga {'':15} Rp{total_harga:8} ")
    print('|------------------------------|')
    uang_pelanggan = int(input(f"Masukkan jumlah uang bayar: Rp {'':1}"))
    kode_transaksi = random.randint(111111111,999999999)
    tanggal = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%5"))
    return name, orders, total_harga, uang_pelanggan,tanggal,kode_transaksi

# Fungsi untuk menyimpan pesanan ke dalam file
def sum_order(total_harga, uang):
    kembalian = int(uang) - int(total_harga)
    return int(kembalian)

def save_order(nama_pelanggan, orders, total_harga):
    order_details = {
        'Tanggal': tanggal,
        'Kode Transaksi': kode_transaksi,
        'Nama Pelanggan': nama_pelanggan,
        'orders': orders,
        'total_harga': total_harga,
        'uang_pelanggan': uang_pelanggan,
        'kembalian': kembalian

    }
    with open('\RANZ\SAAS\1 Februari\pesanan.txt', 'a') as file:
        file.write(json.dumps(order_details) + "\n")

# Fungsi untuk membaca dan menampilkan pesanan dari file
def read_orders():
    with open('pesanan.txt', 'r') as file:
        lines = file.readlines()
        baris_terakhir = lines[-1]
        order_details = json.loads(baris_terakhir)
        print()
        print('|==============================|')
        print(f" | Nama Pelanggan: {order_details['Nama Pelanggan']:15}           |")
        print('|==============================|')
        print("|        Detail Pesanan        |")
        print('|==============================|')
        print(f"|{'       Menu':20} | {'Porsi':2} | {'    Harga  ':6} |")
        print('|==============================|')
        for order in order_details['orders']:
            print(f"| {order[ 'item'  ]:17} |{order['porsi']:5}  | Rp{order['harga']:8} |")
            print('|==============================|')
        print(f"|Total Harga {'':15}     Rp{order_details['total_harga']:8} |")
        print('|------------------------------|')
        print('|==============================|')
        print('|         Terima Kasih         |')
        print('|==============================|')

# Penggunaan fungsi
nama_pelanggan, orders, total_harga = take_order(menu)
save_order(nama_pelanggan, orders, total_harga)
read_orders()
print()
