import numpy as np
#TODO: Add single opening and closing quotation marks

open_quote = False
size = []
# page = page
charactersPerLine = 28
symbols = {'a' : np.array([[1,0],[0,0],[0,0]]),
            'b' : np.array([[1,0],[1,0],[0,0]]),
            'c' : np.array([[1,1],[0,0],[0,0]]),
            'd' : np.array([[1,1],[0,1],[0,0]]),
            'e' : np.array([[1,0],[0,1],[0,0]]),
            'f' : np.array([[1,1],[1,0],[0,0]]),
            'g' : np.array([[1,1],[1,1],[0,0]]),
            'h' : np.array([[1,0],[1,1],[0,0]]),
            'i' : np.array([[0,1],[1,0],[0,0]]),
            'j' : np.array([[0,1],[1,1],[0,0]]),
            'k' : np.array([[1,0],[0,0],[1,0]]),
            'l' : np.array([[1,0],[1,0],[1,0]]),
            'm' : np.array([[1,1],[0,0],[1,0]]),
            'n' : np.array([[1,1],[0,1],[1,0]]),
            'o' : np.array([[1,0],[0,1],[1,0]]),
            'p' : np.array([[1,1],[1,0],[1,0]]),
            'q' : np.array([[1,1],[1,1],[1,0]]),
            'r' : np.array([[1,0],[1,1],[1,0]]),
            's' : np.array([[0,1],[1,0],[1,0]]),
            't' : np.array([[0,1],[1,1],[1,0]]),
            'u' : np.array([[1,0],[0,0],[1,1]]),
            'v' : np.array([[1,0],[1,0],[1,1]]),
            'w' : np.array([[0,1],[1,1],[0,1]]),
            'x' : np.array([[1,1],[0,0],[1,1]]),
            'y' : np.array([[1,1],[0,1],[1,1]]),
            'z' : np.array([[1,0],[0,1],[1,1]]),
            '1' : np.array([[1,0],[0,0],[0,0]]),
            '2' : np.array([[1,0],[1,0],[0,0]]),
            '3' : np.array([[1,1],[0,0],[0,0]]),
            '4' : np.array([[1,1],[0,1],[0,0]]),
            '5' : np.array([[1,0],[0,1],[0,0]]),
            '6' : np.array([[1,1],[1,0],[0,0]]),
            '7' : np.array([[1,1],[1,1],[0,0]]),
            '8' : np.array([[1,0],[1,1],[0,0]]),
            '9' : np.array([[0,1],[1,0],[0,0]]),
            '0' : np.array([[0,1],[1,1],[0,0]]),
            ' ' : np.array([[0,0],[0,0],[0,0]]),
            ',' : np.array([[0,0],[1,0],[0,0]]),
            ';' : np.array([[0,0],[1,0],[1,0]]),
            ':' : np.array([[0,0],[1,1],[0,0]]),
            '.' : np.array([[0,0],[1,1],[0,1]]),
            '!' : np.array([[0,0],[1,1],[1,0]]),
            "'" : np.array([[0,0],[0,0],[1,0]]),
            '-' : np.array([[0,0],[0,0],[1,1]]),
            '?' : np.array([[0,0],[1,0],[1,1]]),
            '#' : np.array([[0,1],[0,1],[1,1]]),
            '(' : np.array([[0,0],[1,1],[1,1]]),
            ')' : np.array([[0,0],[1,1],[1,1]]),
            'Ξ' : np.array([[0,1],[0,1],[1,1]]),
            '“' : np.array([[0,0],[1,0],[1,1]]),
            '”' : np.array([[0,0],[0,1],[1,1]]),
            'opening "' : np.array([[0,0],[1,0],[1,1]]),
            'closing "' : np.array([[0,0],[0,1],[1,1]]),
            'ζ' : np.array([[0,0],[0,0],[0,1]]),
            'η' : np.array([[0,0,0,0],[0,0,0,0],
            [0,1,0,1]]),
            '_' : np.array([[0,1,0,0],[0,0,0,0],
            [0,1,1,1]]),
            '[' : np.array([[0,1,1,0],[0,0,1,0],
            [0,1,0,1]]),
            ']' : np.array([[0,1,0,1],[0,0,0,1],
            [0,1,1,0]]),
            '*' : np.array([[0,0,0,0],[0,1,0,1],
            [0,0,1,0]]),
            '$' : np.array([[0,1,0,1],[0,0,1,0],
            [0,0,1,0]])
            }

