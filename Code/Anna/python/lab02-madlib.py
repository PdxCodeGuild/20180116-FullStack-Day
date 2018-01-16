"""
Lab 2
Python Mad Libs = PyLibs!
"""
import random

print("Hello, and welcome to the PyLib!")
name = input("Please tell me your name: ")

print(f"Thanks, {name}, though I didn't really need that.")
run = input("Do you want to get started? Y/N: ")

go = True
story = ""

if run == "Y":

    # get variables for Mad Lib

    city1 = input("What city are you from? ")
    places = input("Name two places in a city (separated by commas): ")
    verbs = input("Give me three verbs ending in '-ing' (separated by commas): ")
    sport = input("Name a sport: ")
    type_of_person = input("Name a type of person: ")
    action = input("Ok, now give me an action: ")
    relatives = input("Name three relatives, separated by commas (i.e. mom, dad, etc.): ")
    city2 = input("Name another city: ")
    ints = input("Enter two numbers (separated by commas): ")
    verb = input("Give me an action verb: ")
    furniture = input("Name a piece of furniture: ")

    # split the inputs
    place_list = places.split(', ')
    verb_list = verbs.split(', ')
    relative_list = relatives.split(', ')
    int_list = ints.split(', ')

else:
    print("OK, maybe next time!")
    go = False

# run the mad lib
if go == True:
    story = input("\nOK, your PyLib is ready! Do you want to hear it? Y/N: ")

while story == "Y":
    print(f"""
    \n\tIn West {city1}, born and raised
    On the {place_list[0]} is where I spent most of my days
    {verb_list[0]}, {verb_list[1]}, {verb_list[2]} all cool
    And all shootin' some {sport} outside of the {place_list[1]}
    When a couple of {type_of_person}s who were up to no good
    Started makin' trouble in my neighborhood
    I got in one little {action} and my {relative_list[0]} got scared
    And said "You're movin' with your {relative_list[1]} and {relative_list[2]} in {city2}"

    I pulled up to the house about {int_list[0]} or {int_list[1]}
    And I yelled to the cabbie "Yo holmes, {verb} ya later"
    Looked at my kingdom, I was finally there
    To sit on my {furniture} as the Prince of {city2}
    """)
    story = input("Do you want to hear your story again? Y/N: ")

print(f"\nThanks for playing PyLibs, {name}!")

if go == True:
    run = input("Do you want to try again with new answers? Y/N: ")


