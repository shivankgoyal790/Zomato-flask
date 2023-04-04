from db import db


class UserMenuItemModel(db.Model):
    __tablename__ = "usermenuitem"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    menuitem_id = db.Column(db.Integer,db.ForeignKey("menuitems.id"))
    