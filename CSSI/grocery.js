print "Enter 4 groceries"

groc=[]
for i in range(4):
  food=raw_input('Enter groceries: ')
  groc.append(food)
print "You need:"
for ia in range(4):
  print "%s. %s" % (ia+1, groc[ia])
