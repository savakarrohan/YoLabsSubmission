#python script to run MENACE
import numpy as np # basic thing to run mathematics
from tabulate import tabulate # makes the tabular look in the command line

row1 = np.array([0,0,0])
row2 = np.array([0,0,0])
row3 = np.array([0,0,0])

OutputTable = np.array([row1,row2,row3])

# tabulate data
table = tabulate(OutputTable, tablefmt = "grid")

# output
print(table)
a = 10*[0]
for i in range(10):
    a[i] = [row1,row2,row3]
    table = tabulate(a[i],tablefmt="grid")
    print(table)
# a[1] = [row1,row2,row3]
# print(a[1])
# table = tabulate(a[1],tablefmt="grid")
# print(table)
