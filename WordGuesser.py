#v1.0
#next version will include GUI
#This program is case sensetive
#Did this program in order to study if and else statements

import random

words= ["emre","eren","sanwoo","goku","ayanami","gram"]
def split(word):
    return list(word)

def game():
    a= random.choice(words)
    print(a)
    b= split(a)
    list=[]

    while "*" not in b:
        ans = input("Please guess a char: ")
        for i in range(len(b)):
            if len(list)!=len(b):
             if b[i] == ans:
                list.append(ans)
                if b[i]==ans:
                    list[i]=ans
             else:
                list.append("*")
            elif len(list)==len(b):
                if b[i]==ans:
                    list[i] = ans
        print(list)
        if list==b:
            quit()

game()








