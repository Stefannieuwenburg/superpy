# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

from rich.console import Console
from get_arguments import get_arguments
from get_report import get_report
from buy_product import buy_product
from sell_product import sell_product


def main(args):
    args = get_arguments()
    if args.command == "report":
        get_report(args)
    elif args.command == "buy":
        buy_product(args)
    elif args.command == "sell":
        sell_product(args)


if __name__ == "__main__":
    console = Console()
    args = get_arguments()
    main(args)
    console.print("$" * 90)
    console.print("# Supermarket 101", args)
    console.print("$" * 90)