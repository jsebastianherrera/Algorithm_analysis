import sys
import random
x = int(sys.argv[1])

rand = [str(i) for i in random.sample(range(1, x*x+1), x*x)]
print(str(x) + "," + str(x))
for i in range(0, x*x+1, x):
    print(','.join(map(lambda x: x, rand[i:i+x])))
