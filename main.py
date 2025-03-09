def int_to_roman(num):
    if num > 3999:
        print("Please enter a number between 0 and 3999")     
    else:
        romans = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        return "".join(symbol * (num // value) + (num := num%value)*'' for value, symbol in romans)
    int_to_roman(1976)