file_path = 'example.txt'
with open(file_path, 'r') as file:
    array = list(map(int, file.readline().strip().split()))
if not array:
    print("Массив пуст.")
else:
    max_index = array.index(max(array))
    min_index = None
    for i in range(max_index + 1, len(array)):
        if min_index is None or array[i] < array[min_index]:
            min_index = i
    if min_index is not None:
        array[max_index], array[min_index] = array[min_index], array[max_index]
    else:
        print("Минимальный элемент не найден после максимального элемента.")
    print("Измененный массив:", array)
