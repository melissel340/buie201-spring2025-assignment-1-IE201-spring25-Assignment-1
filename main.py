def int_to_roman(num):
    if num > 3999:
        print("Please enter a number between 0 and 3999")
    else:
        dec_1_int = num // 1000
        num = num - dec_1_int*1000
        roman_1 = dec_1_int*"M"
        dec_2_int = (num // 100)
        num = num - dec_2_int*100
        roman_2 = ""
        if dec_2_int == 4:
            roman_2 = "CD"
        elif dec_2_int == 5:
            roman_2 = "D"
        elif dec_2_int == 9:
            roman_2 = "CM"
        elif dec_2_int < 4:
            roman_2 = dec_2_int*"C"
        else:
            roman_2 = "D" + (dec_2_int - 5)*"C"        
        dec_3_int = num // 10
        num = num - dec_3_int*10
        roman_3 = ""
        if dec_3_int == 4:
            roman_3 = "XL"
        elif dec_3_int == 5:
            roman_3 = "L"
        elif dec_3_int == 9:
            roman_3 = "XC"   
        elif dec_3_int < 4:
            roman_3 = dec_3_int*"X"
        else:
            roman_3 = "L" + (dec_3_int - 5)*"X"
        dec_4_int = num
        roman_4 = ""
        if dec_4_int == 4:
            roman_4 = "IV"
        elif dec_4_int == 5:
            roman_4 = "V"
        elif dec_4_int == 9:
            roman_4 = "IX"
        elif dec_4_int < 4:
            roman_4 = dec_4_int*"I"
        else:
            roman_4 = "V" + (dec_4_int - 5)*"I"
        return roman_1 + roman_2 + roman_3 + roman_4