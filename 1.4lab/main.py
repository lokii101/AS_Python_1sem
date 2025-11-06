# Дан список. Вывести вначале его элементы с четными номерами (в порядке возрастания номеров), а затем — элементы с нечетными номерами (также в порядке возрастания номеров).
lst = input().split()
even_elements = [lst[i] for i in range(0, len(lst), 2)]
odd_elements = [lst[i] for i in range(1, len(lst), 2)]
result = even_elements + odd_elements
print(' '.join(result))
print(even_elements)
print(odd_elements)
