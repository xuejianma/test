print(123)
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
plt.ioff()
ax = plt.plot([1,2,3],[4,5,6])
plt.savefig("test.png")
