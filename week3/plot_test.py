import numpy as np
import math
import matplotlib.pyplot as plt

#sample plots
#plt.plot(np.power(range(5),2),'ro--')
#plt.plot(np.power(range(5),3),'gx--')

xData = np.arange(-10,10,0.1)
sinData = np.sin(xData)
cosData = np.cos(xData)


#plt.plot(xData,sinData,'g',xData,cosData,'b')
for i in range(4):
    print 'hello'
    test = i*np.power(xData,2) + 2*xData + 4
    plt.plot(xData,test,'ro')
    plt.show()
