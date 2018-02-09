def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    if int(alist[0]) < int(alist[1]):
        del alist[0]
    else:
        del alist[1]
    return find_largest(alist)

alist = [5, 1, 8, 7, 2]
print(find_largest(alist))
