# Nicholas Jordan 
# CS480 Milestone 2

import sys
import lexical_analyzer

# Remove comments (both single and multiline) and remove tabs
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

            # Single comment
            if current_char == '/' and next_char == '/':
                if line[len(line)-1] == '\n': cleaned_line = cleaned_line + '\n'
                break;
            # Block comment start
            if current_char == '/' and next_char == '*':
                multi_comment = True
                i = i + 1
                continue
            # Block comment end
            if current_char == '*' and next_char == '/':
                multi_comment = False
                i = i + 2
                continue
            # Tab
            if current_char == '\t':
                current_char = ' '

            if multi_comment == False:
                cleaned_line = cleaned_line + current_char

            i = i + 1

        #print 'Cleaned line = ' + cleaned_line


        cleaned_file = cleaned_file + cleaned_line

    #print 'Cleaned file = \n' + cleaned_file
    return cleaned_file


def main():

    input_file = open(sys.argv[1], 'r')


    parsed_file = cleanFile(input_file)

    lexical_analyzer.Tokenize(parsed_file)

    #print parsed_file

       
if __name__ == '__main__':
    main()


    