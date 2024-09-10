numberList = [2, 66, 95, 33, 23, 7, 9, 555, 47, 86]


# 选择排序
def selection_sort(numbers):
    _numbers = [i for i in numbers]  # before sorted
    max_number = _numbers[0]
    max_number_index = 0
    numbers_ = []  # after sorted
    length = len(_numbers)
    for i in range(length):
        for j in range(length-i):
            if _numbers[j] > max_number:
                max_number = _numbers[j]
                max_number_index = j
        numbers_.append(max_number)
        _numbers.pop(max_number_index)
        if _numbers:  # 判断_numbers是否为空列表
            max_number = _numbers[0]
        max_number_index = 0
    return numbers_


print(selection_sort(numberList))
