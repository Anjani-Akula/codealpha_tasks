print("------------------------")
print("HANGMAN GAME ")
print("------------------------")

#HANGMAN GAME

import random
l=['magazine','transform','building','uniform','pendrive']
guess=6
count=0
user2=''
word=l[random.randint(0,4)]
while(guess!=0):
    user=''
    s=input("enter a letter of the word ")
    if(s in word):
        count=1
        for i in range(len(word)):
            if(word[i]==s or (word[i] in user2)):
                user=user+word[i]
            else:
                user=user+'_'
        print("you guessed correctly")
        print("the word is ",user)
        user2=user
    else:
        print("your guess is wrong")
        guess-=1
        if(user2!=''):
            print("the word is ",user2)
    if(user==word):
        print("you won the game")
        break
    else:
        print("you still have ",guess,'guesses')
        print("----------------------")
if(guess==0):
    print("you are out of chances!! please try again")

