#Для заданного натурального n подсчитать сумму:\begin{align} 1 - 2^3 + 3^3 - ... + (-1)^{n + 1}n^3. \end{align}
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        term = (-1) ** (i + 1) * (i ** 3)
        total += term
    return total
n = int(input(" n: "))
result = calculate_sum(n)
print(f" n = {n}: {result}")
