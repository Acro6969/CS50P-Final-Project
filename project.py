import random
import sys

games = ["hangman", "tictactoe", "blackjack"]

def main():
    game = input("What game would you like to play (Hangman, TicTacToe, Blackjack)? ").strip().lower()

    if game == "hangman":
        hangman = Hangman()
    elif game == "tictactoe":
        tictactoe = TicTacToe()
    elif game == "blackjack":
        blackjack = Blackjack()
    else:
        print("Invalid game choice.")

class Hangman:
    vocabularies = {

        'place': ["Cathedral", "Skyscraper", "Lighthouse", "Monastery", "Observatory", "Theater",
        "Warehouse", "Courthouse", "Aquarium", "Pyramid", "Fortress", "Laboratory", "Museum",
        "Planetarium", "Colosseum", "Canyon", "Oasis", "Cemetery", "Hospital", "Stadium"],

        'animal': ["Chimpanzee", "Rhinoceros", "Hippopotamus", "Porcupine", "Armadillo", "Anteater", 
        "Wolverine", "Barracuda", "Jellyfish", "Swordfish", "Stingray", "Manatee", "Hummingbird", 
        "Woodpecker", "Grasshopper", "Tarantula", "Salamander", "Caterpillar", "Dragonfly", "Centipede",],

        'adjective': ["Mysterious", "Melancholy", "Flamboyant", "Whimsical", "Symmetrical", "Luminescent",
        "Microscopic", "Transparent", "Fluorescent", "Courageous", "Arrogant", "Eccentric", "Compassionate",
        "Mischievous", "Catastrophic", "Hazardous", "Peculiar", "Enigmatic", "Redundant"],

        'movie': ["Inception", "Interstellar", "Gladiator", "Matrix", "Ratatouille", "Shrek", "Moana",
        "Zootopia", "Avengers", "Batman", "Spiderman", "Ironman", "Titanic", "Godfather", "Whiplash",
        "Oppenheimer", "Jaws", "Se7en", "Shutterisland", "Conjuring"],

        'general': ["Photosynthesis", "Supernova", "Gravity", "Atmosphere", "Fossilization", "Hemoglobin",
        "Microscope", "Ultraviolet", "Electricity", "Chromosome", "Literature", "Orchestra", "Sculpture", 
        "Calligraphy", "Biography", "Metaphor", "Choreography", "Philosophy", "Equator", "Hemisphere", "Avalanche",
        "Tornado", "Constellation", "Continent", "Ecosystem", "Biodiversity", "Geothermal", "Glacier", "Architecture",
        "Democracy", "Geography", "Astronomy", "Psychology", "Mathematics", "Technology", "Revolution", "Monarchy"]
        
    }

    def __init__(self):
        self.art = {
                    0: ["   "],
                    1: [" o "],
                    2: [" o ", 
                        " | "],
                    3: [" o ", 
                        "/| ",],
                    4: [" o ", 
                        "/|\\"],
                    5: [" o ", 
                        "/|\\", 
                        "/  "],
                    6: [" o ", 
                        "/|\\", 
                        "/ \\"],
                    }

        print("Welcome to Hangman!")
        category = self.get_category()
        word = self.get_random_word(category)

        wrong_guesses = 0
        hint = ["_"] * len(word)
        guessed_letters = set()
        is_running = True

        while is_running:
            self.display_man(wrong_guesses)
            self.display_hint(hint)
            guess = input("Guess a letter: ").lower().strip()

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        hint[i] = guess
                        guessed_letters.add(guess)
            else:
                wrong_guesses += 1
            
            if wrong_guesses == 6:
                self.display_man(wrong_guesses)
                print("You lost!")
                self.display_answer(word)
                sys.exit()
            elif "_" not in hint:
                print("You won!")
                self.display_answer(word)
                sys.exit()
                

    def get_category(self):
        category = input("Choose a category (place, animal, adjective, movie, general): ").lower().strip()
        if category not in self.vocabularies:
            print("Invalid category. Please choose from place, animal, adjective, movie, or general.")
            return self.get_category()
        else:
            return category


    def get_random_word(self, category):
        self.get_random_word = random.choice(self.vocabularies[category])
        return self.get_random_word.lower()

    def display_man(self, wrong_guesses):
        print("**************")
        for line in self.art[wrong_guesses]:
            print(line)
        print("\n**************")
        
    def display_hint(self, hint):
        print(" ".join(hint))
    
    def display_answer(self, word):
        print(f"The word was: {word}")

class TicTacToe:
    def __init__(self):
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        is_running = True

        self.display_board(board)
            
    def display_board(self, board):
        print("Current Board:")
        print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
        print("---+---+---")
        print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
        print("---+---+---")
        print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

if __name__ == "__main__":
    main()