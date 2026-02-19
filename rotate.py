def rotate_arr(arr,k):
    res = arr[len(arr)-k - 1:] + arr[:len(arr) -k-1]
    return res



arr = [1,2,3,4,5]
k = int(input())
print(rotate_arr(arr,k))