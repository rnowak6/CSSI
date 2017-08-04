print "Enter 4 groceries"

groc=[]
amnt=[]
for i in range(4):
  food=raw_input('Enter groceries: ')
  groc.append(food)
  if food == "milk":
      print "milk is dumb"
  times=raw_input('Enter amount: ')
  amnt.append(times)

print "You need:"
for ia in range(4):
  print "%s. %s - %s" % (ia+1, groc[ia], amnt[ia])
