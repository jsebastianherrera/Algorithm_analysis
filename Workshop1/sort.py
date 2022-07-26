import random
array = [random.randint(0, 1000)for i in range(0, 10)]
for i in range(0, len(array)):
    for j in range(0, len(array)):
        if array[i] < array[j]:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
