message = input("Enter string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in message:
    if ch in vowels:
        count += 1

print("Vowels:", count)