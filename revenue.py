from inventory import get_sold_between_dates, get_sold_items
from rich import print

def get_total_revenue():
    sold_items = get_sold_items()
    total = 0
    for item in sold_items:
        total += float(item['sell_price'])
    return total


def print_total_revenue():
    total_revenue = get_total_revenue()
    print(f'The total revenue is: ${total_revenue}')


def get_revenue_between_dates():
    total = 0
    while True:
        try:
            first_date = input('Please enter the earliest of the two dates: ')
            break
        except:
            print("Please use format: 'YYYY-MM-DD'")
    while True:
        try:
            second_date = input('Please enter the latest of the two dates: ')
            break
        except:
            print("Please use format: 'YYYY-MM-DD'")
    items = get_sold_between_dates(first_date, second_date)
    for item in items:
        total += float(item['sell_price'])
    return total


def print_revenue_between_dates():
    revenue = get_revenue_between_dates()
    print(f'The total revenue in the given period was: ${revenue}')
