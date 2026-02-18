def removeDup(arr):
    seen = set()
    ans = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            ans.append(num)
    return ans


arr = [2,1,4,3,3,4]
print(removeDup(arr))