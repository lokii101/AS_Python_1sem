def filter_items(items, condition=None):
    if condition is None:
        return items.copy()
    return [item for item in items if condition(item)]
print(filter_items([1, 2, 3, 4, 5]))
print(filter_items([1, 2, 3, 4, 5], condition=lambda x: x > 3))

def merge_and_filter(list1, list2, filter_function=None):
    merged = list1 + list2
    if filter_function is None:
        return merged
    return [item for item in merged if filter_function(item)]
print(merge_and_filter([1, 2], [3, 4]))
# → [1, 2, 3, 4]
print(merge_and_filter([1, 2], [3, 4], filter_function=lambda x: x % 2 == 0))
# → [2, 4]

def common_in_all(*lists):
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return list(common)
print(common_in_all([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(common_in_all(['яблоко', 'вишня'], ['виноград', 'вишня'], ['вишня', 'дыня']))

def find_primes(*numbers):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]
print(find_primes(2, 3, 4, 5, 6, 7))  
print(find_primes(10, 15, 17, 19, 23))
