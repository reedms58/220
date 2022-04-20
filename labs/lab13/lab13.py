"""
Name: Maddie Reed
lab13.py

Problem: This program alerts a user of spikes in the amounts of trades per second.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(file_name):
    my_file = open(file_name, 'r')
    trade_str = my_file.readline()
    trade_list = trade_str.split()
    seconds_of_trade = len(trade_list)
    for i in range(seconds_of_trade):
        trade_list[i] = eval(trade_list[i])
        if trade_list[i] > 830:
            print("WARNING: High trade volume at {} seconds".format(i + 1))
        elif trade_list[i] == 500:
            print("ALERT: pay attention! {} seconds".format(i + 1))
    my_file.close()

