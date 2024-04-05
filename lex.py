class lexeme:
    def __init__(self):
        # self.test_file_name = None
        self.source_program = None
        self.source_stream = None
        self.lexemeForward_character = None
        self.EOF = None
        self.id_number = None
        self.errors = None
        self.token_stream = None
        self.line_No = None
        self.buffer = None
        self.lexemeBeginner_index = None
        self.symbol_table = None
        self.number_of_the_source_program_characters = None
        self.bool_ = "<T_Bool>\n"
        self.break_ = "<T_Break>\n"
        self.char_ = "<T_Char>\n"
        self.continue_ = "<T_Continue>\n"
        self.else_ = "<T_Else>\n"
        self.false_ = "<T_False>\n"
        self.true_ = "<T_True>\n"
        self.for_ = "<T_For>\n"
        self.if_ = "<T_If>\n"
        self.int_ = "<T_Int>n"
        self.print_ = "<T_Print>\n"
        self.return_ = "<T_Return>\n"
        self.plus_ = "<T_AOp_PL>\n"
        self.minus_ = "<T_AOp_MN>n"
        self.multiplication_ = "<T_AOp_ML>\n"
        self.division_ = "<T_AOp_DV>\n"
        self.remainder = "<T_AOp_RM>\n"
        self.less_ = "<T_ROp_L>\n"
        self.greater_ = "<T_ROp_G>\n"
        self.less_equal_ = "<T_ROp_LE>\n"
        self.great_equal_ = "<T_ROp_GE>\n"
        self.notequal_ = "<T_ROp_NE>\n"
        self.equal_ = "<T_ROp_E>\n"
        self.and_ = "<T_LOp_AND>\n"
        self.or_ = "<T_LOp_OR>\n"
        self.not_ = "<T_LOp_NOT>\n"
        self.assign_ = "<T_Assign>\n"
        self.lp_ = "<T_LP>\n"
        self.rp_ = "<T_RP>\n"
        self.lc_ = "<T_LC>\n"
        self.rc_ = "<T_RC>\n"
        self.lb_ = "<T_LB>\n"
        self.rb_ = "<T_RB>\n"
        self.semicolon_ = "<T_Semicolon>\n"
        self.comma_ = "<T_Comma>\n"
        self.variable_function_names_ = "<T_Id>\n"
        self.decimal_integers_ = "<T_Decimal>\n"
        self.hexadecimal_integers_ = "<T_Hexadecimal>\n"
        self.constant_strings_ = "<T_String>\n"
        self.constant_characters = "<T_Char>\n"
        self.comment_ = "<T_Comment>\n"
        self.whitespace_ = "<T_Whitespace>\n"

        self.keywords = ["bool", "break", "char",
                         "continue", "else", "if",
                         "false", "for", "true",
                         "int", "print", "return", "true"]
        self.punctuators = ["{", "}", "(", ")", ";", "[", "]", ","]
        self.id_punctuators = self.punctuators.copy()
        self.id_punctuators.extend(["'", '"'])
        self.data_types = ["bool", "char", "int", "float", "string"]
        self.relational_operators = [">", "<", ">=", "<=", "==", "!="]
        self.arithmatic_operators = ["+", "-", "*", "/", "%"]
        self.whitespaces = [" ", "\t", "\n"]
        self.comment_starter = "/"
        self.comment_ender = "/"
        # self.symbol_table = {}
        # self.buffer = ""
        # self.index = 0
        # self.line_No = 1
        # self.token_stream = ""
        # self.id_number = 1
        # self.errors = "<line number> <error found>\n"
        # self.end = False
        # self.peek = ""
        # self.test_file = ""
        # self.test_file_name = ""
        # self.length = 0

        self.errors_ = ["Error: Identifier is too long", "Error: Number is too long", "Error: Invalid symbol",
                        "Error: Invalid assignment operator", "Error: Invalid keyword",
                        "Error: Invalid symbol after assignment operator", "Error: Invalid symbol after number"]

    def lex_configuration_starter(self):
        self.symbol_table = {}
        self.buffer = ""
        self.lexemeBeginner_index = 0
        self.line_No = 1
        self.token_stream = ""
        self.id_number = 1
        self.errors = "<line number> <error found>\n"
        self.EOF = False
        self.lexemeForward_character = ""
        self.source_program = ""
        # self.test_file_name = ""
        self.number_of_the_source_program_characters = 0
        # self.the_next_lexemeBeginner_index = self.lexemeBeginner_index + 1

    @property
    def out_of_range_detector(self):  # Accessing source_stream[lexemeBeginner+1= will not lead to index out of range
        return self.lexemeBeginner_index + 1 < self.number_of_the_source_program_characters

    @property
    def the_next_lexemeBeginner_index(self):
        return self.lexemeBeginner_index + 1

    def tokenization_director(self):

        while not self.EOF:
            self.whitespace()
            if self.EOF:
                break
            else:
                if self.lexemeForward_character == '+':
                    self.token_stream += self.plus_
                elif self.lexemeForward_character == '-':
                    self.token_stream += self.minus_
                elif self.lexemeForward_character == '*':
                    self.token_stream += self.multiplication_
                elif self.lexemeForward_character == "%":
                    self.token_stream += self.remainder
                # elif self.lexemeForward_character in self.punctuators:
                # self.token_stream +=
                # pass
                elif self.lexemeForward_character == self.comment_starter:
                    self.comment_analyzer()
                elif self.lexemeForward_character == '>':
                    self.great_analyzer()
                elif self.lexemeForward_character == '<':
                    self.less_analyzer()
                elif self.lexemeForward_character == '=':
                    self.equal_analyzer()
                elif self.lexemeForward_character == '!':
                    self.not_analyzer()
                elif self.lexemeForward_character == '"':
                    self.doublequote_analyzer()

            # print(self.lexemeForward_character)
            # break
        return

    def doublequote_analyzer(self):
        self.buffer = []
        if self.out_of_range_detector():
            temporary_index = self.the_next_lexemeBeginner_index()
            while not self.EOF:
                if temporary_index >= self.number_of_the_source_program_characters:
                    single_quote_enclosed = "".join(self.buffer)
                    if len(single_quote_enclosed) <= 1:
                        self.errors += '{0} {1} (incomplete comment)\n'.format(str(self.line_No),
                                                                               str(single_quote_enclosed))
                    else:
                        self.errors += '{0} {1} (Invalid string literal)\n'.format(str(self.line_No),
                                                                                   str(single_quote_enclosed))

    def not_analyzer(self):
        if self.out_of_range_detector() and self.token_stream[self.the_next_lexemeBeginner_index()] == '=':
            self.token_stream = self.notequal_
            self.lexemeBeginner_index = self.the_next_lexemeBeginner_index()
        else:
            self.token_stream = self.not_

    def equal_analyzer(self):
        if self.out_of_range_detector() and self.source_stream[self.the_next_lexemeBeginner_index] == '=':
            self.token_stream += self.equal_
            self.lexemeBeginner_index += self.the_next_lexemeBeginner_index()
        else:
            self.token_stream += self.assign_
        return

    def less_analyzer(self):
        if self.out_of_range_detector() and self.token_stream[self.the_next_lexemeBeginner_index] == '=':
            self.token_stream += self.less_equal_
            self.lexemeBeginner_index = self.the_next_lexemeBeginner_index()
        else:
            self.token_stream += self.less_

    def great_analyzer(self):
        if self.out_of_range_detector() and self.source_stream[self.the_next_lexemeBeginner_index()]:
            self.token_stream += self.great_equal_
            self.lexemeBeginner_index = self.the_next_lexemeBeginner_index()
        else:
            self.token_stream += self.greater_

        return

    def comment_analyzer(self):
        if self.out_of_range_detector() and self.source_stream[self.lexemeBeginner_index + 1] == self.comment_ender:
            while not self.EOF:
                if self.source_stream[self.lexemeBeginner_index + 2] == '\n':
                    self.errors += '{0} incomplete comment\n'.format(str(self.line_No))
                    self.line_No += 1
                    self.lexemeBeginner_index += 2
                    break
                elif self.source_stream[self.lexemeBeginner_index + 1] == self.comment_ender:
                    self.lexemeBeginner_index += 1
                    self.token_stream += self.comment_

                else:
                    self.lexemeBeginner_index += 1
                    self.token_stream += self.division_
                    break
        else:
            pass
        return

    def whitespace(self):
        while not self.EOF:
            if self.lexemeBeginner_index >= self.number_of_the_source_program_characters:
                self.EOF = True
                continue
            self.lexemeForward_character = self.source_stream[self.lexemeBeginner_index]
            # print(f"begin index is {self.lexemeBeginner_index}")
            # print(f"the lexeme forward character is :{self.lexemeForward_character}")
            if self.lexemeForward_character in self.whitespaces:
                self.lexemeBeginner_index += 1
                self.token_stream += self.whitespace_
                print(self.source_stream[self.lexemeBeginner_index])
            elif self.lexemeForward_character == '\n':
                self.lexemeBeginner_index += 1
                self.line_No += 1
                self.token_stream += self.whitespace_
            else:
                break

        return

    def lex_starter(self, source_program):
        self.lex_configuration_starter()
        self.source_program = open(source_program, "r")
        self.source_stream = self.source_program.read()
        # print(self.source_stream[0])
        self.number_of_the_source_program_characters = len(self.source_stream)
        self.tokenization_director()
        return
