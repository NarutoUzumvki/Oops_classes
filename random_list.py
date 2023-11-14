import random

def generate_random(digit):  
    random_list = [] 
       
    for __ in range(digit): 
        val = random.randint(10, 50) 
        random_list.append(val) 
           
    return random_list 
    
# print(generate_random(15))


