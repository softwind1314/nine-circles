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

def is_movable(flags, index):
    log.debug('check movable, flag={:08b}; index={}'.format(flags,index))
    if index == 0:
        return True
    if flags & 0x01<<index:
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

    flags = 0x03
    while True:
        ch_code = scr.getch()
        ch = chr(ch_code)
        if ch == 'q':
            curses.endwin()
            sys.exit(0)

        idx = int(ch)
        idx -= 1
        log.debug('idx={}'.format(idx))
        ok = is_movable(flags, idx)
        if ok:
            # update flags
            if idx == 0:
                if not G[0]: # it is hooked, not unlocked (down-side)
                    # seek from left to right, and lock nth then unlock nth+1 flag
                    log.info('G#0 is moving down!')
                    for i in range(1,8):
                        if not G[i]: # locked
                            flags = 0x01 + (0x01 << i+1 )
                            log.info('update flags: {:8b}'.format(flags))
                            break
                else:
                    flags = 0x03

            G[idx] = not G[idx]
            show_game(scr, G)
        else:
            pass

