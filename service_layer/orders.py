import DatabaseManager
from Models import orders as Order
def create_order(order, user_id):
    dm = DatabaseManager()
    #pull the data from the json object       
    order = Order(orderNumber=order['orderNumber'],orderDate=order['orderDate'], userId=user_id)
        
    dm.insert("orders", order.to_list)
    
def get_orders():
    dm = DatabaseManager()
    df =dm.get_df("orders")
    return df
def get_order_by_id(id):
    dm = DatabaseManager()
    df =dm.get_df("orders")
    return df.loc[id]