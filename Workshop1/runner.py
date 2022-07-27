import sys
import os
input_file = sys.argv[1]
b = int(sys.argv[2])
e = int(sys.argv[3])
s = int(sys.argv[4])
n = sys.argv[5]
for i in range(0, 10):
    os.system(
        f"python3 run_random_experiment.py {input_file} {b} {e} {s} > {n}/output{i}.csv")
