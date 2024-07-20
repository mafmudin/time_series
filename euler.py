import numpy as np


def f(x, y):
    return y - x


def euler_method(x0, y0, h, x_end):
    # Jumlah langkah yang diperlukan
    n_steps = int((x_end - x0) / h)

    # Inisialisasi array untuk menyimpan nilai x dan y
    x_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)

    # Nilai awal
    x_values[0] = x0
    y_values[0] = y0

    # Metode Euler
    for i in range(1, n_steps + 1):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])
        x_values[i] = x_values[i - 1] + h

    return x_values, y_values


# Parameter
x0 = 0
y0 = 1
h = 0.1
x_end = 0.3

if __name__ == '__main__':

    # Hitung menggunakan metode Euler
    x_vals, y_vals = euler_method(x0, y0, h, x_end)

    # Output hasil
    for x, y in zip(x_vals, y_vals):
        print(f"x = {x:.1f}, y = {y:.4f}")
