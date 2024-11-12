def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ""
    for i in range(len(val)):
      while num >= val[i]:
        roman_numeral += syb[i]
        num -= val[i]
    return roman_numeral

num = int(input("Enter a number: "))
print("Roman numeral:", int_to_roman(num))