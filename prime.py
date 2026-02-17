# num = int(input())

# if num < 1 :
#     print("false")

# for i in range(2, (int(num ** 0.5)+1)):
#     if num % i == 0:
#         print("False")
#         break
# else:
#     print(num)

for num in range(1,10):
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)