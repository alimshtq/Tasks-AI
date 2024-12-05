def luhn_check(card_number):
    card_number = str(card_number).replace(" ", "")  # Remove spaces if any
    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Double every second digit
            n *= 2
            if n > 9:  # If the result is greater than 9, subtract 9
                n -= 9
        total += n

    return total % 10 == 0  # Valid if total modulo 10 is 0

# Example Usage
card_numbers = [
    "4532 1488 0343 6467",  # Valid
    "1234 5678 9012 3456",  # Invalid
    "4485 1756 2952 8705"   # Valid
]

for number in card_numbers:
    if luhn_check(number):
        print(f"{number} is valid.")
    else:
        print(f"{number} is invalid.")