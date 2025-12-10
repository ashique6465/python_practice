def Solve(nums):
    Freq = {}
    for n in nums:
        if n not in Freq:
            Freq[n] = 1 
        else:
            Freq[n] += 1 
    res = [] 
    for e , v in Freq.items():
        if v > len(nums) // 3 :
            res.append(v)
    return res, len(nums) // 3

nums = [ 3, 2, 3]
print(Solve(nums))