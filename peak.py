arr=[5, 10, 20, 15]
empty=[]
for i in range(1,len(arr)-1):
    if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
        empty.append(arr[i])
print(empty)    
