def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

# Test the functions
print(greet("World"))
print(greet("Python"))

result = add_numbers(5, 10)
print(f"5 + 10 = {result}")

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")