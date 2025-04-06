# This script defines a function to check if a number is positive.
def is_positive(number):
    if number > 0:
        return True
    else:
        return False

# Testing
test_number = 10
output = is_positive(test_number)
print(f"Is the number positive? {output}")