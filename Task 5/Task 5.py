import csv
contact_fields = ['Serial No.', 'name', 'age', 'email', 'phone']
contact_database = 'Contact.csv'
def display_menu():
    print("--------------------------------------")
    print(" Welcome to Contact Book")
    print("---------------------------------------")
    print("1. Add a New Contact")
    print("2. View a Contact")
    print("3. Search a Contact")
    print("4. Update a Contact")
    print("5. Delete a Contact")
    print("6. Quit")
def add_contact():
    print("-------------------------")
    print("Add Contact Information")
    print("-------------------------")
    global contact_fields
    global contact_database
    contact_data = []
    for field in contact_fields:
        value = input("Enter " + field + ": ")
        contact_data.append(value)
    with open(contact_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([contact_data])
    print("Data saved successfully")
    input("Press any key to continue")
    return
def view_contact():
    global contact_fields
    global contact_database
    print("--- Contact Records ---")
    with open(contact_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in contact_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press any key to continue")
def search_contact():
    global contact_fields
    global contact_database
    print("--- Search Contact ---")
    sl = input("Enter serial no. to search: ")
    with open(contact_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if sl == row[0]:
                    print("----- Contact Found -----")
                    print("Serial: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Serial No. not found in our database")
    input("Press any key to continue")
def update_contact():
    global contact_fields
    global contact_database
    print("--- Update Contact ---")
    sl= input("Enter serial no. to update: ")
    index_contact= None
    updated_data = []
    with open(contact_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if sl == row[0]:
                    index_contact = counter
                    print("Contact Found: at index ",index_contact)
                    contact_data = []
                    for field in contact_fields:
                        value = input("Enter " + field + ": ")
                        contact_data.append(value)
                    updated_data.append(contact_data)
                else:
                    updated_data.append(row)
                counter += 1
    if index_contact is not None:
        with open(contact_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Serial No. not found in our database")
    input("Press any key to continue")
def delete_contact():
    global contact_fields
    global contact_database
    print("--- Delete Contact ---")
    sl = input("Enter serial no. to delete: ")
    contact_found = False
    updated_data = []
    with open(contact_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if sl != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    contact_found = True
    if contact_found is True:
        with open(contact_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Serial no. ", sl, "deleted successfully")
    else:
        print("Serial No. not found in our database")
    input("Press any key to continue")
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    else:
        break
print("-------------------------------")
print(" Thank you for using this contact book!")
print("-------------------------------")
