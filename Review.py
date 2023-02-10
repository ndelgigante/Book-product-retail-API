import pandas as pd
from DatabaseManager import DatabaseManager 
from Models.product_reviews import review
dm = DatabaseManager()

class Review():
    def __init__(self):
        self.reviewdf = dm.get_df("review")

#param
#review: the review object to be added
def add_review(self, review):
    dm.insert("product_reviews", review.to_list())
    self.reviewdf = dm.get_df("product_reviews")

#param
#reviewid: the review id of the mysql database to be removed from that database       
def remove_reviewid(self, reviewid):
    dm.delete("product_reviews", f"review_id={reviewid}")
    self.reviewdf = dm.get_df("product_reviews")

#param
#reviewid: is the id of the review that is being changed

def edit_review_(self, reviewid, new_rating):
    cmd = f"SET rating = {new_rating} WHERE review_id = {reviewid}"
    dm.update("product_reviews", cmd)
    self.reviewdf = dm.get_df("product_reviews")

#param
#product id: the id of the product to be searched for
#returns: The dataframe of reviews only for that prod id
def search_review_by_prodid(self, prod_id):
    searched = self.reviewdf.loc[(self.reviewdf['product_id'] == prod_id)]
    return searched

#param
#revew id: the id of the review to be searched for
#returns: The dataframe of the review being searched
def search_review_by_revid(self, rev_id):
    searched = self.reviewdf.loc[(self.reviewdf['review_id'] == rev_id)]
    return searched


#param
#user id: the id of the user to be searched for
#returns: The dataframe of the review being searched
def search_review_by_userid(self, user_id):
    searched = self.reviewdf.loc[(self.reviewdf['user_id'] == user_id)]
    return searched