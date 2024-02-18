word_list = ["shershah", "yehjawaniyehdeewani", "thappad", "dearzindagi"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
import random
chosen_word = random.choice(word_list)
lives =6
print("welcome to bollywood hangman")
display = []
for letter in chosen_word:
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()
    if guess in display:
       print(f"You've already guessed the letter {guess}")  
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    if guess not in chosen_word:
       print(f"you guessd {guess}, that'not in the word. you lose a life")
       lives -=1
       if lives == 0:
          end_of_game = True
          print("You lose")
    print(f"{''.join(display)}")
    if "_" not in display:
       end_of_game = True
       print("you win")
    print(stages[lives])