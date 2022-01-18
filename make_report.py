import csv
import os
from rich.console import Console
from rich.table import Table
from datetime import date, timedelta, datetime
from arguments import arguments
from make_pdf_report import make_pdf_report
import dates


# Making the report:
def make_report(args):
    with open("stock_edit.csv", "r") as file_reader, open("selling.csv", "w", newline='') as file_writer:
        bought_report = csv.reader(file_reader)
        new_csv_file = csv.writer(file_writer)

        table_bought = Table(show_header=True, header_style="bold", show_lines=False)
        table_sold = Table(show_header=True, header_style="bold", show_lines=False)
        table_revenue = Table(show_header=True, header_style="bold", show_lines=False)
        table_profit = Table(show_header=True, header_style="bold", show_lines=False)
        console = Console()
        # Columns for 'bought'table
        table_bought.add_column("ID")
        table_bought.add_column("Date")
        table_bought.add_column("Product")
        table_bought.add_column("Buy Price")
        table_bought.add_column("Amount")
        table_bought.add_column("Expiration Date")
        # Columns for 'sold' report
        table_sold.add_column("ID")
        table_sold.add_column("Sell Date")
        table_sold.add_column("Product")
        table_sold.add_column("Amount")
        table_sold.add_column("Sell Price")
        table_sold.add_column("Profit")
        # Column for 'revenue' report
        table_revenue.add_column("Revenue")
        # Column for 'profit' report
        table_profit.add_column("Profit")

        # Get the inventory report of today:
        if args.subcommand == "inventory" and args.time == "today":
            for line in bought_report:
                if args.file == "true":
                    new_csv_file.writerow(line)
                elif args.pdf == "true":
                    try:
                        make_pdf_report()
                    except:
                        None
                else:
                    table_bought.add_row(
                        line[0], line[1], line[2], line[3], line[4], line[5]
                    )
            console.print(table_bought)

        # Get the inventory report of yesterday:
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

        # Get the inventory report of last week:
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

        # Get the inventory report of a specific day:
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

        # Get the report with all the expiration dates, from today:
        if args.subcommand == "expdates" and args.time == "today":
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

        # Get the report with all the expiration dates, from a specific day:
        if args.subcommand == "expdates" and args.time == "date":
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

    with open("selling.csv", "r") as sold_file:
        sold_report = csv.reader(sold_file)

        # Get the report with all the sold items:
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


        # Get the report of the revenue of today:
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

        # Get the report of the revenue on a specific date:
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

        # Get the report of the profit of today:
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

        # Get the report of the profit on a specific day:
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
