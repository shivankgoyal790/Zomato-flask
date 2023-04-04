from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import RestaurantSchema, MenuitemSchema, existingitemschema, OrderSchema
from models import RestaurantModel
from models import ItemModel, MenuitemModel, MenuModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt

blp = Blueprint("restaurant", __name__, description="Operations on restaurant")


@blp.route("/restaurant/<string:rest_id>")
class Allrestarants(MethodView):
    @blp.response(200, RestaurantSchema)
    def get(self, rest_id):
        return RestaurantModel.query.get_or_404(rest_id)


@blp.route("/restaurant/<string:rest_id>/menu")
class RestaurantMenu(MethodView):
    @blp.response(200, MenuitemSchema(many=True))
    def get(self, rest_id):
        menu = MenuModel.query.get_or_404(rest_id)
        return menu.menuitems.all()


@blp.route("/restaurant/<string:rest_id>")
class RestaurantList(MethodView):
    @jwt_required()
    @blp.response(201, MenuitemSchema)
    @blp.arguments(MenuitemSchema)
    def post(self, item_body, rest_id):

        claim = get_jwt()

        if claim["role"] != "restaurant" or claim["sub"] != int(rest_id):
            abort(401, "unauthorised")

        menu = MenuModel.query.get_or_404(rest_id)
        item = ItemModel(name=item_body["name"])
        db.session.add(item)
        db.session.commit()
        menuitem = MenuitemModel(
            item_id=item.id, price=item_body["price"], menu_id=menu.id
        )
        db.session.add(menuitem)
        db.session.commit()

        return menuitem, 201

    @jwt_required()
    def put(self, rest_id):

        claim = get_jwt()
        if claim["role"] != "restaurant" or claim["sub"] != int(rest_id):
            abort(401, "unauthorised")

        rest = RestaurantModel.query.get_or_404(rest_id)
        if rest.isopen:
            rest.isopen = False
        else:
            rest.isopen = True

        db.session.add(rest)
        db.session.commit()

        return "status updated", 201


@blp.route("/restaurant/<string:rest_id>/item/<string:item_id>")
class Restaurantitems(MethodView):
    @jwt_required()
    @blp.response(201, MenuitemSchema)
    @blp.arguments(existingitemschema)
    def post(self, item_body, rest_id, item_id):

        claim = get_jwt()
        if claim["role"] != "restaurant" or claim["sub"] != int(rest_id):
            abort(401, "unauthorised")

        menu = MenuModel.query.get_or_404(rest_id)
        menuitem = MenuitemModel(
            item_id=item_id, menu_id=menu.id, price=item_body["price"]
        )
        db.session.add(menuitem)
        db.session.commit()
        return menuitem

    @jwt_required()
    def delete(self, rest_id, item_id):

        claim = get_jwt()
        if claim["role"] != "restaurant" or claim["sub"] != int(rest_id):
            abort(401, "unauthorised")

        MenuitemModel.query.filter(MenuitemModel.id == item_id).delete()
        db.session.commit()
        return {"message": "menuItem removed from menu"}


@blp.route("/restaurant/<string:rest_id>/orders")
class RestaurantOrders(MethodView):
    @jwt_required()
    @blp.response(200, OrderSchema(many=True))
    def get(self, rest_id):

        claim = get_jwt()
        if claim["role"] != "restaurant" or claim["sub"] != int(rest_id):
            abort(401, "unauthorised")

        rest = RestaurantModel.query.get_or_404(rest_id)
        return rest.order.all()


@blp.route("/restaurant/<string:rest_id>/orders/<string:order_id>")
class RestaurantOrders(MethodView):
    @jwt_required()
    @blp.response(200, OrderSchema(many=True))
    def get(self, rest_id, order_id):

        claim = get_jwt()
        if claim["role"] != "restaurant" or claim["sub"] != int(rest_id):
            abort(401, "unauthorised")

        rest = RestaurantModel.query.get_or_404(rest_id)
        return rest.order.query.get_or_404(order_id)
