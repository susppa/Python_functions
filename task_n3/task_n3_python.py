import re


def find_abbreviations(text: str) -> list:
    """Находит аббревиатуры в тексте

    :param text: текст в котором надо найти аббревиатуры
    :return: список найденных аббревиатур
    """
    pattern = r'\b[A-ZА-ЯЁ]{2,6}\b'
    result = re.findall(pattern, text)

    return result


def main():
    input_text = input('Введите строку для поиска аббревиатур: ')

    print(find_abbreviations(input_text))


main()
