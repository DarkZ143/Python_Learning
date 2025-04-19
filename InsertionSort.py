n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i} element =>  ")))
print(f"Unsorted array => {arr}")   
#Insertion sort logic
for i in  range (1,n):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key
print(f"Sorted array => {arr}")    
