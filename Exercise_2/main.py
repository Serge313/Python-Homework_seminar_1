def each_person_birds(s):
    boys = s // 3
    a = boys // 2
    b = boys * 2
    c = a
    return a, b, c


def testing_each_person_birds(test_summary_of_birds=60):
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
number_of_crane_birds = int(input("Enter number of crane birds: "))
birds = each_person_birds(number_of_crane_birds)
is_even = number_of_crane_birds % 2 == 0 and number_of_crane_birds % 3 == 0
if is_even:
    print(f"{number_of_crane_birds} -> {birds}")
else:
    print("Invalid value entered!")
