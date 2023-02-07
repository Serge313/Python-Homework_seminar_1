"""Задача 1: Найдите сумму цифр трехзначного числа"""

import sys


def find_sum_of_digits(number):
    """The method separates digits and finds their sum"""
    if number == 0:
        return number
    else:
        return number % 10 + find_sum_of_digits(number // 10)


def testing_find_sum_of_digits(test_number=123):
    """The method tests find_sum_of_digits method"""
    print("Testing of the \"find_sum_of_digits\" method has been launched...")
    expected = 6
    actual = find_sum_of_digits(test_number)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_find_sum_of_digits()
print()


class InvalidNumber(Exception):
    pass


try:
    three_digit_number = int(input("Enter your three-digit number: "))
    if three_digit_number < 99 or three_digit_number > 1000:
        raise InvalidNumber("The number must be three digits!")
except InvalidNumber as ex:
    print(ex)
    sys.exit()
except Exception as ex:
    print(f"Error! {ex}")
    sys.exit()


print()
summary = find_sum_of_digits(three_digit_number)
print(f"{three_digit_number} -> {summary}")
