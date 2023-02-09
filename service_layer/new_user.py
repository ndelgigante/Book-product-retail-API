import DatabaseManager
from Models import user as User
def new_user(user):
    #user is a json object with the following keys:
    #email, password, fullname,
    #search for the user's email in the dataframe
    dm = DatabaseManager()
    df = dm.get_df("users")
    if user['email'] in df["email"].values:
        return "account already exists. Please login first at /login"
    else:
        #call the add user to database funtion
        dm.insert("users", user)
        return "account created successfully"