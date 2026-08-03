def verify_card_number(card_no):
    clean = ''
    total = 0
    double = False

    for ch in card_no:
        if ch.isdigit():
            clean += ch

    for i in range(len(clean) - 1, -1, -1):
        digit = int(clean[i])
        if double:
            digit = digit * 2
            if digit > 9:
                digit -= 9
        total += digit
        double = not double

    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'


print(verify_card_number('1234 5678 9012 3456'))
print(verify_card_number('453914889'))