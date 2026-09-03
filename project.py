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
    difficulties = {'easy': 7, 'medium': 6, 'hard': 5}
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
        print("Welcome to Hangman!")
        self.difficulty = self.get_difficulty()
        self.strike_limit = self.difficulties[self.difficulty]
        print(f"You have chosen {self.difficulty} difficulty. You have {self.strike_limit} strikes.")

        self.category = self.get_category()
        self.word = self.get_random_word(self.category)

        self.strikes = 0
        self.points = 0


    def get_difficulty(self):
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower().strip()
        if difficulty not in self.difficulties:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")
            return self.get_difficulty()
        else:
            return difficulty
        

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


if __name__ == "__main__":
    main()