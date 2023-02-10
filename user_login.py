from DatabaseManager import DatabaseManager
def login(username, password):
    #check if username is in the dataframe
    dm = DatabaseManager()
    df = dm.get_df("users")
    
    if username in df["email"].values:
    
        #get the index of the username
        index = df["email"].values.tolist().index(username)
        #check if password is in the dataframe
        if password in df["password"].values[index]:
            return True
        else:
            return False
    else:
        return False