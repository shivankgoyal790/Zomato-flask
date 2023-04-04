from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    password = db.Column(db.String(80),nullable=False)
    mobile = db.Column(db.String(80),nullable=False)
    cart = db.relationship("UserMenuItemModel",backref="users",lazy="dynamic",cascade="all, delete")
    order = db.relationship("OrderModel",backref="users",lazy="dynamic")
