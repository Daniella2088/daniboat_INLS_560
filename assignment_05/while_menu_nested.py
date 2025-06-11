birthday_surprise = ''
while birthday_surprise != '3':
    print (f'''
           Shop information FAQS:
           1: Make breakfast in bed for roommate
           2: Throw a surprise party
           3: Go ask someone for ideas
           ''')
    birthday_surprise = input ('Enter a number for what I should do for my roomates birthday party: ')
    if birthday_surprise == '1':
        print ('Go get some groceries now!')
    elif birthday_surprise == '2':
        friend = input(str('Do you know any of her friends that you can invite? (Y/N): ')).strip().upper()
        if friend == 'Y':
            print ("Great, let's make a group chat!")
        else: 
            print ("That's okay, I can ask someone else to do the inviting!")