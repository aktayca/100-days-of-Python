from art import logo
print("\n")
print(logo)
print("Welcome to the auction!\n")
again= "yes"
bids = {}
# max_bid = 0
# max_bidder = ""
# def highest_bid():
#     global max_bidder
#     global max_bid
#     for key in bids:
#         if bids[key] > max_bid:
#             max_bid = bids[key]
#             max_bidder = key
#
while again.lower() == "yes":
    name = input("What's your name?: \n")
    bid = int(input("What's your bid?: \n"))
    bids[name] = bid
    again = input("Type 'yes' if there are other bidders.: \n")
# highest_bid()
# print(f"The winner of the auction is {max_bidder.title()} with $(max_bid}")
winner = max(bids, key=bids.get)
winning_bid = bids[winner]
print(f"The winner of the auction is {winner.title()} with ${winning_bid}.")