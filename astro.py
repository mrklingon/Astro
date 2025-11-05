import time
import random
import board
import neopixel
import touchio
from ncount import *
from prt import *
from wise import *

REPL=True

# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

star = []
locx = []
locy = []

map = ["..........","..........","..........","..........","..........","..........","..........","..........","..........",".........."]
def placeNM():
    #build a random star name
    start = ["Gi","Ro","Ah","Mi","Pa","Ki","Re","Sy","Th","Zo"]
    mid = ["eu","af","gh","uu","a","e","i","o","u","y"]
    end = ["nk","as","of","z","d","n","ll","ah","ei","ie"]

    Place = random.choice(start)+random.choice(mid)+random.choice(end)
    return (Place)

def chartStars():
    compthink()

    for i in range(random.randrange(3,11,1)):
        star.append(placeNM())
        locx.append(random.randrange(10))
        locy.append(random.randrange(10))

        s = map[locy[i]]
        s = s[:locx[i] ] + "*" + s[locx[i]+1:]
        map[locy[i]] = s
chartStars()

def dist(l1,l2):
    dst = (((locx[l1]-locx[l2])**2+((locy[l1]-locy[l2])**2))**.5)
    return dst

while True:

    Val = 0

    if touch1.value:
        Val = Val + 1


    if touch2.value:
        Val = Val + 2


    if Val == 1:

        star = []
        locx = []
        locy = []

        map = ["..........","..........","..........","..........","..........","..........","..........","..........","..........",".........."]

        chartStars()
        compthink()

        prt("",REPL)
        prt("",REPL)

        for i in range(len(star)):
            prt (star[i] + ":" + str(locx[i])+", " + str(locy[i]),REPL)

        for i in range(10):
            prt (map[i],REPL)

    if Val == 2:
        #pick a location
        prt(" ",REPL)
        loc = random.randrange(len(star))
        prt("location = " + star[loc],REPL)
        for i in range(len(star)):
            prt (star[i] + ":" + str(locx[i])+", " + str(locy[i])+": "+str(dist(i,loc)),REPL)




    time.sleep(1)