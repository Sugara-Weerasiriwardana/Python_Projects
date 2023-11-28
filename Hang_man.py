import random

words = ['rank','building','appartment']

display = []

hangman_draw = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



selected_word=words[random.randint(0,len(words)-1)]

for char in selected_word:
    display.append("_")


#print(selected_word)
print(display)

check_blanks = 1
hangman_draw_no =6

while(check_blanks==1 and hangman_draw_no!=-1):
    match_found = 0 
    guess = input("enter your guess letter : ")

    x=guess.lower()

    i =0
    for char in selected_word:
        
        if char == x:
            display[i] = x
            match_found = 1
      
            

        i+=1  

    print(display)
    if match_found == 0:
        print(hangman_draw[hangman_draw_no])
        hangman_draw_no-=1   

    if "_" not in display:
        check_blanks = 0
        print("You win")

    if hangman_draw_no ==-1:
        print("You Lose")