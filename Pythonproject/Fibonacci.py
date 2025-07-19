def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

try:
    terms = int(input("Enter the number of terms: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = generate_fibonacci(terms)
        print("Fibonacci sequence:", result)
except ValueError:
    print("Invalid input! Please enter an integer.")
