import random
def get_numbers_ticket(min, max, quantity):
    if min <1 or max >1000 or min > max or quantity not in range (min, max) or quantity > (max - min):
        return "Incorrect parameters"
    
    random_number_list = []
    while (len(random_number_list) < quantity): 
        num = random.randint (min, max)
        if num not in random_number_list:
            random_number_list.append (num)
    random_number_list.sort ()
    return random_number_list

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Your lottery numbers:", lottery_numbers)



