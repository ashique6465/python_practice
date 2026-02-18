def largest(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest
arr = [5,6,2,3,4]
print(largest(arr))