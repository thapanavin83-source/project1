import random
three_digit_code= (random.randint(0,9)), (random.randint(0,9)), (random.randint(0,9))
four_digit_code= (random.randint(1,6)),(random.randint(1,6)), (random.randint(1,6)), (random.randint(1,6))
three_str= ''.join(map(str, three_digit_code))
four_str=''.join(map(str, four_digit_code ))
print("3-digit code: "+three_str)
print("4-digit code: "+four_str)