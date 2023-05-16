#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer and sums.
    Args:
        roman_string (str): string of Roman numerals
    Returns:
        int: number will be between 1 to 3999
    """
    if type(roman_string) is not str or roman_string is None:
        return (0)

    rome_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string:
        if char not in rome_nums:
            return 0

        current_value = rome_nums[char]

        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value

        prev_value = current_value

    return result
