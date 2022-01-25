from date import get_date
import csv
import datetime
from inventory import bought_link
from rich import print


def get_new_id(file):
    with open(file) as f:
        reader = csv.reader(f)
        new_id = len(next(zip(*reader)))
    return new_id


def get_expiration_date(days):
    date = get_date()
    today = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    new_date = today + datetime.timedelta(days=days)
    return new_date


def buy_item():
    product_name = input('Product: ')
    today = get_date()
    while True:
        try:
            amount = int(input('Amount of items bought: '))
            break
        except:
            print('Please try again with a whole number, example: 5')
    while True:
        try:
            buy_price = float(input('Amount paid (example input: 1.25): '))
            break
        except:
            print('Please try again with the correct format, example: 1.25')
    while True:
        try:
            expiration_days = int(input('Expiration date (days from now): '))
            break
        except:
            print('Please try again and enter the number of days, example: 5')
    expiration = get_expiration_date(expiration_days)
    with open(bought_link, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        for i in range(amount):
            id = get_new_id(bought_link) + i
            product = [id, product_name, today, buy_price, expiration]
            csv_writer.writerow(product)
    print(
        f'You have purchased {product_name} costing {buy_price} times {amount}, they wil expire on {expiration}')
