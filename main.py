# Imports
import os
import sys
import csv
import pandas as pd
import argparse
from datetime import timedelta, datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass

#voorbeeld//bought.cvs/Function to get inventory items //nog omzetten.

def get_inventory():
   with open('bought.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    all_rows = []
    for row in csv_reader:
       all_rows.append(row)
    return all_rows

#voorbeeld//bought.csv/function for buy products

# def buy_product(id, product_name, price, expiry, buy_date):
#        with open('bought.csv', mode='a', newline='') as file:
#        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#        writer.writerow([id, product_name, buy_date, price, expiry])
#    sys.stdout.write("OK")

#voorbeeld//sold.csv/function for buy products

# def sell_product(id, product_name, product_price, inventory, current_date):
#    product = None
#    for item in inventory:
#       if item[1] == product_name:
#          product = item

#    if product == None:
#       sys.stdout.write("ERROR: Product not in stock")
#    else:
#       with open('sold.csv', mode='a', newline='') as file:
#        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#        writer.writerow([id, product[0], current_date, product_price])
#        sys.stdout.write("OK")

#voorbeeld//function to set datetime//nog omzetten

# def advance_time(days_to_increase):
#        current_date = get_date()
#    dt = datetime.strptime(current_date, '%Y-%m-%d')
#    yesterday = dt + timedelta(days = days_to_increase)
#    current_date = yesterday.strftime('%Y-%m-%d')
#    file = open("current_date.txt", "w")
#    file.write(current_date)
#    file.close()
#    sys.stdout.write("OK")

#voorbeeld//function validate_date invalid expiration date// nog omzetten

# def validate_date(date_string):
#        try:
#       datetime.strptime(date_string, '%Y-%m-%d')
#       return True
#    except ValueError:
#       sys.stdout.write("Invalid expiration date. It must be formatted like YYYY-MM-DD")
#       return False

if __name__ == "__main__":
    main()
