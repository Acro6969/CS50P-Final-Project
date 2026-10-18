# CS50P-Final-Project: Arcade
#### Video Demo:  <URL HERE>
### Description

Arcade is a Python-based mini arcade that contains multiple games in one program. The project currently includes three games: Hangman, Tic-Tac-Toe, and Blackjack.

As a high school student living alone in an apartment far away from home, I sometimes find myself getting bored. My daily routine is relatively mundane, consisting of waking up, going to school, studying, eating lunch and dinner, and going to bed. To make my free time a little more entertaining, I decided to create my own virtual arcade using the Python programming skills I acquired over the past weeks through Harvard's CS50's Introduction to Programming with Python (CS50P) course.

Rather than creating three completely separate programs, I wanted to bring the games together into a single arcade experience. This project allowed me to apply what I learned in CS50P while exploring how to organize a larger program into smaller, more manageable components.

### Games

### 1. Hangman

Hangman is a word-guessing game in which the player attempts to identify a hidden word by guessing its letters. The player must figure out the word before running out of allowed incorrect guesses.

Planned features:

- Difficulty levels: Allow players to choose between different levels of difficulty.

- Themes and vocabulary: Organize words into categories, such as animals, food, technology, and more.

- Point system: Award points based on the player's performance.

- Strike system: Track incorrect guesses and limit the number of mistakes allowed.

- Letter checker: Validate guesses and determine whether a letter appears in the hidden word.

- Used letters list: Display previously guessed letters to prevent repeated guesses.

- Win and lose displays: Inform players whether they successfully guessed the word or ran out of attempts.

### 2. Tic-Tac-Toe

Tic-Tac-Toe is a two-player strategy game played on a 3-by-3 grid. Players take turns placing their symbols, X and O, on the board. The first player to align three symbols horizontally, vertically, or diagonally wins.

Planned features:

- Game board: Display a 3-by-3 grid and update it after each move.

- Player turns: Alternate between X and O.

- Input validation: Ensure players select valid, unoccupied positions.

- Win detection: Check for three matching symbols in a row, column, or diagonal.

- Draw detection: Identify when the board is full and neither player has won.

- Replay option: Allow players to start another round without restarting the entire arcade.

### 3. Blackjack

Blackjack is a card game in which the player attempts to achieve a hand value closer to 21 than the dealer's hand without exceeding 21.

Planned features:

- Card deck: Generate and shuffle a deck of cards.

- Card values: Calculate the values of numbered cards, face cards, and aces according to Blackjack rules.

- Player actions: Allow the player to hit (draw another card) or stand (keep their current hand).

- Dealer behavior: Have the dealer draw cards according to predefined rules.

- Hand evaluation: Determine whether the player or dealer wins, including busts and ties.

- Replay option: Allow players to play multiple rounds.

### Design Choices

I chose Python because it was the language taught throughout CS50P, making this project an opportunity to apply the concepts I learned in the course. I also chose three familiar games so I could focus on implementing their rules and logic rather than spending too much time designing entirely new games.

The arcade format brings the games together under one program, making it easier for players to select a game and switch between different activities. Separating the games into their own components also makes the code easier to understand, test, maintain, and expand in the future.

### What I Learned

Through this project, I aim to strengthen my understanding of Python by applying programming concepts to a practical project. These include functions, conditional statements, loops, input validation, data structures, and object-oriented programming.

Developing multiple games within a single program also provides an opportunity to practice organizing code, handling different game states, and anticipating unexpected user inputs. In addition, implementing each game's rules requires breaking a larger problem into smaller steps and testing each component to ensure that it behaves as intended.

### Future Improvements

In the future, I would like to expand the arcade by completing the planned features for each game and potentially introducing additional mini-games. Other possible improvements include a unified scoring system, a more polished interface, and additional customization options.

Ultimately, this project began as a way to make my free time more entertaining, but it also became an opportunity to apply what I learned in CS50P and continue developing my programming skills.

### How to Run

1. Ensure Python is installed on your computer.

2. Clone or download this repository.

3. Open a terminal in the project directory.

4. Run the main Python file:

5. python project.py

6. Replace project.py with the name of the actual entry-point file if it is different.

7. Follow the on-screen instructions to select and play a game.

### Requirements

- Python 3

- Any additional libraries required by the project, if applicable
