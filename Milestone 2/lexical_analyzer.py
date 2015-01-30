# Nicholas Jordan 
# CS480 W15 Milestone 2

from token import *
import symbol_table

class Tokenize:

    def isDigit(self, symbol):
    	return symbol.isdigit()

    def isLetter(self, symbol):
    	return symbol.isalpha()
		
    def isQuote(self, symbol):
		if symbol == '"': return True
		else: return False

    def isUnderscore(self, symbol):
		if symbol == '_': return True
		else: return False 


	# Determines next symbol action
    def symbolCompare(self, symbol):

    	# Continue on with next symbol or keep using current?
		if self.holdAdvance == False:
			symbol = self.getSymbol()
		# If there is a hold, remove it
		else:
			self.holdAdvance = False

		if self.endFile:
			print "Reached end of file"
			return

		if self.isDigit(symbol) : 
			self.digitHandler(symbol, "", False)
		elif self.isQuote(symbol):
			self.stringHandler(symbol, "")
		elif self.isLetter(symbol) or self.isUnderscore(symbol):
			self.identifierHandler(symbol, "")
		else:
			# Skip whitespace and newlines
			if symbol != ' ' and symbol != '\n':
				self.otherSymbolHandler(symbol)
			else:
				self.symbolCompare(symbol)


	# Retrieves the symbol from the buffer to look at, advances position for the next call
    def getSymbol(self):
        if self.inFirst:
            symbol = self.buffer0[self.current_pos]
        else : 
            symbol = self.buffer1[self.current_pos]

        if symbol == 'eof' :
            self.endFile = True     

        # Have we extended past buffer size?
        if ((self.current_pos + 1) < 10):
            self.current_pos += 1
        else : 
            self.reloadBuffer()
            
        return symbol


    # Fills up a buffer in the pair with the next 10 symbols from file
    # If no more symbols in file, place end of file marker in buffer
    def reloadBuffer(self):
		i = 0
		if self.inFirst:
			while (i < 10):
				if self.file_pos < len(self.file):
					self.buffer1[i] = self.file[self.file_pos]
				else:
					self.buffer1[i] = 'eof'
					break
				self.file_pos += 1
				i += 1
			self.inFirst = False

		else:
			while (i < 10):
				if self.file_pos < len(self.file):
					self.buffer0[i] = self.file[self.file_pos]
				else:
					self.buffer0[i] = 'eof'
					break
				self.file_pos += 1
				i += 1
			self.inFirst = True

		# Reset since we just switched to alternate buffer
		print self.buffer0
		print self.buffer1
		self.current_pos = 0


	# When a digit is seen, build the int/float
	# Float tag is set when a '.' is found after a digit
    def digitHandler(self, symbol, token_value, floatTag):
		current_symbol = symbol
		next_symbol = self.getSymbol() 

		token_value = token_value + current_symbol

		if self.isDigit(next_symbol) == False:
			# If this is first '.' encountered
			if next_symbol == '.' and floatTag == False:
				# Designate as a float for token generation
				floatTag = True 
				self.digitHandler(next_symbol, token_value, floatTag)

			# Done building the number, generate token
			else:
				if floatTag: self.tokens.append(Token("FLOAT", token_value)) 
				else: self.tokens.append(Token("INT", token_value))

				self.holdAdvance = True

				# Continue file iteration
				self.symbolCompare(next_symbol)
				return

		# Next is a digit
		else:
			self.digitHandler(next_symbol, token_value, floatTag)


	# When a quotation is seen, build the string until closing quotation found
    def stringHandler(self, symbol, token_value):
		current_symbol = symbol
		next_symbol = self.getSymbol() 

		token_value = token_value + current_symbol

		# Next symbol is not a quote, continue building string
		if self.isQuote(next_symbol) == False and self.endFile == False:
			self.stringHandler(next_symbol, token_value)

		# Next symbol is a quote (indicating end of string), generate token
		else:
			self.tokens.append(Token("STRING", token_value + next_symbol))

			# Continue file iteration
			self.symbolCompare('')


	# When letter/underscore found, build the id until an invalid id symbol found
    def identifierHandler(self, symbol, token_value):
		current_symbol = symbol
		next_symbol = self.getSymbol() 

		token_value = token_value + current_symbol

		if self.isLetter(next_symbol) or self.isDigit(next_symbol) or self.isUnderscore(next_symbol):
			self.identifierHandler(next_symbol, token_value)
		else:
			foundSymbol = self.symbolTable.inTable(token_value)
			if  foundSymbol != '':
				self.tokens.append(Token(foundSymbol, token_value))
			else:
				self.tokens.append(Token("ID", token_value))

			self.holdAdvance = True

			# Continue file iteration
			self.symbolCompare(next_symbol)


	# Anything not handled as of yet, mainly going to be separators and operators
    def otherSymbolHandler(self, symbol):
		current_symbol = symbol
		
		token_value = current_symbol
		foundSymbol = self.symbolTable.inTable(token_value)

		# Try a single character operator or separator, e.g. ( , < , +
		if foundSymbol != '':
			self.tokens.append(Token(foundSymbol, token_value))
			# Continue file iteration
			self.symbolCompare('')
			return

		# Try a double character, e.g. <= , !=
		next_symbol = self.getSymbol()
		token_value = token_value + next_symbol
		foundSymbol = self.symbolTable.inTable(token_value)
		self.holdAdvance = True

		if foundSymbol != '':
			self.tokens.append(Token(foundSymbol, token_value))
			self.holdAdvance = False
		
		# Continue file iteration
		self.symbolCompare(next_symbol)


    def __init__(self, parsed_file):
		self.file = parsed_file
		self.endFile = False
		self.buffer0 = ['']*10
		self.buffer1 = ['']*10
		self.current_pos = 0 # Current position within the current buffer
		self.inFirst = True # Current buffer being observed
		self.file_pos = 0 # Current character position in the file
		self.holdAdvance = False # Flag used to put a hold on iteration
		self.symbolTable = symbol_table.Symbols()
		self.tokens = []

        # Do initial load
		self.reloadBuffer()

		# Begin iteration of file
		self.symbolCompare('')
