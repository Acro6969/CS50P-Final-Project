import random

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
        self.category = self.get_category()
        self.word = self.get_random_word(self.category)

        wrong_guesses = 0
        hint = ["_"] * len(self.word)
        guessed_letters = set()
        is_running = True

        self.display_man(wrong_guesses)

        

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
        print("**************")
        
    
    def display_answer(self):
        print(f"The word was: {self.word}")


if __name__ == "__main__":
    main()