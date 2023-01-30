three_digit_number = int(input("Enter your three-digit number: "))


def find_digits(number):
    if number == 0:
        return number
    else:
        return number % 10 + find_digits(number // 10)


is_three_digit_number = 99 < three_digit_number < 1000

if is_three_digit_number:
    summary = find_digits(three_digit_number)
    print(summary)
else:
    print("Please enter a THREE-DIGIT number!")
