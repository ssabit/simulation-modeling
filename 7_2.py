# -*- coding: utf-8 -*-
"""7-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MJM3Vq8b8XcRY6ti6CoLBGFGILlQ6FQ0
"""

import matplotlib.pyplot as plt 
  
Moisturizer = [9200,6100,9550,8870,7760,7490] 

Month = [1,2,3,4,5,6]

plt.figure(figsize=(10, 6))
 
plt.scatter(Month,Moisturizer, label= "Moisturizer sales", color= "green",  marker= ".", s=80) 

plt.xlabel('Month no.') 

plt.ylabel('Sales unit') 

plt.title('Moisturizer sales data') 

plt.legend(loc='upper right') 

plt.show()