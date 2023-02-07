"""Задача 3: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех."""

import sys


def lucky_or_not(number):
    """The method counts the sums of the first
    and last three digits of the ticket number
    and compares them"""
    first_half_of_number = 0
    second_half_of_number = 0
    for i in range(len(number) // 2):
        first_half_of_number += number[i]
    for i in range(len(number) // 2, len(number)):
        second_half_of_number += number[i]
    is_equal = first_half_of_number == second_half_of_number
    if is_equal:
        return "Yes"
    else:
        return "No"


def testing_lucky_or_not(test_number=(3, 8, 5, 9, 1, 6)):
    """The method tests lucky_or_not method"""
    print("Testing of the \"lucky_or_not\" method has been launched...")
    expected = "Yes"
    actual = lucky_or_not(test_number)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_lucky_or_not()
print()


class InvalidTicketNumber(Exception):
    pass


try:
    ticket_number = input("Enter the number of your ticket: ")
    if len(ticket_number) != 6:
        raise InvalidTicketNumber("Ticket number must be six digits!")
except InvalidTicketNumber as e:
    print(e)
    sys.exit()

try:
    int_ticket_number = list((int(i) for i in ticket_number))
except Exception as ex:
    print(f"Error! {ex}")
    sys.exit()

RESULT = lucky_or_not(int_ticket_number)
print()
print(f"{ticket_number} -> {RESULT}")
