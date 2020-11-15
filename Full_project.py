from First_project import odd_even_project
from Second_project import average_project
from Third_project import multiplication_project
from Fourth_project import guess_project

class Projects:

    # The constructor :
    def __init__(self):
        print("Welcome into the full project , Choose your project from our collection !")
        print("Press[1] : Try Odd Even project\nPress[2] : Try Average project\n"
              "Press[3] : Try Multiplication project\nPress[4] : Try Guess numbers project")
        self.Choices()
    # The choices :
    def Choices(self):
        user_choice = input("Enter the number of the project that you wanna check :")
        while user_choice != "x":
            try:
                user_choice = int(user_choice)
                if user_choice == 1:
                    print("You choose Odd Even project , Let's check it")
                    self.Odd_Even_project()
                elif user_choice == 2:
                    print("You choose Average project , Let's check it")
                    self.average_project()
                elif user_choice == 3:
                    print("You choose Multiplication project , Let's check it")
                    self.multiplicationn_project()
                elif user_choice == 4:
                    print("You choose Guess numbers project")
                    self.guess_project()
                else:
                    print("Sorry we don't have your choice =) ")
            except ValueError:
                print("Sorry we can't find what you want !")
            user_choice = input("Enter the number of the project that you wanna check again , if you wanna exit type 'x' :")

    # Odd,Even project :
    def Odd_Even_project(self):
        odd_even_project()

    # Average project :
    def average_project(self):
        average_project()

    # Multiplication project :
    def multiplicationn_project(self):
        multiplication_project()

    # Guess numbers project :
    def guess_project(self):
        guess_project()

# Create the object :
project = Projects()
