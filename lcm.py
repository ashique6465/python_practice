def lcm(num1,num2):
    if num1  > num2:
        greater = num1
    else:
        greater = num2

    while(True):
        if ((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break

        greater += 1 
    return lcm

num1 = 54
num2 = 24
print(lcm(num1,num2))