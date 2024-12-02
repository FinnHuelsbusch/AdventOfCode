from enum import Enum
class hand_type(Enum):
    high_card = 1
    one_pair = 2
    two_pairs = 3
    three_of_a_kind = 4
    full_house = 5
    four_of_a_kind = 6
    five_of_a_kind = 7


    


class hand: 
    def __init__(self, card_string, bit_value):
        # Split the string into a list of characters
        self.bit_value = bit_value
        self.cards_original = list(card_string)
        if 'J' in card_string:
            # Replace all Js with the most common card in the hand that is not a J
            most_common_card = max(set(card_string.replace('J',"0")), key=card_string.count)
            if most_common_card == '0':
                card_string = "AAAAA"
            else:
                card_string = card_string.replace('J', most_common_card)
        self.cards = list(card_string)
        assert len(self.cards) == 5, "Invalid hand"
        # determine if cards are all the same 
        if len(set(self.cards)) == 1:
            self.type = hand_type.five_of_a_kind
        # determine if cards are four of a kind or full house
        elif len(set(self.cards)) == 2:
            if self.cards.count(self.cards[0]) == 4 or self.cards.count(self.cards[0]) == 1:
                self.type = hand_type.four_of_a_kind
            else:
                self.type = hand_type.full_house
        # determine if cards are three of a kind or two pairs
        elif len(set(self.cards)) == 3:
            card_set = list(set(self.cards))
            if self.cards.count(card_set[0]) == 3 or self.cards.count(card_set[1]) == 3 or self.cards.count(card_set[2]) == 3:
                self.type = hand_type.three_of_a_kind
            else:
                self.type = hand_type.two_pairs
        # determine if cards are one pair or high card
        elif len(set(self.cards)) == 4:
            self.type = hand_type.one_pair
        else:
            self.type = hand_type.high_card

        self.cards = self.cards_original
    
    def __gt__(self, other):
        # If the hands are of different types, the one with the higher type wins
        if self.type.value > other.type.value:
            return True
        elif self.type.value < other.type.value:
            return False
        # If the hands are of the same type, the one with the higher card wins
        else:
            for i in range(5):
                # digits are less than letters
                # lower digits are less than higher digits
                # A, K, Q, J, T are the letters from highest to lowest
                
                # If the cards are the same, continue to the next card
                if self.cards[i] == other.cards[i]:
                    continue
                # If the cards are different, compare them
                else:
                    if self.cards[i].isalpha() and self.cards[i] == 'J':
                        return False
                    elif other.cards[i].isalpha() and other.cards[i] == 'J':
                        return True
                    elif self.cards[i].isdigit() and other.cards[i].isdigit():
                        return self.cards[i] > other.cards[i]
                    elif self.cards[i].isdigit() and other.cards[i].isalpha():
                        return False
                    elif self.cards[i].isalpha() and other.cards[i].isdigit():
                        return True
                    else:
                        if self.cards[i] == "A" and other.cards[i] != "A":
                            return True
                        elif self.cards[i] != "A" and other.cards[i] == "A":
                            return False
                        elif self.cards[i] == "K" and other.cards[i] != "K":
                            return True
                        elif self.cards[i] != "K" and other.cards[i] == "K":
                            return False
                        elif self.cards[i] == "Q" and other.cards[i] != "Q":
                            return True
                        elif self.cards[i] != "Q" and other.cards[i] == "Q":
                            return False
                        elif self.cards[i] == "J" and other.cards[i] != "J":
                            return True
                        elif self.cards[i] != "J" and other.cards[i] == "J":
                            return False
                        elif self.cards[i] == "T" and other.cards[i] != "T":
                            return True
                        elif self.cards[i] != "T" and other.cards[i] == "T":
                            return False
                        
            # If all cards are the same, use the bit value to determine the winner
            return int(self.bit_value) > int(other.bit_value)
    
    def __lt__(self, other):
        return not self.__gt__(other)
    
    def __eq__(self, other):
        return not self.__gt__(other) and not self.__lt__(other)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __repr__(self):
        return f"{''.join(self.cards)} {self.type} {self.bit_value}"
    
try: 
    with open("./Day7/input.txt") as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print("File input.txt not found")
else:
    hands = []
    for line in lines: 
        current_hand, bit_value = line.strip().split(" ")
        current_hand = hand(current_hand, bit_value)
        hands.append(current_hand)
    hands.sort()
    total_sum = 0
    for index, current_hand in enumerate(hands):
        print(current_hand)
        total_sum += (index + 1) * int(current_hand.bit_value)
    print(total_sum)
        