def square(n):
    for i in range(n):
        yield i * i
squares_list = [i*i for i in range(5)]
print(squares_list)
print(type(squares_list))

squares_gen = square(5)
print(squares_gen)
print(type(squares_gen))

for num in squares_gen:
    print(num)