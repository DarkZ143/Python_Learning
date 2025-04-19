red = "\033[31m"
green = "\033[32m"
n = int(input("Enter the number element : "));
arr = []
for i in range(n):
    arr.append(int(input(f"Enter the {i} element : ")))
print(f"{red}Before sorting : ", arr)
#Bubble sort logic
for i in range(n-1):
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(f"{green}After sorting : ", arr)
