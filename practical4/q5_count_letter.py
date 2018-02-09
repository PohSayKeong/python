def count_letter(str,ch):
    if len(str) == 0:
        return 0
    return (str[0] == ch) + count_letter(str[1:],ch)

print (count_letter("Welcome", 'e'))
