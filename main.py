def int_to_roman(num):
    dec_1_int = num // 1000
    num = num - dec_1_int*1000
    print(f"{num}, {dec_1_int}")
    dec_2_int = (num // 100)
    num = num - dec_2_int*100
    print(f"{num}, {dec_2_int}")
    dec_3_int = num // 10
    num = num - dec_3_int*10
    print(f"{num}, {dec_3_int}")
    dec_4_int = num
    print(f"{num}, {dec_4_int}")
int_to_roman(3333)
