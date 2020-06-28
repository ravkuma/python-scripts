"""

This is a simple Bubble Sort Program

To run: python bubble_sort.py

Input: Script will take a list of elements as an argument.

"""

def bs(a):
    b=len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a


## Main

print("This is a Bubble Sort")

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
print("Enter %d numbers one by one" %n)

for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the elemenat

print("List to sort ",lst) 

print("Sorted List:", bs(lst))

