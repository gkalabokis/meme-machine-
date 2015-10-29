import random

def get_multi (choices):
    # write code to actually do this here
    raw_input (choices)
    
    return '1'

def get_random (choices):
    # write code to actually do what you want here...
    return answer

def game_over ():
    # Write code to do what you want here...
    print 'done'

def play_game ():
    print 'not written yet...'
    # WRITE YOUR ACTUAL GAME LOGIC HERE
    # USING get_multi, get_random, if statements, etc...
    # e.g.
    food = get_multi(['Pizza','Burger','Salad'])
    if food=='Pizza':
        print 'Pizza is poison'
        game_over()
    else:
        print 'Yum'
        next = get_multi(['Go to sleep','Go to school']) # something like that...
        if next == 'Go to sleep':
            game_over()
        else:
            get_multi(['Go to class','Talk to friends','Go to Mario\'s'])
            # ...



def test_random():
    # this should call get_random...
    raw_input("1,2,3")
    print (["1","2","3"])
    print random.choice(["regular pepe","rare pepe","legendary pepe"])

#test_random()



def test_getmulti():
    # this test should call get_multi...
    choices = ['1','2','3']
    print 'TESTING get_multi with choices: ',choices
    answer = get_multi(choices) 
    if answer in choices: print 'SUCCESS!'
    else: print 'FAILURE','returned:',answer,'not in',choices
    choices = ['red','yellow','blue']
    print 'TESTING get_multi with choices: ',choices
    answer = get_multi(choices)
    if answer in choices: print 'SUCCESS!'
    else: print 'FAILURE','returned:',answer,'not in',choices
    #raw_input(["chocolate","vanilla","strawberry"])
    #print (["Chocolate","Vanilla","Strawberry"])

test_getmulti()

def test_restartgame():
    raw_input("continue,exit")
    print(["Continue","Exit"])
    if "Exit": print(["GAME OVER"])
    if "Continue": print("You may continue")
   
  
#test_restartgame()

