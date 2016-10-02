import numpy as np
import math
import matplotlib.pyplot as plt

#sample plots
#plt.plot(np.power(range(5),2),'ro--')
#plt.plot(np.power(range(5),3),'gx--')

xData = np.arange(-10,10,0.1)
sinData = np.sin(xData)
cosData = np.cos(xData)
test = 3*np.power(xData,2) + 2*xData + 4
#plt.plot(xData,sinData,'g',xData,cosData,'b')
plt.plot(xData,test)

plt.show()
