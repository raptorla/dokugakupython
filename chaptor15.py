from random import shuffle

class Card:
    suits_list = ["spades", "hearts", "diamonds", "clubs"]

    values_list = ["None", "None", "2", "3", "4", "5", "6", "7", "8", "9",
                   "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else: 
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else: 
                return False
        return False

    def __repr__(self):
        v = self.values_list[self.value] + " of " \
        + self.suits_list[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards_list = []
        for i in range(2, 15):
            for j in range(4):
                self.cards_list.append(Card(i, j))
        shuffle(self.cards_list)
            
    def remove_card(self):
        if len(self.cards_list) == 0:
            return
        return self.cards_list.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前:")
        name2 = input("プレーヤー2の名前:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは {} が勝ちました".format(winner)
        print(w)

    def draw(self, p1name, p1card, p2name, p2card):
        d = "{}は{}、{}は{}を引きました".format(p1name, p1card, p2name, p2card)
        print(d)

    def play_game(self):
        cards = self.deck.cards_list
        print("Start war!")
        while len(cards) >= 2:
            m = "quit to q, or other keys to play"
            response = input(m)
            if response == "q":
                break
            p1card = self.deck.remove_card()
            p2card = self.deck.remove_card()
            p1name = self.p1.name
            p2name = self.p2.name

            self.draw(p1name, p1card, p2name, p2card)

            if p1card > p2card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 10
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"

game = Game()
game.play_game()