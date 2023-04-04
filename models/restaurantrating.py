from db import db

class RestaurantRatingModel(db.Model):
    __tablename__ = "restaurant_rating"


    id = db.Column(db.Integer,primary_key=True)
    rest_id = db.Column(db.Integer,db.ForeignKey("restaurant.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    rating = db.Column(db.Integer,nullable=False)
    user = db.relationship("UserModel",backref="restaurant_rating")
    restaurant = db.relationship("RestaurantModel",backref="restaurant_rating")