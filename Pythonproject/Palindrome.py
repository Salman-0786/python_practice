def is_palindrome_number(num):
    original = str(num)
    reversed_num = original[::-1]
    return original == reversed_num

num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
