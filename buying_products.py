import os
import csv
import arguments
import dates


# Buy new products for in stock
def buy_product(args):
    with open("stock.csv", "r") as inp, open("stock_edit.csv", "a", newline='') as out:
        reader = csv.reader(inp)
        writer = csv.writer(out)
        id_buy = id(1)

        isAdded = False
        for line in reader:
            # When product is already in stock, only update amount of product.
            if args.product == line[2]:
                new_amount = int(args.amount) + int(line[4])

                # If the date-argument is given, the product can be added to the stock on 
                # a different day than today.

                if args.date == None:
                    new_amount_arr_for_csvfile = [
                        id_buy,
                        dates.display_today,
                        args.product,
                        args.buy_price,
                        new_amount,
                        args.expiration_date,
                    ]
                    isAdded = True
                    writer.writerow(new_amount_arr_for_csvfile)

                elif len(args.date) > 2:
                    new_amount_and_date_arr_for_csvfile = [
                        id_buy,
                        args.date,
                        args.product,
                        args.buy_price,
                        new_amount,
                        args.expiration_date,
                    ]
                    isAdded = True

                    writer.writerow(new_amount_and_date_arr_for_csvfile)
                    try:
                        os.rename("stock_edit.csv", "stock.csv")  # The 'stock_edit.csv' will be the 'new' stock.
                    except:
                        None
            # Whenever the product is not the same as the lines in the stock file, the line will be copied.
            else:
                writer.writerow(line)
                try:
                    os.rename("stock_edit.csv", "stock.csv")
                except:
                    None

        # Whenever the product isn't already in the stock, the product is added to the file.
        if not isAdded:
            if args.date == None:
                new_arr_for_csvfile = [
                    id_buy,
                    dates.display_today,
                    args.product,
                    args.buy_price,
                    args.amount,
                    args.expiration_date,
                ]
                writer.writerow(new_arr_for_csvfile)
            elif len(args.date) > 2:
                new_amount = int(args.amount) + int(line[4])
                new_amount_and_date_arr_for_csvfile = [
                    id_buy,
                    args.date,
                    args.product,
                    args.buy_price,
                    new_amount,
                    args.expiration_date,
                ]
                writer.writerow(new_amount_and_date_arr_for_csvfile)
                try:
                    os.rename("stock_edit.csv", "stock.csv")
                except:
                    None


if __name__ == "__main__":
    pass
