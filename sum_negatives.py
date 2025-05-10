def sum_negatives_between_max_min(arr):
    """
    Возвращает сумму отрицательных элементов между первыми вхождениями
    максимального и минимального элементов массива.
    """

    if len(arr) < 3:
        return 0, "not_enough_elements"

    value_min = min(arr)
    value_max = max(arr)

    index_min = arr.index(value_min)
    index_max = arr.index(value_max)

    # Новый случай: максимум и минимум рядом
    if abs(index_min - index_max) == 1:
        return 0, "max_min_adjacent"

    start_pos = min(index_min, index_max) + 1
    end_pos = max(index_min, index_max)

    if start_pos >= end_pos:
        return 0, "no_elements"

    interval_slice = arr[start_pos:end_pos]
    negatives_in_slice = [num for num in interval_slice if num < 0]

    if not negatives_in_slice:
        return 0, "no_negatives"

    negative_sum = sum(negatives_in_slice)
    return negative_sum, None


def get_valid_array():
    """
    Запрашивает у пользователя ввод целых чисел до тех пор, пока не будет введено
    минимум три числа. Обрабатывает ошибки ввода.
    """
    while True:
        user_input = input("Введите целые числа через пробел (не менее трёх чисел): ")
        elements = user_input.strip().split()

        if not elements:
            print("❗ Ошибка: вы ничего не ввели. Попробуйте ещё раз.")
            continue

        try:
            arr = list(map(int, elements))
        except ValueError:
            print("❗ Ошибка: все элементы должны быть целыми числами.")
            continue

        if len(arr) < 3:
            print(f"⚠️ Мало элементов: {len(arr)}. Введите не менее трёх чисел.")
        else:
            return arr


if __name__ == "__main__":
    print("🔢 Кейс-задача №1. Сумма отрицательных элементов между max и min.")
    print("Данная программа позволяет найти сумму отрицательных элементов,")
    print("расположенных между максимальным и минимальным элементами массива.")
    print()
    print("📌 Формат ввода:")
    print("Введите целые числа через пробел (не менее трёх чисел).")
    print("Пример ввода: 5 -1 -4 2 -5 6 -2 0")
    print("Пример вывода: 0")
    print()

    array = get_valid_array()
    result, reason = sum_negatives_between_max_min(array)
    print("🏁 Результат:", result)

    match reason:
        case "no_elements":
            print("ℹ️ Примечание: между максимальным и минимальным элементами нет чисел.")
        case "no_negatives":
            print("ℹ️ Примечание: отрицательных чисел между max и min не найдено.")
        case "not_enough_elements":
            print("⚠️ Примечание: введено меньше трёх чисел — интервал определить нельзя.")
        case "max_min_adjacent":
            print("ℹ️ Примечание: максимальный и минимальный элементы находятся рядом — между ними нет чисел.")
        case _:
            print("✅ Отрицательные числа успешно учтены.")