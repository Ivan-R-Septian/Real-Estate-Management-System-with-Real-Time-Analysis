from datetime import datetime, date, time, timedelta
import random
from tabulate import tabulate
import matplotlib.pyplot as plt
import json

products = [
    {
        "location": "bandung",
        "capital": "graha citra",
        "type": "type 21",
        "detail": "3 x 7 m2",
        "stock": 15,
        "sell_price": 300000000,
        "rent_price": 15000000
    },
    {
        "location": "bandung",
        "capital": "graha citra",
        "type": "type 36",
        "detail": "6 x 6 m2",
        "stock": 12,
        "sell_price": 400000000,
        "rent_price": 20000000
    },
    {
        "location": "bandung",
        "capital": "graha citra",
        "type": "type 45",
        "detail": "6 x 7.5 m2",
        "stock": 10,
        "sell_price": 500000000,
        "rent_price": 25000000
    },
    {
        "location": "jakarta",
        "capital": "graha mega",
        "type": "type 90",
        "detail": "9 x 10 m2",
        "stock": 5,
        "sell_price": 1200000000,
        "rent_price": 60000000
    },
    {
        "location": "jakarta",
        "capital": "graha mega",
        "type": "type 120",
        "detail": "10 x 12 m2",
        "stock": 4,
        "sell_price": 1500000000,
        "rent_price": 75000000
    },
    {
        "location": "bandung",
        "capital": "graha mega",
        "type": "type 90",
        "detail": "9 x 10 m2",
        "stock": 3,
        "sell_price": 1100000000,
        "rent_price": 55000000
    },
    {
        "location": "bandung",
        "capital": "graha mega",
        "type": "type 120",
        "detail": "10 x 12 m2",
        "stock": 3,
        "sell_price": 1300000000,
        "rent_price": 65000000
    },
    {
        "location": "surabaya",
        "capital": "graha beverly",
        "type": "type 54",
        "detail": "6 x 9 m2",
        "stock": 15,
        "sell_price": 600000000,
        "rent_price": 30000000
    },
    {
        "location": "surabaya",
        "capital": "graha beverly",
        "type": "type 60",
        "detail": "6 x 10 m2",
        "stock": 14,
        "sell_price": 700000000,
        "rent_price": 35000000
    },
    {
        "location": "surabaya",
        "capital": "graha beverly",
        "type": "type 70",
        "detail": "7 x 10 m2",
        "stock": 16,
        "sell_price": 800000000,
        "rent_price": 40000000
    }]

def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

dict_list = load_data("user.json")
products = load_data("products.json")
buy_item = []
rent_item = []
table_data = []
user_calculation_list= []
table_user = []
