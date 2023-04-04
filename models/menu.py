from db import db

class MenuModel(db.Model):
    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True)
    rest_id = db.Column(db.Integer,db.ForeignKey("restaurant.id"))
    menuitems = db.relationship("MenuitemModel",back_populates="menu",lazy="dynamic")

    