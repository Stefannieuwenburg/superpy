from date import get_date
from inventory import get_available_product, sold_link
from buy import get_new_id
from rich import print
import csv


def sell_item():
    product_name = input('Product: ')
    today = get_date()
    available_products = get_available_product(product_name)
    if available_products != None:
        while True:
            try:
                amount = int(input('Amount of items sold: '))
                if amount <= len(available_products):
                    break
                else:
                    print(
                        f"Sorry, there are only {len(available_products)} of item: '{product_name}' currently in stock")
            except:
                print('Please try again with a whole number, example: 5')
        while True:
            try:
                sell_price = float(input('Sold for amount: '))
                break
            except:
                print('Please try again with the correct format, example: 1.25')
        with open(sold_link, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            for i in range(amount):
                bought_id = available_products[i]['id']
                id = get_new_id(sold_link) + i
                product = [id, bought_id, today, sell_price]
                csv_writer.writerow(product)
        print(
            f"You have sold {amount} of '{product_name}' for €{sell_price} on {today}, well done!")
