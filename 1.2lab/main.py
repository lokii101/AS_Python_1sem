#Напечатать квадраты всех целых чисел от A до B (A<B) с шагом H.
A = int(input("A:"))
B = int(input("B (B > A): "))
H = int(input("H: "))
if A >= B or H <= 0:
    print(": A > B, а H > 0")
else:
    for number in range(A, B + 1, H):
        square = number ** 2
        print(f"2** {number} == {square}")
