arr=[45, 12, 78, 23, 9, 56, 34, 67, 1, 89]
print("Original Array:", arr)
print("1. Ascending order")
print("2. Descending order")
choice=int(input("Enter your choice:"))
if choice==1:
    arr.sort()
    print(arr)
elif choice==2:
    arr.sort(reverse=True)
    print(arr)
else:
    print("Invalid choice!")