import numpy as np

symbols = {'A' : np.array([[1,0],[0,0],[0,0]]),
           'B' : np.array([[1,0],[1,0],[0,0]]),
           'C' : np.array([[1,1],[0,0],[0,0]]),
           'D' : np.array([[1,1],[0,1],[0,0]]),
           'E' : np.array([[1,0],[0,1],[0,0]]),
           'F' : np.array([[1,1],[1,0],[0,0]]),
           'G' : np.array([[1,1],[1,1],[0,0]]),
           'H' : np.array([[1,0],[1,1],[0,0]]),
           'I' : np.array([[0,1],[1,0],[0,0]]),
           'J' : np.array([[0,1],[1,1],[0,0]]),
           'K' : np.array([[1,0],[0,0],[1,0]]),
           'L' : np.array([[1,0],[1,0],[1,0]]),
           'M' : np.array([[1,1],[0,0],[1,0]]),
           'N' : np.array([[1,1],[0,1],[1,0]]),
           'O' : np.array([[1,0],[0,1],[1,0]]),
           'P' : np.array([[1,1],[1,0],[1,0]]),
           'Q' : np.array([[1,1],[1,1],[1,0]]),
           'R' : np.array([[1,0],[1,1],[1,0]]),
           'S' : np.array([[0,1],[1,0],[1,0]]),
           'T' : np.array([[0,1],[1,1],[1,0]]),
           'U' : np.array([[1,0],[0,0],[1,1]]),
           'V' : np.array([[1,0],[1,0],[1,1]]),
           'W' : np.array([[0,1],[1,1],[0,1]]),
           'X' : np.array([[1,1],[0,0],[1,1]]),
           'Y' : np.array([[1,1],[0,1],[1,1]]),
           'Z' : np.array([[1,0],[0,1],[1,1]]),
           '1' : np.array([[0,1,1,0],[0,1,0,0],
           [1,1,0,0]]),
           '2' : np.array([[0,1,1,0],[0,1,1,0],
           [1,1,0,0]]),
           '3' : np.array([[0,1,1,1],[0,1,0,0],
           [1,1,0,0]]),
           '4' : np.array([[0,1,1,1],[0,1,0,1],
           [1,1,0,0]]),
           '5' : np.array([[0,1,1,0],[0,1,0,1],
           [1,1,0,0]]),
           '6' : np.array([[0,1,1,1],[0,1,1,0],
           [1,1,0,0]]),
           '7' : np.array([[0,1,1,1],[0,1,1,1],
           [1,1,0,0]]),
           '8' : np.array([[0,1,1,0],[0,1,1,1],
           [1,1,0,0]]),
           '9' : np.array([[0,1,0,1],[0,1,1,0],
           [1,1,0,0]]),
           '0' : np.array([[0,1,0,1],[0,1,1,1],
           [1,1,0,0]]),
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
           'opening "' : np.array([[0,0],[1,0],[1,1]]),
           'closing "' : np.array([[0,0],[0,1],[1,1]]),
           'cap letter' : np.array([[0,0],[0,0],[0,1]]),
           'cap word' : np.array([[0,0,0,0],[0,0,0,0],
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

def convert_to_braille(segment):
    '''
    Converts the entirety of the segment into a dot matrix based on the "symbols" dictionary in this class
    Args: the whole segment in english
    Returns: the whole segment in braille
    '''
    braille_text = []
    for char in segment:
        translate_text(char)
        braille_text.append(char)
    return braille_text

def translate_text(char):
    '''
    Converts a single character into braille based on "symbols"; handles more of the syntactical things and other rules with Braille 
    Args: A single English character
    Returns: A single Braille character
    '''
    # TODO: How should the quotes be tracked?! UGH! And all cap words? Maybe this isn't the right structure? It seems more modular though gahhhhh

    # TODO: Handle cap letters and words, prob not here
    open_quote = False
    
    if char != '"':
        print(symbols['%s' % char])
    elif char == '"':
        if open_quote != True:
            open_quote = True
            return symbols['opening "']
        else: 
            return symbols['closing "']
    return 0

def split_into_lines(braille_segment):
    '''
    Takes the segment and splits it into 24 character lines
    Args: Entire segment in braille
    Returns: An array that is broken up by line
    '''
    return 0

def set_num_lines(number_of_lines):
    '''
    Sets the number of Braille lines in a given segment
    Args: Length of the split into lines array 
    '''
    # FIXME: Should this take in something else?
    return 0

def get_num_lines():
    '''
    Gets the number of Braille lines in a given segment
    Returns: Number of lines in the document 
    '''
    return 0

def size_on_page(num_lines):
    '''
    Determines the amount of space on a page which the segment will take up and converts that to an amount of inches 
    Args: number of lines in a segment
    Returns: the dimensions in inches in the form of a list 
    '''
    return 0