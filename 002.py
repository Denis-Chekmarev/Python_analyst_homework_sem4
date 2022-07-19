"""
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

"""

def do_set(some_list: list) -> list:
    result = []
    if some_list == []:
        return []
    for i in some_list:
        if i not in result:
            result.append(i)
    return result


origin_list = [1, 3, 1, 5, 3, 6, 5]
result_list = do_set(origin_list)
print(result_list)