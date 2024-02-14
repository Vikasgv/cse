import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import math
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i],arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
def quicksort(arr,low,high):
    if len(arr)==1:
        return arr
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
data=[36,56,12,20,4,98,30,71]
print("Before sorting:",data)
quicksort(data,0,len(data)-1)
print("After sorting:",data)
x=list(range(1,10000))
plt.plot(x,[math.log(y,2) for y in x])
plt.title("Binary search - Time complexity is O(logn)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()

