message = input("Enter string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in message:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonants:", count)