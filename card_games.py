from deck_of_cards import Card, Deck
from chips import Chip, ChipPurchase

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self._chips = []

    @property
    def chips(self):
        colors = ["black", "green", "red", "white"]

        chip_colors = [chip.color for chip in self._chips]

        chip_color_count = {color:chip_colors.count(color) for color in colors}

        return chip_color_count

    def add_chips(self, cash):
        self._chips.extend(ChipPurchase.chip_set(cash) ) 

    def check_card_in_hand(self):
        for card in self.hand:
            yield card

    def __repr__(self):
        return f"Player Name: {self.name} \nChips: {self.chips}"

class Game:
    def __init__(self, players = []):
        self.players = players
        self.deck = Deck()
        self.deck.shuffle()

    def add_player(self, player):
        if not isinstance(player, Player):
            raise Exception("You have to be a player in order to join a game")

        self.players.append(player)
        return f"{player.name} has joined the game"

    def deal_players(self, num):
        for player in self.players:
            player.hand = self.deck.deal_hand(num)

    def clear_hand(self):
        for player in self.players:
            player.hand.clear()

        self.deck = Deck()
        self.deck.shuffle()

    def __repr__(self):
        return '\n'.join(f"Name: {player.name}" for player in self.players)

class Blackjack(Game):

    dealer = Player("Dealer")

    def __init__(self, players = []):
        super().__init__(players)

    def hit(self, player):
        if player not in self.players and player.name != "Dealer":
            raise Exception(f"{player.name} is not in the game")
        elif self.check_hand_value(player) >= 21:
            raise Exception(f"{player.name} has 21 or over")

        player.hand.append(self.deck.deal_card() )

    def check_hand_value(self, player):
        special_values = dict(zip(["A", "J", "Q", "K"], [1, 10, 10, 10]))

        card_values = [
            int(card.value) if card.value not in ["A", "J", "Q", "K"] else special_values[card.value] for card in player.hand
            ]

        return sum(card_values)

    def __repr__(self):
        return ''.join(f"Player Name: {player.name} \nHand: {player.hand} \nValue: {self.check_hand_value(player)} \n\n" 
            for player in self.players)

    def dealers_play(self):
        Blackjack.dealer.hand = self.deck.deal_hand(2)

        while self.check_hand_value(Blackjack.dealer) <= 17:
            self.hit(Blackjack.dealer)

        if self.check_hand_value(Blackjack.dealer) > 21:
            return f"Dealer's Play \nHand: {Blackjack.dealer.hand} Value: {self.check_hand_value(Blackjack.dealer)} \nBUST!"

        return f"Dealer's Play \nHand: {Blackjack.dealer.hand} Value: {self.check_hand_value(Blackjack.dealer)}"

    def player_won(self):
        pass

class Poker_Rules:
    # pair
    def pair(self, cards):
        for i in cards:
            result = 0
            for j in cards:
                result += 1 if i.value == j.value else 0
                if (result == 2):
                    return True
        return False

    # triple
    def trio(self, cards):
        for i in cards:
            result = 0
            for j in cards:
                result += 1 if i.value == j.value else 0
                if (result == 3):
                    return True
        return False

    # straight
    def straight(self, cards):
        special_values = dict(zip(["A", "J", "Q", "K"], [1, 11, 12, 13]))

        card_values = [
            int(card.value) if card.value not in ["A", "J", "Q", "K"] else special_values[card.value] for card in cards
        ]

        card_values.sort()
        card_values = set(card_values)
        card_values = list(card_values)

        forward_straight = True

        reverse_straight = True

        w = 1

        while forward_straight and w < len(card_values):
            forward_straight = card_values[w] == card_values[w - 1] + 1
            w += 1

        r = len(card_values) - 2

        while reverse_straight and r >= 0:
            reverse_straight = card_values[r] == card_values[r + 1] - 1
            r -= 1

        return (forward_straight or reverse_straight) and len(card_values) >= 5

    # flush
    def flush(self, cards):
        card_suits = [card.suit for card in cards]

        diamonds = card_suits.count("diamonds") >= 5
        spades = card_suits.count("spades") >= 5
        hearts = card_suits.count("hearts") >= 5
        clubs = card_suits.count("clubs") >= 5

        return diamonds or spades or hearts or clubs

    # full house
    def full_house(self, cards):
        card_pair = None
        card_values = [card.value for card in cards]

        for card in card_values:
            if card_values.count(card) == 2:
                card_pair = card

        if card_pair:
            card_values.remove(card_pair)
            card_values.remove(card_pair)

            for i in card_values:
                result = 0
                for j in card_values:
                    result += 1 if i == j else 0
                    if result == 3:
                        return True

        return False

    # quad
    def quad(self, cards):
        for i in cards:
            result = 0
            for j in cards:
                result += 1 if i.value == j.value else 0
                if (result == 4):
                    return True
        return False

    # straight flush (It is flawed for now. It is going to work with 5 cards but not with 7 cards.)
    def straight_flush(self, cards):
        return self.straight(cards) and self.flush(cards)

    # royal flush (Same story as the straight flush)
    def royal_flush(self, cards):
        card_values = [card.value for card in cards]

        royalties = ["10", "J", "Q", "K", "A"]

        for royal in royalties:
            if royal not in card_values:
                return False

        return self.flush(cards)

class TexasHoldEmPoker(Game, Poker_Rules):
    pass

# cards = [Card("hearts", "10"), Card("hearts", "J"), Card("hearts", "Q"), Card("hearts", "K"), Card("hearts", "A")]
# cards = [Card("spades", str(val) ) for val in range(2, 6)]
# cards.insert(0, Card("spades", "A"))
# cards = [Card("hearts", "10"), Card("spades", "K"), Card("clubs", "10"), Card("hearts", "K"), Card("spades", "10")]

# poker = Poker_Rules()

# print(poker.straight_flush(cards))
# print(poker.quad(cards) )
# print(poker.full_house(cards))
# print(poker.royal_flush(cards))

player = Player("Lebron")

player.add_chips(572)

print(player)




