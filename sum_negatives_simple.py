def sum_negatives(arr):
    if len(arr) < 2:
        return 0

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    start = min(max_index, min_index) + 1
    end = max(max_index, min_index)

    negative_sum = sum(x for x in arr[start:end] if x < 0)

    return negative_sum
# Пример использования
arr = [5, -18, -20, 4, -5, 10, -3, 8]
print(sum_negatives(arr))
# -5