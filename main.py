import random
print("""
Welcome To the Game Stone–paper–scissors 
========================================
by:- Rohan vivek
Enjoy :)
""")


chars = 'stone', 'paper', 'scissor'
for pwd in range(1):
    c = ''
    for c in range(1):
        c = random.choice(chars)
p = input('stone (r), paper (p) or scissors (s)?')
if p== 'r'and c =='paper':
    print("computer chooses",c)
    print("You Lose")
elif p== 'r'and c =='stone':
    print("computer chooses",c)
    print("Draw")
elif p== 'r'and c =='scissor':
    print("computer chooses",c)
    print("You Won")
elif p== 'p'and c =='stone':
    print("computer chooses",c)
    print("You Won")
elif p== 'p'and c =='paper':
    print("computer chooses",c)
    print("Draw")
elif p== 'p'and c =='scissor':
    print("computer chooses",c)
    print("Computer Won")
elif p== 's'and c =='stone':
    print("computer chooses",c)
    print("You LOse")
elif p== 's'and c =='paper':
    print("computer chooses",c)
    print("You Won")
elif p== 's'and c =='scissor':
    print("computer chooses",c)
    print("Draw")
else:
    print("Huh......????")


