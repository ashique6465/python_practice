def findSecond(arr):
    largest = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num  and num > second:
            second = num
    return second if second != float('-inf') else None


arr = [3,2,5,6,1]
print(findSecond(arr))