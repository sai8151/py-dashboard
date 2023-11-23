# user_manager.py

user_data = {
    "ram": "1234",
    "sita": "1432",
    "oppo": "poco",
    "john": "Joh1234",
    "lisa": "Lis5678",
    "emma": "Emm8765",
    "mike": "Mik4321",
    "sophie": "Sop5678",
    "david": "Dav9876",
    "olivia": "Oli8765",
    "james": "Jam3456",
    "chloe": "Chl2345",
    "daniel": "Dan6789",
    "mia": "Mia9876",
    "ryan": "Rya5432",
    "amelia": "Ame6543",
    "jack": "Jac8901",
    "charlotte": "Cha7890",
    "ben": "Ben0123",
    "isabella": "Isa4567",
    "harry": "Har2345"
}


def login(username, password):
    if username in user_data and user_data[username] == password:
        print("Entered user id and pswd is in db.\nLogin succes.")
        return True
    print("Login fail.")
    return False


def register(username, password):
    if username not in user_data:
        user_data[username] = password
        return True
    return False


def delete_account(username):
    if username in user_data:
        del user_data[username]
        return True
    return False


def update_user(username, new_password):
    if username in user_data:
        user_data[username] = new_password
        return True
    return False


def get_user_data():
    return user_data
