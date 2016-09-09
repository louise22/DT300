#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brettl
#
# Created:     30/08/2016
# Copyright:   (c) brettl 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def set_reserve():
    global reserve
    reserve = read_int("What is the reserve?")


def get_bids(names, bid):
    print ("Collecting bids")
    name = ""
    top_bid = 0
    top_bidder = 0
    while name.upper() != 'F':
        name = input("What is your name? (\"F\" to finish)")
        if name.upper()!= "F":
            names.append(name)
            bid =read_int("What is your bid " + name + " ?")
            bids.append(bid)
            global top_bid
            global top_bidder
            if top_bid >= int(bid):
                print("Sorry " + name + ", you'll need to make a higher bid")
            else:
                top_bid = bid
                top_bidder = name
            print("The highest bid is " + str(top_bid))


def show_bids(names, bids):
    PRICE_PER_DOZEN = 6.5
    print("Showing bids")
    for i in range(len(names)):
        print("{} bid ${}.".format(names[i], bids[i]))


def highest_bid ():
    if top_bid < reserve:
        print("The reserve of " + str(reserve) +" was not met")
    else:
        print(str(top_bidder) + " won the bid with $" + str(top_bid))

def read_int(prompt):
    choice = -1;
    while choice == -1:
        try:
            choice = int(input(prompt))
        except ValueError:
            print ("Not a valid integer")
    return choice


#main routine

names = []
bids = []
bid = 0
top_bidder = ''
top_bid = 0
set_reserve()
get_bids(names, bid)
show_bids(names, bids)
highest_bid()