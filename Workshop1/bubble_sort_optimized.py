import random
array = [random.randint(0, 1000)for i in range(0, 10)]
for i in range(1, len(array)):
    for j in range(0, len(array)-i):
        if array[j+1] < array[j]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)
