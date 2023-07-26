import matplotlib.pyplot as p
import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([9,2,3,4,5,0])
p.title("LINE CHART")
p.plot(a,b,'black',linestyle='-',marker='o',linewidth = '6',markerfacecolor='red',markersize=17,markeredgecolor='black')
p.xlabel("SPEED")
for i in range(len(a)):
    p.text(a[i], b[i], f'({a[i]}, {b[i]})',va='bottom',ha='right')
p.ylabel("TIME")
p.show()
