
#пробуем дальше №5ур1
x = [2, 4, 7, 9]
y = [3, 8, 5, 1]
s = sum([x[i]*y[i] for i in range(len(x))])
print(s)


#пробуем ещё №8ур2
arr = [5, 8, 9, 3, 2]
max_index = arr.index(max(arr))
sub_array = arr[max_index + 1:]
if sub_array:
    min_in_sub = min(sub_array)
    min_index_in_sub = sub_array.index(min_in_sub) + max_index + 1
    arr[max_index], arr[min_index_in_sub] = arr[min_index_in_sub], arr[max_index]

print(arr)

#№12ур3
arr = [5, -3, 8, -1, 0, 7, -6, 4, -9, 2, -8, 6]
arr = [x for x in arr if x >= 0]

print(arr)