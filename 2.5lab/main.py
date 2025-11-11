def C(m, n, call_counter=None):
    if call_counter is None:
        call_counter = 0
    call_counter += 1
    if m == 0 or m == n:
        return 1, call_counter
    c1, calls1 = C(m, n - 1, call_counter)
    c2, calls2 = C(m - 1, n - 1, calls1)
    return c1 + c2, calls2
N = 5
M_values = [1, 2, 3, 4, 5]
for M in M_values:
    result, num_calls = C(M, N)
    print(f"C({M}, {N}) = {result}, {num_calls}")
