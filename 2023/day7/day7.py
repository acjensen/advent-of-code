
import os
from collections import defaultdict


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example"]:
    lines = read_input_lines(_input)
    stuff = [l.split() for l in lines]

    bids = dict()
    for hand, bid in stuff:
        bids[hand] = int(bid)

    card_weight = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".replace(
        ',', '').split()
    card_weight.reverse()

    card_weights = {k: v for v, k in enumerate(card_weight)}

    def get_hand_type(hand):
        d = defaultdict(int)
        for card in hand:
            d[card] += 1
        if [5] == sorted(list(d.values())):
            return 1
        elif [1, 4] == sorted(list(d.values())):
            return 2
        elif [2, 3] == sorted(list(d.values())):
            return 3
        elif [1, 1, 3] == sorted(list(d.values())):
            return 4
        elif [1, 2, 2] == sorted(list(d.values())):
            return 5
        elif [1, 1, 1, 2] == sorted(list(d.values())):
            return 6
        elif [1, 1, 1, 1, 1] == sorted(list(d.values())):
            return 7
        return None

    # print(get_hand_type('AAAAA'))
    # print(get_hand_type('AABAA'))
    # print(get_hand_type('23332'))
    # print(get_hand_type('TTT98'))
    # print(get_hand_type('23432'))
    # print(get_hand_type('A23A4'))
    # print(get_hand_type('23456'))

    def pt1():
        ans = 0
        d = defaultdict(list)
        for hand, bid in stuff:
            d[get_hand_type(hand)].append(hand)
        print(d)
        d_2 = dict()
        for k, hands in d.items():
            hands_sorted = hands
            for i in range(len(hands[0])):
                print('hands_sorted', hands_sorted)
                hands_sorted = sorted(
                    hands, key=lambda hand: card_weights[hand[i]])
            d_2[k] = hands_sorted
        print(d_2)

        ranked = []
        for x in range(0, 10):
            if x in d_2.keys():
                ranked.extend(d_2[x])
        ranked.reverse()
        print(ranked)
        ans = 0
        for idx, r in enumerate(ranked):
            print('math', r, (idx+1), '*', bids[r])
            ans += (idx+1)*bids[r]
        print("pt1", _input, ans)
    pt1()

    def pt2():
        ans = None
        print("pt2", _input, ans)
    pt2()
