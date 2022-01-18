# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
import sys
from arguments import arguments
from datetime import *
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
        
# test advance-time     
def advance_time(days_to_increase):
   today = date.today()
   dt = datetime.strftime(today, "%d-%m-%Y")  # Using the dd-mm-yyyy format
   yesterday = dt + timedelta(days_to_increase)
   current_date = yesterday.strftime('%Y-%m-%d')
   file = open("advance-time.txt", "w")
   file.write(current_date)
   file.close()
   sys.stdout.write("OK")


if __name__ == "__main__":
    console = Console()
    args = arguments()
    main(args)
    console.print("$" * 90)
    console.print("# Supermarket 101", args)
    console.print("$" * 90)