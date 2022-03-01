import random

print("welcome to the game")
print("enter your name")
a=input()
print(a,"computer has chosen a 2 digit number\n you have 6 guesses to crack the exact number\n")
while(True):
    print("guess any 2 digit natural number")
    i=0
    c=random.randint(10,99)

    while (i<6):
        b=int(input())
        if (b>99 or b<10):
            print("jab bola hai 2 digit daalne ko,kardiya na 1 waste\n")
            print("you have", 5 - i, "guesses left")
            continue
        if b==c:
            print("you won!!!",a,"\n yes the number was ",c)
            break
        elif b>c:
            print("you are greater than the number")
            i=i+1
        elif b<c:
            print("you are lesser than the number")
            i=i+1
        print("you have", 6 - i, "guesses left\n")
    if b != c:
        print("oops! the number was",c,"\n")
    print("Play Again?\n0-yes\n1-no")
    while(True):
        d=int(input())
        if d==0:
            break
        if d==1:
            print("thanks for playing")
            exit()
        if d != 0:
            print("choose between 0 or 1 only")
            continue




