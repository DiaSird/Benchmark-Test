# Time (mean ± σ):     170.8 ms ±  34.8 ms    [User: 4.8 ms, System: 5.4 ms]
# Range (min … max):   124.5 ms … 219.7 ms    20 runs

# Time (mean ± σ):     746.1 ms ± 434.3 ms    [User: 11.0 ms, System: 9.7 ms]
# Range (min … max):   462.4 ms … 1847.2 ms    10 runs

# Time (mean ± σ):      1.137 s ±  0.305 s    [User: 0.005 s, System: 0.011 s]
# Range (min … max):    0.878 s …  1.939 s    10 runs

import numpy as np
import matplotlib.pyplot as plt

# unit: msec
x_py = np.random.normal(170.8, 34.8, 1000)
x_rs = np.random.normal(746.1, 434.3, 1000)
x_f90 = np.random.normal(1137, 305, 1000)

plt.xlabel("time [msec]")
plt.ylabel("probability")
plt.title("Benchmark hyperfine")

plt.hist(x_py, bins=150)
plt.hist(x_rs, bins=150)
plt.hist(x_f90, bins=150)

filename = "dist/output.png"
plt.savefig(filename)
