import subprocess
import time
import numpy as np

# Function to find the closest power of 2

# Generate the argument values
n_values = [2 ** i for i in range(1, 11)]  # Powers of 2 from 2 to 1024
p_values = [2 ** i for i in [17, 20, 23, 27]]
f_values = np.logspace(-6, -1, num=16)

# Prepare to record execution times
execution_times = []

# Execute function.py with all combinations of arguments
for n in n_values:
    for p in p_values:
        for f in f_values:
            start_time = time.time()
            filename = f"output_n{n}_p{p}_f{f:.6f}.csv"
            cmd = f"python test_lessmixedsir.py -n {n} -p {p} -f {f} --filename {filename}"
            subprocess.run(cmd, shell=True)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append((cmd, execution_time))

# Write the execution times to a log file
with open('execution_times_log.txt', 'w') as file:
    for cmd, exec_time in execution_times:
        file.write(f"{cmd}: {exec_time} seconds\n")
