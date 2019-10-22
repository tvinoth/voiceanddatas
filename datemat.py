import numpy as np
import matplotlib.pyplot as plt

t = np.arange(1, 2, 3,4,5)
s = np.sin(2 * np.pi * t)

upper = 1
lower = 0

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)

fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()