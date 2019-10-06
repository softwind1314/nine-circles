#!/usr/bin/env python3

import curses


scr = curses.initscr()

curses.noecho()

scr.nodelay(False)

ch = scr.getch()

print( type(ch))

#if ch == ord('1'):
#  print('it is 1')

#if ch == ord('2'):
#  print('it is 2')


print( int(chr(ch)) ) # success to convert char to int

