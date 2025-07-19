def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a positive number.")
    else:
        print(f"Sum of digits of {num} is {sum_of_digits(num)}")
except ValueError:
    print("Invalid input! Please enter an integer.")
