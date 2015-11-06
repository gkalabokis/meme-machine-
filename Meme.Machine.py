import random

def get_multi (choices):
    '''Ask the user to choose one of choices. Return user choice'''
    print 'Here are your choices...'
    raw_input()
    for choice in choices:
        print choice
    answer = raw_input('Your choice')
    if answer not in choices:
        print answer,'Pick again skrub'
        return get_multi(choices)
    else:
        return answer

 
def get_random (choices):
    # write code to actually do what you want here...
    raw_input("1,2,3")
    print (["1","2","3"])
    answer = random.choice(choices)
    return answer

def game_over ():
    # Write code to do what you want here...
    print 'done'

def play_game ():
    print 'not written yet...'
    # WRITE YOUR ACTUAL GAME LOGIC HERE
    # USING get_multi, get_random, if statements, etc...
    # e.g.
    pepe = get_multi(['Pepe','Rare pepe','Legendary pepe'])
    if pepe=='pepe':
        print 'U looz skrub'
        game_over()
    else:
        print 'Whoa, 2spooky4me'
        print 'Do you know the muffin man?'
        next = get_multi(['Of course','']) # something like that...
        if next == 'Go to sleep':
            game_over()
        else:
            get_multi(['Go to class','Talk to friends','Go to Mario\'s'])
            # ...



def test_random():
    # this should call get_random...
    print 'Returns:',get_random(['1','2','3'])
    print 'Returns:',get_random(['peanuts','cashews','walnuts'])
    print 'Returns:',get_random(["regular pepe","rare pepe","legendary pepe"])





def test_getmulti():
    # this test should call get_multi...
    choices = ['1','2','3']
    answer = get_multi(choices)
    if answer in choices: print 'SUCCESS!'
    else: print 'FAILURE','returned:',answer,'not in',choices
    choices = ['red','yellow','blue']
    answer = get_multi(choices)
    if answer in choices: print 'SUCCESS!'
    else: print 'FAILURE','returned:',answer,'not in',choices
    #raw_input(["chocolate","vanilla","strawberry"])
    #print (["Chocolate","Vanilla","Strawberry"])



def test_restartgame():
    raw_input("continue,exit")
    print(["Continue","Exit"])
    if "Exit": print(["GAME OVER"])
    if "Continue": print("You may continue")
   
  
#test_restartgame()

test_random()
