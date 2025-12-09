#Chapter 6 Team Project
import io
import os
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
    outfile = open('contact.txt', 'a')
    
    c = int(input('How many contacts would you like to make: '))
    
    for num in range(1, c + 1):
        print(f'Enter information for contact #{num}: ')
        n = input('Enter your Name: ')
        sa = input('Enter your Street Adress: ')
        pn = input('Enter your phone number: ')
        ea = input('Enter your email adress: ')
        outfile.write(str(n + '\n'))
        outfile.write(str(sa + '\n'))
        outfile.write(str(pn + '\n'))
        outfile.write(str(ea + '\n'))
    
    print('All files were saved to contact.txt')
    
    outfile.close()
                      
    
    

def search_contact():
    found = False
    
    search = input('Enter a contact to search for: ')
    
    try:
        open_file = open('contact.txt', 'r')
        
        n = open_file.readline()
        
        while n != '' and found == False:
            sa = open_file.readline()
            pa = open_file.readline()
            ea = open_file.readline()
                
            n = n.rstrip('\n')
            sa = sa.rstrip('\n')
            pa = pa.rstrip('\n')
            ea = ea.rstrip('\n')
            if n.lower() == search.lower():
                print('\nFile found!')
                print('Name:', n)
                print('Street Adress:', sa)
                print('Phone Number:', pa)
                print('Email Adress:', ea)
                break
    except Exception as e:
        print('Error: contact not found.')
        
        
        if not found:
            print('\n----- The record was not found -----\n')
                        

        
    
    

def edit_contact():
    print('works3')

def delete_contact():
    found = False
    search = input('Enter the contact you would like to delete: ')
    try:
        contact_file = open('contact.txt', 'r')
        temp_file = open('temp.txt', 'w')
        
        name = contact_file.readline()
        
        while name != '':
            street = contact_file.readline()
            phone = contact_file.readline()
            email = contact_file.readline()
            
            name = name.rstrip('\n')
            street = street.rstrip('\n')
            phone = phone.rstrip('\n')
            email = email.rstrip('\n')
            
            if name.lower() != search.lower():
                temp_file.write(name + '\n')
                temp_file.write(street + '\n')
                temp_file.write(phone + '\n')
                temp_file.write(email + '\n')
            name = contact_file.readline()
    except Exception as e:
        print('Error: Error reading file')
                
    contact_file.close()
    temp_file.close()
            
    os.remove('contact.txt')
            
    os.rename('temp.txt', 'contact.txt')
            
    
    if found == True:
        print('\contact not found.')
    else:
        print('The information has been changed.')
                
                
                
            
        


def display_contacts():
    found = False
    try:
        open_file = open('contact.txt', 'r')
        line = open_file.readline().rstrip()
        print(line)
        
        while line != '':
            for num in range(4):
                print(line)
                line = open_file.readline().rstrip()
                print()
            
    except Exception as e:
        print(e)
        
       
        
        
        
        
            
        
    
    
    

            
       
        
    
    
    
    
    

def menu():
    print('1. Add Contact\n2. Search Contact\n3. Edit Contact\n4. Delete Contact\n5. Display All Contacts\n6. Exit')
    choice = int(input('>: '))
    return choice

main()
 