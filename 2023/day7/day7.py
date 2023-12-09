
import os
from collections import defaultdict


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example", "input"]:

    def pt1_pt2(is_part_1=False):
        stuff = [l.split() for l in read_input_lines(_input)]

        bids = dict()
        for hand, bid in stuff:
            bids[hand] = int(bid)

        card_weight = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".replace(
            ',', '').split() if is_part_1 else "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".replace(
                ',', '').split()
        card_weight.reverse()
        card_weights = {k: v for v, k in enumerate(card_weight)}

        def get_hand_type(hand: str):
            if not is_part_1:
                # Replace all 'J' with value of highest card count
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

            hand_types = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]
            count_per_card = defaultdict(int)
            for card in hand:
                count_per_card[card] += 1
            for idx, hand_type in enumerate(hand_types):
                rank = idx + 1
                if hand_type == sorted(list(count_per_card.values())):
                    return rank
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

        def sort_by_hand_type():
            hands_by_hand_type = defaultdict(list)
            for hand, _ in stuff:
                hands_by_hand_type[get_hand_type(hand)].append(hand)
            d = dict()
            for hand_type, hands in hands_by_hand_type.items():
                hands_sorted = hands
                for i in range(len(hands[0])):
                    hands_sorted = sorted(hands, key=lambda hand: card_weights[hand[i]])
                d[hand_type] = hands_sorted
            hands = []
            for k in reversed(sorted(d.keys())):
                hands.append(d[k])
            return hands
        
        hands = sort_by_hand_type()

        i = 0
        total_cards_per_hand = len(stuff[0][0])
        for i in range(0, total_cards_per_hand):
            hands = sort_by_card_weight(i, hands)
            i += 1

        # Calculate the answer based on rank and bid
        ans = 0
        for idx, _hands in enumerate(hands):
            ans += (idx+1)*bids[_hands[0]]
        print("pt1" if is_part_1 else "pt2", _input, ans)

    pt1_pt2(is_part_1=True)
    pt1_pt2(is_part_1=False)
