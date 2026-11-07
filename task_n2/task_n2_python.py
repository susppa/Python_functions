from functools import lru_cache

@lru_cache(maxsize=None)
def get_nth_fibonacci(num: int) -> int:
    """Получает номер n и возвращает n-ный член ряда Фибоначчи

    :param num: номер n
    :return: число, n-ный член ряда Фибоначчи
    """
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return get_nth_fibonacci(num - 1) + get_nth_fibonacci(num - 2)


def main():
    input_number = int(input('Введите порядковый номер: '))

    print(get_nth_fibonacci(input_number))


main()