'''
Data Analysis
-------------
-->This is process of inspeccting, cleaning, transforming, and modeling data to discover
useful insights...

Types of DA
-----------
1.Descriptive Analysis
----------------------
-->Summarizing Data

2.Diagnostic Analysis
---------------------
-->Understanding Causes

3.Predictive Analysis
---------------------
-->Forecasting future outcomes

4.Prescriptive Analysis
-----------------------
-->Suggesting actions based on data

Why DA
------
--> TO improve Decision making
--> Detects Trends & Patterns

Numpy(Numerical Python)
-----------------------
--> This python library for numerical computing. It provides support for multi-dimensional
arrays, and linear algebra operations, making it essential for data analysis...

using numpy in DA
-----------------
--> Improved Performance
--> Simplifies complex operations
--> Easy data manipulation...


import numpy as np
arr_1 = np.array([[4, 5, 6, 7],[1, 2, 3, 4],[5, 6, 7, 9]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshape(4, 3)
print(reshaped)


import numpy as np
arr_1 = np.array([10, 20, 30, 40, 50])
print(arr_1[2])
print(arr_1 + 5)


import numpy as np
arr_1 = np.array([[20, 30], [50, 60]])
arr_2 = np.array([[5, 6], [7, 8]])

print(np.dot(arr_1, arr_2))

import numpy as np

arr_1 = np.array([10, 20, 30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)

copy_deep = arr_1.copy()
arr_1[1] = 200
print(copy_deep)
print(arr_1)

'''
'''
Pandas
------
-->The pandas is a powerful data manipulation and analysis library..
-->Where it provides data structure like series and dataframe for efficient data handling...

methods Series
--------------
mean()
sum()
max()
min()
apply()
map()


import pandas as pd
any = pd.Series([2999, 15999, 52999, 4999, 1999],
                index = ['Earbuds', 'Smartphone', 'Lap', 'Watch', 'Footware'])

print(any)

Dataframe
---------
'''
import pandas as pd
data = {
    'Product':['Earbuds','Smartphone','Lap','Watch','Footware'],
    'Brand':["realme", 'Samsung', 'HP', 'TIMEWEL', 'Puma'],
    'Price':[1599, 30000, 50000, 3000, 1799],
    'stock':[50, 15, 25, 40, 70]
    }
dip = pd.DataFrame(data)
print(dip)

