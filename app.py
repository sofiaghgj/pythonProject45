from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from info import *
from datetime import datetime
from utils import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

    def instance_to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def instance_to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def instance_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
        }


with app.app_context():
    db.create_all()
    for user in users:
        db.session.add(User(**user))
        db.session.commit()

    for i in offers:
        db.session.add(Offer(**i))
        db.session.commit()

    for order in orders:
        order["start_date"] = datetime.strptime(order["start_date"], '%m/%d/%Y').date()
        order["end_date"] = datetime.strptime(order["end_date"], '%m/%d/%Y').date()
        db.session.add(Order(**order))
        db.session.commit()



@app.route("/users/<int:user>", methods=['GET', 'DELETE', 'PUT'])
def users(user):
    if request.methods == 'GET':
        userss = User.query.get(user)
        return jsonify(instance_to_user(userss))
    if request.methods == 'DELETE':
        users = User.query.get(user)
        db.session.delete(users)
        db.session.commit()
        return jsonify("")
    if request.methods == 'PUT':
        user_data = request.json
        users = User.query.get(user)
        if user_data.get('first_name'):
            users.first_name = user_data['user_data']
        if user_data.get('last_name'):
            users.last_name = user_data['last_name']
        if user_data.get('age'):
            users.age = user_data['age']
        if user_data.get('email'):
            users.email = user_data['email']
        if user_data.get('role'):
            users.role = user_data['role']
        if user_data.get('phone'):
            users.phone = user_data['phone']

        db.session.add(users)
        db.session.commit()
        return jsonify(instance_to_user(users))


@app.route("/users", methods=['GET', 'POST'])
def user():
    if request.methods == 'GET':
        result = []
        users = User.query.all()
        for user in users:
            result.append(instance_to_user(user))
        return jsonify(result)
    if request.methods == 'POST':
        data = request.json
        users = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=data.get('age'),
            email=data.get('email'),
            role=data.get('role'),
            phone=data.get('phone')
        )
        db.session.add(users)
        db.session.commit()
        return jsonify(instance_to_user(users))


@app.route("/orders/<order>", methods=['GET', 'DELETE', 'PUT'])
def orders(order):
    if request.methods == 'GET':
        orders = Order.query.get(order)
        return jsonify(instance_to_oder(orders))
    if request.methods == 'DELETE':
        orders = Order.query.get(order)
        db.session.delete(orders)
        db.session.commit()
        return jsonify("")
    if request.methods == 'PUT':
        orders_data = request.json
        orders = Order.query.get(order)
        if orders_data.get('name'):
            users.name = orders_data['name']
        if orders_data.get('description'):
            users.description = orders_data['description']
        if orders_data.get('start_date'):
            users.start_date = orders_data['start_date']
        if orders_data.get('end_date'):
            users.end_date = orders_data['end_date']
        if orders_data.get('address'):
            users.address = orders_data['address']
        if orders_data.get('price'):
            users.price = orders_data['price']

        db.session.add(orders)
        db.session.commit()
        return jsonify(instance_to_oder(orders))


@app.route("/orders", methods=['GET', 'POST'])
def order():
    if request.methods == 'GET':
        result = []
        orders = Order.query.all()
        for order in orders:
            result.append(instance_to_oder(order))
        return jsonify(result)
    if request.methods == 'POST':
        data = request.json
        orders = Order(
            name=data.get('name'),
            description=data.get('description'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            address=data.get('address'),
            price=data.get('price')
        )
        db.session.add(orders)
        db.session.commit()
        return jsonify(instance_to_oder(orders))


@app.route("/offers/<offer>", methods=['GET', 'DELETE', 'PUT'])
def offers(offer):
    if request.methods == 'GET':
        offers = Offer.query.get(offer)
        return jsonify(instance_to_oder(offers))
    if request.methods == 'DELETE':
        offers = Offer.query.get(offer)
        db.session.delete(offers)
        db.session.commit()
        return jsonify("")
    if request.methods == 'PUT':
        offers_data = request.json
        offers = Offer.query.get(offer)
        if offers_data.get('name'):
            offers.name = offers_data['name']
        if offers_data.get('order_id'):
            offers.order_id = offers_data['order_id']
        if offers.get('executor_id'):
            offers.executor_id = offers_data['executor_id']
        db.session.add(offers)
        db.session.commit()
        return jsonify(instance_to_oder(offers))


@app.route("/offers", methods=['GET', 'POST'])
def offer():
    if request.methods == 'GET':
        result = []
        offers = Offer.query.all()
        for offer in offers:
            result.append(instance_to_offer(offer))
        return jsonify(result)
    if request.methods == 'POST':
        data = request.json
        offers = Offer(
            order_id=data.get('order_id'),
            executor_id=data.get('executor_id'),
            )
        db.session.add(offers)
        db.session.commit()
        return jsonify(instance_to_oder(offers))




if __name__ == '__main__':
    app.run()

