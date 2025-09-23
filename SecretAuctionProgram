def find_highest_bidder(bidder_dictionary):
    winner = " "
    highest_bidder  = 0

    max(bidder_dictionary)

    for bidder in bidder_dictionary:
        bid_amount = bidder_dictionary[bidder] 
        if bid_amount > highest_bidder:
            highest_bid = bid_amount
            winner = bidder   

    print(f"The winner is {winner} with a bid of ${highest_bid}.")  

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidder? Type 'Yes' or 'no'. \n")
    
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "Yes":
       print("\n" * 20)

          

