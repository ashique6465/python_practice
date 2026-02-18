def reverse(s):
    ans = ""
    for i in range(len(s)-1,-1,-1):
        ans += s[i]
    return ans


s = input()
print(reverse(s))
