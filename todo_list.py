"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    """
    variable to store list
    take user input
    add new item to end list

    """
    #choice = "Q"

    new_task = raw_input('What new task do you want to add?')

    my_list.append(new_task)
    return my_list

   


def view_list(my_list):
    """Print each item in the list."""
    for item in my_list:
        print item

    


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""



    # if choose A then go to add list
    # if choose B call function view_list
    # if choose C then quit out of programuser_options:
        
       
    user_options = """
        \nWould you like to:
        A. Add a new item
        B. View list
        C. Quit the program
        >>> """

    while True:
        print user_options
        choice = raw_input("what you want girl? ")
        if choice == 'a':
            add_to_list(my_list)
        elif choice == 'b':
            view_list(my_list)

        elif choice == 'c':
            break
        else:
            print "pick from the list"
                



    

#-------------------------------------------------

my_list = ["coffee", "cookies"]
# add_to_list(my_list)
display_main_menu(my_list)


