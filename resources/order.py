from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import OrderSchema
from models import RestaurantModel, OrderModel

blp = Blueprint("order", __name__, description="Operations on order")


@blp.route("/orders/<string:order_id>")
class Orders(MethodView):
    @blp.response(200, OrderSchema)
    def get(self, order_id):

        order = OrderModel.query.get_or_404(order_id)
        return order
