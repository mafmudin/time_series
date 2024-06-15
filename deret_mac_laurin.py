import sympy as sp

# Definisikan variabel dan fungsi
x = sp.Symbol('x')
f = sp.sin(x)**2

# Hitung turunan pertama hingga ke-n
n = 5  # jumlah suku dalam deret Maclaurin
derivatives = [f]
for i in range(1, n):
    derivatives.append(sp.diff(derivatives[-1], x))

# Evaluasi turunan pada x = 0
evaluated_derivatives = [deriv.subs(x, 0) for deriv in derivatives]

# Bangun deret Maclaurin
maclaurin_series = sum(evaluated_derivatives[i] / sp.factorial(i) * x**i for i in range(n))

# Sederhanakan hasil
maclaurin_series = sp.simplify(maclaurin_series)

# Tampilkan deret Maclaurin
print(maclaurin_series)
