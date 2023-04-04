from db import db

class MenuitemModel(db.Model):
    __tablename__ = "menuitems"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer,nullable=False)
    menu_id = db.Column(db.Integer,db.ForeignKey("menu.id"))
    item_id = db.Column(db.Integer,db.ForeignKey("items.id"))
    item = db.relationship("ItemModel",back_populates="menuitems",uselist=False)
    menu = db.relationship("MenuModel",back_populates="menuitems")
    rating = db.Column(db.Float,default=0)
    ratedby = db.Column(db.Integer,default=0)

    
    