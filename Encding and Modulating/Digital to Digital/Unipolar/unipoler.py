import numpy as np
from matplotlib import pyplot as plt

data = [int(x) for x in input().split()]
time = np.arange(len(data))

plt.step(time, data,where='post')
plt.title('Unipolar')
plt.xlabel('Amplitude')
plt.ylabel('Time')

plt.text(0, 2, data)

plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time)
plt.show()

