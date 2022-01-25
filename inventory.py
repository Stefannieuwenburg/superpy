import csv
from rich import style
from date import get_date
from rich.console import Console
from rich.table import Table

bought_link = './data/bought.csv'
sold_link = './data/sold.csv'
inventory_link = './data/inventory.csv'
console = Console()


def get_bought_items():
    bought_items = []
    with open(bought_link, 'r', encoding='utf-8-sig') as bought_object:
        reader = csv.DictReader(bought_object)
        for row in reader:
            bought_items.append(row)
    return bought_items


def get_sold_ids():
    sold_ids = []
    with open(sold_link, 'r', encoding='utf-8-sig') as sold_object:
        reader = csv.DictReader(sold_object)
        for row in reader:
            sold_ids.append(row['bought_id'])
    return sold_ids


def get_sold_items():
    sold_items = []
    with open(sold_link, 'r', encoding='utf-8-sig') as sold_object:
        reader = csv.DictReader(sold_object)
        for row in reader:
            sold_items.append(row)
    return sold_items


def get_available_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date()
    for item in bought_items:
        if item['id'] not in sold_ids and item['expiration_date'] >= today:
            available_products.append(item)
    return available_products


def get_expired_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    expired_products = []
    today = get_date()
    for item in bought_items:
        if item['id'] not in sold_ids and item['expiration_date'] < today:
            expired_products.append(item)
    return expired_products


def get_available_product(product_name):
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    availabe_products = []
    today = get_date()
    for item in bought_items:
        if item['id'] not in sold_ids and item['expiration_date'] >= today and item['product_name'] == product_name:
            availabe_products.append(item)
    if availabe_products == []:
        print('Sorry, no available items were found.')
    else:
        return availabe_products


def get_sold_between_dates(first_date, second_date):
    sold_items = get_sold_items()
    items = []
    for item in sold_items:
        if item['sell_date'] >= first_date and item['sell_date'] <= second_date:
            items.append(item)
    return items


def get_inventory():
    items = get_available_products()
    inventory = {}
    for item in items:
        if item['product_name'] in inventory.keys():
            inventory[item['product_name']] += 1
        else:
            inventory.update({item['product_name']: 1})
    return inventory


def display_inventory():
    # Takes the inventory and diplays it in a table
    inventory = get_inventory()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column('Product', style='dim', width=12)
    table.add_column('Current stock')
    for key, value in inventory.items():
        table.add_row(
            key,
            str(value),
        )
    console.print(table)


def display_sales():
    sales = get_sold_items()
    purchases = get_bought_items()
    for item in sales:
        for product in purchases:
            if item['bought_id'] == product['id']:
                item.update({'product_name': product['product_name']})
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column('Product', style='dim', width=12)
    table.add_column('Date of sale')
    table.add_column('Price')
    for item in sales:
        table.add_row(
            item['product_name'],
            item['sell_date'],
            item['sell_price']
        )
    console.print(table)


def display_purchases():
    purchases = get_bought_items()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column('Product', style='dim', width=12)
    table.add_column('Date of purchase')
    table.add_column('Price')
    table.add_column('Expiration date')
    for item in purchases:
        table.add_row(
            item['product_name'],
            item['buy_date'],
            item['buy_price'],
            item['expiration_date']
        )
    console.print(table)