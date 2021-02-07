# -*- coding: utf-8 -*-
"""SM-1_Monte-Carlo_Assignment-1_Solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mfcFku7ZFKDYb7wQPRItvuemN7fpb6OQ
"""

import math
import random
import matplotlib.pyplot as plt

darts=[100,1000,5000,10000]
hits=0
PI_value_list=[]
circle_area=[]
rectangle_area=60
x_missed=[]
y_missed=[]
x_hit=[]
y_hit=[]
for darts in darts:
  print("Darts:",darts)
  hits=0
  for i in range(darts):
    x=random.uniform(-3, 3)
    y=random.uniform(-5, 5)
    
    value=math.sqrt(x**2+y**2)
    if value<=3:
      x_hit.append(x)
      y_hit.append(y)
      hits=hits+1
    else:
      x_missed.append(x)
      y_missed.append(y)

  PI=(rectangle_area/9)*(hits/darts)
  PI_value_list.append(PI)
  area_circle=rectangle_area**(hits/darts)
  circle_area.append(area_circle)    
  print("PI:",PI)
  print("Area Of Circle:",area_circle)
  
  #Scatter Plot
  plt.figure(figsize=(10, 6))
  plt.scatter(x_missed,y_missed, color= "green",  marker= ".", s=80,label = "Missed Points")
  plt.scatter(x_hit,y_hit, color= "red",  marker= ".", s=80,label = "Hits Points")
  plt.title('Scatter Plot') 
  plt.legend(loc='upper right') 
  plt.show()
 
print("PI List:",PI_value_list)

plt.figure(figsize=(8, 6))

x=["100","1000","5000","10000"]

plt.ylim(0, 4)

plt.bar(x,PI_value_list, tick_label = x, width = 0.2, color = ['steelblue']) 

plt.xlabel('Number of trials') 

plt.ylabel('PI Values') 

plt.title('PI Values vs Number of trials') 

plt.show()

plt.figure(figsize=(8, 6))

x=["100","1000","5000","10000"]

plt.ylim(1, 10)

plt.bar(x,circle_area, tick_label = x, width = 0.2, color = ['steelblue']) 

plt.xlabel('Number of trials') 

plt.ylabel('Area of the circle') 

plt.title('Area of the circle vs Number of trials') 

plt.show()