"""
В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.

В файле содержится, например:
Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

"""


def is_word(word: str) -> bool:
    numbers = [str(i) for i in range(10)]
    for symbol in word:
        if symbol in numbers:
            return False
    return True


def get_words(text: str) -> str:
    list = text.split(' ')
    result = ''
    for word in list:
        if is_word(word):
            result += word + ' '
    return result


with open('file.txt', encoding='utf-8') as file:
    s = ''
    for line in file:
        s += line

print(get_words(s))
