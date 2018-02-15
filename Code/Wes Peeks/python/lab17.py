user1 = input("Put a word here.\n:")
check = user1[::-1]

if user1 == check:
    print("You are a drome.")
elif user1 != check:
    print('NOPE NOPE NOPE')