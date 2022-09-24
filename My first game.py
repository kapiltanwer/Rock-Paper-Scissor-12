def game(Bhaiya,My):
    if Bhaiya == My:
        return None
    elif Bhaiya == 'r':
        if My == 's':
            return False
        elif My == 'p':
            return True
    elif Bhaiya == 's':
        if My == 'r':
            return True
        elif My == 'p':
            return False
    elif Bhaiya == 'p':
        if My ==  'r':
            return True
        elif My == 's':
            return False


BhaiyaTurn = input("Bhaiya turn: Rock(r) Seaser(s) Paper(p)")
MyTurn =  input("My turn: Rock(r) Seaser(s) Paper(p)")
a=game(BhaiyaTurn,MyTurn)
if a == None:
    print("The game is a tie!")
elif a:
    print("Bhaiya win or You lose")
else:
    print("Bhaiya loose and I won")
