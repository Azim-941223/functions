import random


def gen_numb():
    nums_run = [1,4,5,7,9,0]
    number = '0444'
    for i in range(6):
        number += str(random.choice(nums_run))
    return number

    
print(gen_numb())