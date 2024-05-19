import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
      return[]
    
    numbers_set = set()
    while len(numbers_set) < quantity:
       number = random.randint(min, max)
       numbers_set.add(number)

    numbers_list = sorted(numbers_set)
    return numbers_list

lottery_numbers = get_numbers_ticket(1, 89, 9)
print("Ваші лотерейні числа:", lottery_numbers)    
      
   