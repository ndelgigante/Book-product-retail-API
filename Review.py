import pandas as pd
from DatabaseManager import DatabaseManager as dm 
from Models.product_reviews import review


class Review():
    def __init__(self):
        self.reviewdf = dm.get_df("review")

#param
#review: the review object to be added
def add_review(self, review):
    dm.insert("product_reviews", review.to_list())
    self.bookdf = dm.get_df("product_reviews")

#param
#reviewid: the review id of the mysql database to be removed from that database       
def remove_Booksid(self, reviewid):
    dm.delete("product_reviews", f"review_id={reviewid}")
    self.bookdf = dm.get_df("product_reviews")

#param
#product id: the id of the product to be seaarched for
#returns: The dataframe of reviews only for that prod id
def search_review_by_prodid(self, prod_id):
    searched = self.reviewdf.loc[(self.reviewdf['product_id'] == prod_id)]
    return searched