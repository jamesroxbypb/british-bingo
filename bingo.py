import curses
from random import randint

# Screen width is 80 x 43

phrases = {1:"On its own",2:"More than 1"}
phrases = {1:"Kelly's Eye",
           2:"One little duck",
           3:"Cup of tea",
           4:"Knock at the door",
           5:"Man alive",
           6:"Half a dozen",
           7:"Lucky",
           8:"Garden gate",
           9:"Doctor's Orders",
           10:"Theresa's Den",
           11:"Legs eleven",
           12:"One dozen",
           13:"Unlucky for some",
           14:"Valentines Day",
           15:"Young and Keen",
           16:"Never been kissed",
           17:"Dancing Queen",
	   18:"Coming of Age",
           19:"Goodbye Teens",
           20:"One Score",
           21:"Key of the Door",
           22:"Two little ducks",
           23:"Thee and Me",
           24:"Knock at the door",
           25:"Duck and dive",
           26:"Two and six, half a crown",
           27:"Duck and a crutch",
           28:"Two and eight, in a state",
           29:"Rise and Shine",	
           30:"Dirty Gertie",
           31:"Get Up and Run",
           32:"Buckle My Shoe",
           33:"All the threes",
           34:"Ask for More",	
           35:"Jump and Jive",
           36:"Three dozen",
           37:"A Flea in Heaven",
           38:"Christmas Cake",
           39:"Steps",
           40:"Naughty Forty",
           41:"Time for Fun",
           42:"Winnie the Pooh",
           43:"Down on your Knees",
           44:"Droopy drawers",
           45:"Halfway there",
           46:"Up to Tricks",
           47:"Four and Seven",
           48:"Four Dozen",
           49:"Nick Nick",
           50:"It's a bullseye!",
           51:"Tweak of the Thumb",
           52:"Chicken vindaloo",
           53:"Here comes Herbie",
           54:"Clean the Floor",	
           55:"Musty Hive",
           56:"Shotts Bus",
           57:"Heinz Varieties",
           58:"Make Them Wait",
           59:"The Brighton Line",
           60:"Grandma's getting frisky",
           61:"Bakers Bun",
           62:"Tickety-boo",
           63:"Tickle me",
           64:"Red raw",	
           65:"Stop work",
           66:"Clickety click",
           67:"Made in Heaven",
           68:"Saving Grace",
           69:"Anyway up. Meal for Two",
           70:"Three score and ten",
           71:"Bang on the Drum",
           72:"Danny La Rue",
           73:"Queen Bee",
           74:"Candy Store",
           75:"Strive and Strive",
           76:"Was she worth it?",
           77:"Sunset Strip",
           78:"Heaven's Gate",
           79:"One More Time",
           80:"Gandhi's Breakfast",
           81:"Stop and Run",
           82:"Fat Lady and a Duck",
           83:"Time for Tea",
           84:"Seven dozen",
           85:"Staying alive",
           86:"Between the sticks",
           87:"Torquay in Devon",
           88:"Two Fat Ladies",
           89:"Nearly there",
           90:"Top of the shop"}

to_use = {1:"#",0:" "}
seven_segment  = {0:[1,1,1,1,1,1,0],1:[0,1,1,0,0,0,0],2:[1,1,0,1,1,0,1],
                  3:[1,1,1,1,0,0,1],4:[0,1,1,0,0,1,1],5:[1,0,1,1,0,1,1],
                  6:[1,0,1,1,1,1,1],7:[1,1,1,0,0,0,0],8:[1,1,1,1,1,1,1],
                  9:[1,1,1,0,0,1,1]}
clear_seven_segment = [0,0,0,0,0,0,0]
max = 90
width = 30
height = 12

def horizontalSegment(stdscr, pixel, x_offset, y_offset):
    for i in range (x_offset+1,x_offset-1+width):
        stdscr.addch(y_offset-1,i,ord(to_use[pixel]))
        stdscr.addch(y_offset+1,i,ord(to_use[pixel]))
    for i in range (x_offset,x_offset+width):
        stdscr.addch(y_offset,i,ord(to_use[pixel]))

def verticalSegment(stdscr, pixel, x_offset, y_offset):
    for i in range (0,height-2):
        stdscr.addch(i+y_offset+1,x_offset-1,ord(to_use[pixel]))
        stdscr.addch(i+y_offset+1,x_offset+1,ord(to_use[pixel]))
    for i in range (0,height):
        stdscr.addch(i+y_offset,x_offset,ord(to_use[pixel]))

def mainLoop(stdscr):
    sofar = []
    while (1):
        stdscr.addstr(42,60,"N:New game, Space: Next number, Q: Quit ")
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == ord('n'):
            stdscr.clear()
            sofar = []
        elif c == ord(' '):
            validNumber = False
            while (not validNumber):
                nextNumber = randint(1,max)
                if nextNumber not in sofar:
                    validNumber = True


            # We have a number, lets display it on the grid
            sofar.append(nextNumber)
            line = int(nextNumber/20)
            col = 3 * (nextNumber % 20)

            stdscr.addstr(34+line, col,str(nextNumber))
            
            stdscr.addstr(40, 0, "                                    ")
            try:
                stdscr.addstr(40, 0, phrases[nextNumber])
            except KeyError:
                # No rhyme for you
                pass
            
            second_digit = nextNumber % 10
            first_digit = int(nextNumber / 10)
            
            if (first_digit > 0):
                pixels = seven_segment[first_digit]
            else:
                pixels = clear_seven_segment
                
            horizontalSegment(stdscr,pixels[0],10,3)
            verticalSegment(stdscr,pixels[1],11+width,4)
            verticalSegment(stdscr,pixels[2],11+width,5+height)
            horizontalSegment(stdscr,pixels[3],10,6+2*height)
            verticalSegment(stdscr,pixels[4],8,5+height)
            verticalSegment(stdscr,pixels[5],8,4)
            horizontalSegment(stdscr,pixels[6],10,4+height)
            
            
            pixels = seven_segment[second_digit]

            horizontalSegment(stdscr,pixels[0],60,3)
            verticalSegment(stdscr,pixels[1],61+width,4)
            verticalSegment(stdscr,pixels[2],61+width,5+height)
            horizontalSegment(stdscr,pixels[3],60,6+2*height)
            verticalSegment(stdscr,pixels[4],58,5+height)
            verticalSegment(stdscr,pixels[5],58,4)
            horizontalSegment(stdscr,pixels[6],60,4+height)
            
def main():
    curses.wrapper(mainLoop)
    
if __name__ == "__main__":
    main()
