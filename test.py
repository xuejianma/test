print(123)
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pylot 
plt.ioff()
ax = plt.figure()
plt.plot([1,2,3],[4,5,6])
plt.savefig("test.png")
plt.close(ax)
