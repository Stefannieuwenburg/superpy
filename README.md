###### Welcome to Supermarket 101.#######

# What do you need to know about this CLI tool for the supermarket?

With this CLI application you can handle your inventory, buy products en sell products.
The options are almost endless. 

# These are the things you can do with this tool:

- Buy products
- Sell products
- Get you inventory(From today or any day in the past)
- Show your revenue(For today or any day in the past)
- Show your profit
- Show your product with expiring dates
- Export all the different reports to new .csv files
- Export the inventory to a PDF file
- more options easy to add for the future


# All dates in this tool have to be defined as dd-mm-yyyy!

- are all done whith a string representation following the format: '%Y-%m-%d'


# Getting started

First we can get the help menu:

>for bash user python main.py -h
>usage: main.py -h 
>
>positional arguments:
>  {buy,report,sell}
>    buy              add products that you bought
>    report           report command
>    sell             add products that you sold
>
>optional arguments:
>  -h, --help         show this help message and exit


# We can also get the help menu for the three positional arguments:

# The Buy-argument:

>for bash user python main.py buy [-h] [-p PRODUCT] [-a AMOUNT] [-bpr BUY_PRICE] [-ex EXPIRATION_DATE]
>usage: main.py buy [-h] [-p PRODUCT] [-a AMOUNT] [-bpr BUY_PRICE] [-ex EXPIRATION_DATE]
>
>optional arguments:
>  -h, --help            show this help message and exit
>  -p PRODUCT, --product PRODUCT
>                        provide name of the product
>  -a AMOUNT, --amount AMOUNT
>                        how many items did you buy
>  -bpr BUY_PRICE, --buy_price BUY_PRICE
>                        provide bought price per item
>  -ex EXPIRATION_DATE, --expiration_date EXPIRATION_DATE


# The Sell-argument:

>for bash user python main.py sell [-h] [-p PRODUCT] [-a AMOUNT] [-spr SELL_PRICE]
>usage: main.py sell [-h] [-p PRODUCT] [-a AMOUNT] [-spr SELL_PRICE]
>
>optional arguments:
>  -h, --help            show this help message and exit
>  -p PRODUCT, --product PRODUCT
>                        name of the product you sold
>  -a AMOUNT, --amount AMOUNT
>                        amount of product
>  -spr SELL_PRICE, --sell_price SELL_PRICE
>                        provide the price of the product


# And the Report-argument:

>for bash user python main.py report [-h] [-d DATE] [-f FILE]
>usage: main.py report [-h] [-d DATE] [-f FILE]
>                      {inventory,revenue,profit,sold,exdates} {today,yesterday,lastweek,date}
>
>positional arguments:
>  {inventory,revenue,profit,sold,exdates}
>                        Choose which report you want to see
>  {today,yesterday,lastweek,date}
>                        if you want to see a report from different days.
>
>optional arguments:
>  -h, --help            show this help message and exit
>  -d DATE, --date DATE  provide date for report. First type 'date' from the time argument. then type -d and the
>                        date as dd-mm-yyyy. For example: report inventory date -d 01-01-2022
>  -f FILE, --file FILE  export report to new file

# Now explain How to use the tool for the supermarket 101. 
>for bash user python main.py befor it
# To buy a product you can type in your CLI:

> main.py buy -p apple -bpr 1.50 -a 200 -ex 01-01-2022

This will add the appels to the bought file

# To sell a product you can type in your CLI:

> main.py sell -p apple -spr 2 -a 100 


# To get reports you can type in your CLI:

> main.py report inventory today
>
> main.py report inventory yesterday
>
> main.py report inventory date -d 02-01-2022
>
> main.py report revenue today
>
> main.py report revenue date -d 03-01-2022 
>
> main.py report profit lastweek
>
> main.py report profit date -d 02-02-2022
>
> main.py report exdates today
>
> main.py report exdates date -d 02-02-2022
>
# To make files of the Information you asked for

> main.py report profit date -d 02-01-2022 -f

>Add -f to your arguments and the output of the CLI will be exported to a new .csv file