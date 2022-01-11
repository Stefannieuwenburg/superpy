# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

from arguments import arguments
from make_report import make_report
from buying_products import buy_product
from selling_products import sell_product
from rich.console import Console

def main(args):
    args = arguments()
    if args.command == "report":
        make_report(args)
    elif args.command == "buy":
        buy_product(args)
    elif args.command == "sell":
        sell_product(args)

if __name__ == "__main__":
    console = Console()
    args = arguments()
    main(args)
    console.print("$" * 90)
    console.print("# Supermarket 101", args)
    console.print("$" * 90)