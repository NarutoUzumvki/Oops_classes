from random_list import generate_random

def sort(seq):
    for x in range(len(seq)):
        for y in range(x+1,len(seq)) :
            if seq[y]<seq[x] :
                seq[y],seq[x] = seq[x], seq[y]
        
    return seq

num = int(input("Enter the number of elements required in the list : \n"))

get_random = generate_random(num)
print(get_random)
print(sort(get_random))