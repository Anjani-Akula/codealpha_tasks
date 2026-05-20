print("------------------------")
print("BASIC CHATBOT ")
print("------------------------")
#BASIC CHATBOT

def greeting():
    print("Hi !!")
def question():
    print( "I'm fine, thanks!")
def end():
    print("Goodbye!")
print("Here is the basic chatbot !")
print('------------------------')
again=1
while(again!=0):
    s=input("ask your question!!")
    if(s.lower()=='hey' or s.lower()=='hello' or s.lower()=='hi'):
        greeting()
        s=input("do you want to ask anything !")
        if(s.lower()=='no'):
            again=0
    elif(s.lower()=='how are you'):
        question()
        s=input("do you want to ask anything !")
        if(s.lower()=='no'):
            again=0
    elif(s.lower()=='bye'):
        end()
        again=0
    else:
        print("I don't understand!!please try again")