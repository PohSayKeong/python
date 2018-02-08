from random import randint

n = int(input("Please enter integer: "))

def print_matrix(n):
    for i in range (n):
        row = []
        for x in range(n):
            row.append(str(randint(0,1)))
        print(' '.join(row))

print_matrix(n)
        
    
