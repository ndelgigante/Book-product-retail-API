def login(username, password):
    #check if username is in the dataframe
    if username in df["username"].values:
        #get the index of the username
        index = df["username"].values.tolist().index(username)
        #check if password is in the dataframe
        if password in df["password"].values[index]:
            return True
        else:
            return False