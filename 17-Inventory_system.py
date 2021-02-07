# -*- coding: utf-8 -*-
"""sm-1-assignment-8-Inventory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uIiv_4XxSLfVAtvsJUQMOp3Jy5IGFHTI
"""

import numpy as np
import matplotlib.pyplot as plt

m = int(input("Enter Maximum Inventory Size:")) 
n=int(input("Enter review Period:"))
#m = 11 #Maximum capacity
#n= 5 #review length

begining_inventory= 3
demand= 0
ending_inventory= 0
shortage_quantity= 0
order_quantity= 8  
days_until_order_arrives= 2
average_ending_inventory=0
total_shortage_days=0
total_ending_inventory= 0
cycle_number=10
total_days=n*cycle_number
x=0
y=0
days_list=[]
ending_inventory_list=[]

for cycle in range(cycle_number):
  #print("Cycle no: ",cycle)
  for day in range (1,n+1):
    print("-------------------")
    print("Cycle-Day no: ",cycle, "-",day)
    print("-------------------")

    ##order arrives code: begining_inventory= begining_inventory+ order_quantity
    days_until_order_arrives=days_until_order_arrives-1
    if (days_until_order_arrives==-1):
      begining_inventory= begining_inventory+order_quantity


    
    daily_demand= np.random.choice(a=[0,1,2,3,4],p=[0.10,0.25,0.35,0.21,0.09])
    total_demand = daily_demand + shortage_quantity
    if total_demand> begining_inventory:
      shortage_quantity= total_demand-begining_inventory
      ending_inventory=0
      total_shortage_days=total_shortage_days+1
      
      ending_inventory_list.append(ending_inventory)
      
    else:
      ending_inventory= begining_inventory-total_demand
      shortage_quantity= 0
      total_ending_inventory=total_ending_inventory+ending_inventory
      y=y+1
      ending_inventory_list.append(ending_inventory)
      

    
    print("Begining Inventory: ",begining_inventory)
    print("Daily Demand: ",daily_demand)
    print("Ending Inventory: ",ending_inventory)
    print("Shortage Quantity: ",shortage_quantity)
    #print("Total Shortage Days: ",total_shortage_days)
    #print("Total ending inventory: ",total_ending_inventory)

    begining_inventory=ending_inventory

    ##Review code (Task-1)
    #when day==n: , then you have to place an order. order_quantity; days_until_order_arrives (randomly)
    if (day==n):
      order_quantity=m-ending_inventory
      days_until_order_arrives=np.random.choice(a=[1,2,3],p=[0.6,0.3,0.1])
    x=x+1
    days_list.append(x)  

print("----------")
print("Total Days: ",total_days)
average_ending_inventory=total_ending_inventory/total_days
print("Avg Ending Inventory: ",average_ending_inventory)
print("Number of Days Shortage Occurs: ",total_shortage_days)

#print("days_list: ",days_list)
#print("ending_inventory_list: ",ending_inventory_list)


#graph plot
plt.figure(figsize=(10, 6))

plt.bar(days_list,ending_inventory_list,tick_label = days_list, color = ['steelblue']) 

plt.xlabel('Day Number') 

plt.ylabel('Ending_inventory of each day') 

plt.title('Inventory_level vs Day graph .') 

plt.show()