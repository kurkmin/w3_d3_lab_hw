from flask import render_template

from app import app

from models.orders import orders

@app.route("/")
def index():
    return render_template('index.html', title = 'My Orders', orders=orders)

@app.route("/orders/<index>")
def order(index):
    chosen_order = orders[int(index)]
    return render_template('order.html', orders=chosen_order)
