import sympy as sp

# Definisikan variabel dan fungsi
x = sp.Symbol('x')
a = 2
f = 1 / (4 * x + 8)

# Hitung turunan pertama hingga ke-n
n = 5  # jumlah suku dalam deret Taylor
derivatives = [f]
for i in range(1, n):
    derivatives.append(sp.diff(derivatives[-1], x))

# Evaluasi turunan pada x = 2
evaluated_derivatives = [deriv.subs(x, a) for deriv in derivatives]

# Bangun deret Taylor
taylor_series = sum(evaluated_derivatives[i] / sp.factorial(i) * (x - a)**i for i in range(n))

# Sederhanakan hasil
taylor_series = sp.simplify(taylor_series)

# Tampilkan deret Taylor
print(taylor_series)