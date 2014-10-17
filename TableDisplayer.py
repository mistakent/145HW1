import curses

class TableDisplayer(object):

	"""
	Display Initializer 

	:param tFile: The table file object
	"""
	def __init__(self, tFile):
		self.tFile = tFile		

		#window setup
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()

	def draw(self):
		self.screen.clear()

		#get max length in cols and put in array size
		size = []
		maxcols = zip(*self.tFile.data)
		for q in range (len(maxcols)):
			size.append(max(maxcols[q], key=len))

		for rows in range(len(self.tFile.data)):
			for cols in range(len(self.tFile.data[0])):
				self.screen.addstr(self.tFile.data[rows][cols].rjust(len(size[cols]))+' ')
			self.screen.addstr('\n')

		self.screen.refresh()

	def restorescreen(self):
		curses.nocbreak()
		curses.echo()
		curses.endwin()

	def prompt_screen(self, should_prompt):
		if should_prompt:
			curses.nocbreak()
			curses.echo()
		else:
			curses.cbreak()
			curses.noecho()



