# Nicholas Jordan 
# CS480 W15 Milestone 2

from token import *

class Symbols:

	def inTable(self, symbol):
		if symbol in self.symbolTable:
			return self.symbolTable[symbol]
		else:
			return ''

	# def add(self, symbol):
	# 	self.symbolTable.append(symbol : 'SOMETHING')

	def __init__(self):
		self.symbolTable = {# Symbols defined in Naive Semantics document
							'and' : 'BOOLOP',
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
							'sin' : 'TRIGOP',
							'cos' : 'TRIGOP',
							'tan' : 'TRIGOP',
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
							':=' : 'ASSIGN',

							# A few other C symbols
							'{' : 'LCBRACK',
							'}' : 'RCBRACK',
							'[' : 'LSBRACK',
							']' : 'RSBRACK',
							'#' : 'MACRO',
							';' : 'ENDLINE',
							'++' : 'INCR',
							'--' : 'DECR',
							'&&' : 'BOOLOP',
							'||' : 'BOOLOP',

							}
