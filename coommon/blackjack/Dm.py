import random

def build_boaed():
    lists=[]
    num = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
    for face in num:
        for _ in range(4):
            lists.append((face,num[face]))
    return lists

class Player:
    def __init__(self,name,board):
        self.name = name
        self.hand = []
        self.points = 0
        self.is_bust = False
        self.is_stand = False
        self.board = board

    def add_card(self, card):
        self.hand.append(card)
        face, value = card
        self.points += value
        self.point()
        return

    def point(self):
        while self.points > 21:
            has_ace = False
            for i, card in enumerate(self.hand):
                face, value = card
                if face == 'A' and value == 11:
                    self.points -= 10
                    self.hand[i] = (face, 1)
                    has_ace = True
                    break
            if not has_ace:
                self.is_bust = True
                break

    def show(self):
        card_faces = [card[0] for card in self.hand]
        print(f'【{self.name}】手牌：{card_faces}  | 点数：{self.points}')


    def touch(self):
        print(f"\n========== 【{self.name}】的回合 ==========")
        while not self.is_bust and not self.is_stand:
            self.show()
            i = input('是否继续要牌？(Y/N)：').strip().upper()
            if i == 'N':
                self.is_stand = True
                print(f"【{self.name}】选择停牌！")
                break
            elif i == 'Y':
                self.board.deal_card(self)
                if self.is_bust:
                    print(f'【{self.name}】爆牌啦！游戏结束！')
                    self.show()
                    break
                self.show()
            else:
                print('输入错误，请输入 Y 或 N！')


# noinspection PyBroadException
class Board:
    def __init__(self):
        self.deck = build_boaed()
        random.shuffle(self.deck)
        self.players = []
        self.dealer = Player('dealer',self)

    def create_players(self):
        while True:
            try:
                count = int(input("请输入玩家数量（1-4人）："))
                if 1 <= count <= 4:
                    break
                else:
                    print("请输入1~4之间的数字！")
            except:
                print("输入无效，请输入数字！")
        for i in range(1, count + 1):
            name = f"玩家{i}"
            self.players.append(Player(name, self))

    def deal_card(self,target_player):
        if not self.deck:
            print('board is empty')
            return
        card = self.deck.pop()
        target_player.add_card(card)

    def start_deal(self):
        print("\n========== 开始发牌 ==========")
        for _ in range(2):
            for p in self.players:
                self.deal_card(p)
        for _ in range(2):
            self.deal_card(self.dealer)
        print("发牌完成！")

    def depart_play(self):
        print("\n========== 庄家回合 ==========")
        while not self.dealer.is_bust and self.dealer.points <17:
            self.deal_card(self.dealer)
        if self.dealer.points > 21:
            self.dealer.is_bust = True
        print(f"庄家最终点数：{self.dealer.points}")

    def start_game(self):
        print("==================== 欢迎来到 21点游戏 ====================")
        self.create_players()
        self.start_deal()
        for player in self.players:
            player.touch()
        all_bust = all(p.is_bust for p in self.players)
        if all_bust:
            print("\n所有玩家都爆牌了，庄家直接获胜！")
            return
        self.depart_play()
        self.judge()


    def judge(self):
        print("\n========== 最终结果 ==========")
        print(f"庄家手牌：{self.dealer.hand}，最终点数：{self.dealer.points}")
        for player in self.players:
            print(f"\n{player.name}手牌：{player.hand}，最终点数：{player.points}")
            if player.is_bust:
                print(f"❌ {player.name} 爆牌，庄家获胜！")
            elif self.dealer.is_bust:
                print(f"✅ {player.name} 获胜！庄家爆牌！")
            elif player.points > self.dealer.points:
                print(f"✅ {player.name} 点数更大，获胜！")
            elif player.points < self.dealer.points:
                print(f"❌ {player.name} 点数更小，庄家获胜！")
            else:
                print(f"🤝 {player.name} 与庄家平局！")

if __name__ == "__main__":
    game = Board()
    game.start_game()