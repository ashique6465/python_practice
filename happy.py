def CheckHappy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        sum_of_square = 0 
        for digit in str(num):
            sum_of_square += int(digit) ** 2
        num = sum_of_square
    return num == 1


num = int(input("Enter a number: "))
print(CheckHappy(num))