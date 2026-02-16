def CountFreq(arr):
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 1 
        else:
            freq[num] += 1 

    return freq

arr = [ 1, 4, 6, 2, 4, 3, 2]
print(CountFreq(arr))