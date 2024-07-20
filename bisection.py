def f(x):
    return x ** 3 - 4 * x - 9


def bisection(a, b, tolerance, max_iterations):
    if f(a) * f(b) > 0:
        print("Fungsi memiliki tanda yang sama di kedua ujung interval. Pilih interval lain.")
        return None

    iteration = 0
    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1
        if iteration >= max_iterations:
            print("Max iterations reached.")
            return midpoint

    return (a + b) / 2

if __name__ == '__main__':

    # Tentukan interval awal [a, b], toleransi, dan jumlah maksimum iterasi
    root = bisection(a=2, b=3, tolerance=1e-6, max_iterations=1000)
    print("Akar adalah:", root)
