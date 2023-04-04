from db import db

class RestaurantModel(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    password = db.Column(db.String(80),nullable=False)
    isopen = db.Column(db.Boolean,default=True)
    rating = db.Column(db.Float,default=0)
    ratedby = db.Column(db.Integer,default=0)
    menu = db.relationship("MenuModel",backref="restaurant",uselist=False ,cascade="all, delete")
    order = db.relationship("OrderModel",back_populates="restaurant",lazy="dynamic")
    

