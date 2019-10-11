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

def set_bit(val, i):
    return val | (0x01 << i)

def clear_bit(val, i):
    return val & ~(0x01<<i)


def get_bit(val, i):
    return val & (0x01 << i)

def get_lsb(val):
    for i in range(9):
        mask = val & (0x01 << i)
        if mask:
            return i
    return False

def reverse_bit(val, i):
    if get_bit(val, i): # if it is 1, treat as True here.
        new = clear_bit(val, i)
    else:
        new = set_bit(val, i)
    return new

def show_game(s,g):
    ''' g is the game status,
        change implement to use bits array
    '''
    for i in range(9):
        if get_bit(g,i): # 1 means unlocked/down-side
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

    g = 0x0
    show_game(scr,g)

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
                if not get_bit(g,0): # it is hooked, not unlocked (down-side)
                    # seek from left to right, and lock nth then unlock nth+1 flag
                    log.info('G#0 is moving down!')
                    for i in range(1,8):
                        if not get_bit(g,i): # locked
                            flags = 0x01 + (0x01 << i+1 )
                            log.info('update flags: {:8b}'.format(flags))
                            break
                else:
                    flags = 0x03

            g = reverse_bit(g, idx)
            show_game(scr, g)
        else:
            pass

