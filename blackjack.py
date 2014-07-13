from random import shuffle

## Assumptions: The card deck will be reloaded only if it's used up


#Divide 4 patterns into different numbers ex 1-13 for spade 14-26 for heart
#So sould apply module beforeing adding the number
def Initial_stack():
    p = range(1, 53)
    shuffle(p)
    return p


def Distribute_the_card(card_stack, target):
    if(len(card_stack) == 0):
        card_stack = Initial_stack()
    target.append(card_stack.pop())
    return card_stack, target


def count_points(player_stack):
    stack = [x % 13 if ((x % 13) > 0 and (x % 13) < 10) else 10
             for x in player_stack]
    points = sum(stack)
    if (1 in stack and (points + 10) <= 21):
        points = points + 10
    return points


def print_status(cards):
    print("Your hand holds: ")
    for x in cards:
        print x, ", "


def decode_cards(cards):
    return [x % 13 if (x % 13) > 0 else 13 for x in cards]


def Distribute_first_two_cards(cards):
    player_cards = []
    dealer_cards = []
    cards, player_cards = Distribute_the_card(cards, player_cards)
    cards, player_cards = Distribute_the_card(cards, player_cards)
    cards, dealer_cards = Distribute_the_card(cards, dealer_cards)
    cards, dealer_cards = Distribute_the_card(cards, dealer_cards)
    return player_cards, dealer_cards, cards


game_continue = True
chips = 100
cards = Initial_stack()

while(game_continue):

    print ("You have chips : ", chips)
    chip_bet = raw_input("How many chips do you want to bet? \
(Answer an integer and smaller than the chips you \
have, or we will assume you to bet 1) ")

    try:
        chip_bet = int(chip_bet)
        if (chip_bet > chips):
            chip_bet = 1
    except:
        chip_bet = 1

    chips = chips - chip_bet

    player_stack, dealer_stack, cards = Distribute_first_two_cards(cards)
    not_endding = True
    player_points = count_points(player_stack)

    while(not_endding):

        while(True):
            print "Here is your current hand and points : ", \
                  decode_cards(player_stack), " ", \
                  player_points

            action = raw_input("Please take one of the following actions: \
H(hit), S(stand): ")

            if(action == "H"):
                cards, player_stack = Distribute_the_card(cards, player_stack)
                player_points = count_points(player_stack)
                if(player_points > 21):
                    player_points = count_points(player_stack)
                    not_endding = False
                    break
                else:
                    pass
            elif (action == "S"):
                not_endding = False
                break
            else:
                print "You type wrong action, please choose again!"

    while (count_points(dealer_stack) < 17):
        cards, dealer_stack = Distribute_the_card(cards, dealer_stack)

    dealer_points = count_points(dealer_stack)

    print "Your cards and points: ", decode_cards(player_stack), " ", \
          player_points, " Dealer's cards and points: ", \
          decode_cards(dealer_stack), " ", dealer_points

    if ((dealer_points > 21 and player_points <= 21)
       or (player_points > dealer_points and player_points <= 21)):
        result = "W"
    else:
        result = "L"

    if(result == "W"):
        print("You win!")
        chips = chips + chip_bet*2
    else:
        print "You lose"

    if(chips == 0):
        print "You lose all chips :("
        game_continue = False
    else:
        ask = raw_input("Press N to quit the game or \
any other button to continue")
        if(ask == "N"):
            game_continue = False
