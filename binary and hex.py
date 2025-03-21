decimal = int(input("請輸入一個十進位數字(範圍 0-255): "))
binary = ""
if decimal < 0 or decimal > 255:
    print("輸入無效，請輸入 0 到 255 之間的數字")
elif decimal == 0:
    binary = "00000000"
else:
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    while len(binary) < 8:
        binary = '0' + binary
    print("二進位數字為: ", binary)

    # 轉換為16進位數字
    hex = ""
    for i in range(0, 8, 4):
        binary_group = binary[i:i+4]
        decimal_value = 0
        power = 0
        for bit in reversed(binary_group):
            if bit == '1':
                decimal_value = (2 ** power) + decimal_value
            power = power + 1
        
        # 根據十進位數字轉換為16進位數字
        if decimal_value == 10:
            hex_digit = 'A'
        elif decimal_value == 11:
            hex_digit = 'B'
        elif decimal_value == 12:
            hex_digit = 'C'
        elif decimal_value == 13:
            hex_digit = 'D'
        elif decimal_value == 14:
            hex_digit = 'E'
        elif decimal_value == 15:
            hex_digit = 'F'
        else:
            hex_digit = str(decimal_value)

        hex = hex + hex_digit
    print("16進位數字為: ", hex)