import time
import matplotlib.pyplot as plt
from iteratif import iteratifAlgo
from rekursif import rekursif_sequential_search

def load_kost_prices(file_path):
    """Membaca file teks dan mengembalikan daftar harga kost."""
    try:
        with open(file_path, 'r') as file:
            # Baca file dan pisahkan data berdasarkan koma atau spasi
            data = file.read().replace('\n', ',').split(',')
            # Ubah ke dalam bentuk integer
            return [int(price.strip()) for price in data if price.strip().isdigit()]
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan. Menggunakan data dummy.")
        return [1000000, 1200000, 1500000]  # Data dummy
    except ValueError:
        print("Error membaca file. Pastikan format data benar.")
        return []

def measure_time_iterative(arr, target):
    """Mengukur waktu eksekusi untuk algoritma iteratif."""
    start_time = time.perf_counter()
    iteratifAlgo(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time

def measure_time_recursive(arr, target):
    """Mengukur waktu eksekusi untuk algoritma rekursif."""
    start_time = time.perf_counter()
    rekursif_sequential_search(arr, target, 0)
    end_time = time.perf_counter()
    return end_time - start_time

def average_time(func, arr, target, repetitions=10):
    """Menghitung rata-rata waktu eksekusi dari suatu fungsi."""
    total_time = 0
    for _ in range(repetitions):
        total_time += func(arr, target)
    return total_time / repetitions

# Load data dari file
kost_prices = load_kost_prices('kost_prices.txt')

# Input harga target dari pengguna
default_price = 1000000
try:
    target_price = int(input("Masukkan harga yang ingin dicari: "))
except ValueError:
    print("Input tidak valid. Menggunakan harga default.")
    target_price = default_price

# Jika harga tidak ditemukan, gunakan default
if target_price not in kost_prices:
    print("Harga tidak ditemukan. Menggunakan harga default.")
    target_price = default_price

# Pencarian menggunakan algoritma iteratif
index_found = iteratifAlgo(kost_prices, target_price)
if index_found != -1:
    print(f"Kost dengan harga {target_price} ditemukan di indeks {index_found}.")
else:
    print("Kost dengan harga tersebut tidak ditemukan.")

# Data untuk grafik
sizes = sorted(list(range(10, len(kost_prices) + 1, 500)))
iterative_times = []
recursive_times = []

# Mengukur waktu eksekusi untuk setiap ukuran data
for size in sizes:
    sublist_prices = kost_prices[:size]
    iterative_times.append(average_time(measure_time_iterative, sublist_prices, target_price))
    recursive_times.append(average_time(measure_time_recursive, sublist_prices, target_price))

# Plot hasil waktu eksekusi algoritma iteratif
plt.figure(figsize=(10, 6))
plt.plot(sizes, iterative_times, label="Iteratif", color="blue")
plt.xlabel("Jumlah Data", fontsize=12)
plt.ylabel("Waktu Eksekusi (detik)", fontsize=12)
plt.title("Kompleksitas Waktu Algoritma Iteratif", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()

# Plot hasil waktu eksekusi algoritma rekursif
plt.figure(figsize=(10, 6))
plt.plot(sizes, recursive_times, label="Rekursif", color="green")
plt.xlabel("Jumlah Data", fontsize=12)
plt.ylabel("Waktu Eksekusi (detik)", fontsize=12)
plt.title("Kompleksitas Waktu Algoritma Rekursif", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()

# Plot perbandingan iteratif dan rekursif
plt.figure(figsize=(10, 6))
plt.plot(sizes, iterative_times, label="Iteratif", color="blue")
plt.plot(sizes, recursive_times, label="Rekursif", color="green")
plt.xlabel("Jumlah Data", fontsize=12)
plt.ylabel("Waktu Eksekusi (detik)", fontsize=12)
plt.title("Perbandingan Waktu: Iteratif vs Rekursif", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
