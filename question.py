def sum_numeric_parts(s):
    total = 0
    current_number = ''

    for char in s:
        if char.isdigit():
            current_number += char  # build the number as a string
        else:
            if current_number:
                total += int(current_number)  # convert and add to total
                current_number = ''  # reset for the next number

    # Add any number left at the end
    if current_number:
        total += int(current_number)

    return total

# Example usage
input_str = "abc12def3"
print(sum_numeric_parts(input_str))  # Output: 15
