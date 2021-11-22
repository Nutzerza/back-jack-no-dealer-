#ใกล้ 21 มากสุดชนะ เกิน 21 แพ้
import random

class Deck:
    def __init__(self):
        self.pack = []
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        group = ["♣","♦","♥","♠"]    
        for n in number:
            for g in group:
                self.pack.append(n+g)
        random.shuffle(self.pack)

    def give_card(self):
        give = self.pack[0]
        self.pack.pop(0)
        return give

class Player:
    def __init__(self, cards):
        self.card_on_hand = cards
        print(self.card_on_hand)

    def choose_stand_hit(self):
        for r in range(3):
            user_choose = input("What will you choose.(Hit/ Stand) !!!Only 3 times!!! : ")
            if user_choose == "hit" or user_choose == "Hit":
                self.hit()
            if user_choose == "stand" or user_choose == "Stand":
                break

    def hit(self):
        self.card_on_hand.append(deck.give_card())
        print(self.card_on_hand)

    def calculate_point(self): #รวมคะแนนการ์ดบนมือ
        self.player_point = 0
        for card in self.card_on_hand:
            if card[:1] == "J" or card[:1] == "Q" or card[:1] == "K" or card[:2] == "10":
                self.player_point += 10
            elif card[:1] == "A":
                user_A_card = int(input("How much point A Card(1/11) : "))
                if user_A_card == 1:
                    self.player_point += 1
                if user_A_card == 11:
                    self.player_point += 11
            else:
                self.player_point += int(card[:1])

    def check_bust(self):
        if self.player_point > 21:
            return "You Bust"
        if self.player_point <= 21:
            return self.player_point

deck = Deck()
print("player1")
player1 = Player([deck.give_card(), deck.give_card()]) #เพิ่มผู้เล่น
print("player2")
player2 = Player([deck.give_card(), deck.give_card()])
print("player3")
player3 = Player([deck.give_card(), deck.give_card()])
print("player1")
player1.choose_stand_hit(), player1.calculate_point()
print("player2")
player2.choose_stand_hit(), player2.calculate_point()
print("player3")
player3.choose_stand_hit(), player3.calculate_point()

point_or_bust = [player1.check_bust(), player2.check_bust(), player3.check_bust()]
point = []
for p in range(len(point_or_bust)):
    if point_or_bust[p] == "You Bust":
        print("player"+str(p+1)+point_or_bust[p])
    elif type(point_or_bust[p]) == int:
        point.append(str(point_or_bust[p])+" is the point of player"+str(p+1))
point.sort(reverse=True)
print("Result is : ")
print(point[0][18:27]+" Winnn")