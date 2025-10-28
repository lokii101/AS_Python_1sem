#Дан список. Выбрать из списка все числа больше заданного числа k и упорядочить их по убыванию.
def filter_and_sort(numbers, k):
    filtered = [num for num in numbers if num > k]
    filtered.sort(reverse=True)
    return filtered
numbers = [10, 3, 7, 15, 2, 9, 12]
k = 5
result = filter_and_sort(numbers, k)
print(result)
