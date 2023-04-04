from db import db

class DeliveryModel(db.Model):
    __tablename__ = "delivery"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(80),nullable=False)
    isengaged = db.Column(db.Boolean,default=False)
    order = db.relationship("OrderModel",backref="delivery",lazy="dynamic")
