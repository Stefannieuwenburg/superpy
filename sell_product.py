import os
import csv
import get_arguments
import dates

# SELL PRODUCTS

def sell_product(args):
    with open("bought.csv", "r") as inp, open("bought_edit.csv", "w") as out, open(
        "sold.csv", "a"
    ) as sold:
        reader = csv.reader(inp)
        writer = csv.writer(out)
        sold_writer = csv.writer(sold)
        isAdded = False

        for line in reader:
            id_buy = line[0]
            
            # IF PRODUCT IS IN STOCK. ADD UPDATED AMOUNT
            if args.product == line[2]:
                if int(line[4]) >= args.amount:
                    new_amount = int(line[4]) - int(args.amount)
                    profit_product = (args.sell_price - float(line[3])) * int(
                        args.amount
                    )
                    
                    # NEW LIST WITH UPDATED AMOUNT
                    new_amount_arr_for_csvfile = [
                        line[0],
                        line[1],
                        line[2],
                        line[3],
                        new_amount,
                        line[5],
                    ]
                    isAdded = True

                    if new_amount == 0:
                        None
                    else:
                        writer.writerow(new_amount_arr_for_csvfile)
                        
                    # MAKE NEW LIST FOR SOLD FILE
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
                        os.rename("bought_edit.csv", "bought.csv")
                    except:
                        None
                else:
                    print("Amount is more than we have in stock")
            elif args.product != line[2]:
                writer.writerow(line)

        if not isAdded:
            writer.writerow(line)
            try:
                os.rename("bought_edit.csv", "bought.csv")
            except:
                None


if __name__ == "__main__":
    pass
