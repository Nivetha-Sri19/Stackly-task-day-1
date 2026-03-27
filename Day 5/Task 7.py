file = open("team_data.txt", "w")

file.write("John, 25, Developer\n")
file.write("Sara, 22, Designer\n")

file.close()

print("File closed:", file.closed)

file = open("team_data.txt", "r")

content = file.read()
print("\nFile Content:\n", content)

file.close()
print("File closed after reading:", file.closed)