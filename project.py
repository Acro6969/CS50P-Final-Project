import random

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

def main():
    print("Welcome to Hangman!")
    difficulty = get_difficulty()
    strike_limit = difficulties[difficulty]
    print(f"You have chosen {difficulty} difficulty. You have {strike_limit} strikes.")

    category = get_category()
    word = get_random_word(category)

    strikes = 0
    points = 0


def get_difficulty():
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower().strip()
    if difficulty not in difficulties:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        return get_difficulty()
    else:
        return difficulty
    

def get_category():
    category = input("Choose a category (place, animal, adjective, movie, general): ").lower().strip()
    if category not in vocabularies:
        print("Invalid category. Please choose from place, animal, adjective, movie, or general.")
        return get_category()
    else:
        return category


def get_random_word(category):
    return random.choice(vocabularies[category])

if __name__ == "__main__":
    main()