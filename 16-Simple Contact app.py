# EG9-07 Tiny Contacts with constructor

from BTCInput import *
import pickle


# Create the contact class

class Contact:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone


def new_contact():
    """
    Reads in a new contact and stores it
    """
    print('Create new contact')
    # add the data attributes
    name = read_text('Enter the contact name: ')
    address = read_text('Enter the contact address: ')
    telephone = read_text('Enter the contact phone: ')
    # create a new instance
    newcontact = Contact(name=name, address=address, telephone=telephone)
    # add the new contact to the contact list
    contacts.append(newcontact)


def find_contact(search_name):
    """
    Finds the contact with the matching name
    Returns a contact instance or None if there is
    no contact with the given name
    """
    # remove any whitespace from around the search name
    search_name = search_name.strip()
    # convert the search name to lower case
    search_name = search_name.lower()
    for contact in contacts:
        # get the name out of the contact
        name = contact.name
        # remove any whitespace from around the name
        name = name.strip()
        # convert the name to lower case
        name = name.lower()
        # see if the names match
        if name.startswith(search_name):
            # return the contact that was found
            return contact
    # if we get here no contact was found
    # with the given name
    return None


def display_contact():
    """
    Reads in a name to search for and then displays
    the content information for that name or a
    message indicating that the name was not found
    """
    print('Find contact')
    search_name = read_text('Enter the contact name: ')
    contact = find_contact(search_name)
    if contact is not None:
        # Found a contact
        print('Name: ', contact.name)
        print('Address: ', contact.address)
        print('Telephone: ', contact.telephone)
    else:
        print('This name was not found.')


def edit_contact():
    """
    Reads in a name to search for and then allows
    the user to edit the details of that contact
    If there is no contact the function displays a
    message indicating that the name was not found
    """
    print('Edit contact')
    search_name = read_text('Enter the contact name:')
    contact = find_contact(search_name)
    if contact is not None:
        # Found a contact
        print('Name: ', contact.name)
        new_name = read_text('Enter new name or . to leave unchanged: ')
        if new_name != '.':
            contact.name = new_name
        new_address = read_text('Enter new address or . to leave unchanged: ')
        if new_address != '.':
            contact.address = new_address
        new_phone = read_text('Enter new telephone or . to leave unchanged: ')
        if new_phone != '.':
            contact.telephone = new_phone
    else:
        print('This name was not found.')


def save_contacts(file_name):
    """
    Saves the contacts to the given filename
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the save fails
    """
    print('save contacts')
    with open(file_name, 'wb') as out_file:
        pickle.dump(contacts, out_file)


def load_contacts(file_name):
    """
    Loads the contacts from the given filename
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the load fails
    """
    global contacts
    print('Load contacts')
    with open(file_name, 'rb') as input_file:
        contacts = pickle.load(input_file)


menu = '''Tiny Contacts

1. New Contact
2. Find Contact
3. Edit Contact
4. Exit program

Enter your command: '''

filename = 'contacts.pickle'
try:
    load_contacts(filename)
except FileNotFoundError:
    print('Contacts file not found')
    contacts = []

while True:
    command = read_int_ranged(prompt=menu, min_value=1, max_value=4)
    if command == 1:
        new_contact()
    elif command == 2:
        display_contact()
    elif command == 3:
        edit_contact()
    elif command == 4:
        save_contacts(filename)
        break
