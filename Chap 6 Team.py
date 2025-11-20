#Chapter 6 Team Project
def main():
    print('Please select an option.')
    choice = menu()
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        edit_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        display_contacts()
    elif choice == 6:
        print('Thank you for using Contact Manager!')
    else:
        print('ruh roh.')

def add_contact():
    print('works')

def search_contact():
    print('works2')

def edit_contact():
    print('works3')

def delete_contact():
    print('works4')

def display_contacts():
    print('works5')

def menu():
    print('1. Add Contact\n2. Search Contact\n3. Edit Contact\n4. Delete Contact\n5. Display All Contacts\n6. Exit')
    choice = int(input())
    return choice