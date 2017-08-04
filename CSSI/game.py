from random import randint
number=randint(0,20)
numb=int(raw_input('Choose a number between 0 to 20 '))
check=0;

while numb!=number:

    if numb>number:
        print 'too high!'
    else:
        print 'too low'
    numb=int(raw_input('Choose a number between 0 to 20 '))
print 'Correct!'
