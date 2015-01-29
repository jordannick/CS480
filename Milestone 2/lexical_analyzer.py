from token import *

class Tokenize:

    def isDigit(self, char):

		if len(char) > 0:
			var = ord(char)
		else: 
			return False

		if var <= 57 and var >= 48 :
			#print char
			return True
		else :
			return False

    def isLetter(self, char):
		if len(char) > 0:
			var = ord(char)
		else: 
			return False

		var = ord(char)
		if (var <= 90 and var >= 65) or (var <= 122 and var >= 97) :
			return True
		else :
			return False

    def isQuote(self, char):
		if char == '"' :
			return True
		else :
			return False

    def isSeparator(self):
		return False

    def getChar(self):
        if self.inFirst:
            char = self.buffer0[self.current_pos]
        else : 
            char = self.buffer1[self.current_pos]

        if char == '' :
            self.endFile = True     

        if ((self.current_pos + 1) < 10):
            self.current_pos += 1
        else : 
            self.reloadBuffer()
            
        return char

    def reloadBuffer(self):
		#i = self.file_pos
		i = 0
		if self.inFirst:
			while (i < 10):
				if self.file_pos < len(self.file):
					self.buffer1[i] = self.file[self.file_pos]
				else:
					self.buffer1[i] = ''
				self.file_pos += 1
				i += 1
			self.inFirst = False

		else:
			while (i < 10):
				if self.file_pos < len(self.file):
					self.buffer0[i] = self.file[self.file_pos]
				else:
					self.buffer0[i] = ''
				self.file_pos += 1
				i += 1
			self.inFirst = True

		self.current_pos = 0
		#print "Buffer0 = " + str(self.buffer0)
		#print "Buffer1 = " + str(self.buffer1)

    def digitHandler(self, symbol, token_value, floatTag):
		current_symbol = symbol
		next_symbol = self.getChar() 

		token_value = token_value + current_symbol

		# Next could be a '.'' or something else
		if self.isDigit(next_symbol) == False:

			# If this is first '.' encountered
			if next_symbol == '.' and floatTag == False:
				floatTag = True # Designate as a float for token generation
				self.digitHandler(next_symbol, token_value, floatTag)

			# Done building the number, generate token
			else:
				if floatTag: print "New Token! (float) = " + token_value
				else: print "New Token! (int) = " + token_value
				# Continue file iteration
				self.symbolCompare()
				return

		# Next is a digit
		else:
			self.digitHandler(next_symbol, token_value, floatTag)

    def stringHandler(self, symbol, token_value):
		current_symbol = symbol
		next_symbol = self.getChar() 

		token_value = token_value + current_symbol

		# Next symbol is not a quote, continue building string
		if self.isQuote(next_symbol) == False and self.endFile == False:
			self.stringHandler(next_symbol, token_value)

		# Next symbol is a quote (indicating end of string), generate token
		else:
			print "New Token! (string) = " + token_value + next_symbol
			# Continue file iteration
			self.symbolCompare()


    #def separatorHandler(self, symbol):

    def symbolCompare(self):
		symbol = self.getChar()

		#print symbol

		if self.endFile:
			print "End File"
			return


		if self.isDigit(symbol):
			self.digitHandler(symbol, "", False)
		# just dot encountered first? e.g. .75 = 0.75
		elif self.isQuote(symbol):
			#print "StringHandler begin "
			self.stringHandler(symbol, "")
		#elif self.isSeparator(symbol):
			#self.separatorHandler(symbol)
		else:
			#symbol = self.getChar()
			self.symbolCompare()
		#TODO more cases, letters, underscores separators, etc

    def __init__(self, parsed_file):
		self.buffer0 = ['']*10
		self.buffer1 = ['']*10
		self.current_pos = 0
		self.inFirst = True
		self.file = parsed_file
		self.file_pos = 0
		self.endFile = False
        #print "Tokenize!"
		#print parsed_file
		#self.isDigit('a')
		self.reloadBuffer()

		self.symbolCompare()
		#while (self.endFile == False):
			#print self.getChar()
