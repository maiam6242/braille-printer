#coding=utf-8
'''Translates text into braille'''

import numpy as np
#TODO: Add single opening and closing quotation marks...
# also figure out if this is already done, oof


# page = page
CHARACTERS_PER_LINE = 28
SYMBOLS = {'a' : np.array([[1, 0], [0, 0], [0, 0]]),
           'b' : np.array([[1, 0], [1, 0], [0, 0]]),
           'c' : np.array([[1, 1], [0, 0], [0, 0]]),
           'd' : np.array([[1, 1], [0, 1], [0, 0]]),
           'e' : np.array([[1, 0], [0, 1], [0, 0]]),
           'f' : np.array([[1, 1], [1, 0], [0, 0]]),
           'g' : np.array([[1, 1], [1, 1], [0, 0]]),
           'h' : np.array([[1, 0], [1, 1], [0, 0]]),
           'i' : np.array([[0, 1], [1, 0], [0, 0]]),
           'j' : np.array([[0, 1], [1, 1], [0, 0]]),
           'k' : np.array([[1, 0], [0, 0], [1, 0]]),
           'l' : np.array([[1, 0], [1, 0], [1, 0]]),
           'm' : np.array([[1, 1], [0, 0], [1, 0]]),
           'n' : np.array([[1, 1], [0, 1], [1, 0]]),
           'o' : np.array([[1, 0], [0, 1], [1, 0]]),
           'p' : np.array([[1, 1], [1, 0], [1, 0]]),
           'q' : np.array([[1, 1], [1, 1], [1, 0]]),
           'r' : np.array([[1, 0], [1, 1], [1, 0]]),
           's' : np.array([[0, 1], [1, 0], [1, 0]]),
           't' : np.array([[0, 1], [1, 1], [1, 0]]),
           'u' : np.array([[1, 0], [0, 0], [1, 1]]),
           'v' : np.array([[1, 0], [1, 0], [1, 1]]),
           'w' : np.array([[0, 1], [1, 1], [0, 1]]),
           'x' : np.array([[1, 1], [0, 0], [1, 1]]),
           'y' : np.array([[1, 1], [0, 1], [1, 1]]),
           'z' : np.array([[1, 0], [0, 1], [1, 1]]),
           '1' : np.array([[1, 0], [0, 0], [0, 0]]),
           '2' : np.array([[1, 0], [1, 0], [0, 0]]),
           '3' : np.array([[1, 1], [0, 0], [0, 0]]),
           '4' : np.array([[1, 1], [0, 1], [0, 0]]),
           '5' : np.array([[1, 0], [0, 1], [0, 0]]),
           '6' : np.array([[1, 1], [1, 0], [0, 0]]),
           '7' : np.array([[1, 1], [1, 1], [0, 0]]),
           '8' : np.array([[1, 0], [1, 1], [0, 0]]),
           '9' : np.array([[0, 1], [1, 0], [0, 0]]),
           '0' : np.array([[0, 1], [1, 1], [0, 0]]),
           ' ' : np.array([[0, 0], [0, 0], [0, 0]]),
           ',' : np.array([[0, 0], [1, 0], [0, 0]]),
           ';' : np.array([[0, 0], [1, 0], [1, 0]]),
           ':' : np.array([[0, 0], [1, 1], [0, 0]]),
           '.' : np.array([[0, 0], [1, 1], [0, 1]]),
           '!' : np.array([[0, 0], [1, 1], [1, 0]]),
           "'" : np.array([[0, 0], [0, 0], [1, 0]]),
           '-' : np.array([[0, 0], [0, 0], [1, 1]]),
           '?' : np.array([[0, 0], [1, 0], [1, 1]]),
           '#' : np.array([[0, 1], [0, 1], [1, 1]]),
           '(' : np.array([[0, 0], [1, 1], [1, 1]]),
           ')' : np.array([[0, 0], [1, 1], [1, 1]]),
           'Ξ' : np.array([[0, 1], [0, 1], [1, 1]]),
           '“' : np.array([[0, 0], [1, 0], [1, 1]]),
           '”' : np.array([[0, 0], [0, 1], [1, 1]]),
           'opening "' : np.array([[0, 0], [1, 0], [1, 1]]),
           'closing "' : np.array([[0, 0], [0, 1], [1, 1]]),
           'ζ' : np.array([[0, 0], [0, 0], [0, 1]]),
           'η' : np.array([[0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 1, 0, 1]]),
           '_' : np.array([[0, 1, 0, 0], [0, 0, 0, 0],
                           [0, 1, 1, 1]]),
           '[' : np.array([[0, 1, 1, 0], [0, 0, 1, 0],
                           [0, 1, 0, 1]]),
           ']' : np.array([[0, 1, 0, 1], [0, 0, 0, 1],
                           [0, 1, 1, 0]]),
           '*' : np.array([[0, 0, 0, 0], [0, 1, 0, 1],
                           [0, 0, 1, 0]]),
           '$' : np.array([[0, 1, 0, 1], [0, 0, 1, 0],
                           [0, 0, 1, 0]])
           }

