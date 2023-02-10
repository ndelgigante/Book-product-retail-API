from DatabaseManager import DatabaseManager

def findemployees ():
    dm = DatabaseManager()
    df = dm.get_df("users")
   
    return df.loc[(df['userRole'] == 'employee') | (df['userRole'] == 'admin')].to_json(orient='values')

def employeesid (id):
    dm = DatabaseManager()
    df = dm.get_df("users")

    return df.loc[df['userid'] == id].to_json(orient='values')
