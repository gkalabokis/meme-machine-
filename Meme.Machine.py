import random

def test_random():
    raw_input("1,2,3")
    print (["1","2","3"])
    print random.choice(["regular pepe","rare pepe","legendary pepe"])

test_random()



def test_getmulti():
    raw_input(["chocolate","vanilla","strawberry"])
    print (["Chocolate","Vanilla","Strawberry"])

test_getmulti()

def test_restartgame():
    raw_input("continue,exit")
    print(["Continue","Exit"])
    if "Exit": print(["GAME OVER"])
    if "Continue": print("You may continue")
   
  
test_restartgame()
    
