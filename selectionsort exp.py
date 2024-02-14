import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
def Selectionsort(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
        print(a)
a=[]
size=int(input("enter the size of array:"))
while True:
    if len(a)<size:
        arr=int(input("enter the array elements:"))
        a.append(arr)
    else:
        break
print("before sorting:",a)
Selectionsort(a)
print("After sorting:",a)
x=list(range(1,10000))
plt.plot(x,[Y*Y for Y in x])
plt.title("Selection sort time complexitites is O(n\u00b2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
