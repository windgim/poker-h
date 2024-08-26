import random

class deck:
    def __init__(self):
        pass

    def deck():
        suits = ["♠️", "♥️", "♦️", "♣️"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        deck = []
        
        for i in suits:
            for j in ranks:
                deck.append(i+j)

        return deck

    def hand(deck):
        hand = []

        for i in range(2):
            hand.append(random.choice(deck))

        return hand

    def board(deck, num_board):
        board = []

        for i in range(num_board):
            board.append(random.choice(deck))

        return board

    def print_cards(cards):
        return ', '.join(map(str, cards))

class check_hand:
    def __init__(self):
        pass

    def combos(hand, board):
        #suits
        diamonds = 0
        clubs = 0
        spades = 0
        hearts = 0

        #combos
        global over_cards
        global pair
        global set_hand
        global straight
        global oesd
        global flush
        global four
        global royal_flush
        pair = False
        set_hand = False
        straight = False
        oesd = False
        flush = False
        four = False
        royal_flush_flush = False
        royal_flush_straight = False
        
        #checking variables
        identical_cards = 0
        full_house_check_set = 0
        full_house_check_pair = 0
        two_pairs_check_num = 0
        over_card = 0
        over_cards = 0
        num_of_straight = 0
        straight_check_list = []
        royal_flush_d = []
        royal_flush_c = []
        royal_flush_s = []
        royal_flush_h = []

        #check hand
        for i in board + hand:
            #list for ranks
            straight_check_list.append(i[2])
    
            #check flush
            if i[0] == '♦️'[0]:
                diamonds += 1

                if i[2] == "1" or i[2] == "J" or i[2] == "Q" or i[2] == "K" or i[2] == "A":
                    if royal_flush_d.count(i[2]) == 0:
                        royal_flush_d.append(i[2])

            elif i[0] == '♠️'[0]:
                clubs += 1

                if i[2] == "1" or i[2] == "J" or i[2] == "Q" or i[2] == "K" or i[2] == "A":
                    if royal_flush_c.count(i[2]) == 0:
                        royal_flush_c.append(i[2]) 

            elif i[0] == '♣️'[0]:
                spades += 1

                if i[2] == "1" or i[2] == "J" or i[2] == "Q" or i[2] == "K" or i[2] == "A":
                    if royal_flush_s.count(i[2]) == 0:
                        royal_flush_s.append(i[2])

            elif i[0] == '♥️'[0]:
                hearts += 1

                if i[2] == "1" or i[2] == "J" or i[2] == "Q" or i[2] == "K" or i[2] == "A":
                    if royal_flush_h.count(i[2]) == 0:
                        royal_flush_h.append(i[2])

            if len(royal_flush_d) == 5 or len(royal_flush_c) == 5 or len(royal_flush_s) == 5 or len(royal_flush_h) == 5:
                royal_flush_flush = True

            elif diamonds >= 5 or clubs >= 5 or spades >= 5 or hearts >= 5:
                flush = True 
    
            card = i[2]
            for j in board + hand:
                if card == j[2]:
                    identical_cards += 1
    
                    #check pairs
                    if identical_cards == 2:
                        pair = True
                        two_pairs_check_num += 1
    
                        #full house check No. 1
                        if full_house_check_pair == full_house_check_set:
                            full_house_check_pair = j[2]
    
                    #check set
                    elif identical_cards == 3:
                        set_hand = True
    
                        #full house check No. 2
                        full_house_check_set = j[2]
    
                    #check four of a kind
                    elif identical_cards == 4:
                        four = True
    
            #update
            identical_cards = 0
    
        #change rank list
        for i in range(len(straight_check_list)):
            if straight_check_list[i] == '1':
                straight_check_list[i] = '10'
        
            elif straight_check_list[i] == 'J':
                straight_check_list[i] = '11'
        
            elif straight_check_list[i] == 'Q':
                straight_check_list[i] = '12'
        
            elif straight_check_list[i] == 'K':
                straight_check_list[i] = '13'
        
            elif straight_check_list[i] == 'A':
                straight_check_list[i] = '14'
        
        #sort rank list
        straight_check_list = [int(i) for i in straight_check_list]
        straight_check_list = set(straight_check_list)
        straight_check_list = sorted(straight_check_list)
        
        #check straight
        for i in straight_check_list:
            straight_check_num = i
            straight_check = 0
    
            for j in straight_check_list:
                if j - straight_check == straight_check_num:
                    straight_check += 1
    
            if straight_check >= 5:
                straight = True
                num_of_straight += 1
    
                #check oesd
                if num_of_straight == 6:
                    oesd = True
                
                #check royal flush
                if j == 14:
                    royal_flush_straight = True
    
                break
    
        #check over cards
        for i in hand:
            for j in board:
                if i[2] > j[2]:
                    over_card += 1 
            if over_card == len(board):
                over_cards += 1

        #check combos
        if royal_flush_flush and royal_flush_straight:
            return 'Роял-флеш'
    
        elif straight and flush:
            return 'Стрит-флеш'
    
        elif four:
            return 'Каре'
    
        elif set_hand and pair and full_house_check_pair != full_house_check_set:
            return 'Фулл хаус'
    
        elif flush:
            return 'Флеш'
    
        elif straight:
            return 'Стрит'
    
        elif set_hand:
            return 'Тройка'
    
        elif two_pairs_check_num // 2 == 2:
            return '2 пары'
    
        elif two_pairs_check_num // 2 > 2:
            return '2 пары (3 пары)'
    
        elif pair:
            return 'Пара'
    
        elif over_cards > 0:
            if over_cards == 1:
                return '1 Оверкарта'
    
            else:
                return '2 Оверкарты'
    
        else:
            return 'Старшая карта'
    
    def outs():
        outs = 0
    
        if oesd and flush and over_cards == 2:
            outs = 21
    
        elif oesd and flush:
            outs = 15
    
        elif flush and over_cards == 2:
            outs = 15
    
        elif oesd and over_cards == 2:
            outs = 14
    
        elif straight and flush:
            outs = 12
    
        elif flush and over_cards == 1:
            outs = 12 
    
        elif oesd and over_cards == 1:
            outs = 11
    
        elif straight and over_cards == 2:
            outs = 10
    
        elif flush:
            outs = 9
    
        elif oesd:
            outs == 8
    
        elif straight and over_cards == 1:
            outs = 7
    
        elif over_cards == 2:
            outs = 6
    
        elif straight:
            outs = 4
    
        elif over_cards == 1:
            outs = 3
    
        return outs