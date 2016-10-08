import curses
from random import randint

phrases = {1:"On its own",2:"More than 1"}
seven_segment  = {1:[0,1,1,0,0,0,0],2:[1,1,0,1,1,0,1]}

max = 2

def mainloop(stdscr):
    sofar = []
    while (1):
        stdscr.addstr(0,10,"N:New game, Space: Next number")
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

            stdscr.addstr(20+line, col,str(nextNumber))
            
            stdscr.addstr(18+line, 0, "                                    ")
            stdscr.addstr(18+line, 0, phrases[nextNumber])

            pixels = seven_segment[nextNumber]
            

def main():
    curses.wrapper(mainloop)
    
if __name__ == "__main__":
    main()
