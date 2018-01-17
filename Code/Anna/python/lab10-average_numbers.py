"""
Lab 10
Don't be average
"""

numbers = []
num = ''
adding = 0
int(adding)

print("We're going to average some numbers. Enter each number, then write 'done' when finished.")

while num != "done":
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num = float(num)
        numbers.append(num)
    except ValueError:
        print("Not a number!")

print(f"You have entered: {numbers}")

for i in range(len(numbers)):
    num = float(numbers[i])
    adding = adding + num

result = float(adding) / float(len(numbers))

print(f"\nYour average is: {result}")

