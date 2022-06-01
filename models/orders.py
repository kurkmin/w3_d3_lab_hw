from models.order import * 
import datetime

order1 = Order("Sumin", datetime.date(2022, 6, 1), 3, "cheese", "The world best cheese")
order2 = Order("James", datetime.date(2022, 6, 1), 4, "bacon", "The world best bacon")

orders = [order1, order2]