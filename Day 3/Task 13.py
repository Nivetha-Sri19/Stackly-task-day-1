num = int(input("Enter a number:"))
i=0
while(num > 0):
    j = num%10
    i = i * 10 + j
    num = num // 10
print(i)