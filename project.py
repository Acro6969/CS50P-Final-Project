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
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
        ]
        is_running = True
        game_mode = input("Do you want to play against the computer? (y/n): ").strip().lower()

        if game_mode == "y":
            while is_running:
                self.display_board(board)
                self.player_move(board)
                self.computer_move(board)
                winner = self.check_winner(board)
                if winner == "X":
                    sys.exit(f"You win!")
                    is_running = False
                elif winner == "O":
                    sys.exit(f"You lose!")
                    is_running = False
                elif all(cell in ["X", "O"] for row in board for cell in row):
                    sys.exit("It's a tie!")
                    is_running = False
                else:
                    continue

        else:
            while is_running:
                self.display_board(board)
                self.player_move(board)
                winner = self.check_winner(board)
                if winner == "X":
                    sys.exit(f"Player 1 wins!")
                    is_running = False
                elif winner == "O":
                    sys.exit(f"Player 2 wins!")
                    is_running = False
                elif all(cell in ["X", "O"] for row in board for cell in row):
                    sys.exit("It's a tie!")
                    is_running = False
                else:
                    continue

    def display_board(self, board):
        print("Current Board:")
        print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
        print("---+---+---")
        print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
        print("---+---+---")
        print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

    def player_move(self, board):
        while True:
            move = input("Enter your move (1-9): ").strip()


                if move == "1" and board[0][0] not in ["X", "O"]:
                    board[0][0] = "X"
                    break
                elif move == "2" and board[0][1] not in ["X", "O"]:
                    board[0][1] = "X"
                    break
                elif move == "3" and board[0][2] not in ["X", "O"]:
                    board[0][2] = "X"
                    break
                elif move == "4" and board[1][0] not in ["X", "O"]:
                    board[1][0] = "X"
                    break
                elif move == "5" and board[1][1] not in ["X", "O"]:
                    board[1][1] = "X"
                    break
                elif move == "6" and board[1][2] not in ["X", "O"]:
                    board[1][2] = "X"
                    break
                elif move == "7" and board[2][0] not in ["X", "O"]:
                    board[2][0] = "X"
                    break
                elif move == "8" and board[2][1] not in ["X", "O"]:
                    board[2][1] = "X"
                    break
                elif move == "9" and board[2][2] not in ["X", "O"]:
                    board[2][2] = "X"
                    break
                else:
                    print("Invalid move. Please try again.")
    
    def computer_move(self, board):
        while True:
            move = str(random.randint(1, 9))
            if move == "1" and board[0][0] not in ["X", "O"]:
                board[0][0] = "O"
                break
            elif move == "2" and board[0][1] not in ["X", "O"]:
                board[0][1] = "O"
                break
            elif move == "3" and board[0][2] not in ["X", "O"]:
                board[0][2] = "O"
                break
            elif move == "4" and board[1][0] not in ["X", "O"]:
                board[1][0] = "O"
                break
            elif move == "5" and board[1][1] not in ["X", "O"]:
                board[1][1] = "O"
                break
            elif move == "6" and board[1][2] not in ["X", "O"]:
                board[1][2] = "O"
                break
            elif move == "7" and board[2][0] not in ["X", "O"]:
                board[2][0] = "O"
                break
            elif move == "8" and board[2][1] not in ["X", "O"]:
                board[2][1] = "O"
                break
            elif move == "9" and board[2][2] not in ["X", "O"]:
                board[2][2] = "O"
                break
        
    def check_winner(self, board):

        for row in board:
            if row[0] == row[1] == row[2]:
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        return None

if __name__ == "__main__":
    main()