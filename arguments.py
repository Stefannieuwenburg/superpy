import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="buy product, div reports, and sell products")
    
    subparser = parser.add_subparsers(dest="command")

    #Buy Parser
    
    buy_parser = subparser.add_parser(
        "buy", help="add products that you bought")
    
    buy_parser.add_argument(
        "-p", "--product", type=str.lower, help="provide name of the product"
    )
    buy_parser.add_argument(
        "-a", "--amount", type=int, help="how many items did you buy"
    )
    buy_parser.add_argument(
        "-bpr",
        "--buy_price",
        type=float,
        help="provide bought price per item. example: when amount is 1.25 euro: -a 1.25",
    )
    buy_parser.add_argument(
        "-ex",
        "--expiration_date",
        type=str,
        help="add the expiration date as dd-mm-yyyy. ",
    )
    buy_parser.add_argument(
        "-d",
        "--date",
        type=str,
        help="provide date if your transaction is another day then today. Type -d and the date as dd-mm-yyyy. For example: buy -d 10-12-2021",
    )

    #Report Parser
    
    report_parser = subparser.add_parser(
        "report", help="report command")
    
    report_parser.add_argument(
        "subcommand",
        choices=["inventory", "revenue", "profit", "sold", "exdates"],
        help="Choose which report you want to see. The sold function displays the total sold products",
    )
    report_parser.add_argument(
        "time",
        choices=["today", "yesterday", "lastweek", "date"],
        help="if you want to see a report from different days.",
    )
    report_parser.add_argument(
        "-d",
        "--date",
        type=str,
        help="provide date for report. First type 'date' from the time argument. then type -d and the date as dd-mm-yyyy. For example: report inventory date -d 10-12-2021",
    )
    report_parser.add_argument(
        "-f", "--file", type=str, help="export report to new csv file. example: -f true"
    )
    # report_parser.add_argument(
    #     "-pdf",
    #     "--pdf",
    #     type=str,
    #     help="export report to new pdf file. example: -pdf true",
    # )

    #Sell Parser
    
    sell_parser = subparser.add_parser(
        "sell", help="add products that you sold")
    
    sell_parser.add_argument(
        "-p", "--product", type=str.lower, help="name of the product you sold"
    )
    sell_parser.add_argument(
        "-a", "--amount", type=int, help="amount of product")
    
    sell_parser.add_argument(
        "-spr",
        "--sell_price",
        type=float,
        help="provide the price of the product. For example: 2.25",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    pass


