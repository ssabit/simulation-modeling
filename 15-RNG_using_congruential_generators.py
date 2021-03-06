# -*- coding: utf-8 -*-
"""sm-1-lab-6-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bCXTGy_b3uWc5LgtSxY6WDkzr1_Fsd7_
"""

import math
import matplotlib.pyplot as plt

trials=[100,1000,5000]
for n in trials:
  #Generator-1
  z1=[12,7]
  u1=[]
  
  x=[]
  for i in range(2,n+2):
    new_z=(13*z1[i-1]+z1[i-2]+3)%16
    z1.append(new_z)
    new_u=new_z/16
    u1.append(new_u)

  l1 = len(u1)
  print("u1=",u1)
  print(l1)

  #Generator-2
  z2=[3,5]
  u2=[]

  for i in range(2,n+2):
    new_z=((12*z2[i-1])**2+13*z2[i-2]+3)%17
    z2.append(new_z)
    new_u=new_z/17
    u2.append(new_u)

  l2 = len(u2)
  print("u2=",u2)
  print(l2)

  #Generator-3
  z3=[2,7]
  u3=[]

  for i in range(2,n+2):
    new_z=((z3[i-1])**3+z3[i-2])%15
    z3.append(new_z)
    new_u=new_z/15
    u3.append(new_u)

  l3 = len(u3)
  print("u3=",u3)
  print(l3)

  #G1, G2 and G3 combined
  u=[]
  for i in range(0,n):
    new_u=u1[i]+u2[i]+u3[i]
    u.append(new_u)
    x.append(i)
  l = len(u)
  print("U=",u)
  print(l)

  #G1, G2 and G3 are combined split Fractional 
  final_u=[]
  for i in u:
    fractional, whole = math.modf(i)
    final_u.append(fractional)
    
  print("Final U=",final_u)
  plt.figure(figsize=(10, 6))

  plt.bar(x,final_u,tick_label = x, color = ['steelblue']) 

  plt.xlabel('index of a random number, i') 

  plt.ylabel('the random number Z i') 

  plt.title('Wichman / Hill Method') 

  plt.show()