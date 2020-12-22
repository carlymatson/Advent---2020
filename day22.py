file = open("day22input.text", 'r')
file_lines = file.readlines()
num_cards = int((len(file_lines) - 3)/2)
deck1 = [int(n) for n in file_lines[1:1+num_cards]]
deck2 = [int(n) for n in file_lines[num_cards+3:]]

def play_round():
    global deck1, deck2
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1.extend([card1, card2])
    else:
        deck2.extend([card2, card1])
    return True

def get_deck_score(deck):
    score = 0
    num_cards = len(deck)
    for i in range(num_cards):
        score += (num_cards - i)*deck[i]
    return score

def play_combat():
    global deck1, deck2
    while len(deck1)>0 and len(deck2)>0:
        play_round()
    if len(deck2) == 0:
        winner = 1
    else:
        winner = 2
    return winner

def play_recursive_combat(deck1, deck2):
    history = set()
    turn_counter = 0
    winner = 1
    while len(deck1) > 0 and len(deck2) > 0:
        deck_state = str(deck1) + str(deck2)
        if deck_state in history:
            return winner
        history.add(deck_state)
        turn_counter += 1
        # Play a round.
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        round_winner = 0
        if (card1 <= len(deck1)) and (card2 <= len(deck2)):
            #print("Sub game")
            round_winner = play_recursive_combat(deck1[:card1], deck2[:card2])
        elif card1 > card2:
            round_winner = 1
        else:
            round_winner = 2
        if round_winner == 1:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
        if turn_counter % 1000 == 0:
            print("-- Round %d --"%(turn_counter))
            print(deck1)
            print(deck2)
    if len(deck1) == 0:
        winner = 2
    return winner


def part_1_and_2():
    #winner = play_combat()
    winner = play_recursive_combat(deck1, deck2)
    if winner == 1:
        winning_deck = deck1
    else:
        winning_deck = deck2
    return get_deck_score(winning_deck)

print("Score: %d"%(part_1_and_2()))
