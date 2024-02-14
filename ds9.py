def binarysearch(a,low,high,key):
    if low<=high:
        mid=(high+low)//2
        if a[mid]==key:
            print("search successful key found at location:",mid+1)
            return
        elif key<a[mid]:
            binarysearch(a,low,mid-1,k)
        else:
            binarysearch(a,mid+1,high,k)
    else:
        print("search unsuccesful")
a=int(input("enter a elements"))
print("The array elements are:",a)
k=int(input("enter a key element to search:"))
binarysearch(a,0,len(a)-1,k)
             
             
             
