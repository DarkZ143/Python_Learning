n = int(input("Enter the number of elements => "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i} element => ")))
print("Unsorted array is => ", arr)
#Selection sort logic
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted array is => ", arr)
