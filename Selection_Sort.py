
def selectionSort(arr):
    size=len(arr)
    for i in range(size-1):
        j=i+1
        while j<size:
             if arr[i]>arr[j]:
                  temp=arr[i] 	
                  arr[i]=arr[j]
                  arr[j]=temp
             j+=1			
        print("\nPass : ",i+1," = ",arr)
                

n = int(input("Enter the size of the input: "))
arr = []
print("Enter the elements of the array:")
for i in range(n):
    element = int(input("Enter the {} element: ".format(i+1)))
    arr.append(element)

print("\nUnsorted array:")
for num in arr:
    print(num, end=" ")

selectionSort(arr)

print("\nSorted array:")
for num in arr:
    print(num, end=" ")
    
    
    
    
    