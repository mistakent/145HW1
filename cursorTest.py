# Try it

import sys, curses

def main():
	try:
		# Start curses
		s = curses.initscr()

		# Start colors
		curses.start_color()
		
		# Paint a box
		s.box()

		# Write something
		s.move(5,5)
		curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
		s.addstr('Hello world!', curses.color_pair(1))

		# Put on console
		s.refresh()

		sys.stdin.read(1)
		curses.endwin()
	except:
		curses.endwin()

if __name__ == '__main__':
	main()