with open('contact.csv', 'r') as file:
    lines = file.read().split('\n')


def save_changes(contact_list):
    content = open("contact.csv", "w")
    content.truncate()

    for x in range(len(contact_list)):
        if x == len(contact_list)-1:
            content.write(contact_list[x].name + "," + contact_list[x].favorate_fruit + "," + contact_list[x].favorate_color)

        else:
            content.write(contact_list[x].name + ","+contact_list[x].favorate_fruit + "," + contact_list[x].favorate_color + "\n")

    content.close()





class contact_person():
    def __init__(self, name, favorate_fruit, favorate_color):
        self.name = name
        self.favorate_fruit = favorate_fruit
        self.favorate_color = favorate_color

    def toString(self):
        return self.name + "'s favorate fruit is " + self.favorate_fruit + " and favorate color is " + self.favorate_color

    def set_name(self, name):
        self.name = name

    def set_favorate_fruit(self, favorate_fruit):
        self.favorate_fruit = favorate_fruit

    def set_favorate_color(self, favorate_color):
        self.favorate_fruit = favorate_color


contact_list = []

for information in lines:
    information = information.split(",")
    person = contact_person(information[0], information[1], information[2])
    contact_list.append(person)

print("Hello, welcome to the contact list. Please enter a number to select what you want to do")
print("1, to add a new person in to the list")
print("2, to delete a person from the list")
print("3, check all of the record on the contact list")
print("4, to show the options gain")
print("5, to change information of the person")
print("6, to leave the System")


while True:
   option =int (input("please enter your option:"))
   if option == 1:
       name = input("please enter the name:")
       fruit = input("please enter his/her favorate fruit:")
       color = input("please enter his/her favorate color:")
       contact_list.append(contact_person(name, fruit, color))
       print("success to add to list")


   elif option == 2:
       name = input("please enter the name:")
       for i in range(len(contact_list)-1):
           if contact_list[i].name == name:
              contact_list.remove(contact_list[i])
              print("already remove the person")
              continue
       print("Sorry, cannot get the name")

   elif option == 3:
       for person in contact_list:
           print(person.toString())

   elif option == 4:
       print("Hello, welcome to the contact list. Please enter a number to select what you want to do")
       print("1, to add a new person in to the list")
       print("2, to delete a person from the list")
       print("3, check all of the record on the contact list")
       print("4, to show the options gain")
       print("5, to change information of the person")
       print("6, to leave the System")

   elif option == 5:
       print("which information you would like to change\n 1,name\n2, fruit\n3,color")
       option1 = int( input("enter you option:"))
       name = input("plese input your name:")

       for i in range(len(contact_list)):
           if contact_list[i].name.__eq__(name):
               if option1 == 1:
                   name = input("please enter the new name:")
                   contact_list[i].set_name(name)
                   break
               elif option1 == 2:
                   fruit = input("please enter the new fruit:")
                   contact_list[i].set_favorate_fruit(fruit)
                   break
               elif option1 == 3:
                   color = input("please enter thr new color:")
                   contact_list[i].set_favorate_color(color)
                   break
               else:
                   print("cannot read your input")
                   break
           print("Sorry, cannot get the name")






   elif option == 6:
       print("thanks for using, do you wants to keep your change?")
       keep_change = input("please enter yes is you want:")
       if keep_change == "yes":
           save_changes(contact_list)

       break

   else: print("your enter is not not valid, please enter again")

