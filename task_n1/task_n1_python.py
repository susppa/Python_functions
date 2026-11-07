BRACKETS_PAIRS = {'(': ')', '{': '}', '[': ']'}


def get_closing_bracket_index(text: str, start: int = 0, expected: str = '') -> int:
    """Возвращает индекс последней закрывающей скобки, если все они сбалансированы, иначе -1
    :param text: проверяемая строка
    :param start: индекс, с которого начинается проверка
    :param expected: закрывающая скобка, которую ожидает этот вызов
    :return: индекс последней закрывающей скобки, если все они сбалансированы, иначе -1
    """
    i = start

    while i < len(text):
        char = text[i]

        if char in BRACKETS_PAIRS:
            i = get_closing_bracket_index(text, i + 1, BRACKETS_PAIRS[char])
            if i == -1:
                return -1

        elif char in BRACKETS_PAIRS.values():
            if char == expected:
                return i + 1
            return -1

        else:
            i += 1

    if expected:
        return -1

    return i


def is_brackets_valid(text: str) -> bool:
    """Проверяет, сбалансированы ли скобки в строке
    :param text: проверяемая строка
    :return: true если скобки сбалансированы, иначе false
    """
    return get_closing_bracket_index(text) != -1


input_string = input('Введите строку для проверки правильности расстановки скобок : ')

if is_brackets_valid(input_string):
    print('Скобки расставлены правильно!')
else:
    print('Скобки расcтавлены неправильно!')