class Translator:
    '''Translates text to braille'''

    OPEN_QUOTE = False
    size = []

    def convert_to_braille(self, segment):
        '''
        Converts the entirety of the segment into a dot matrix based
        on the'SYMBOLS' dictionary in this class
        Args: the whole segment in english
        Returns: the whole segment in braille
        '''
        braille_text = []
        if not self.is_new_line(segment):
            print(segment)
            segment = self.find_caps(segment)
            segment = self.find_nums(segment)
            segment = str.lower(str(segment))
            for char in segment:
                char_trans = self.translate_text(char)
                braille_text.append(char_trans)
            braille_text, num_lines = self.split_into_lines(braille_text)
        else:
            braille_text = self.make_new_line()
            num_lines = 1
        # print(braille_text)

        return braille_text, num_lines

    def is_new_line(self, segment):
        '''
        Determines whether or not the segment is a new line character (ie paragraph break)
        Args: The original english segment
        Returns: True if the segment is a new line character, False if it is not
        '''
        if segment == '\n':
            return True
        else:
            return False

    def make_new_line(self):
        '''
        Creates a new line of braille text (row of spaces)
        Returns: A numpy array that is equal to a row of spaces (24/30 spaces) in braille
        '''

        return SYMBOLS[' ']*CHARACTERS_PER_LINE

    def find_caps(self, segment):
        '''
        Finds every capital letter or word and inserts the corresponding characters in braille
        Args: segment in English
        Returns: The segment in English with a weird symbol
        (non-english)characters interspersed to denote capitalization
        i.e. MAIA -> ||MAIA  or Maia -> | Maia

        # >>> find_caps('HELLO')
        # 'ηHELLO'
        # >>> find_caps('Hello')
        # 'ζHello'
        # >>> find_caps('HI THERE I am wondering what You think About this wacky STRING')
        # 'ηHI ηTHERE ζI am wondering what ζYou think ζAbout this wacky ηSTRING'
        # >>> find_caps('HEy! This is super COOOL! Cool cool CooL! HOw do you feeEEEEl?')
        # 'ηHEy! ζThis is super ηCOOOL! ζCool cool ζCooζL! ηHOw do you feeηEEEEl?'
        '''
        #TODO: Whatever you make this letter(s) associate it with the cap letter and
        # cap word things in the dictionary, so that the translate_text
        # function can recognize everything
        #TODO: Talk to real people about how capitals work so we can handle them better
        # Notes:
            #  For some reason setting newlist_segment = list_segment causes them both to
            # be changed when one is so adding list() fixes this for reasons I don't understand
            # islower() and isupper() both return false if the string is a space so you
            #  need to use not isupper() which is super annoying but works

        list_segment = list(segment)
        newlist_segment = list(list_segment)
        offset = 0
        for i, _ in enumerate(list_segment):
            if i == 0:
                lastupper = False # If there is no character
                            #before it tell it that the last character was not uppercase
            else:
                lastupper = list_segment[i-1].isupper()

            if list_segment[i].isupper():
                if i < len(list_segment) -1 and list_segment[i+1].isupper() and not lastupper:
                    newlist_segment.insert(i+offset, 'η')
                    offset += 1
                else:
                    if not lastupper:
                        newlist_segment.insert(i+offset, 'ζ')
                        offset += 1


        output_string = ''
        return output_string.join(newlist_segment)

    def find_nums(self, segment):
        '''
        Finds every number in the string and adds a
        Args: segment in English
        Returns: The segment in English with a weird symbol
        (non-english)characters interspersed to denote capitalization
        i.e. MAIA -> ||MAIA  or Maia -> | Maia

        # >>> find_nums('1 2 3')
        # 'Ξ1 Ξ2 Ξ3'
        # >>> find_nums('123')
        # 'Ξ123'
        # >>> find_nums('The numbers are 1 and 123 and 35,245')
        # 'The numbers are Ξ1 and Ξ123 and Ξ35245'

        '''
        # Notes:
            #  For some reason setting newlist_segment = list_segment
            # causes them both to be changed when one is so adding list()
            # fixes this for reasons I don't understand

        list_segment = list(segment)
        i = 0
        while i < len(list_segment):   # This is needed for numbers
                                    #with a comma in them to prevent it from being two numbers
            if list_segment[i] == ',':
                if list_segment[i-1].isnumeric() and list_segment[i+1].isnumeric():
                    list_segment.pop(i)
            i += 1

        newlist_segment = list(list_segment)
        offset = 0
        for i, _ in enumerate(list_segment):
            if i == 0:
                lastupper = False # If there is no character
                                #before it tell it that the last character was not uppercase
            else:
                lastupper = list_segment[i-1].isnumeric()

            if list_segment[i].isnumeric():
                if i< len(list_segment) -1 and list_segment[i+1].isnumeric() and not lastupper:
                    newlist_segment.insert(i+offset,'Ξ')
                    offset += 1
                else:
                    if not lastupper:
                        newlist_segment.insert(i+offset, 'Ξ')
                        offset += 1

        output_string = ''

        return output_string.join(newlist_segment)

    def translate_text(self, char):
        '''
        Converts a single character into braille based on "SYMBOLS"; 
        handles more of the syntactical things and other rules with Braille
        Args: A single English character
        Returns: A single Braille character

        # >>> translate_text('"')
        # array([[0, 0],
        #     [1, 0],
        #     [1, 1]])
        # >>> translate_text('"')
        # array([[0, 0],
        #     [0, 1],
        #     [1, 1]])
        # >>> translate_text('>')
        # character wasn't found
        # array([[0, 0],
        #     [1, 0],
        #     [1, 1]])
        # >>> translate_text('l')
        # array([[1, 0],
        #     [1, 0],
        #     [1, 0]])
        '''
        global OPEN_QUOTE
        # print(char)
        if char == '"':
            if not OPEN_QUOTE:
                OPEN_QUOTE = True
                return SYMBOLS['opening "']
            else:
                OPEN_QUOTE = False
                return SYMBOLS['closing "']
        else:
            try:
                # print(SYMBOLS[char])
                return SYMBOLS[char]
            except:   #FIXME: Figure what error is being excepted
                print('character wasn\'t found')
                return SYMBOLS['?']

    def split_into_lines(self, braille_segment):
        '''
        Takes the segment and splits it into 24? 30? character lines
        Args: Entire segment in braille (as a list of numpy arrays)
        Returns: A numpy array that is a segment (size is twice the number of characters per line)

        # >>> test_array = [np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]])]
        # >>> test_array_2 = [np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], 
        # [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0],
        #  [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0],
        #  [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0],
        #  [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0],
        #  [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),
        # np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0], [1, 0], [1, 0]]),np.array([[1, 0],
        #  [1, 0], [1, 0]])]
        # >>> split_into_lines(test_array)
        # array([[1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        #         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
        # >>> split_into_lines(test_array_2)
        # array([[1., 0., 1., 0., 1., 0., 1., 0., 1., 0, 1, 0, 1, 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 0., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 0., 0.],
        #     [1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        #         1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 0., 0.]])
        '''
        current_line = []
        lines = []
        characters_in_line = 0
        space = np.array([[0, 0], [0, 0], [0, 0]])

        for character in braille_segment:
            if np.size(character, 0) == 4:
                character_size = 2
            else:
                character_size = 1
            if character_size + characters_in_line <= CHARACTERS_PER_LINE:
                current_line.append(character)
                characters_in_line += character_size
            else:
                lines.append(current_line)
                current_line = []
                characters_in_line = 0
        lines.append(current_line)

        line_arrays = []

        for line in lines:

            line_length = np.shape(line)[0]
            print(line_length)
            line_array = []
            if CHARACTERS_PER_LINE - line_length != 0:
                spaces = []

                for _ in range(0, (CHARACTERS_PER_LINE - line_length)):
                    spaces.append(space)

                if np.size(line) != 0:
                    line_array = np.concatenate((np.asarray(line), np.asarray(spaces)), axis=0)
                else:
                    line_array = np.asarray(spaces)
            if not len(line_array):
                line_arrays.append([line])
            else:
                line_arrays.append([line_array])

        output_array = np.vstack(np.asarray(line_arrays))
        num_lines = len(lines)
        print(type(output_array))

        return output_array, num_lines


if __name__ == '__main__':
    import doctest
    # doctest.run_docstring_examples(split_into_lines, globals())
    doctest.testmod()
    TRANS = Translator()
    TRANS.convert_to_braille('“Yay Braille!”')
