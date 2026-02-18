def count_digit(n):
    if n == 0 :
        return 1 
    n = abs(n)  
    count = 0 
    while n > 0:
        n //= 10 
        count += 1 
    return count 

def is_arm(num):
    if num < 0 :
        return False

    n = count_digit(num)
    temp = num
    total = 0 
    while temp > 0 :
        digit = temp % 10
        total += digit ** n 
        temp //= 10 

    return total == num

num = 123
print(is_arm(num))