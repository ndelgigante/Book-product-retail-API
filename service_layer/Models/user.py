

class User:
    def __init__(self, userid, full_name, email, password, userRole):
        self.userid = userid
        self.full_name = full_name
        self.email = email
        self.password = password
        self.userRole = userRole

    def to_list(self):
        return [self.userid, self.full_name, self.email, self.password, self.userRole ]