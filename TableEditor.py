import curses, time, copy

class TableEditor(object):
	"""
	Table Editor

	:param tFile: The table file object
	:param display: The Table Displayer object to display results
	"""
	def __init__(self, tFile, display):
		self.tFile = tFile
		self.display = display
		self.history = []
		# Add to history
		self.history.append(copy.deepcopy(self.tFile))

	def run(self):
		self.display.draw()

		while True:
			c = self.display.screen.getch()
			c = chr(c)
			if c == 'q': break
			elif c == 'c': self.change()
			elif c == 'a': self.add()
			elif c == 'd': self.remove()
			elif c == 's': self.tFile.writeFile()
			elif c == 'u': self.undo()

		self.display.restorescreen()

	def change(self):
		self.display.prompt_screen(True)
		self.display.screen.addstr(curses.LINES - 1, 0, "Enter 'row column value' with spaces in between: ")
		response = self.display.screen.getstr().split()
		new_row, new_col, new_val = int(response[0]), int(response[1]), response[2]
		self.tFile.data[new_row][new_col] = new_val
		self.display.draw()
		self.display.prompt_screen(False)
		# Add to history
		self.history.append(copy.deepcopy(self.tFile))
		
	def add(self):
		self.display.prompt_screen(True)
		self.display.screen.addstr(curses.LINES - 1, 0, "Enter r or c for row/column, then r/c number, then data: ")
		response = self.display.screen.getstr().split()
		newrow=[]
		newcol=[]

		if response[0] == 'r':
			for cols in range(len(self.tFile.data[0])):
				newrow.append(response[cols+2])

			if int(response[1]) > len(self.tFile.data):
				self.tFile.data.append(newrow)
			else:
				self.tFile.data.insert(int(response[1]),newrow)

		elif response[0] == 'c':
			for rows in range(len(self.tFile.data)):
				newcol.append(response[rows+2])

			if int(response[1]) > len(self.tFile.data[0]):
				for r in range(len(self.tFile.data)):
					self.tFile.data[r].append(newcol[r])
			else:
				for r in range(len(self.tFile.data)):
					self.tFile.data[r].insert(int(response[1])-1,newcol[r])

		self.display.draw()
		self.display.prompt_screen(False)
		# Add to history
		self.history.append(copy.deepcopy(self.tFile))

	def remove(self):
		self.display.prompt_screen(True)
		self.display.screen.addstr(curses.LINES - 1, 0, "Enter r or c for row/colum, then r/c number you want to remove: ")
		response = self.display.screen.getstr().split()
		
		if response[0] == 'r':
			self.tFile.data.pop(int(response[1]))

		elif response[0] == 'c':
			for rows in range(len(self.tFile.data)):
				self.tFile.data[rows].pop(int(response[1]))

		self.display.draw()
		self.display.prompt_screen(False)
		# Add to history
		self.history.append(copy.deepcopy(self.tFile))

	def undo(self):
		# If is the first, can't undo
		if len(self.history) > 1:
			# history list shape:
			# [1 2 3 ... a-2 a-1 a] (a the actual state)
			# pop a and put a-1
			self.history.pop()
			self.tFile = self.history[-1]
			self.display.tFile = self.history[-1]
			# Print again
			self.display.draw()