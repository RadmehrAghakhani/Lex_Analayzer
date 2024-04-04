from lex import *
import sys
import os


def tokenize_source_program(source_program, lex):
    if os.path.exists(source_program):

        lex.lex_starter(source_program)
        # with open(source_program, 'r') as file:
        #     for line in file:
        #         tokenization(line)
        # file.close()

    else:
        print("The file does not exist")


def whitespace(character):
    return character == ' ' or character == '\t' or character == '\n'


def word_compare(string):
    return


if __name__ == "__main__":
    current_character = ""
    lex = lexeme()
    if len(sys.argv) < 2:
        print("Usage of incomplete analyzer.py")
        sys.exit(1)

    source_program = os.path.abspath(sys.argv[1])
    tokenize_source_program(source_program, lex)
