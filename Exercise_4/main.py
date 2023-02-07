"""Задача 4: Требуется определить, можно ли от шоколадки размером
n × m долек отломить k долек, если разрешается сделать один разлом
по прямой между дольками (то есть разломить шоколадку на два прямоугольника)."""

import sys


def can_be_broken_off(n, m, k):
    """The method calculates whether it is possible to break off
    \"k\" slices"""
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        return "Yes"
    else:
        return "No"


def testing_can_be_broken_off(test_n=3, test_m=2, test_k=4):
    """The method tests can_be_broken_off method"""
    print("Testing of the \"can_be_broken_off\" method has been launched...")
    expected = "Yes"
    actual = can_be_broken_off(test_n, test_m, test_k)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_can_be_broken_off()
print()

try:
    n = int(input("Enter \"n\": "))
    m = int(input("Enter \"m\": "))
    k = int(input("Enter \"k\": "))
except Exception as ex:
    print(f"Error! {ex}")
    sys.exit()

RESULT = can_be_broken_off(n, m, k)
print(f"{n, m, k} -> {RESULT}")
