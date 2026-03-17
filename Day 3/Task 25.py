message = input("Enter string: ")
reverse = message[::-1]

if message == reverse:
    print("Palindrome")
else:
    print("Not palindrome")
