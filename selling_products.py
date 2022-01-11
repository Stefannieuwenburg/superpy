import os
import csv

import arguments
import dates


# Sell products from the stock:
def sell_product(args):
    with open("stock.csv", "r") as input, open("stock_edit.csv", "w", newline='') as output, open(
        "selling.csv", "a", newline='') as sold:
        reader = csv.reader(input)
        writer = csv.writer(output)
        sold_writer = csv.writer(sold)
        isAdded = False

        for line in reader:
            id_buy = line[0]
            # Whenever the product is in stock, update the number of items:
            if args.product == line[2]:
                if int(line[4]) >= args.amount:
                    new_amount = int(line[4]) - int(args.amount)
                    profit_product = (args.sell_price - float(line[3])) * int(
                        args.amount
                    )
                    # New list with the updated number of items for the specific product:
                    new_amount_arr_for_csvfile = [
                        line[0],
                        line[1],
                        line[2],
                        line[3],
                        new_amount,
                        line[5],
                    ]
                    isAdded = True
                    # Whenever, due to the selling, the new number of items is 0, remove product
                    if new_amount == 0:
                        None
                    else:
                        writer.writerow(new_amount_arr_for_csvfile)
                    # Making a new list for the sold products file
                    arr_for_soldfile = [
                        id_buy,
                        dates.display_today,
                        args.product,
                        args.amount,
                        args.sell_price,
                        profit_product,
                    ]
                    sold_writer.writerow(arr_for_soldfile)
                    try:
                        os.rename("stock_edit.csv", "stock.csv")  # The 'stock_edit.csv' file will be the new 'stock.csv' file
                    except:
                        None
                else:
                    print("Number of sold items is more than available in stock")
            elif args.product != line[2]:
                writer.writerow(line)

        if not isAdded:
            writer.writerow(line)
            try:
                os.rename("stock_edit.csv", "stock.csv")
            except:
                None


if __name__ == "__main__":
    pass
