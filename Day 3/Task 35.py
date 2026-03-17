num = [1, 2, 3, 4, 5]
x = int(input("Enter number: "))
found = False

for n in num:
    if n == x:
        found = True

if(found):
    print("Exists")
else:
    print("Not found")