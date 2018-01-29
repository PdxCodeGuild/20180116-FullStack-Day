first = input("please enter the first word:")
second = input("please enter the second word:")

first = first.lower()
first = list(first.replace(" ", ""))
first.sort()
first = ''.join(first)

second = second.lower()
second = list(second.replace(" ", ""))
second.sort()
second = ''.join(second)

print(first == second)