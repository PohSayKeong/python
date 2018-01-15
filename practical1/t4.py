num = int(input("Please enter your integer:"))
if num < 0 or num > 1000:
    print("please enter an integer that is between 0 and 1000")
numbers = []
while num > 10:
    last_num = numbers.append(num % 10)
    num = num // 10
numbers.append(num)
print(numbers)
print(sum(numbers))