class translator:
    
    def convert_to_braille(self, segment):
        '''
        Converts the entirety of the segment into a dot matrix based on the "symbols" dictionary in this class
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
        print(braille_text)

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

        return symbols[' ']*charactersPerLine

    def find_caps(self, segment):
        '''    
        Finds every capital letter or word and inserts the corresponding characters in braille
        Args: segment in English
        Returns: The segment in English with a weird symbol (non-english)characters interspersed to denote capitalization
        i.e. MAIA -> ||MAIA  or Maia -> | Maia

        # >>> find_caps("HELLO")
        # 'ηHELLO'
        # >>> find_caps("Hello")
        # 'ζHello'
        # >>> find_caps("HI THERE I am wondering what You think About this wacky STRING")
        # 'ηHI ηTHERE ζI am wondering what ζYou think ζAbout this wacky ηSTRING'
        # >>> find_caps("HEy! This is super COOOL! Cool cool CooL! HOw do you feeEEEEl?")
        # 'ηHEy! ζThis is super ηCOOOL! ζCool cool ζCooζL! ηHOw do you feeηEEEEl?'
        '''
        #TODO: Whatever you make this letter(s) associate it with the cap letter and cap word things in the dictionary, so that the translate_text function can recognize everything 
        #TODO: Talk to real people about how capitals work so we can handle them better
        # Notes: 
            #  For some reason setting newListSegment = listSegment causes them both to be changed when one is so adding list() fixes this for reasons I don't understand
            # islower() and isupper() both return false if the string is a space so you need to use not isupper() which is super annoying but works

        listSegment = list(segment)
        newListSegment = list(listSegment)   
        offset = 0
        for i in range(len(listSegment)):
            if i == 0:
                lastupper = False # If there is no character before it tell it that the last character was not uppercase
            else:
                lastupper = listSegment[i-1].isupper()
        
            if listSegment[i].isupper():
                if i< len(listSegment) -1 and listSegment[i+1].isupper() and not lastupper:
                    newListSegment.insert(i+offset, "η")
                    offset+=1
                else:
                    if not lastupper:
                        newListSegment.insert(i+offset, "ζ")
                        offset+=1


        outputString = ""
        return outputString.join(newListSegment)

    def find_nums(self, segment):
        '''    
        Finds every number in the string and adds a 
        Args: segment in English
        Returns: The segment in English with a weird symbol (non-english)characters interspersed to denote capitalization
        i.e. MAIA -> ||MAIA  or Maia -> | Maia

        # >>> find_nums("1 2 3")
        # 'Ξ1 Ξ2 Ξ3'
        # >>> find_nums("123")
        # 'Ξ123'
        # >>> find_nums("The numbers are 1 and 123 and 35,245")
        # 'The numbers are Ξ1 and Ξ123 and Ξ35245'
        
        '''
        # Notes: 
            #  For some reason setting newListSegment = listSegment causes them both to be changed when one is so adding list() fixes this for reasons I don't understand
            
        listSegment = list(segment)
        i=0
        while i<len(listSegment):   # This is needed for numbers with a comma in them to prevent it from being two numbers
            if listSegment[i] == ',':
                if listSegment[i-1].isnumeric() and listSegment[i+1].isnumeric():
                    listSegment.pop(i)
            i+=1

        newListSegment = list(listSegment)   
        offset = 0
        for i in range(len(listSegment)):
            if i == 0:
                lastupper = False # If there is no character before it tell it that the last character was not uppercase
            else:
                lastupper = listSegment[i-1].isnumeric()
        
            if listSegment[i].isnumeric():
                if i< len(listSegment) -1 and listSegment[i+1].isnumeric() and not lastupper:
                    newListSegment.insert(i+offset, "Ξ")
                    offset+=1
                else:
                    if not lastupper:
                        newListSegment.insert(i+offset, "Ξ")
                        offset+=1

        outputString = ""

        return outputString.join(newListSegment)

    def translate_text(self, char):
        '''
        Converts a single character into braille based on "symbols"; handles more of the syntactical things and other rules with Braille 
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
        global open_quote
        # print(char)
        if char == '"':
            if open_quote != True:
                open_quote = True
                return symbols['opening "']
            else: 
                open_quote = False
                return symbols['closing "']
        else: 
            try:
                # print(symbols[char])
                return(symbols[char])
            except:
                print('character wasn\'t found')
                return(symbols['?'])

    def split_into_lines(self, braille_segment):
        '''
        Takes the segment and splits it into 24? 30? character lines
        Args: Entire segment in braille (as a list of numpy arrays)
        Returns: A numpy array that is a segment (size is twice the number of characters per line)
        
        # >>> test_array = [np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]])]
        # >>> test_array_2 = [np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]]),np.array([[1,0],[1,0],[1,0]])]
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
        currentLine = []
        lines = []
        charactersInLine = 0
        space = np.array([[0,0],[0,0],[0,0]])

        for character in braille_segment:
            if np.size(character, 0) == 4:
                characterSize = 2
            else:
                characterSize = 1
            if characterSize + charactersInLine <= charactersPerLine:
                currentLine.append(character)
                charactersInLine += characterSize
            else:
                lines.append(currentLine)
                currentLine = []
                charactersInLine = 0
        lines.append(currentLine)
    
        lineArrays = []
       
        for line in lines:
           
            lineLength = np.shape(line)[0]
            print(lineLength)

            if charactersPerLine * 2 - lineLength != 0:
                spaces = []

                for count in range(0,(charactersPerLine * 2 - lineLength)):
                    spaces.append(space)

                if(np.size(line)!= 0):
                    lineArray = np.concatenate((np.asarray(line), np.asarray(spaces)), axis = 0)
                else:
                    lineArray = np.asarray(spaces)
            lineArrays.append(lineArray)        

        outputArray =  np.vstack(np.asarray(lineArrays)) 
        num_lines = len(lines)

        return outputArray, num_lines
        
    # def get_num_lines(self):
    #     '''
    #     Gets the number of Braille lines in a given segment
    #     Returns: Number of lines in the document 
    #     '''
    #     return self.num_lines

    def size_on_page(self, num_lines):
        '''
        Determines the amount of space on a page which the segment will take up and converts that to an amount of millimeters, sets the variable size to the dimensions in millimeters in the form of a list
        Args: number of lines in a segment
        Returns: the dimensions in millimeters in the form of a list
        '''
        
        # A braille line is .28 inches in height
        # Braille lines are typically spaced .04 inches from top to top (not .04 apart)

        # |____|  | is y_size and _ is x_size

        # TODO: Check this
        line_height = 6.3
        line_spacing = 8.66 #FIXME!!!
        character_width = 3.9

        y_size = line_height*num_lines + line_spacing*num_lines
        x_size = charactersPerLine*character_width # NEED TO ACTUALLY CALC AND FIND THIS
        size = [round(x_size,2), round(y_size,2)]
        return size

if __name__ == "__main__":
    import doctest
    # doctest.run_docstring_examples(split_into_lines, globals())
    doctest.testmod()
    trans = translator
    trans.convert_to_braille(trans, '“Yay Braille!”')