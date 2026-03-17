num = [5, 2, 8, 1]

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if(num[i] > num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print(num)