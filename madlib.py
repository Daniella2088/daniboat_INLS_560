def madLib (adj1, noun1,adj2, noun2, noun3, noun4, exclamation):
    story = (f'''
    Move-in Mad Lib: 
    
    Today I went shopping for move-in day. 
    The store was {adj1} and packed with people. 
    I grabbed a {noun1} and a {adj2} {noun2}
    for my dorm. While walking down the aisle, I tripped over 
    a {noun3} and almost dropped my {noun4}.
    Everyone turned and I shouted, "{exclamation}!"
             ''')
    return story 

def get_input():
    adj1 = input('Please enter an adjective: ')
    noun1 = input ('Please enter a noun: ')
    adj2 = input ('Please enter an adjective: ')
    noun2 = input ('Please enter a noun: ')
    noun3 = input ('Please enter a noun: ')
    noun4 = input ('Please enter a noun: ')
    exclamation = input ('Please enter an exclamation: ')
    return adj1, noun1, adj2, noun2, noun3, noun4, exclamation

inputs = get_input()
print (madLib(*inputs))
