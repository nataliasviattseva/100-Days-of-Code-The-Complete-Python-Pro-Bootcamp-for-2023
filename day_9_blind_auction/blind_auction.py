# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Blind%20Auction%20Flow%20Chart#R3VnbcpswEP0aPzYDCLB5tHNrZ9pMpu6kzaMMilEDiBHyLV%2FfFYirHMdp7JD4JUGrXV3Ont2V5AE6j9fXHKfhDxaQaGAZwXqALgaWZRqmAf%2BkZFNIHM8qBHNOA6VUC6b0iZSWSrqgAclaioKxSNC0LfRZkhBftGSYc7Zqqz2wqD1riudEE0x9HOnS3zQQoZK6jl13fCV0HpZTm65X9MS41FZbyUIcsFVDhC4H6JwzJoqveH1OIoleCUxhd%2FVMb7UyThKxj8Hs4R5fx%2BMlu%2F52dxPepdM7H31BxShLHC3UjtVixaaEgASAiGoyLkI2ZwmOLmvphLNFEhA5jQGtWuc7YykITRD%2BJUJslHvxQjAQhSKOVG8xp5zo2b0pUcYW3Cc7NlSSBPM5ETv0rMoDwF3CYiL4Buw4ibCgy%2FY6sCLRvNKrYYYPhfQrUDc11Ke%2Fxj9%2FadDXwEqUViEVZJrifP8riLdtIC4JF2S9G0Z928rAHimuqmi1VXNVU99TorBBemQcCSfn1Nhp7clOu092Wjo7Q0hclhEBcDKJchbn6VWcpZsPx1mvZ84OT42z9p6cdfvkrK2hPs4e84LP4e8NjokcIUkXon%2FCOk6LsKajM9a0t1DWPhZlvVOjrLsnZUd9UtbdSdkJ2FrGLaew0Y%2FG2OpI2xtjTf0E9ckp%2B1YqKtNbRmHmynOO1fYcGnU8UoSIsuo4pVrG%2F%2FtppHM8COqEjJOgojqsQB4usLwsUl9QcESOAKwUIjmU6o9kUxnlQ54NLBfHkvDJLEsrh%2FQZKmh41gmWLQcSc%2BjoweIcLVhGfcQGWVPxR5nL7%2FuG%2FGLd6LjYlI0EdpubAISqed%2Fsq83yVml3wCg00Z6VwxweIl7HnONNQyGVcZg9H872yGxxy%2B5e%2BTv6yHN26cNHsYKDxnwFdi90Mxt0Uzw6CcI1noz6eLDQ34mKwwp9KLIzz9N5%2FpfJ5kCu141gR5MZNNy5%2FFpkhMtsvgplpl%2FhnKp51p%2FJEtBN3SGLZ4usp7RdVcqX0na3oh4Oc%2F2AeE8yDSbYtGjjgSM6T%2BDbh82DJ9BEQkN9HI1VR0yDoIg6ktEnPMuHksRW%2BQfGdSYD50KOBYGWFTF3IKiRZ7dzkmFrQG87S1pHw9nrtTxWOeo1BbKVrerk9Q75arhnvnrrC9b2gmZ1HnvQcL%2Fz7GsLbbdwOvbuQttd12v1zeE7FGZTf5o6jwjm1fk68zkhiZ6I3%2FkMjZzOK%2FSWVLztSe9ot80y9TSAu6L5LaTALYQ1kEyUdQyuMlVX%2ByqT2wTEj4pKCSpx%2B4azokkii2fPHnCGL3vA9LYUQ%2FdoLrA0F9ywT18LXdTB2dBxRoephdCsf2osMkr9iy26%2FAc%3D

# from replit import clear
# HINT: You can call clear() to clear the output in the console.

from blind_auction_logo import logo
from os import system, name

# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)

no_answer = False
bids = {}

while not no_answer:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\nf").lower()
    if should_continue == "no":
        no_answer = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

# My answer was to do price (bid) as a key and name as a value and then print a max price and name for it
# bids[price] = name
# print(f"The winner is {max(bids[price])} with a bid of ${max(bids)}")
