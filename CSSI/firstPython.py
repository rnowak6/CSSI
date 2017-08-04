#name = raw_input('Enter your name: ')
#print "Hello"+" " + name

#person=raw_input('Enter noun (person): ')
#place=raw_input('Enter place: ')
#verb=raw_input('Enter verb: ')
#food=raw_input('Enter restaurant name: ')
#noun=raw_input('Enter noun: ')
#print "Once a year, I like to go with"+" "+person+" to the "+place+". Each year we"+" "+verb+" the animals and then go to"+" "+food+" to get"+" "+noun

#print "Hello %s nice to meet you. " % (name)

from random import randint

#groceries = ['bana', 'milk', 'eggs']
#print groceries[randint(0,5)]

#tasks=["do the dishes", "do my homework", "make dinner", "pick up my brother"]
#excuses=["my dog ran away", "I cannot find my house", "I got stranded in Australia on my way home from school", "Chicago no longer exists", "my grandma got run over by a reindeer"]

#print "I did not %s because %s" % (tasks[randint(0,len(tasks)-1)] , excuses[randint(0,len(excuses)-1)])

#def ps():
#    print "banana"
#    print "apple"
#print "no really"

#def cool(number, number2):
#    print number+number2
#cool(2,3)

#def randomList(list):
#    print list[randint(0,len(list)-1)]

#cats=['kitty', 'kitten', 'dog']
#randomList(cats)

numbs = ['1', '2', '3', '4', 'a', 'b', 'c', 'd']
def ranIndex(listt):
    return listt[randint(0,len(listt)-1)]

new_password=""
for i in range(8):
    new_password=new_password + ranIndex(numbs)
    print i+1
    print  new_password

#for index in range(len(numbs)):
#    print numbs[index]

#def ranNum(listt):
#    print ("Password: %s%s%s%s%s ") % (ranIndex(listt), ranIndex(listt), ranIndex(listt), ranIndex(listt), ranIndex(listt))

#ranNum(numbs)
