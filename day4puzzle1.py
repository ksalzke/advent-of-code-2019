def check_password(password):
    has_double = False
    previous_digit = 0
    for digit in password:
        if int(digit) < previous_digit:
            return False
        elif int(digit) == previous_digit:
            has_double = True
        previous_digit = int(digit)
    return has_double


input = "168630-718098"

min, max = input.split("-")

total_possible = 0
for password in range(int(min), int(max)):
    if check_password(str(password)):
        total_possible += 1


print(total_possible)
