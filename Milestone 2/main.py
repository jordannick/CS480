# Nicholas Jordan 
# CS480 W15 Milestone 2

import sys
import lexical_analyzer

# Remove comments, tabs, extra whitespace
# Generates new cleaned file line by line
def cleanFile(input_file):
    cleaned_file = ''
    cleaned_line = ''
    current_char = ''
    next_char = ''
    multi_comment = False

    for line in input_file.readlines():
        cleaned_line = ''
        i = 0
        while (i < len(line)):
            current_char = line[i]

            if (i+1 < len(line)):
                next_char = line[i+1]
            else:
                next_char = ''

            # C-style single comment
            if current_char == '/' and next_char == '/':
                if line[len(line)-1] == '\n': cleaned_line = cleaned_line + '\n'
                break;
            # C-style block comment start
            if current_char == '/' and next_char == '*':
                multi_comment = True
                i = i + 1
                continue
            # C-style block comment end
            if current_char == '*' and next_char == '/':
                multi_comment = False
                i = i + 2
                continue
            # Double whitespace -- interferes with whitespaces in strings
            # if current_char == ' ' and next_char == ' ':
            #     current_char = ''
            # Tab
            if current_char == '\t':
                current_char = ' '

            if multi_comment == False:
                cleaned_line = cleaned_line + current_char

            i = i + 1

        cleaned_file = cleaned_file + cleaned_line

    return cleaned_file

def printTokens(tokens):
    for token in tokens:
        print token.name + " , " + token.value


def main():

    input_file = open(sys.argv[1], 'r')

    # Scanning phase
    parsed_file = cleanFile(input_file)

    # Lexical analysis phase
    tokens = lexical_analyzer.Tokenize(parsed_file).tokens

    printTokens(tokens)
       
if __name__ == '__main__':
    main()


    