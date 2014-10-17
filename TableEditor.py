import curses, time

class TableEditor(object):
	"""
	Table Editor

	:param tFile: The table file object
	:param display: The Table Displayer object to display results
	"""
	def __init__(self, tFile, display):
		self.tFile = tFile
		self.display = display

	def run(self):
		self.display.draw()

		while True:
			c = self.display.screen.getch()
			c = chr(c)
			if c == 'q': break
			elif c == 'c': self.change()
			elif c == 's': self.tFile.writeFile()

		self.display.restorescreen()

	def change(self):
		self.display.prompt_screen(True)
		self.display.screen.addstr(curses.LINES - 1, 0, "Enter 'row column value' with spaces in between: ")
		response = self.display.screen.getstr().split()
		new_row, new_col, new_val = int(response[0]), int(response[1]), response[2]
		self.tFile.data[new_row][new_col] = new_val
		self.display.draw()
		self.display.prompt_screen(False)
		
