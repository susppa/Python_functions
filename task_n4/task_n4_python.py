def factorials(n: int):
    """Генератор: по очереди возвращает факториалы чисел от 1 до n

    :param n: число, до которого считаем факториалы
    :return: генератор факториалов 1!, 2!, ..., n!
    """

    result = 1

    for i in range(1, n + 1):
        result *= i

        yield result


def main():
    n = int(input('Введите n: '))

    print(*factorials(n))


main()