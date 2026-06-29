import random


logo = r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ┌─────────┐    ┌─────────┐    ┌─────────┐                                ║
║   │A        │    │K        │    │Q        │                                ║
║   │♠        │    │♣        │    │♥        │                                ║
║   │         │    │         │    │         │                                ║
║   │    ♠    │    │    ♣    │    │    ♥    │                                ║
║   │         │    │         │    │         │                                ║
║   │        ♠│    │        ♣│    │        ♥│                                ║
║   │        A│    │        K│    │        Q│                                ║
║   └─────────┘    └─────────┘    └─────────┘                                ║
║                                                                            ║
║██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗    ║
║██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝    ║
║██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝     ║
║██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗     ║
║██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗    ║
║╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ║
║                                                                            ║
║                    ♠  Beat the Dealer • Get 21!  ♥                         ║
║                           ♣      ♦                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""


# a=11
# queen=10
# king=10
# jack=10
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🤪"
    elif c_score == 0:
        return "Lose, opponent has a Blackjack 😢"
    elif u_score == 0:
        return "Yayy! you win with a Blackjack 🥳"
    elif u_score > 21:
        return "Lose,your score is over 21 😢"
    elif c_score > 21:
        return "Yayy! you win because oppnent score is above 21 😁"
    elif u_score > c_score:
        return "Yayy! you win with a with a higher score 🥳"
    else:
        return "You lose opponent defeated you with a higher score 😔"


def play_game():
    print(logo)
    user_card = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards :{user_card} \nYour score:{user_score}")
        print("-----------------------")
        print(f"Computer's first card :{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' if you want to draw another card and type 'n' if you want to pass.")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_card} and your final score: {user_score}.")
    print(f"Computer's cards {computer_cards} and computer's final score :{computer_score}.")
    print(compare(user_score, computer_score))

play_game()


while input("Do you want to restart the game(enter 'y' or 'n): ") == "y":
    print("\n" * 20)
    play_game()