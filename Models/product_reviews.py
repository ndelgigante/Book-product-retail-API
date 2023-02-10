class ProductReview:
    def __init__(self, review_id, product_id, user_id, rating):
        self.review_id = review_id
        self.product_id = product_id
        self.user_id = user_id
        self.rating = rating

    def to_list(self):
        return[self.review_id,self.product_id, self.user_id, self.rating]