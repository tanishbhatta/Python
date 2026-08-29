users_list = []

def create_user(idno, name, role):
    for user in users_list:
        if user['Id'] == idno:
            print(f"Error: User with ID {idno} already exists!")
            return
    
    users_data = {
        'Id' : idno,
        'Name' : name,
        'Role' : role
    }
    users_list.append(users_data) 

def create_backup(data):
    backup_data = data.copy()
    return backup_data

def list_users(data):
    print("Currect Users:\n")
    for user_data in data:
        print(f"Id: {user_data['Id']} | Name: {user_data['Name']} | Role: {user_data['Role']}")

def restore_backup(back_data):
    users_list = back_data.copy()
    return users_list

create_user("8081", "Aarush Bhatta", "Admin")
create_user("8001", "Jebisha Thapa", "Admin")
backup_list = create_backup(users_list)
create_user("8401", "Christiano Ronaldo", "Employee")
restore_backup(backup_list)

list_users(users_list)
list_users(backup_list)