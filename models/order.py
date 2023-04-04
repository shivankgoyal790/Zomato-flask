from db import db

class OrderModel(db.Model):
    __tablename__ = "orders"


    id = db.Column(db.Integer,primary_key=True)
    rest_id = db.Column(db.Integer,db.ForeignKey("restaurant.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    agent_id = db.Column(db.Integer,db.ForeignKey("delivery.id"))
    totalbill = db.Column(db.Integer)
    isdelivered = db.Column(db.Boolean,default=False)
    cart = db.relationship("OrderMenuItemModel",backref="orders",lazy="dynamic")
    restaurant = db.relationship("RestaurantModel",back_populates="order")
    
