def is_armstrong_number(number):
    number_str = str(number)
    var = len(number_str)
    
    #inisialisasi
    sum_of_power = 0 
    for char in number_str:
        revert_to_int = int(char)
        power = revert_to_int**var
        sum_of_power+=power

    return bool(sum_of_power == number)
    