def int_to_roman(num):
    dec_1_int = num // 1000
    num = num - dec_1_int*1000
    print(f"{num}, {dec_1_int}")
    roman_1 = dec_1_int*"M"
    dec_2_int = (num // 100)
    num = num - dec_2_int*100
    print(f"{num}, {dec_2_int}")
    roman_2 = ""
    if dec_2_int == 4:
        roman_2 = "CD"
    elif dec_2_int == 5:
        roman_2 = "D"
    elif dec_2_int == 9:
        roman_2 == "CM"
    elif dec_2_int < 4:
        roman_2 = dec_2_int*"C"
    else:
        roman_2 = "D" + dec_2_int*"C"        
    dec_3_int = num // 10
    num = num - dec_3_int*10
    print(f"{num}, {dec_3_int}")
    dec_4_int = num
    print(f"{num}, {dec_4_int}")
    print(roman_1 + roman_2)
int_to_roman(3333)
