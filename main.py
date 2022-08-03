import numpy as np
from scipy.stats import beta #scipy собственно сам
import beta as bet
import matplotlib.pyplot as plot
import random as rnd
from my_random import MyRandom
import new_random as random


 # Определить группу альфа и бета-значений
alpha_beta_values = [[0.5,0.5], [5, 1], [1,3], [2,2], [2,5]]
linestyles = []


rand = MyRandom()
n = 10000
a = 0
b = 1
x = rand.rand_range(a, b, n)
x = np.sort(x)

#
#x= rnd.gammavariate(2.0,2.0)
#for i in range(1000):
 # x1 = rnd.betavariate(2.0,2.0)
#  x.append(x1)
#print (x)
for alpha_beta_value in alpha_beta_values:
  x = random.Generate(alpha_beta_value[0], alpha_beta_value[1],10000)
  x = np.sort(x)
  #print(x)
  dist_y = bet.Betapdf(alpha_beta_value[0], alpha_beta_value[1],x)


  plot.plot(x, dist_y, label=r'$\alpha=%.1f,\ \beta=%.1f$' % (alpha_beta_value[0], alpha_beta_value[1]))

 # Установите заголовок
plot.title ('Плотность бета распределения')
 # Установите диапазон х, оси Y
plot.xlim(0, 1)
plot.ylim(0, 2.5)
plot.legend()
plot.show()

alpha_beta_values = [[0.5,0.5], [5, 1], [1,3], [2,2], [2,5]]

for alpha_beta_value in alpha_beta_values:
  #x2 = np.linspace(0, 1)
  x = random.Generate(alpha_beta_value[0], alpha_beta_value[1],10000)
  x = np.sort(x)
  dist_y = bet.Betacdf(alpha_beta_value[0], alpha_beta_value[1],x,0,1)
  dist_y1 = beta.cdf(x, alpha_beta_value[0], alpha_beta_value[1],0,1)

  plot.plot(x,np.sort(dist_y), label=r'$\alpha=%.1f,\ \beta=%.1f$' % (alpha_beta_value[0], alpha_beta_value[1]))


 # Установите заголовок
plot.title (' бета распределение')
 # Установите диапазон х, оси Y
plot.xlim(0, 1)
plot.ylim(0, 1)
plot.grid()
plot.legend()
plot.show()


# Plot the PDF.
xmin, xmax = plot.xlim()

i =0

  #x = beta.rvs(alpha_beta_value[0], alpha_beta_value[1], size=1000)
  #x.sort()
  #print(x)
x = random.Generate(2.0,2.0, 10000)

x = np.sort(x)
dist_y = bet.Betapdf(2.0, 2.0, x)
#x = np.linspace(xmin, xmax, 10000)

#dist_y = beta.pdf(2.0, 2.0, x)
a1, b1, loc1, scale1 = beta.fit(x)

  # Plot the histogram.
plot.hist(x, bins=100, density=True, alpha=0.1, color="green")
print(x)

plot.plot(x, dist_y, 'k', linewidth=1)
title = "Fit results: alpha = %.2f,  beta = %.2f" % (2.0, 2.0)

plot.xlim(0, 1)
plot.ylim(0, 2.5)
plot.title(title)
plot.show()