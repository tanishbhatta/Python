array = [5,5,2,8]
add = 0
for index, i in enumerate(array):
    if index != 0:
        if i > array[index-1]:
            add += i
    else:
        add += i
print(add)