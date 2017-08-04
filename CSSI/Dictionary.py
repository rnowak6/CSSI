snacks = {
'apples' : 2,
'nuts': 3,
'chips' : 7,
'cookies' : 9
}

print snacks
snacks[1] = "apples"
for item in snacks:
    print item

snacks["apples"] = 5

for snak in snacks:
    print "%s get a %s out of 10" % (snak, snacks[snak])
