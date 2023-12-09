
import os
from collections import defaultdict


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example", "input"]:

    def pt1():
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

        def sortt(i, groups):
            more_sorting_to_do = False
            result = []
            for group in groups:
                if len(group) == 1:
                    result.append(group)
                    continue
                _sorted = sorted(
                    group, key=lambda hand: card_weights[hand[i]])
                prev = _sorted[0][i]
                g = [_sorted[0]]
                for hand in _sorted[1:]:
                    if prev != hand[i]:
                        result.append(g)
                        g = [hand]
                    else:
                        more_sorting_to_do = True
                        g.append(hand)
                    prev = hand[i]
                if g:
                    result.append(g)
            return result, more_sorting_to_do

        d = defaultdict(list)
        for hand, bid in stuff:
            d[get_hand_type(hand)].append(hand)
        # print(d)
        d_2 = dict()
        for k, hands in d.items():
            hands_sorted = hands
            for i in range(len(hands[0])):
                # print('hands_sorted', hands_sorted)
                hands_sorted = sorted(
                    hands, key=lambda hand: card_weights[hand[i]])
            d_2[k] = hands_sorted
        # print(d_2)

        r = []
        ks = sorted(d_2.keys())
        ks.reverse()
        for k in ks:
            r.append(d_2[k])
        # print(r)

        more_sorting_to_do = True
        i = 0
        rr = r
        while more_sorting_to_do or i == 5:
            rr, more_sorting_to_do = sortt(i, rr)
            i += 1
        # print('rr', rr)

        ans = 0
        for idx, r in enumerate(rr):
            # print('math', r[0], (idx+1), '*', bids[r[0]])
            ans += (idx+1)*bids[r[0]]
        print("pt1", _input, ans)

    pt1()

    def pt2():
        stuff = [l.split() for l in read_input_lines(_input)]

        bids = dict()
        for hand, bid in stuff:
            bids[hand] = int(bid)

        card_weight = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".replace(
            ',', '').split()
        card_weight.reverse()
        card_weights = {k: v for v, k in enumerate(card_weight)}

        def get_hand_type(hand: str):
            d = defaultdict(int)
            for card in hand:
                if card != 'J':
                    d[card] += 1
            if 'J' in hand:
                vs = sorted(d.values())
                vs.reverse()
                def get_top_letter():
                    for k, v in d.items():
                        if v == vs[0]:
                            return k
                    return None
                top_letter = get_top_letter()
                if top_letter:
                    hand = hand.replace('J', top_letter)

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
    

        def sort_by_card_weight(i, groups):
            result = []
            for group in groups:
                if len(group) == 1:
                    result.append(group)
                    continue
                _sorted = sorted(
                    group, key=lambda hand: card_weights[hand[i]])
                prev = _sorted[0][i]
                g = [_sorted[0]]
                for hand in _sorted[1:]:
                    if prev != hand[i]:
                        result.append(g)
                        g = [hand]
                    else:
                        g.append(hand)
                    prev = hand[i]
                if g:
                    result.append(g)
            return result

        d = defaultdict(list)
        for hand, _ in stuff:
            d[get_hand_type(hand)].append(hand)
        d_2 = dict()
        for k, hands in d.items():
            hands_sorted = hands
            for i in range(len(hands[0])):
                hands_sorted = sorted(
                    hands, key=lambda hand: card_weights[hand[i]])
            d_2[k] = hands_sorted

        r = []
        ks = sorted(d_2.keys())
        ks.reverse()
        for k in ks:
            r.append(d_2[k])

        i = 0
        rr = r
        while i != 5:
            rr = sort_by_card_weight(i, rr)
            i += 1

        ans = 0
        for idx, r in enumerate(rr):
            ans += (idx+1)*bids[r[0]]
        print("pt2", _input, ans)

    pt2()

"""
pt1 input_example 6440
pt2 input_example 5905
pt1 input 253910319
pt2 input 254083736
"""
