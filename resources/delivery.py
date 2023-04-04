from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import DeliveryboySchema, OrderSchema
from models import DeliveryModel
from db import db
from flask_jwt_extended import jwt_required,get_jwt

blp = Blueprint("delivery", __name__, description="Operations on delivery agent")


@blp.route("/delivery/<string:agent_id>")
class Deliveryroutes(MethodView):
    @blp.response(200, DeliveryboySchema)
    def get(self, agent_id):
        agent = DeliveryModel.query.get_or_404(agent_id)
        return agent

    @jwt_required()
    def put(self, agent_id):
        claim = get_jwt()
        if claim["role"] != "agent" or claim["sub"] != int(agent_id):
            abort(401, "unauthorised")
        agent = DeliveryModel.query.get_or_404(agent_id)
        if agent.isengaged:
            agent.isengaged = False
        else:
            agent.isengaged = True

        db.session.commit()

        return "succesfully updated your status", 201


@blp.route("/delivery/<string:agent_id>/orders")
class AgentOrders(MethodView):
    @jwt_required()
    @blp.response(200, OrderSchema(many=True))

    def get(self, agent_id):

        claim = get_jwt()
        if claim["role"] != "agent" or claim["sub"] != int(agent_id):
            abort(401, "unauthorised")
        agent = DeliveryModel.query.get_or_404(agent_id)
        return agent.order.all()
