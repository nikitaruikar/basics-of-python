#Dictionaries in python
mydic={'name':'nikita','City':'nagpur','age':21}
mydic

mydic['Area']='Teacher colony'
mydic
#Setrs
myset={1234,1234,22334,1233}
myset


myset.add(546)

myset.__sizeof__()

#Inroduction of numpy package
sales=[12232,23344,432,123]
profit=[343,345,123,127]
import numpy as np
sales_array=np.array(sales)
profit_array=np.array(profit)
ratio=profit_array/sales_array

ratio
list=["nikita",1234,24342]
import numpy as np
arr=np.array(list)
list


sales_us=[23425,567,897,5435]
sales_apac=[26725,6578,4345,213]
sales_jp=[345,678,9098,345]
sales_matrix=np.array([sales_us,sales_apac,sales_jp])

sales_matrix

sales_us=[23425,567,897,5435]
sales_apac=[26725,6578,4345,213]
sales_jp=[345,678,9098,345]
sales_matrix=np.array([sales_us,sales_apac,sales_jp])
profit_us=[4563,5646,546,678]
profit_apac=[345,675,789,45646]
profit_jp=[33442,766,897,980]
profit_matrix=np.array([profit_us,profit_apac,profit_jp])
profit_matrix/sales_matrix

profit_matrix[2,2]




quarter=['q1','q2','q3','q4']
region=['us','apac','jp']

qdict={'q1':0,'q2':1,'q3':2,'q4':3}
rdict={'us':0,'apac':1,'jp':2}
profit_matrix[rdict['us']][qdict['q1']]

profit_matrix[rdict['jp']][qdict['q4']]




