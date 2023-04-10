from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, MenuitemSchema, RatingSchema, OrderSchema
from models import (
    UserModel,
    MenuitemModel,
    UserMenuItemModel,
    ItemRatingModel,
    RestaurantRatingModel,
    RestaurantModel,
    OrderModel,
    OrderMenuItemModel,
)
from db import db
from flask_jwt_extended import jwt_required, get_jwt
import random

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/user/<string:user_id>")
class UserRoutes(MethodView):

    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user


@blp.route("/user/<string:user_id>/order")
class Userorder(MethodView):

    @jwt_required()
    def post(self, user_id):

        claim = get_jwt()
        if claim["role"] != "user" or claim["sub"] != int(user_id):
            abort(401, "unauthorised")

        x = random.randint(1, 4)
        user = UserModel.query.get_or_404(user_id)
        cart = user.cart
        totalbill = 0

        for i in cart:
            totalbill += MenuitemModel.query.get_or_404(i.menuitem_id).price

        if totalbill == 0:
            return "cart is empty please add something", 404

        order = OrderModel(rest_id=1, agent_id=x, user_id=user_id, totalbill=totalbill)
        db.session.add(order)
        db.session.commit()

        for i in user.cart:
            newentry = OrderMenuItemModel(
                user_id=user_id,
                menuitem_id=i.menuitem_id,
                order_id=order.id,
            )
            db.session.add(newentry)
            db.session.commit()

        UserMenuItemModel.query.filter(UserMenuItemModel.user_id == user_id).delete()

        db.session.add(order)
        db.session.add(user)
        db.session.commit()

        return "order placed",201

    @jwt_required()
    @blp.response(200, OrderSchema(many=True))
    
    def get(self, user_id):
        claim = get_jwt()
        if claim["role"] != "user" or claim["sub"] != int(user_id):
            abort(401, "unauthorised")
        user = UserModel.query.get_or_404(user_id)
        return user.order.all()


@blp.route("/user/<string:user_id>/cart")
class UserCart(MethodView):
    @jwt_required()
    @blp.response(200, MenuitemSchema(many=True))
    def get(self, user_id):

        claim = get_jwt()
        if claim["role"] == "user" and claim["sub"] == int(user_id):

            user = UserModel.query.get_or_404(user_id)
            cart = user.cart
            mylist = []
            for i in cart:
                mylist.append(MenuitemModel.query.get_or_404(i.menuitem_id))

            return mylist
        else:
            abort(401, "user privledge required")


@blp.route("/user/<string:user_id>/item/<item_id>")
class Usercartitems(MethodView):
    @jwt_required()
    def post(self, user_id, item_id):
        claim = get_jwt()
        if claim["role"] != "user" or claim["sub"] != int(user_id):
            abort(401, "unauthorised")
        try:
            newcartitem = UserMenuItemModel(menuitem_id=item_id, user_id=user_id)
            db.session.add(newcartitem)
            db.session.commit()
        except:
            return "could not add item", 400

        return "item added succesfully", 201

    @jwt_required()
    def delete(self, user_id, item_id):
        claim = get_jwt()
        if claim["role"] != "user" and claim["sub"] != int(user_id):
            abort(401, "unauthorised")
        UserMenuItemModel.query.filter(
            UserMenuItemModel.menuitem_id == item_id
            and UserMenuItemModel.user_id == user_id
        ).delete()
        db.session.commit()
        return {"message": "menuItem removed from cart"}, 201


@blp.route("/user/<string:user_id>/item/<string:item_id>/rate")  # rate item
class RateItem(MethodView):
    @jwt_required()
    @blp.arguments(RatingSchema)
    def post(self, rate_body, user_id, item_id):
        claim = get_jwt()
        if claim["role"] != "user" or claim["sub"] != int(user_id):
            abort(401, "unauthorised")
        prev_rating = ItemRatingModel.query.get(user_id)
        menuitem = MenuitemModel.query.get_or_404(item_id)
        if prev_rating:

            rating = menuitem.rating
            ratedby = menuitem.ratedby
            newrating = (
                rating * ratedby + rate_body["rating"] - prev_rating.rating
            ) / (ratedby)
            menuitem.rating = newrating
            prev_rating.rating = rate_body["rating"]
            db.session.commit()
        else:
            newrating1 = ItemRatingModel(
                user_id=user_id, menuitem_id=item_id, rating=rate_body["rating"]
            )
            rating = menuitem.rating
            ratedby = menuitem.ratedby
            newrating = (rating * ratedby + rate_body["rating"]) / (ratedby + 1)
            menuitem.ratedby = menuitem.ratedby + 1
            menuitem.rating = newrating
            db.session.add(newrating1)
            db.session.commit()

        return "rating updated", 201


@blp.route("/user/<string:user_id>/restaurant/<string:rest_id>/rate")  # rate rest
class RateRestaurant(MethodView):
    @jwt_required()
    @blp.arguments(RatingSchema)
    def post(self, rate_body, user_id, rest_id):

        claim = get_jwt()
        if claim["role"] != "user" or claim["sub"] != int(user_id):
            abort(401, "unauthorised")

        prev_rating = RestaurantRatingModel.query.get(user_id)
        rest = RestaurantModel.query.get_or_404(rest_id)
        if prev_rating:

            rating = rest.rating
            ratedby = rest.ratedby
            newrating = (
                rating * ratedby + rate_body["rating"] - prev_rating.rating
            ) / (ratedby)
            rest.rating = newrating
            prev_rating.rating = rate_body["rating"]
            db.session.commit()
        else:
            newrating1 = RestaurantRatingModel(
                user_id=user_id, rest_id=rest_id, rating=rate_body["rating"]
            )
            rating = rest.rating
            ratedby = rest.ratedby
            newrating = (rating * ratedby + rate_body["rating"]) / (ratedby + 1)
            rest.ratedby = rest.ratedby + 1
            rest.rating = newrating
            db.session.add(newrating1)
            db.session.commit()

        return "rating updated"
