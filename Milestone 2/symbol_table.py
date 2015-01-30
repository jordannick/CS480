from token import *

class Symbols:

	def inTable(self, symbol):
		if symbol in self.symbolTable:
			return self.symbolTable[symbol]
		else:
			return ''

	def __init__(self):
		self.symbolTable = {'and' : 'BOOLOP',
							'or' : 'BOOLOP',
							'not' : 'BOOLOP',
							'true' : 'BOOLCONST',
							'false' : 'BOOLCONST',
							'+' : 'OP',
							'-' : 'OP',
							'*' : 'OP',
							'/' : 'OP',
							'%' : 'MODOP',
							'^' : 'POWEROP',
							'=' : 'RELOP',
							'<' : 'RELOP',
							'>' : 'RELOP',
							'<=' : 'RELOP',
							'>=' : 'RELOP',
							'!=' : 'RELOP',
							'bool' : 'TYPE',
							'int' : 'TYPE',
							'real' : 'TYPE', 
							'string' : 'TYPE',
							'(' : 'LPAREN',
							')' : 'RPAREN',
							'stdout' : 'PRINT',
							'if' : 'IF',
							'while' : 'WHILE',
							'let' : 'LET',
							':=' : 'ASSIGN'
							}
