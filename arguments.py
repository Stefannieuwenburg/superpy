import argparse


def arguments():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    # For the buying parser:
    buy_parser = subparser.add_parser("buy", help="Add the bought products to stock")
    buy_parser.add_argument(
        "-p", "--product", type=str.lower, help="Fill in the name of the bought product"
    )
    buy_parser.add_argument(
        "-a", "--amount", type=int, help="How many items are bought?"
    )
    buy_parser.add_argument(
        "-bp",
        "--buy_price",
        type=float,
        help="Fill in the price per bought item. e.g. 1.50 euro: 1.50",
    )
    buy_parser.add_argument(
        "-exp",
        "--expiration_date",
        type=str,
        help="Fill in the expiration date of the product as dd-mm-yyyy. ",
    )
    buy_parser.add_argument(
        "-d",
        "--date",
        type=str,
        help="Fill in the date of the transaction when it's on a different day than today. Type -d and the date as dd-mm-yyyy. For example: buy -d 29-05-2021",
    )

    # For the reporting parser:
    report_parser = subparser.add_parser("report", help="Make a report")
    report_parser.add_argument(
        "subcommand",
        choices=["inventory", "revenue", "profit", "sold", "expdates"],
        help="Choose the wanted report. For the sold function: Displays the total list of sold products",
    )
    report_parser.add_argument(
        "time",
        choices=["today", "yesterday", "lastweek", "date"],
        help="Whenever a report is wished from a different time than today",
    )
    report_parser.add_argument(
        "-d",
        "--date",
        type=str,
        help="Fill in the date for the report. Firstly, type wished 'date' from time argument, then type -d and the date as dd-mm-yyyy. For example: report inventory date -d 29-05-2021",
    )
    report_parser.add_argument(
        "-f", "--file", type=str, help="When the report should be exported to a new csv file, write -f true"
    )
    report_parser.add_argument(
        "-pdf",
        "--pdf",
        type=str,
        help="When the report should be exported to a pdf file, write -pdf true",
    )

    # For the selling parser:
    sell_parser = subparser.add_parser("sell", help="Provide the sold item")
    sell_parser.add_argument(
        "-p", "--product", type=str.lower, help="Fill in the name of the sold product"
    )
    sell_parser.add_argument("-a", "--amount", type=int, help="How many products are sold?")
    sell_parser.add_argument(
        "-sp",
        "--sell_price",
        type=float,
        help="Fill in the price the item is sold for. e.g. 2.75",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    pass
