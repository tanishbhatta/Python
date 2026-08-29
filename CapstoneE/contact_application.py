'''
Contact Book Application
'''
def create_contact():
    print("\nCreating contact.")
    try:
        phone = int(input("Phone number: "))
        name = str(input("Name: ")).strip()
        email = str(input("Email: ")).strip()
        address = str(input("Address: ")).strip()
    except Exception as err:
        print(f"{err}: invalid character input")

    user = {
        'Phone': phone,
        'Name': name,
        'Email': email,
        'Address': address
        }
    return user

def search_contact():
    list_contact()
    search_data = []
    try:
        search = str(input("\nSearch: ")).strip()
        
        if search.isdigit():
            for contacts in contact_database:
                if search in str(contacts['Phone']):
                    search_data.append(contacts)

            if search_data:
                print(f"{len(search_data)} results found:")
                for index, number in enumerate(search_data):
                    print(f"{index+1}. {number['Phone']}")
            else:
                print("No results found.")

            return search_data   
        else: 
            print("Invalid token: enter positive number")
    except Exception as err:
        print(f"Invalid: {err}")


def view_contact(data_function_return):
    function_return_data = data_function_return()
    flag = False
    try:
        view = str(input("\nView contact number: ")).strip()
        for output in contact_database:
            if view == str(output['Phone']):
                flag = True
                print(f"""\n\nContact Details - {output['Phone']}:\n
Phone number: {output['Phone']}
Name: {output['Name']}
Email: {output['Email']}
Address: {output['Address']}\n""")
        if not flag:
            print("Number not found in the contact list.")

    except Exception as err:
        print(f"Invalid: {err}")

def update_contact(data_function_return):
    data_function_return()
    flag = False

    try:
        mod_number = int(input("\nContact number you want to modify: "))
        for data in contact_database:
            if mod_number == data['Phone']:
                 flag = True
                 while True:
                    modification = int(input("""\nModify:
1. Name
2. Email
3. Address
4. Exit
-> """))
                
                    if modification == 1:
                        name = input("Enter new name: ").strip()
                        data['Name'] = name
                        print("Changed name sucessfully!\n")

                    if modification == 2:
                        email = input("Enter new email: ").strip()
                        data['Email'] = email
                        print("Changed email sucessfully\n")

                    if modification == 3:
                        address = input("Enter new address: ").strip()
                        data['Address'] = address
                        print("Changed address sucessfully!\n")

                    if modification == 4:
                        break
        if not flag:
            print("Number not found in the contact list.")

    except Exception as err:
        print(f"Invalid: {err}")
    

def delete_contact(data_function_return):
    data_function_return()
    flag = False

    try:
        del_number = int(input("\nDelete contact number: "))
        
        for data in contact_database:
            if del_number == data['Phone']:
                flag = True

                list.remove(data)
                print("Contact deleted sucessfully!\n")
        if not flag:
            print("\nNumber not found in the contact list.")

    except Exception as err:
        print(f"Invalid: {err}")

def list_contact():
    print()
    print("Contact List".center(18, '~'))
    for index, number in enumerate(contact_database):
        print(f"{index+1}. {number['Phone']} - {number['Name']}")
    return contact_database

print("Contact Book Application".center(37, '*'))

contact_database = [
]

while True:
    while True:
        raw_option = input("""\nPerform a contact operation:
1. Create a Contact
2. View Contacts
3. Modify Contact Info.
4. Remove Contact
5. Exit
-> """).strip()
        if raw_option.isdigit():
            if 1 <= int(raw_option) <= 5:
                option = int(raw_option)
                break
            else:
                print("Error: option out of range")
        else: 
            print("Invalid token: enter a positive integer")

    if option == 1:
        user_data = create_contact()
        contact_database.append(user_data)

    elif option == 2:
        while True:
            try:
                search_option = input("Do you want to search contacts? (y/n): ").strip()
                if search_option.lower() == 'y':
                    view_contact(search_contact)
                    break
                elif search_option.lower() == 'n':
                    view_contact(list_contact)
                    break
                else:
                    print("Invalid token: input yes (y) or no (n).")
            except Exception as err:
                print(f"{err}: Invalid input")

    elif option == 3:
        while True:
            try:
                search_option = input("Do you want to search contacts? (y/n): ").strip()
                if search_option.lower() == 'y':
                    update_contact(search_contact)
                    break
                elif search_option.lower() == 'n':
                    update_contact(list_contact)
                    break
                else:
                    print("Invalid token: input yes (y) or no (n).")
            except Exception as err:
                print(f"{err}: Invalid input")

    elif option == 4:
        while True:
            try:
                search_option = input("Do you want to search contacts? (y/n): ").strip()
                if search_option.lower() == 'y':
                    delete_contact(search_contact)
                    break
                elif search_option.lower() == 'n':
                    delete_contact(list_contact)
                    break
                else:
                    print("Invalid token: input yes (y) or no (n).")
            except Exception as err:
                print(f"{err}: Invalid input")
    else:
        break