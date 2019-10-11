#!/usr/bin/env python3
import curses
import logging as log
log.basicConfig(filename='example.log',level=log.DEBUG)

scr = curses.initscr()

# scr.addch(y,x, "a")
# scr.refresh( y, x)

#for i in range(10):
#    scr.addch(10,i, str(i+1))

#scr.refresh()

def is_movable(g, i):
    ''' G for down-side, if true, it is in down-side'''
    log.debug('check movable, index={}'.format(i))
    if i == 0:
        return True
    if i == 1 and g[0] == False:
        return True

    if g[i-1] == False:
        if False not in g[0:i-1]:
            return True

    return False

def show_game(s,g):
    for i in range(9):
        if g[i]:
            scr.addch(1,i,str(i+1))
            scr.addch(0, i, " ")
        else:
            scr.addch(0,i,str(i+1))
            scr.addch(1, i, " ")
    s.refresh()

import sys
    
if __name__ == "__main__":
    curses.noecho()

    scr = curses.initscr()

    G =[False] * 9

    for i in range(9):
        if G[i]:
            scr.addch(1,i,str(i+1))
            scr.delch(0,i)
        else:
            scr.addch(0,i,str(i+1))
            scr.delch(1,i)
    scr.refresh()

    while True:
        ch_code = scr.getch()
        ch = chr(ch_code)
        if ch == 'q':
            curses.endwin()
            sys.exit(0)

        idx = int(ch)
        idx -= 1

        ok = is_movable(G, idx)
        if ok:
            G[idx] = not G[idx]
            show_game(scr, G)
        else:
            pass

