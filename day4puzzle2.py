def check_password(password):
    # print(password)
    has_double = False
    previous_digit = 0
    i = 0
    while i < len(password):
        digit = int(password[i])
        if digit < previous_digit:
            return False
        elif digit == previous_digit:
            if (i > 1 and int(password[i-2]) == digit) or (i < len(password) - 1 and int(password[i+1]) == digit):
                pass
            else:
                has_double = True

        previous_digit = digit
        i += 1
    return has_double


input = "168630-718098"

min, max = input.split("-")


# print(check_password("112233"))
# print(check_password("123444"))
# print(check_password("111122"))

total_possible = 0
for password in range(int(min), int(max)):
    if check_password(str(password)):
        total_possible += 1


print(total_possible)
