import matplotlib.pyplot as plt
import numpy as np
imgname = str(input("Enter file name: "))

plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
plt.savefig(imgname)
plt.show()
