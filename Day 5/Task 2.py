def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

result = calculate_total(10, 20, 30, 40)
print("Total:", result[0])
print("Average:", result[1])