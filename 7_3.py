# -*- coding: utf-8 -*-
"""7-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lz_gGi1wQzDWwXoLST8x4gdWdK5P_tEo
"""

import matplotlib.pyplot as plt
from operator import add

Toothpaste = [2500, 2630, 2140, 3400, 3600, 2760]
Facewash = [1500, 1200, 1340, 1130, 1740, 1555]
Shampoo = [5200, 5100, 4550, 5870, 4560, 4890]
Moisturizer = [9200, 6100, 9550, 8870, 7760, 7490]
Soap = [1200, 2100, 3550, 1870, 1560, 1890]
Month = [1, 2, 3, 4, 5, 6]

sales_sum1 = list(map(add, Toothpaste, Facewash))
sales_sum2 = list(map(add, Shampoo, Moisturizer))
sales_sum3 = list(map(add, sales_sum1, sales_sum2))
sales_sum4 = list(map(add, sales_sum3, Soap))

plt.figure(figsize=(10, 8))

# print(sales_sum1)
# print(sales_sum2)
# print(sales_sum3)
# print(sales_sum4)

plt.bar(Month, sales_sum4, tick_label=Month, width=0.5, color=['blue', 'green'])

plt.xlabel('Month no.')

plt.ylabel('Total sales unit')

plt.title('Total number of sales each month')

plt.show()
