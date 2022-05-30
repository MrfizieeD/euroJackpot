import random

myNumbers1 = []
myNumbers2 = []

while len(myNumbers1) < 5:
    
    newNumber = random.randint(1,51)
    
    if newNumber in myNumbers1:
        print('Already typed {}'.format(newNumber))
        continue
    
    myNumbers1.append(newNumber)
    
while len(myNumbers2) < 2:
    
    newNumber1 = random.randint(1,11)
    
    if newNumber1 in myNumbers2:
        print('Already typed {}'.format(newNumber1))
        continue
    
    myNumbers2.append(newNumber1)
    
print('Those numbers will win: {} and {}'.format(myNumbers1, myNumbers2))