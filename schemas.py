from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    mobile = fields.Str(required=True)


class LoginSchema(Schema):
    email = fields.Str(required=True, load_only=True)
    password = fields.Str(required=True, load_only=True)


class RestaurantSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    rating = fields.Int(dump_only=True)
    ratedby = fields.Int(dump_only=True)


class DeliveryboySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    isengaged = fields.Boolean(dump_only=True)


class PlainMenuSchema(Schema):
    id = fields.Int(dump_only=True)


class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class MenuitemSchema(ItemSchema):
    id = fields.Int(dump_only=True)
    price = fields.Int(required=True)
    item = fields.Nested(ItemSchema(), dump_only=True)
    rating = fields.Int(dump_only=True)
    ratedby = fields.Int(dump_only=True)


class MenuSchema(Schema):
    menuitems = fields.Nested(MenuitemSchema(), dump_only=True)


class existingitemschema(Schema):
    price = fields.Int(required=True)

class OrderAndItemSchema(Schema):
    id = fields.Int(dump_only=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    totalbill = fields.Int(dump_only=True)
    cart = fields.List(fields.Nested(OrderAndItemSchema(), dump_only=True))


class RatingSchema(Schema):
    id = fields.Int(dump_only=True)
    rating = fields.Float(required=True)


