import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
%matplotlib qt

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

def root5_cal(x):
    return 1/2 * (x + 5/x)

labels = ['x0', 'x1', 'x2', 'x3', 'x4']

list_x0_1 = []
list_x0_2 = []

temp1 = 1
temp2 = 2

for i in range(5):
    list_x0_1.append(abs(round(5**(1/2) - temp1, 4)))
    temp1 = root5_cal(temp1)    

for j in range(5):
    list_x0_2.append(abs(round(5**(1/2) - temp2, 4)))
    temp2 = root5_cal(temp2)
    
x = np.arange(len(labels))  
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, list_x0_1, width, label='1) Setting : X0=1')
rects2 = ax.bar(x + width/2, list_x0_2, width, label='2) Setting : X0=2')

ax.set_ylabel('root5 - Xn')
ax.set_xlabel('Xn (n=0,1,2,3,4)')
ax.set_title('ROOT5 minus Xn (n=0,1,2,3,4)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()