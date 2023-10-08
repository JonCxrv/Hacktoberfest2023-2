# Import the random library
import random

# Create a list of operators
operators = ["+", "-", "*", "/", "%", "**"]

# Shuffle the operators
random.shuffle(operators)

# Create a list of cards
cards = []
for i in range(len(operators)):
    cards.append((operators[i], operators[i]))

# Randomly flip the cards
for i in range(len(cards)):
    if i % 2 == 0:
        cards[i] = (cards[i][1], cards[i][0])

# Start the game
while True:
    # Display the cards
    for card in cards:
        print(card[0], end=" ")
    print()

    # Get the player's input
    i = input("Select a card: ")

    # Flip the card
    cards[int(i)] = (cards[int(i)][1], cards[int(i)][0])

    # Check if the player found a match
    for j in range(len(cards)):
        if cards[i] == cards[j]:
            # The player found a match
            print("Match!")
            # Remove the matched cards
            cards.remove(cards[i])
            cards.remove(cards[j])

            # Check if the game is over
            if len(cards) == 0:
                print("Game over!")
                break

            # Shuffle the remaining cards
            random.shuffle(cards)
            break
    else:
        # The player did not find a match
        print("No match.")
