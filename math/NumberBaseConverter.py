def convert_base(number, from_base, to_base):
    number10, final_result=0,""
    
    for digit in str(number):
        number10 *= from_base
        number10+= int(digit)
        
    while number10:
        final_result += str(number10 % to_base)
        number10//=to_base
    return int(final_result[::-1])

print(convert_base(3456,6,10))