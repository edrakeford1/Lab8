"""
Program Name: UPC Validator

Name: Elijah Drakeford

Purpose: This program checks if the 12-digit UPC that was input is valid.

Date: Mar 6, 2026
"""

def find_UPC(first_11_digits):
    odd_sum = 0
    even_sum = 0

    for i in range(1,12):
        digit = int(first_11_digits[i])

        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    total = (odd_sum * 3) + even_sum
    modulo = total % 10
    if modulo == 0:
        check_digit = 0
    else:
        check_digit = 10 - modulo
    
    return check_digit