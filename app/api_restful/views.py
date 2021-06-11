# -*- coding: utf-8 -*-
from app.api_restful import api_restful_bp
from app.api_restful.models import *
from app import db

# import flask.scaffold
#
# flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

api = Api(api_restful_bp)

product_create_args = reqparse.RequestParser()
product_create_args.add_argument('name', type=str, help='"name" field is required', required=True)
product_create_args.add_argument('type', type=str, help='"type" field is required', required=True)
product_create_args.add_argument('price', type=int, help='"price" field is required', required=True)
product_create_args.add_argument('amount', type=int, help='"amount" field is required', required=True)
product_create_args.add_argument('company', type=str, help='"company" field is required', required=True)
product_create_args.add_argument('date_shipped', type=str, required=False)

product_update_args = reqparse.RequestParser()
product_update_args.add_argument('name', type=str, help='"name" field is required', required=True)
product_update_args.add_argument('type', type=str, help='"type" field is required', required=True)
product_update_args.add_argument('price', type=int, help='"price" field is required', required=True)
product_update_args.add_argument('amount', type=int, help='"amount" field is required', required=True)
product_update_args.add_argument('company', type=str, help='"company" field is required', required=True)
product_update_args.add_argument('date_shipped', type=str, required=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'type': fields.String,
    'price': fields.Integer,
    'amount': fields.Integer,
    'company': fields.String,
    'date_shipped': fields.String
}


class AllProducts(Resource):
    def get(self):
        products = Product.query.all()
        products_list = {}
        for t in products:
            products_list[t.id] = {"id": t.id, "name": t.name, "type": t.type, "price": t.price, "amount": t.amount,
                                   "company": t.company, "date_shipped": str(t.date_shipped)}
        return products_list

    @marshal_with(resource_fields)
    def post(self):
        args = product_create_args.parse_args()
        try:
            if args['date_shipped']:
                product = Product(name=args['name'], type=args['type'], price=args['price'], amount=args['amount'],
                                  company=args['company'],
                                  date_shipped=datetime.strptime(args['date_shipped'], '%Y-%m-%d'))
            else:
                product = Product(name=args['name'], type=args['type'], price=args['price'], amount=args['amount'],
                                  company=args['company'])

            db.session.add(product)
            db.session.commit()
            return product, 201
        except:
            db.session.rollback()
            abort(400, message="Wrong entered data!")


class OneProduct(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            abort(404, message="Product not found!")

        return product

    # @marshal_with(resource_fields)
    def delete(self, id):
        product = Product.query.filter_by(id=id).first()

        if not product:
            abort(404, message="Product not found!")

        db.session.delete(product)
        db.session.commit()

        return "Product deleted!", 204

    @marshal_with(resource_fields)
    def put(self, id):
        product = Product.query.filter_by(id=id).first()

        if not product:
            abort(404, message="Task not found!")

        args = product_update_args.parse_args()

        product.name = args['name']
        product.type = args['type']
        product.price = args['price']
        product.amount = args['amount']
        product.company = args['company']
        if args['date_shipped']:
            product.date_shipped = datetime.strptime(args['date_shipped'], '%Y-%m-%d')

        try:
            db.session.commit()
            return product, 201
        except:
            db.session.rollback()
            abort(400, message="Wrong entered data!")


api.add_resource(AllProducts, '/products')
api.add_resource(OneProduct, '/products', '/products/<int:id>')
