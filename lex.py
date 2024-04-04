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

            # print(self.lexemeForward_character)
            # break
        return

    @property
    def out_of_range_detector(self):  # Accessing source_stream[lexemeBeginner+1= wont lead to index out of range
        return self.lexemeBeginner_index + 1 < self.number_of_the_source_program_characters

    def comment_analyzer(self):
        if self.out_of_range_detector() and self.source_stream[self.lexemeBeginner_index + 1] == self.comment_ender:
            while not self.EOF:
                if self.source_stream[self.lexemeBeginner_index + 2] == '\n':
                    self.errors += '{0} incomplete comment\n'.format(str(self.line_No))
                    self.line_No += 1
                    self.lexemeBeginner_index += 2
                    break
                elif self.source_stream[self.lexemeBeginner_index+1] == self.comment_ender:
                    self.lexemeBeginner_index += 1
                    self.token_stream += self.comment_

                else:
                    self.lexemeBeginner_index += 1
                    self.token_stream += self.division_
                    break



    def whitespace(self):
        while not self.EOF:
            if self.lexemeBeginner_index >= self.number_of_the_source_program_characters:
                self.EOF = True
                continue
            self.lexemeForward_character = self.source_stream[self.lexemeBeginner_index]
            print(f"begin index is {self.lexemeBeginner_index}")
            print(f"the lexeme forward character is :{self.lexemeForward_character}")
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
        print("545454")
        return

    def lex_starter(self, source_program):
        self.lex_configuration_starter()
        self.source_program = open(source_program, "r")
        self.source_stream = self.source_program.read()
        # print(self.source_stream[0])
        self.number_of_the_source_program_characters = len(self.source_stream)
        self.tokenization_director()
        return
