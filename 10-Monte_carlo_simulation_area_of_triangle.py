# -*- coding: utf-8 -*-
"""SM-1_Monte-Carlo_Assignment-2_Solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1boLZKc75pe0G78AfyrU8MM-2Ms3F8_-K
"""

import math
import random
import matplotlib.pyplot as plt

darts=[100,1000,5000,10000]
hits=0
circle_area=[]
x_missed=[]
y_missed=[]
x_hit=[]
y_hit=[]
area_rectangle=12
for darts in darts:
  print("Darts:",darts)
  hits=0
  for i in range(darts):
    x=random.uniform(0, 2)
    y=random.uniform(0, 6)
    
    y1=2*x+2
    if y<=y1:
      x_hit.append(x)
      y_hit.append(y)
      hits=hits+1
    else:
      x_missed.append(x)
      y_missed.append(y)

  area_triangle=(hits/darts)*area_rectangle
   
  print("Area Of Triangle:",area_triangle)
  ######### Scatter Plot#########
  plt.figure(figsize=(10, 6))
  plt.scatter(x_missed,y_missed, color= "green",  marker= ".", s=80,label = "Missed Points")
  plt.scatter(x_hit,y_hit, color= "red",  marker= ".", s=80,label = "Hits Points")
  plt.title('Scatter Plot') 
  plt.legend(loc='upper right') 
  plt.show()