"""
Lab 02: Mad Lib

"""
import random

print("Please provide some info:")

name = input("Name: ")
food = input("Weird food: ")
animal = input("Uncommon animal: ")
subject = input("Subject you hate: ")

sentence = f"I found someone named {name} and he threw some {food} at some pedestrians,\n" \
           f"the pedestrians did not like it one bit but my {animal} was able to rescue me because\n" \
           f"he is an expert in {subject}."

print(sentence)

# Another way to print input string

print("I found someone named {} and he threw some {} at some pedestrians,\n" \
      "the pedestrians did not like it one bit but my {} was able to rescue me because\n" \
      "he is an expert in {}.".format(name, food, animal, subject))

# Super Advanced and Advanced combined
answer = True

while answer != 'no':
    the_Three_Words = input("Provide three adjectives seperated by commas: ")
    a, b, c = the_Three_Words.split(",")
    myList = [a, b, c]
    print("I found someone named {} and he threw some {} at some pedestrians,\n" \
          "the pedestrians did not like it one bit but my {} was able to rescue me because\n" \
          "he is an expert in {}.".format(random.choice(myList), random.choice(myList), random.choice(myList),
                                          random.choice(myList)))
    answer = input("Would you like to redo the Mad Lib again?")
