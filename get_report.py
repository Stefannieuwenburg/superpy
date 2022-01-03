import csv
import os
from rich.console import Console
from rich.table import Table
from datetime import date, timedelta, datetime
from get_arguments import get_arguments
from export_to_pdf import export_to_pdf
import dates

# GET REPORT
def get_report(args):
    with open("bought.csv", "r") as f, open("report.csv", "w") as file_writer:
        bought_report = csv.reader(f)
        new_csv_file = csv.writer(file_writer)

        table_bought = Table(show_header=True, header_style="bold", show_lines=False)
        table_sold = Table(show_header=True, header_style="bold", show_lines=False)
        table_revenue = Table(show_header=True, header_style="bold", show_lines=False)
        table_profit = Table(show_header=True, header_style="bold", show_lines=False)
        console = Console()

        table_bought.add_column("ID")
        table_bought.add_column("Date")
        table_bought.add_column("Product")
        table_bought.add_column("Buy Price")
        table_bought.add_column("Amount")
        table_bought.add_column("Expiration Date")

        table_sold.add_column("ID")
        table_sold.add_column("Sell Date")
        table_sold.add_column("Product")
        table_sold.add_column("Amount")
        table_sold.add_column("Sell Price")
        table_sold.add_column("Profit")

        table_revenue.add_column("Revenue")

        table_profit.add_column("Profit")

        # GET INVENTORY TODAY
        if args.subcommand == "inventory" and args.time == "today":
            for line in bought_report:
                if args.file == "true":
                    new_csv_file.writerow(line)
                elif args.pdf == "true":
                    try:
                        export_to_pdf()
                    except:
                        None
                else:
                    table_bought.add_row(
                        line[0], line[1], line[2], line[3], line[4], line[5]
                    )
            console.print(table_bought)

        # GET INVENTORY YESTERDAY
        if args.subcommand == "inventory" and args.time == "yesterday":
            for line in bought_report:
                if (datetime.strptime(line[1], "%d-%m-%Y")) < datetime.strptime(
                    dates.display_yesterday, "%d-%m-%Y"
                ):
                    if args.file == "true":
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

        # GET INVENTORY FROM LAST WEEK
        if args.subcommand == "inventory" and args.time == "lastweek":
            display_last_week = datetime.strftime(dates.last_week, "%d-%m-%Y")

            for line in bought_report:
                if (
                    datetime.strptime(display_last_week, "%d-%m-%Y")
                    < datetime.strptime(line[1], "%d-%m-%Y")
                    < datetime.strptime(dates.display_today, "%d-%m-%Y")
                ):
                    if args.file == "true":
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

        # GET INVENTORY ON SPECIFIC DATES
        if args.subcommand == "inventory" and args.time == "date":
            display_date = datetime.strptime(args.date, "%d-%m-%Y")

            for line in bought_report:
                if (datetime.strptime(line[1], "%d-%m-%Y")) <= display_date:
                    if args.file == "true":
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

        # GET REPORT WITH EXPIRATION DATES
        if args.subcommand == "exdates" and args.time == "today":
            for line in bought_report:
                if (datetime.strptime(line[5], "%d-%m-%Y")) <= datetime.strptime(
                    dates.display_yesterday, "%d-%m-%Y"
                ):
                    if args.file == "true":
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

        # GET REPORT WITH EXPIRATION DATES ON SPECIFIC DATES
        if args.subcommand == "exdates" and args.time == "date":
            display_date = datetime.strptime(args.date, "%d-%m-%Y")
            for line in bought_report:
                if (datetime.strptime(line[5], "%d-%m-%Y")) <= display_date:
                    if args.file == "true":
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

    with open("sold.csv", "r") as sold_file:
        sold_report = csv.reader(sold_file)

        # # GET REPORT WITH SOLD PRODUCTS
        if args.subcommand == "sold":
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%Y")) <= dates.display_today:

                    if args.file == "true":
                        new_csv_file.writerow(line)
                    else:
                        table_sold.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
                console.print(table_sold)


        # GET REPORT WITH REVENUE
        if args.subcommand == "revenue" and args.time == "today":
            sum_revenue = 0
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%Y")) == dates.display_today:

                    total_revenue_per_product = float(line[3]) * float(line[4])
                    sum_revenue += total_revenue_per_product
                    if args.file == "true":
                        new_csv_file.writerow(sum_revenue)
                    else:
                        None
                else:
                    table_revenue.add_row(str(sum_revenue))
            console.print(table_revenue)

        # GET REPORT WITH REVENUE ON SPECIFIC DATES
        if args.subcommand == "revenue" and args.time == "date":
            display_date = datetime.strptime(args.date, "%d-%m-%Y")
            sum_revenue = 0
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%Y")) <= display_date:
                    total_revenue_per_product = float(line[3]) * float(line[4])
                    sum_revenue += total_revenue_per_product
                    if args.file == "true":
                        new_csv_file.writerow(sum_revenue)
                    else:
                        None
                else:
                    table_revenue.add_row(str(sum_revenue))
            console.print(table_revenue)

        # GET REPORT WITH PROFIT
        if args.subcommand == "profit" and args.time == "today":
            sum_profit = 0
            for line in sold_report:
                sum_profit += float(line[5])
                if args.file == "true":
                    new_csv_file.writerow(sum_profit)
                else:
                    None
            else:
                table_profit.add_row(str(sum_profit))
            console.print(table_profit)

        # GET REPORT WITH PROFIT ON SPECIFIC DATES
        if args.subcommand == "profit" and args.time == "date":
            display_date = datetime.strptime(args.date, "%d-%m-%Y")
            sum_profit = 0
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%Y")) <= display_date:
                    sum_profit += float(line[5])
                    if args.file == "true":
                        new_csv_file.writerow(sum_profit)
                    else:
                        None
                else:
                    table_profit.add_row(str(sum_profit))
            console.print(table_profit)


if __name__ == "__main__":
    pass