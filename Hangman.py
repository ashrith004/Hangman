#HANGMAN GAME 
import random 

word_list = ["apple", "banana","aardvark", "baboon", "camel",
              "jazz", "grass", "follow", "castle", "cloud"]
stages = [''' 
       ______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
  ___|___
 ''',
 ''' 
       _______
     |/      |
     |      (_)
     |      \|/
     |       | 
     |         
     |
  ___|___
 ''',
 ''' 
       _______
     |/      |
     |      (_)
     |      \|/
     |        
     |         
     |
  ___|___ 
 ''',
 '''
       _______
     |/      |
     |      (_)
     |       |  
     |        
     |         
     |
  ___|___
 ''',
 '''   _______
     |/      |
     |      (_)
     |         
     |        
     |         
     |
  ___|___
 ''',
 ''' 
       ________
      /      |
     |         
     |         
     |        
     |         
     |
  ___|___
 '''
]
print('''Welcome to the Hangman Game !!!
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')  
lives = 5
choosen_word = random.choice(word_list)
print(choosen_word)
#TO DO-1 Randomly choose aword from thea
#  word_list and 
placeholder = " "
word_length = len(choosen_word)
for position in range(1,6):
    placeholder += " _"
print("Word to guess : "+placeholder)
# TO DO -Use a while loop to let the user guess again
game_over =  False
correct_letter = []
while not game_over:
    print("***************************<???> /6 LIVES LEFT ***********************")
    guess = input("Guess a letter :").lower()
    if guess in correct_letter:
        print(f"You have already guessed{guess}")

    display = ""
 
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += " _"
    print(display)
    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word .You lose a life.")
        if lives == 0:
            game_over = True
            print("******************** YOU LOSE ********************")
    if "_" not in display:
        game_over = True
        print("******************** YOU WIN ********************")

    print(stages[lives])