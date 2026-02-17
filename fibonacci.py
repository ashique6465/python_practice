def fib(num):
    ans = [0,1]
     
    for i in range(2,num):
        ans.append(ans[i-1] + ans[i-2])

    return ans
num = 5 
print(fib(num))