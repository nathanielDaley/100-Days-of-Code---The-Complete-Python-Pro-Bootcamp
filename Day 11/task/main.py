import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    """returns a random card from the deck"""
    return random.choice(cards)

def show_player_cards():
    """displays the player's current hand"""
    print("You have a(n) ", end="")

    for index in range(len(player_hand) - 1):
        print(f"{player_hand[index]} and a(n) ", end="")

    print(f"{player_hand[len(player_hand) - 1]}.")

def show_computer_cards(hidden):
    """displays the computer's current hand"""
    print("The computer has a(n) ", end="")

    for index in range(len(computer_hand) - 1):
        print(f"{computer_hand[index]} and a(n) ", end="")
    if hidden:
        print("hidden card.")
    else:
        print(f"{computer_hand[len(computer_hand) - 1]}.")

def show_player_sum(sum_to_show):
    """displays the player's score"""
    if sum_to_show == 0:
        print("You have a blackjack!")
    else:
        print(f"You have a total of {player_sum}.")

def show_computer_sum(sum_to_show):
    """displays the computer's score"""
    if sum_to_show == 0:
        print("The computer has a blackjack!")
    else:
        print(f"The computer has a total of {computer_sum}.")

def calc_hand_sum(hand):
    """returns the score(int) of the provided hand(array of ints)"""
    hand_sum_with_elevens = 0
    hand_sum_with_ones = 0
    for card in hand:
        if card == 11:
            hand_sum_with_elevens += 11
            hand_sum_with_ones += 1
        else:
            hand_sum_with_elevens += card
            hand_sum_with_ones += card

    if hand_sum_with_elevens == 21 and len(hand) == 2:
        return 0
    if hand_sum_with_elevens > 21:
        return hand_sum_with_ones
    return hand_sum_with_elevens


computer_hand = [draw_card(), draw_card()]
player_hand = [draw_card(), draw_card()]
computer_sum = 14
player_sum = 13
computer_hand_hidden = True

print(logo)

playing = "yes"
while playing == "yes":
    show_computer_cards(computer_hand_hidden)
    show_player_cards()
    show_player_sum(player_sum)

    player_drawing = ""
    if player_sum == 0:
        player_drawing = "no"
    else:
        player_drawing = "yes"
    while player_drawing == "yes":
        player_drawing = input("Would you like to draw another card? \"Yes\" or \"No\": ").lower()
        if player_drawing == "yes":
            player_hand.append(draw_card())
            player_sum = calc_hand_sum(player_hand)
            show_computer_cards(computer_hand_hidden)
            show_player_cards()
            show_player_sum(player_sum)

            if player_sum > 21:
                player_drawing = "no"

    computer_hand_hidden = False
    show_computer_cards(computer_hand_hidden)
    show_computer_sum(computer_sum)
    if not (player_sum == 0 or computer_sum == 0):
        while computer_sum < 17 and player_sum < 21:
            print("The computer draws a card")
            computer_hand.append(draw_card())
            computer_sum = calc_hand_sum(computer_hand)
            show_computer_cards(computer_hand_hidden)
            show_computer_sum(computer_sum)

    if player_sum == 0 and not computer_sum == 0:
        print("You win!")
    elif not player_sum == 0 and computer_sum == 0:
        print("You lose!")
    elif player_sum == computer_sum:
        print("It's a draw!")
    elif player_sum > computer_sum and player_sum <= 21 or computer_sum > 21:
        print("You win!")
    else:
        print("You lose!")

    playing = input("Would you like to play again? \"Yes\" or \"No\": ").lower()

    if playing == "yes":
        computer_hand = [draw_card(), draw_card()]
        player_hand = [draw_card(), draw_card()]
        player_sum = calc_hand_sum(player_hand)
        computer_sum = calc_hand_sum(computer_hand)
        computer_hand_hidden = True
