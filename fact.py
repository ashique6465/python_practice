def Fact(num):
    if num == 0 or num == 1 :
        return 1 

    return num * Fact(num-1)
num = int(input())
print(Fact(num))