###### Welcome to Supermarket 101.#######

# What do you need to know about this CLI tool for the supermarket?

With this CLI application you can handle your inventory, buy products en sell products.
The options are almost endless. 

# Getting started

First we can get the help menu:

> for bash user python main.py -h
> usage: main.py -h 
>
> supermarket 101 inventory.

># positional arguments are: scroll down for more info 

>{advance-time,show-date,set-today,total-revenue,date-revenue,buy,sell,inventory,sales,purchases}

    advance-time        Advance the date a number of days.
    show-date           Show the system date.
    set-today           Set the system date to the current date.
    total-revenue       Show the total revenue, between now and the beginning of time.
    date-revenue        Show the total revenue, between between two dates.
    buy                 Register the purchasing of a product.
    sell                Register a sale.
    inventory           Shows the amounts of currently available products.
    sales               Shows all sales made since the beginning of time.
    purchases           Shows all purchases made since the dawn of man.

>optional arguments:
  -h, --help            show this help message and exit
# advance-time 
$ python main.py advance-time
Please tell me how many days you would like to chance date/time:5
The new date is now 2022-01-30.
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Supermarket 101 Namespace(command='advance-time',)
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# set-today
$ python main.py set-today
The date is now: 2022-01-20
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Supermarket 101 Namespace(command='set-today',)
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# buy 
$ python main.py buy
Product: chees
Amount of items bought: 2
Amount paid (example input: 1.25): 1.00
Expiration date (days from now): 3
You have purchased chees costing 1.0 times 2, they wil expire on 2022-01-23
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Supermarket 101 Namespace(command='buy',)
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# total-revenue
$ python main.py total-revenue
The total revenue is: $31.75
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Supermarket 101 Namespace(command='total-revenue',) 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# purchases
$ python main.py purchases
┌──────────────┬──────────────────┬───────┬─────────────────┐
│ Product      │ Date of purchase │ Price │ Expiration date │
├──────────────┼──────────────────┼───────┼─────────────────┤
│ banana       │ 2021-08-24       │ 1.25  │ 2021-08-28      │
│ banana       │ 2021-08-24       │ 1.25  │ 2021-08-28      │
│ banana       │ 2021-08-24       │ 1.25  │ 2021-08-28      │
│ banana       │ 2021-08-24       │ 1.25  │ 2021-08-22      │
│ apple        │ 2021-08-24       │ 1.25  │ 2021-08-27      │
│ apple        │ 2021-08-24       │ 1.25  │ 2021-08-27      │
│ peach        │ 2021-08-24       │ 1.3   │ 2021-08-27      │
│ peach        │ 2021-08-24       │ 1.0   │ 2021-08-27      │
│ peach        │ 2021-08-24       │ 1.0   │ 2021-08-27      │
│ brood        │ 2022-01-25       │ 2.0   │ 2022-01-30      │
│ chees        │ 2022-01-20       │ 1.0   │ 2022-01-23      │
│ chees        │ 2022-01-20       │ 1.0   │ 2022-01-23      │
└──────────────┴──────────────────┴───────┴─────────────────┘
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Supermarket 101 Namespace(command='purchases',)
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# have fun whit this master tool