from db import db

class OrderMenuItemModel(db.Model):
    __tablename__ = "ordermenuitem"
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey("orders.id"))
    menuitem_id = db.Column(db.Integer,db.ForeignKey("menuitems.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    menuitem = db.relationship("MenuitemModel",backref="ordermenuitem",uselist=False)