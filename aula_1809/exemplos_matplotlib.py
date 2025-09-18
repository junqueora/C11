import numpy
import pandas as pd
import matplotlib.pyplot as plt

x = numpy.array([1,2,3,4,5])
y = x * 2
y2 = 2 ** x

plt.xlabel('x') #adiciona legenda em x
plt.ylabel('y') #adiciona legenda em y

plt.subplot(1, 2, 1) #matriz de subplots (separar os gráficos)
plt.plot(x, y, '*-r', linewidth=2, markersize=5) #a string indica o formato do gráfico, o resto é literal

plt.subplot(1, 2, 2)
plt.plot(x, y2, 's-g', linewidth=2, markersize=5) #a string indica o formato do gráfico, o resto é literal

#plt.show()