from db import db

class ItemRatingModel(db.Model):
    __tablename__ = "item_rating"


    id = db.Column(db.Integer,primary_key=True)
    menuitem_id = db.Column(db.Integer,db.ForeignKey("menuitems.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    rating = db.Column(db.Integer,nullable=False)
    user = db.relationship("UserModel",backref="item_rating")
    menuitem = db.relationship("MenuitemModel",backref="item_rating")