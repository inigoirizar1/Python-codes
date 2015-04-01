import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
f = plt.figure()
plots = gridspec.GridSpec(2,1 ,height_ratios=[3,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
plt.show()
