import os
import csv
import dates

# BUY STOCK
def buy_product(args):
    with open("bought.csv", "r") as inp, open("bought_edit.csv", "a") as out:
        reader = csv.reader(inp)
        writer = csv.writer(out)
        id_buy = id(1)

        isAdded = False
        for line in reader:
            
            # IF PRODUCT IS ALREADY IN STOCK
            if args.product == line[2]:
                new_amount = int(args.amount) + int(line[4])

                # IF THE ARGUMENT DATE HAS BEEN GIVEN, YOU WANT TO PURCHASE SOMETHING ON A
                # DIFFERENT DATE THAN TODAY

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
                        os.rename("bought_edit.csv", "bought.csv")
                    except:
                        None
                        
            # IF PRODUCT IS NOT EQUAL TO LINE IN FILE. JUST COPY THE LINE
            else:
                writer.writerow(line)
                try:
                    os.rename("bought_edit.csv", "bought.csv")
                except:
                    None

        # IF PRODUCT IS NOT STOCK, ADD PRODUCT TO FILE
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
                    os.rename("bought_edit.csv", "bought.csv")
                except:
                    None


if __name__ == "__main__":
    pass
