def get_number(text: str, error_text = 'Wrong input. Try again -> ') -> int:
    print(text, end='')
    while True:
        numb = input()
        if numb.isdigit():
            numb = float(numb)
            return numb
        else:
            print(error_text, end='')


def input_float_numb(text: str, error_text = 'Wrong input. Try again -> ') -> float:
    while True:
        number = input(text)
        try: 
            return float(number)
        except ValueError:
            print(error_text, end='')
