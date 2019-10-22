import numpy as np
#TODO: Add single opening and closing quotation marks

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
num_lines = 0

def convert_to_braille(segment):
    '''
    Converts the entirety of the segment into a dot matrix based on the "symbols" dictionary in this class
    Args: the whole segment in english
    Returns: the whole segment in braille
    '''
    # braille_text = np.array([])
    braille_text = []
    segment = find_caps(segment)
    segment = find_nums(segment)
    segment = str.lower(segment)
    for char in segment:
        char_trans = translate_text(char)
        braille_text.append(char_trans)
    braille_text = np.asarray(braille_text)
    split_into_lines(braille_text)
    return braille_text

def find_caps(segment):
    '''    
    Finds every capital letter or word and inserts the corresponding characters in braille
    Args: segment in English
    Returns: The segment in English with a weird symbol (non-english)characters interspersed to denote capitalization
    i.e. MAIA -> ||MAIA  or Maia -> | Maia

    >>> find_caps("HELLO")
    'ηHELLO'
    >>> find_caps("Hello")
    'ζHello'
    >>> find_caps("HI THERE I am wondering what You think About this wacky STRING")
    'ηHI ηTHERE ζI am wondering what ζYou think ζAbout this wacky ηSTRING'
    >>> find_caps("HEy! This is super COOOL! Cool cool CooL! HOw do you feeEEEEl?")
    'ηHEy! ζThis is super ηCOOOL! ζCool cool ζCooζL! ηHOw do you feeηEEEEl?'
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

def find_nums(segment):
    '''    
    Finds every number in the string and adds a 
    Args: segment in English
    Returns: The segment in English with a weird symbol (non-english)characters interspersed to denote capitalization
    i.e. MAIA -> ||MAIA  or Maia -> | Maia

    >>> find_nums("1 2 3")
    'Ξ1 Ξ2 Ξ3'
    >>> find_nums("123")
    'Ξ123'
    >>> find_nums("The numbers are 1 and 123 and 35,245")
    'The numbers are Ξ1 and Ξ123 and Ξ35245'
    
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

def translate_text(char):
    '''
    Converts a single character into braille based on "symbols"; handles more of the syntactical things and other rules with Braille 
    Args: A single English character
    Returns: A single Braille character
    '''
    open_quote = False
    print(char)
    if char == '"':
        if open_quote != True:
            open_quote = True
            return symbols['opening "']
        else: 
            open_quote = False
            return symbols['closing "']
    else: 
        try:
            print(symbols[char])
            return(symbols[char])
        except:
            print('character wasn\'t found')
            return(symbols['?'])

def split_into_lines(braille_segment):
    '''
    Takes the segment and splits it into 24 character lines
    Args: Entire segment in braille
    Returns: An array that is broken up by line
    '''
    # TODO: Should this be reshaped? What's up with this logic?
    # @MAIA START HERE TOMORROW
    by_lines = np.array([])
    num_in_line = 0 
    for character in braille_segment: 
        print(character)
        if(num_in_line + int(character.size/len(character)) <= 24):
            num_in_line += int(character.size/len(character))
        else:
            print('yoooo')
            print(braille_segment[num_in_line])
            by_lines.horzcat(braille_segment())
            num_in_line = 0
        print('next')
    return 0

def set_num_lines(number_of_lines):
    '''
    Sets the number of Braille lines in a given segment
    Args: Length of the split into lines array 
    '''
    # FIXME: Should this take in something else?
    num_lines = number_of_lines

def get_num_lines():
    '''
    Gets the number of Braille lines in a given segment
    Returns: Number of lines in the document 
    '''
    return num_lines

def size_on_page(num_lines):
    '''
    Determines the amount of space on a page which the segment will take up and converts that to an amount of inches 
    Args: number of lines in a segment
    Returns: the dimensions in inches in the form of a list 
    '''
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    convert_to_braille('Why in the world do you walk sideways like that? said a Mother Crab to her son. “You should always walk straight forward with your toes turned out.”')
    # print(find_caps("HI THERE I am wondering what You think About this wacky STRING"))