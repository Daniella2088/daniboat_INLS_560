birthday_surprise = ''
while birthday_surprise != '3':
    print ('BIRTHDAY SURPRISE: ', '1: Make breakfast in bed for roommate', 
           '2: Throw a surprise party', '3: Go ask someone for ideas',sep='\n')
    birthday_surprise = input ('Enter a number for what I should do for my roomates birthday party: ')

    if birthday_surprise == '1':
        print ('Go get some groceries now!')

    elif birthday_surprise == '2':
        print ('Make a group chat without her and let everyone know!')