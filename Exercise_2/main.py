"""Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"""

import sys


def each_person_birds(summary):
    """The method counts the number of crane birds made by each person"""
    boys = summary // 3
    first_boy = boys // 2
    girl = boys * 2
    second_boy = first_boy
    return first_boy, girl, second_boy


def testing_each_person_birds(test_summary_of_birds=60):
    """The method tests each_person_birds method"""
    print("Testing of the \"each_person_birds\" method has been launched...")
    expected = (10, 40, 10)
    actual = each_person_birds(test_summary_of_birds)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_each_person_birds()
print()


class InvalidTicketNumber(Exception):
    pass


try:
    number_of_crane_birds = int(input("Enter number of crane birds: "))
    if number_of_crane_birds % 2 != 0 or number_of_crane_birds % 3 != 0:
        raise InvalidTicketNumber("Invalid value entered!")
except InvalidTicketNumber as e:
    print(e)
    sys.exit()
except Exception as ex:
    print(f"Error! {ex}")
    sys.exit()

birds = each_person_birds(number_of_crane_birds)
print(f"{number_of_crane_birds} -> {birds}")
