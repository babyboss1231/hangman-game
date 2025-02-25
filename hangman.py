import random
import words
 

def get_word():
    
    with open('/GeeksforGeeks/Hangman/words.txt', 'r') as f:
        
        words1 = f.read().splitlines()
        
    return random.choice(words1)
 
def hangman():
    
    chosen_word = get_word()
    display = []
    for _ in chosen_word:
        display += "_"
 
   
    end_of_loop = False
    lives = 6
 
  
    print("\n-------------Welcome to Hangman-------------\n")
    print("Guess the word:- ", end=" ")
    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")
     
    while not end_of_loop:
        guess = input("Guess a Letter: ").lower()
       
        if not (guess in chosen_word):
            lives -= 1
       
        index = 0
        for c in chosen_word: 
            if c == guess:
                display[index] = guess
            index += 1
 
       
        print(f"{' '.join(display)}")
        print(f"Lives: {lives}")
        print(stages[lives-1])
 
        if "_" not in display:
            print("You Win")
            end_of_loop = True
 
        
        if lives == 0:
            print("You Lose")
            print(f"The word was: {chosen_word}")
            end_of_loop = True
 

   
    ask = input("Do you want to play Hangman? (y/n): ").lower()
   
    if ask == 'y' or ask == 'yes':
        hangman()
    
    elif ask == 'n' or ask == 'no':
        print("Program Exit Successful")
        end_of_game = True
  
    else:
        print("Your given input could not be processed.")
        print("Please enter a correct input.")
         
        