def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    return (str[0].isupper()) + find_num_uppercase(str[1:])

print(find_num_uppercase('Good MorninG!'))
