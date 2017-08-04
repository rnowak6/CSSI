emoji_dic = {
':)' : 'happy',
'<3' : 'love',
':(' : 'sad',
'._.': 'unimpressed',
':o' : 'shocked'

}

emoji=raw_input('Enter an emoji ')
if(emoji in emoji_dic):
    print emoji_dic[emoji]
else:
    print 'do u not know what emojis are?'
