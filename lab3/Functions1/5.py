from itertools import permutations

def print_permutations():
    user_input = input()
    
    perms = permutations(user_input)
    
    for perm in perms:
        print(''.join(perm))

print_permutations()