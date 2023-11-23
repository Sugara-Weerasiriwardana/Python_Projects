import random

words = ['rank','building','appartment']

display = []

selected_word=words[random.randint(0,len(words)-1)]

for char in selected_word:
    display.append("_")


print(selected_word)
print(display)

check_blanks = 1
while(check_blanks==1):
    
    guess = input("enter your guess letter : ")

    x=guess.lower()

    i =0
    for char in selected_word:
        
        if char == x:
            display[i] = x
            

        i+=1  

    print(display)

    if "_" not in display:
        check_blanks = 0