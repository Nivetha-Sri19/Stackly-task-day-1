try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")