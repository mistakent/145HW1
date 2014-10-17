import curses

class TableDisplayer(object):

	"""
	Display Initializer 

	:param table: The table expected as a list of lists
	"""
	def __init__(self, table):
		self.table = table
		self.size = []
		
		#get max length in cols and put in array size
		maxcols = zip(*self.table)
		for q in range (len(maxcols)):
			self.size.append(max(maxcols[q], key=len))

		#window setup
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()

	def display(self):
		self.screen.clear()

		for rows in range(len(self.table)):
			for cols in range(len(self.table[0])):
				self.screen.addstr(self.table[rows][cols].rjust(len(self.size[cols]))+' ')
			self.screen.addstr('\n')

		self.screen.refresh()

	def restorescreen():
		curses.nocbreak()
		curses.echo()
		curses.endwin()



