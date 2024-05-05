import matplotlib.pyplot as plt
import numpy as np

# Data pengunjung pasien per minggu (contoh data)
minggu = np.arange(1, 53)  # 52 minggu dalam setahun
pengunjung = np.random.randint(50, 200, size=52)  # Data jumlah pengunjung, di sini dihasilkan secara acak


def eda_plot(minggu, pengunjung):
    # Plot data
    plt.figure(figsize=(10, 6))
    plt.plot(minggu, pengunjung, marker='o', linestyle='-')

    # Menambahkan judul dan label sumbu
    plt.title('Grafik Jumlah Pengunjung Pasien per Minggu')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah Pengunjung')

    # Menambahkan grid
    plt.grid(True)

    # Menampilkan plot
    plt.show()

def eda_bar(minggu, pengunjung):
    # Grafik Batang
    plt.figure(figsize=(10, 6))
    plt.bar(minggu, pengunjung, color='skyblue')
    plt.title('Grafik Jumlah Pengunjung Pasien per Minggu')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah Pengunjung')
    plt.grid(True)
    plt.show()

def eda_his(pengunjung):
    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(pengunjung, bins=10, color='lightgreen', edgecolor='black')
    plt.title('Histogram Jumlah Pengunjung Pasien per Minggu')
    plt.xlabel('Jumlah Pengunjung')
    plt.ylabel('Frekuensi')
    plt.grid(True)
    plt.show()

def eda_pie(minggu, pengunjung):
    # Diagram Lingkaran
    plt.figure(figsize=(8, 8))
    plt.pie(pengunjung[:12], labels=minggu[:12], autopct='%1.1f%%', startangle=140)
    plt.title('Diagram Lingkaran Jumlah Pengunjung Pasien per Minggu (12 Minggu Pertama)')
    plt.axis('equal')
    plt.show()

def eda_scatter(minggu, pengunjung):
    # Scatter Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(minggu, pengunjung, color='orange')
    plt.title('Scatter Plot Jumlah Pengunjung Pasien per Minggu')
    plt.xlabel('Minggu')
    plt.ylabel('Jumlah Pengunjung')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    eda_plot(minggu, pengunjung)
    eda_bar(minggu, pengunjung)
    eda_his(pengunjung)
    eda_pie(minggu, pengunjung)
    eda_scatter(minggu, pengunjung)
