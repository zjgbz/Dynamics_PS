import numpy as np
import matplotlib.pyplot as plt

n = input('Dimensionality:')

mat = np.zeros((n,n))

for i in range(n):
    mat[i,i] = 2
    if i > 0:
        mat[i, i-1] = -1
    if i < n-1:
        mat[i, i+1] = -1

w, v = np.linalg.eigh(mat)

sort_index = np.argsort(w)
t = np.arange(n)

fig = plt.figure(4, figsize = (10,8))
for i in range(4):
    index = sort_index[i]
    subplot = fig.add_subplot(2,2,i+1)
    subplot.plot(t, v[:, index], '-o')
    subplot.set_xlim(0, n-1)
    subplot.set_title(r'Frequency=%.3f$\omega_0$'%np.sqrt(w[index]))
plt.savefig('ps10_3.png', dpi=190)
