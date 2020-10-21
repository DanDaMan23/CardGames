from card_games import Player, Blackjack

player1 = Player("Dan")

blackjack = Blackjack()

join_game = input("Do you want to join the game? (y/n): ")
join_game = join_game.lower()

if join_game == "y":
    blackjack.add_player(player1)
    blackjack.deal_players(2)

print(blackjack)

hit = None

while blackjack.check_hand_value(player1) < 21 and hit != "n":
    hit = input("Hit? (y/n): ")
    hit = hit.lower()

    if hit == "y":
        blackjack.hit(player1)

    if blackjack.check_hand_value(player1) > 21:
        print(f"Player Name: {player1.name} \nHand: {player1.hand} \nValue: {blackjack.check_hand_value(player1)} \nBUST!!!")
    else:
        print(f"Player Name: {player1.name} \nHand: {player1.hand} \nValue: {blackjack.check_hand_value(player1)}")

