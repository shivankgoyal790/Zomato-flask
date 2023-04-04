from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, DeliveryboySchema, RestaurantSchema, LoginSchema
from models import RestaurantModel, UserModel, DeliveryModel
from models import MenuModel
from db import db
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    create_refresh_token,
    get_jwt_identity,
)
from blocklist import BLOCKLIST
from resources.util.email_checker import validemailcheck

blp = Blueprint("zomato", __name__, description="Operations on zomato")


@blp.route("/login")
class Login(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):

        user = UserModel.query.filter(UserModel.email == user_data["email"]).first()
        restaurant = RestaurantModel.query.filter(
            RestaurantModel.email == user_data["email"]
        ).first()
        agent = DeliveryModel.query.filter(
            DeliveryModel.email == user_data["email"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(
                identity=user.id, additional_claims={"role": "user"}
            )
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        if restaurant and pbkdf2_sha256.verify(
            user_data["password"], restaurant.password
        ):
            access_token = create_access_token(
                identity=restaurant.id, additional_claims={"role": "restaurant"}
            )
            refresh_token = create_refresh_token(restaurant.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        if agent and pbkdf2_sha256.verify(user_data["password"], agent.password):
            access_token = create_access_token(
                identity=agent.id, additional_claims={"role": "agent"}
            )
            refresh_token = create_refresh_token(agent.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": new_token}, 200


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200


@blp.route("/restaurant")
class ResRegister(MethodView):
    @blp.response(200, RestaurantSchema(many=True))
    def get(self):
        return RestaurantModel.query.all()

    @blp.arguments(RestaurantSchema)
    def post(self, user_data):

        if validemailcheck(user_data["email"]) == 0:
            abort(406, "Enter valid email")
        checkvalid_email(user_data)
        if len(user_data["password"]) < 8:
            abort(406, "Enter valid email")

        res = RestaurantModel(
            name=user_data["name"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        menu = MenuModel(rest_id=res.id)

        res.menu = menu
        db.session.add(res)
        db.session.commit()

        return {"message": "Restaurant created successfully."}, 201


@blp.route("/user")
class UserRegister(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users

    @blp.arguments(UserSchema)
    def post(self, user_data):

        email = user_data["email"]
        if validemailcheck(email) == 0:
            abort(406, "Enter valid email")

        checkvalid_email(user_data)
        if len(user_data["password"]) < 8:
            abort(406, "Enter valid email")

        user = UserModel(
            name=user_data["name"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            mobile=user_data["mobile"],
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201


@blp.route("/deliveryboy")
class delivery_Register(MethodView):
    @blp.response(200, DeliveryboySchema(many=True))
    def get(self):
        agents = DeliveryModel.query.all()
        return agents

    @blp.arguments(DeliveryboySchema)
    def post(self, user_data):

        email = user_data["email"]
        if validemailcheck(email) == 0:
            abort(406, "Enter valid email")
        checkvalid_email(user_data)

        if len(user_data["password"]) < 8:
            abort(406, "Enter valid email")

        user = DeliveryModel(
            name=user_data["name"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "delivery boy created successfully."}, 201


def checkvalid_email(user_data):
    if UserModel.query.filter(UserModel.email == user_data["email"]).first():
        abort(409, message="this email already exists.")
    if RestaurantModel.query.filter(
        RestaurantModel.email == user_data["email"]
    ).first():
        abort(409, message="this email already exists.")
    if DeliveryModel.query.filter(DeliveryModel.email == user_data["email"]).first():
        abort(409, message="this email already exists.")
